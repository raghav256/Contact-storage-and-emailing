from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Contact(db.Model):
    __tablename__ = 'contacts'
    name = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "Name": self.name,
            "Email": self.email,
            "Phone_Number": self.phone
        }

with app.app_context():
    db.create_all()

@app.route('/get_details', methods = ['GET'])
def get_details():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    person = Contact.query.get(name)
    if person:
        return jsonify(person.to_dict()), 200
    else:
        return jsonify({"error": f"Name {name} not found in the database"}), 404

@app.route('/add_details', methods = ['POST'])
def add_details():
    content = request.json
    name = content.get('Name')
    email = content.get('Email')
    phone = content.get('Phone')

    if not name:
        return jsonify({'Error' : "Name is Required"}), 400
    if Contact.query.get(name):
        return jsonify({'Error': 'This name already exists, use other api for modification'}), 409
    c = Contact(name = name, email = email, phone = phone)
    db.session.add(c)
    db.session.commit()
    return jsonify({"message": "Data added successfully", "name": name}), 201

@app.route('/update_details', methods = ['PUT'])
def update_details():
    content = request.json
    name = content.get('Name')
    email = content.get('Email')
    phone = content.get('Phone')

    if not name:
        return jsonify({'Error' : 'Name is Required'}), 400
    person = Contact.query.get(name)

    if not person:
        return jsonify({'Error' : "This person doesn't exist" }), 404
    if email:
        person.email = email

    if phone:
        person.phone = phone
    db.session.commit()
    return jsonify({"message": "Data updated successfully", "name": name, "updated_data": person.to_dict()}), 200


@app.route('/delete_details', methods = ['DELETE'])
def delete_details():
    name = request.args.get("name")
    if not name:
        return jsonify({'Error': 'Name is required!!!'}), 400
    person = Contact.query.get(name)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({
            "Message" : "Successfully deleted details for "+ str(name)
        }), 200
    else:
        return jsonify({"error": "Name not found in the database"}), 404


if __name__ == "__main__":
    app.run(port=5001, debug=True)