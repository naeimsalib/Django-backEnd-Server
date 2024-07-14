# Project Summary

This project is a full-stack application that consists of a React frontend and a Django backend. The application allows users to manage a to-do list, with the ability to add, delete, and persist to-do items across sessions.

## Frontend (React)

The React frontend is structured with a focus on component-based architecture, making the code modular and reusable. The primary components in this project are:

1. **App Component (`App.js`)**:

   - This is the main component of the application. It manages the state of the to-do items and handles adding and deleting items.
   - It fetches the list of to-do items from the backend on component mount and renders the `ItemList` and `AddItemForm` components.
   - It includes the functions `addItem` and `deleteItem` to interact with the backend API for adding and deleting to-do items.

2. **ItemList Component (`ItemList.js`)**:

   - This component receives the list of to-do items as props and renders them.
   - It also includes a delete button for each item, allowing users to remove items from the list.

3. **AddItemForm Component (`AddItemForm.js`)**:
   - This component includes an input field and a button to add new to-do items.
   - It manages the input state and calls the `addItem` function from the `App` component when a new item is submitted.

### Frontend Folder Structure

FrontEnd
│
├── node_modules
├── public
├── src
│ ├── components
│ │ ├── AddItemForm.css
│ │ ├── AddItemForm.js
│ │ ├── ItemList.css
│ │ ├── ItemList.js
│ ├── App.css
│ ├── App.js
│ ├── index.css
│ ├── index.js
├── package.json

### Key Points

- **Component-Based Architecture**: The project uses React components to separate concerns and make the code more maintainable.
- **State Management**: The `App` component uses React's state to manage the list of to-do items.
- **API Integration**: Axios is used to interact with the Django backend, ensuring the to-do items are persisted in the database.

## Backend (Django)

The Django backend provides a RESTful API to manage the to-do items. It includes models, serializers, views, and URL configurations to handle the necessary operations.

### Key Components

1. **TodoItem Model** (`models.py`):

   - Represents a to-do item with a title and a timestamp for when it was created.

2. **TodoItem Serializer** (`serializers.py`):

   - Transforms the `TodoItem` model instances into JSON format for the API responses and vice versa.

3. **API Views** (`views.py`):

   - `TodoItemListCreate`: Handles GET requests to list all to-do items and POST requests to create a new to-do item.
   - `TodoItemDetail`: Handles GET, PUT, and DELETE requests for a single to-do item identified by its ID.

4. **URL Configuration** (`urls.py`):
   - Maps the API endpoints to the corresponding views.

### API Endpoints

1. **List and Create Todo Items (GET and POST)**

   - **Endpoint**: `/api/todos/`
   - **Methods**:
     - **GET**: Retrieves a list of all to-do items.
     - **POST**: Creates a new to-do item.

2. **Retrieve, Update, and Delete a Single Todo Item (GET, PUT, DELETE)**
   - **Endpoint**: `/api/todos/<int:pk>/`
   - **Methods**:
     - **GET**: Retrieves a single to-do item by its ID.
     - **PUT**: Updates a to-do item by its ID.
     - **DELETE**: Deletes a to-do item by its ID.

### Backend Folder Structure

backEnd
├── backend
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── todo
│ ├── migrations
│ │ ├── init.py
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── views.py
│ ├── urls.py
├── db.sqlite3
├── manage.py

### Key Points

- **Django REST Framework**: Used to create RESTful API endpoints.
- **Data Persistence**: The to-do items are stored in a SQLite database, ensuring data is persisted across page refreshes.
- **CORS Configuration**: The backend is configured to allow cross-origin requests from the frontend application.

## Summary

This project demonstrates a complete full-stack application with a React frontend and a Django backend. The React frontend showcases the use of components, state management, and API integration, while the Django backend provides RESTful API endpoints to manage to-do items, ensuring data persistence. The integration between the frontend and backend is achieved through Axios and proper CORS configuration, allowing seamless interaction between the two parts of the application.
