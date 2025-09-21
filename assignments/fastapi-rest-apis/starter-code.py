from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI instance
app = FastAPI(
    title="Book Library API",
    description="A simple REST API to manage a book library",
    version="1.0.0"
)

# Pydantic models for data validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    year_published: int
    genre: str

class BookCreate(BaseModel):
    title: str
    author: str
    year_published: int
    genre: str

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year_published: Optional[int] = None
    genre: Optional[str] = None

# In-memory storage (in a real app, you'd use a database)
books_db = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960, "genre": "Fiction"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year_published": 1949, "genre": "Dystopian Fiction"},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "year_published": 1813, "genre": "Romance"},
]

# TODO: Implement the following endpoints:

@app.get("/")
async def root():
    """
    Welcome endpoint
    TODO: Return a welcome message for your API
    """
    pass

@app.get("/books", response_model=List[Book])
async def get_books(author: Optional[str] = None, genre: Optional[str] = None):
    """
    Get all books, with optional filtering by author or genre
    TODO: Implement this endpoint
    """
    pass

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """
    Get a specific book by ID
    TODO: Implement this endpoint
    """
    pass

@app.post("/books", response_model=Book, status_code=201)
async def create_book(book: BookCreate):
    """
    Create a new book
    TODO: Implement this endpoint
    """
    pass

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_update: BookUpdate):
    """
    Update an existing book
    TODO: Implement this endpoint
    """
    pass

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """
    Delete a book by ID
    TODO: Implement this endpoint
    """
    pass

# Helper function to find book by ID
def find_book_by_id(book_id: int):
    """
    Helper function to find a book by its ID
    TODO: Implement this helper function
    """
    pass

# To run the server, use: uvicorn main:app --reload