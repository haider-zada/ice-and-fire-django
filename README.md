# iceandfire
After successfully clonning the project follow these steps to setup the project.
* Create a database in mysql with anyname.
* update settings.py file in iceandfire directory.
Go to line #82 change db name, db password and port if required
* Now create a virtualenv with python version 3.7
* I am assuming that you are in project root dir and os is linux
activate your virtual environment.
```
source venv/bin/activate
pip install -r requiremnets.txt
```
* After successful installation. Apply migrations.
```
python manage.py migrate
```

* Create django-admin
```
python manage.py createsuperuser
```

* Run Server
```
python manage.py runserver
```
* API end points with v1 are using api-views and v2 are using view-sets.

##For Ice&Fire Api
```
GET http://localhost:8000/api/external-books?name=A Game of Thrones
```

##Create Country
```
POST http://localhost:8000/api/v2/country/
Request_body--> {
	"name" : "china"
}
```

##List of Countries
```
GET http://localhost:8000/api/v2/country/
```

##Country by id
```
GET http://localhost:8000/api/v2/country/:id/
```

##Update Country
```
Patch http://localhost:8000/api/v2/country/:id/
```

##Delete Country
```
Delete http://localhost:8000/api/v2/country/:id/
```

##List Of Books
```
GET http://localhost:8000/api/v1/books/
```

##Book by id
```
GET http://localhost:8000/api/v1/books/:id/
```

##Create Book
```
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
```    

##Update Book
In body provide the fields you want to update
```
PATCH http://localhost:8000/api/v1/books/:id/
```

#Delete Book
```
DELETE http://localhost:8000/api/v1/books/:id/
```

#Filter Book
It is a generic filter you can filter on name, on name and year and publisher
```
POST http://localhost:8000/api/v1/books/filter/
body --> {
    "year":1996
}
```

##List Of Books
```
GET http://localhost:8000/api/v2/books/
```

##Book by id
```
GET http://localhost:8000/api/v2/books/:id/
```

##Create Book
```
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
```

##Update Book
In body provide the fields you want to update
```
PATCH http://localhost:8000/api/v2/books/:id/
```

##Delete Book
```
DELETE http://localhost:8000/api/v2/books/:id/
```
