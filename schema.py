from pydantic import BaseModel, EmailStr, field_validator, Field
import re


class UserCreate(BaseModel):
    username: str = Field(examples="arit", min_length=4, max_length=15, description="Username must be 4-15 characters")
    email: EmailStr
    password: str = Field(min_length=12, description="Password must be at least 12 characters")


    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str):
        if not re.match(r"^[a-zA-Z0-9_-]+$", value):
            raise ValueError("Username can only contain letters, numbers, underscores and hypens")
        return value.strip()

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str):
        if len(value) < 12:
            raise ValueError("Password must be at least 12 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        return value

class Googlesignup(BaseModel):
    google_auth_url: str 


class BookResponse(BaseModel):
    book_id: str
    title: str
    author: str