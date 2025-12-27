from fastapi import FastAPI
from schema import BookResponse

app = FastAPI(title="Library Management System", root_path="/api/v1")


@app.get("/")
def home():
    return {"message": "Welcome to my Library Management System"}


def create_user():
    pass

def get_user():
    pass

@app.get("/books")
def get_booklist():
    return {"message": "These are the list of books in the library"}

@app.get("/books/{book_id}", response_model= BookResponse)
def get_book(book_id:str):
    return {"message": "This is the book details"}


