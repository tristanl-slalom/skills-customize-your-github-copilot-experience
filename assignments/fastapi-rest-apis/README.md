# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a complete REST API using the FastAPI framework to manage a simple book library system. This assignment will introduce you to modern web API development, HTTP methods, data validation, and API documentation.

## 📝 Tasks

### 🛠️ Basic API Setup

#### Description
Set up a FastAPI application with basic configuration and create your first endpoint to ensure the framework is working correctly.

#### Requirements
Completed program should:

- Install FastAPI and required dependencies using pip
- Create a main.py file with a FastAPI application instance
- Implement a root endpoint that returns a welcome message
- Start the development server and verify the API is accessible
- Access the automatic API documentation at /docs endpoint

### 🛠️ Book Management Endpoints

#### Description
Create a complete set of CRUD (Create, Read, Update, Delete) endpoints to manage books in your library system.

#### Requirements
Completed program should:

- Define a Book model with fields: id, title, author, year_published, and genre
- Implement POST /books endpoint to add new books
- Implement GET /books endpoint to retrieve all books
- Implement GET /books/{book_id} endpoint to retrieve a specific book
- Implement PUT /books/{book_id} endpoint to update book information
- Implement DELETE /books/{book_id} endpoint to remove books
- Use proper HTTP status codes for all responses
- Include data validation for all input fields

### 🛠️ Advanced Features

#### Description
Enhance your API with additional features like filtering, error handling, and response models.

#### Requirements
Completed program should:

- Add query parameters to filter books by author or genre
- Implement proper error handling with meaningful error messages
- Return appropriate HTTP status codes (200, 201, 404, 422)
- Use Pydantic models for request and response validation
- Add at least 5 sample books to test your endpoints
- Document your API endpoints with descriptions and examples