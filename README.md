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
