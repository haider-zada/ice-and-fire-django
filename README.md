# iceandfire
codingtask
After successfully clonning the project follow these steps to setup the project.
Create a database in postgres with anyname.
update settings.py file in iceandfire directory.
go to line #82 change db name, db password and port if required
Now create a virtualenv with python version 3.7
I am assuming that you are in project root dir and os is linux
activate your virtual environment by writting (source venv/bin/activate)
on terminal write pip install -r requiremnets.txt
Now its time to migrate all the migrations so type (python manage.py migrate) (assuming virtual env is activated)
now write a command on terminal python manage.py runserver (default port is 8000)

#ForIceFire Api
GET http://localhost:8000/api/external-books?name=A Game of Thrones

#Local Books V1 using API-Views

#List Of Books
GET http://localhost:8000/api/v1/books/
#Book by id
GET http://localhost:8000/api/v1/books/:id/
#Create Book
POST http://localhost:8000/api/v1/books/
request_body --> {
        "name": "Game",
        "isbn": "978-0553103544",
        "authors": [
            "George R. R. Martin"
        ],
        "number_of_pages": 694,
        "publisher": "Bantam Books",
        "country": "United States",
        "release_date": "1996-08-01"
    }
#Update Book
PATCH http://localhost:8000/api/v1/books/:id/
In body provide the fields you want to update
#Delete Book
DELETE http://localhost:8000/api/v1/books/:id/
#Filter Book
POST http://localhost:8000/api/v1/books/filter/
body --> {
    "year":1996
}

It is a generic filter you can filter on name, on name and year and publisher

#Local Books V2 using ViewSet

#List Of Books
GET http://localhost:8000/api/v2/books/
#Book by id
GET http://localhost:8000/api/v2/books/:id/
#Create Book
POST http://localhost:8000/api/v2/books/
request_body --> {
        "name": "Tom $ Jerry",
        "isbn": "978-0553103555",
        "authors": [
            "George R. R. Martin"
        ],
        "number_of_pages": 694,
        "publisher": "Bantam Books",
        "country": "United States",
        "release_date": "1997-08-01"
    }
#Update Book
PATCH http://localhost:8000/api/v2/books/:id/
In body provide the fields you want to update
#Delete Book
DELETE http://localhost:8000/api/v2/books/:id/

