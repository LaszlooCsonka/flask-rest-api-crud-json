# Flask REST API with JSON Persistence

A professional User Management API built with Python and Flask. This project demonstrates modern software development practices, including **BPMN process modeling**, **Scrum methodology**, and **automated API testing**.

## 🚀 Features
- **Full CRUD functionality**: Create, Read, Update, and Delete users.
- **Persistence**: Data is stored in a local `users.json` file.
- **Error Handling**: Comprehensive validation for missing fields, duplicate IDs, and non-existent users.
- **Process Documentation**: Visualized workflow using BPMN 2.0 standards.

## 🛠️ Technology Stack
- **Backend:** Python, Flask
- **Database:** JSON (File-based persistence)
- **Design:** Camunda Modeler (BPMN 2.0)
- **Project Management:** Jira (Scrum)
- **Testing:** Postman

## 📊 Business Logic (BPMN)
The API workflow was designed prior to implementation to ensure robust logic.
![User Flow](./assets/user-flow.png)
*Figure 1: BPMN diagram of the User Creation process.*

## 📋 Project Management
This project was managed using **Scrum** in Jira.
- **Epics:** `Project Design & Documentation`, `Core API Development`
- **Tasks:** Modeled as User Stories with specific Acceptance Criteria.
- **Tracking:** Developed in a dedicated Sprint (USER-1 to USER-5).

## 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/users` | Get all users |
| **POST** | `/users` | Create a new user (requires `id`, `name`) |
| **PUT** | `/users/<id>` | Update an existing user's name |
| **DELETE** | `/users/<id>` | Remove a user by ID |

### Example Request (POST):
```json
{
    "id": 3,
    "name": "Jane Doe"
}

⚙️ Setup & Installation
Clone the repository.

Install dependencies: pip install flask

Run the application: python app.py

Access the API at http://127.0.0.1:5000/users