from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  
db = client['EmpSch']  # Replace with your desired database name

@app.route('/signup', methods=['POST'])
def addUser():
    data = request.json

    firstName = data.get('firstName')
    lastName = data.get('lastName')
    email = data.get('email')
    age = data.get('age')
    address = data.get('address')
    username = data.get('username')
    password = data.get('password')

    if not firstName or not lastName or not email or not age or not address or not username or not password:
        return jsonify({'error': 'Missing Fields!'})

    users_collection = db['Signup']  # Replace 'signup' with your desired collection name

    user_data = {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'age': age,
        'address': address,
        'username': username,
        'password': password
    }

    try:
        users_collection.insert_one(user_data)
        return jsonify({'message': 'User added to the database successfully'})
    except Exception as e:
        return jsonify({'error': f'Failed to add user. {str(e)}'})
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)