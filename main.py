from fastapi import FastAPI, Request, HTTPException, Response
from schema import BookResponse
from uuid_extension import uuid7
from datetime import datetime
from models.book import Book
from typing import Any
#from models.customer import User

app = FastAPI(title="Library Management System", root_path="/api/v1")

timestamp = datetime.utcnow().isoformat() +'Z'

@app.get("/")
def home():
    return {"message": "Welcome to my Library Management System"}

@app.get("/books")
def get_booklist():
    return {"message": "These are the list of books in the library"}

@app.get("/books/{book_id}", response_model= BookResponse)
def get_book(book_id:str):
    for books in Book:
        if books.get("id") == book_id:
            return {"book": book_id}
        
    raise HTTPException(status_code = 404)
    # return {"message": "This is the book details"}

@app.post("/books")
def create_book(request: Request):
    body = request.json()
    new: Any = {
        "book_id": str(uuid7),
        "title": body.get("title"),
        "author": body.get("author"),
        "issn_or_isbn": body.get("author"),
        "publisher": body.get("publisher"),
        "book_amount": body.get("book_amount"),
        "created_at": timestamp
    }
    Book.append(new)
    return {"book": new}

@app.put("/books/{book_id}")
def update_booklist(book_id: str, body: dict[str, Any]):
    for index, book in enumerate(Book):
        if book.get("id") == book_id:
            updated: Any = {
                "book_id": str(uuid7),
                "title": body.get("title"),
                "author": body.get("author"),
                "issn_or_isbn": body.get("author"),
                "publisher": body.get("publisher"),
                "book_amount": body.get("book_amount"),
                "created_at": book.get("created_at")
            }
            Book[index] = updated
        
        return {"book": updated}

    raise HTTPException(status_code=404)     

@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    for index, book in enumerate(Book):
        if book.get("id") == book_id:
            book.pop(index)
        return Response(status_code = 204)
    raise HTTPException(status_code=404) 