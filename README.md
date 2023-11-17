# Django Rest Framework (DRF) Post CRUD Application

This Django Rest Framework application allows users to perform CRUD operations on posts. It includes authentication, ownership enforcement, email notifications on post creation, and advanced permissions.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework

### Installation


1. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    pip install -r requirements.txt
    ```

2. Apply migrations:

    ```bash
    python manage.py migrate
    ```

3. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the DRF API at http://localhost:8000/api/posts/

## API Endpoints

- `GET /api/posts/`: Retrieve a list of all posts.
- `POST /api/posts/`: Create a new post owned by the authenticated user.
- `GET /api/posts/<int:pk>/`: Retrieve a single post by ID.
- `PUT /api/posts/<int:pk>/`: Update a single post owned by the authenticated user.
- `DELETE /api/posts/<int:pk>/`: Delete a single post owned by the authenticated user.

## Authentication and Permissions

- Regular users can CRUD their own posts.
- Superusers have full access to all posts and can update or delete any post.

## Advanced Features

- Nested serializer to include the author's username and email when retrieving a single post.
- Filtering posts by title, body, and author using query parameters on the GET /api/posts/ endpoint.
- Pagination for the GET /api/posts/ endpoint.
- Rate limiting to prevent abuse of the API.
- API for filtering posts by author.

## Django Signals

- Email notifications are sent to the author whenever a new post is created.

## Contributing

If you would like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.



