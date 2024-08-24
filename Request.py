import requests
import time

url = 'http://127.0.0.1:5001'

def find_details(name, url):
    if not name or not url:
        return {"Error": "Check name or URL details"}
    try:
        t1 = time.time()
        response = requests.get(url + '/get_details', params={"name": name})
        t2 = time.time()
        if response.status_code == 200:
            return {
                "Status": response.status_code,
                "Time for request to return": t2 - t1,
                "Data": response.json()
            }
        else:
            return {
                "Error": response.json().get('Error', 'Unknown Error')
            }
    except Exception as e:
        return {"Error": str(e)}

def post_data(name, email, number, url):
    if not name or not email or not url:
        return {"Error": "Data is missing"}
    try:
        data = {
            "Name": name,
            "Email": email,
            "Phone": number
        }
        t1 = time.time()
        response = requests.post(url + '/add_details', json=data)
        t2 = time.time()
        if response.status_code == 201:
            return {
                "Status Code": response.status_code,
                "Message": "Data uploaded successfully",
                "Time to post": t2 - t1,
                "Response data": response.json()
            }
        else:
            return {
                "Error": response.json().get('Error', 'Failed to add data')
            }
    except Exception as e:
        return {"Error": str(e)}

def update_details(name, email, phone, url):
    if not name or not url:
        return {'Error': "Name and URL are required"}
    try:
        data = {
            "Name": name,
            "Email": email,
            "Phone": phone
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        t1 = time.time()
        response = requests.put(url + '/update_details', json=data)
        t2 = time.time()
        if response.status_code == 200:
            return {
                "Status": response.status_code,
                "Time taken": t2 - t1,
                "Message": "Data updated successfully",
                "Response Data": response.json()
            }
        else:
            return {
                'Error': response.json().get('Error', 'Failed to update data')
            }
    except Exception as e:
        return {"Error": str(e)}

def delete_details(name, url):
    if not name or not url:
        return {'Error': 'Name and URL are required'}
    try:
        t1 = time.time()
        response = requests.delete(url + '/delete_details', params={'name': name})
        t2 = time.time()
        if response.status_code == 200:
            return {
                'Status': response.status_code,
                'Delete time': t2 - t1,
                'Message': f'Successfully deleted the data for {name}',
                'Response data': response.json()
            }
        else:
            return {"Error": response.json().get('Error', 'Failed to delete data')}
    except Exception as e:
        return {'Error': str(e)}

if __name__ == "__main__":
    print("""
    Which Operation to perform,
    1) Type 'GET' to retrieve data of someone.
    2) Type 'POST' to add data for a new person.
    3) Type 'PUT' to edit data for existing person.
    4) Type 'DELETE' to delete data for the person.
    """)
    operation = input("Which operation:-> ").strip().upper()
    if operation == "GET":
        person_name = input("Enter Name: ").strip()
        response = find_details(person_name, url)
        print(response)
    elif operation == "POST":
        person_name = input("Enter Name         : ").strip()
        email = input("Enter Email        : ").strip()
        phone = input("Enter Phone Number : ").strip()
        response = post_data(person_name, email, phone, url)
        print(response)
    elif operation == "PUT":
        person_name = input("Enter Name                              : ").strip()
        email = input("Enter Email (leave blank to skip)       : ").strip() or None
        phone = input("Enter Phone Number (leave blank to skip): ").strip() or None
        response = update_details(person_name, email, phone, url)
        print(response)
    elif operation == "DELETE":
        person_name = input("Enter Name to Delete: ").strip()
        response = delete_details(person_name, url)
        print(response)
    else:
        print("Invalid Operation")
