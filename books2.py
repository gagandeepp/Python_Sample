from typing import Optional
from fastapi import FastAPI, HTTPException,Request,status,Form,Header
from pydantic import BaseModel,Field
from uuid import UUID
from starlette.responses import JSONResponse


class NegativeNumberException(Exception):
    def __init(self,books_to_return):
        self.books_to_return = books_to_return


app = FastAPI()


class Book(BaseModel):
    id: UUID
    title:str = Field(min_length= 1)
    author:str = Field(min_length=1,max_length=100)
    description:Optional[str] = Field(title = "Description of the book",max_length=100,min_length=1)
    rating:int = Field(gt=1,lt=101)

    class Config:
        schema_extra = {
            "example":{
                "id":"",
                "title":"",
                "author":"",
                "description":""
            }
        }


class BookNoRating(BaseModel):
    id: UUID
    title:str = Field(min_length= 1)
    author:str = Field(min_length=1,max_length=100)
    description:Optional[str] = Field(title = "Description of the book",max_length=100,min_length=1)
    rating:int = Field(gt=1,lt=101)


BOOKS = []


@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request:Request,
                                            exception:NegativeNumberException):
    return JSONResponse(status_code=418,
                        content={"message":f"Hey do you want {exception.books_to_return}"})


@app.post("books/login")
async def book_login(username:str = Form(...),password:str = Form(...)):
    return {"username":username,"password":password}


@app.get("/header")
async def read_header(random_header:Optional[str]= Header(None)):
    return {"Random-Header":random_header}


@app.get("/")
async def read_all_books(books_to_return: Optional[int]=None):
    if len(BOOKS)<1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i =1
        new_books = []
        while i<= books_to_return:
            new_books.append((BOOKS[i-1]))
            i+=1
        return new_books
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise HTTPException(status_code=404, detail="Book not found",
                        headers={"X-Header-Error": "Nothing to be seen at the UUID"})


@app.get("/book/rating/{book_id}",response_model=BookNoRating)
async def read_book_no_rating(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise HTTPException(status_code=404, detail="Book not found",
                        headers={"X-Header-Error": "Nothing to be seen at the UUID"})


@app.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
async def update_book(book_id:UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter-1]= book
            return BOOKS[counter -1]


@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter = 0
    for x in BOOKS:
        if x.id == book_id:
            del BOOKS[book_id]
            return f"ID:{book_id} has been deleted"
    raise HTTPException(status_code=404,detail="Book not found",
                        headers={"X-Header-Error": "Nothing to be seen at the UUID"})


def create_books_no_api():
    book_1 = Book(id="",title="",author="",description="",rating=40)
