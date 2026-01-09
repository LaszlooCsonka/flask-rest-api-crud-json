import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
DATA_FILE = 'users.json'

# Helper function to load data
def load_data():
    if not os.path.exists(DATA_FILE):
        # If file doesn't exist, start with default data
        default_data = [
            {"id": 1, "name": "John Doe"},
            {"id": 2, "name": "Anna Smith"}
        ]
        # Automatic save to create the file
        save_data(default_data)
        return default_data

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Helper function to save data
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Welcome message on the home page
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the REST API! Use the /users endpoint."})

# --- CRUD OPERATIONS ---

# 1. GET: All users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(load_data())

# 2. POST request: Add new users with error handling
@app.route('/users', methods=['POST'])
def add_user():
    new_data = request.get_json()

    # Error handling: check for missing fields
    if not new_data or 'id' not in new_data or 'name' not in new_data:
        return jsonify({"error": "Missing data! Required: id, name"}), 400

    data = load_data()

    # Error handling: does the ID already exist?
    if any(u['id'] == new_data['id'] for u in data):
        return jsonify({"error": "This ID is already taken!"}), 400

    data.append(new_data)
    save_data(data)
    return jsonify({"message": "Successfully saved!", "data": new_data}), 201

# 3. PUT request: Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_data = request.get_json()
    if not updated_data or 'name' not in updated_data:
        return jsonify({"error": "Missing data! 'name' is required for update."}), 400

    data = load_data()
    user_found = False

    for u in data:
        if u['id'] == user_id:
            u['name'] = updated_data['name']
            user_found = True
            break

    if not user_found:
        return jsonify({"error": "User with this ID not found!"}), 404    

    save_data(data)
    return jsonify({"message": "Successfully updated!", "data": next(u for u in data if u['id'] == user_id)})

# 4. DELETE request: Delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = load_data()
    new_list = [u for u in data if u['id'] != user_id]

    if len(new_list) == len(data):
        return jsonify({"error": "User not found!"}), 404
    
    save_data(new_list)
    return jsonify({"message": f"User with ID {user_id} has been deleted!"})

if __name__ == '__main__':
    load_data()
    app.run(debug=True)