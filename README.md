# <p align = "center"> Book Store </p>

## <p align = "center"> This is a dynamic Book Store made in Fast API Framework. </p>

# <p align = "center"> Setup your local server </p>

1. Clone the repository:

```CMD
git clone https://github.com/anshumannandan/BookStore_Fast
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Navigate to the project directory: 

```CMD
cd BookStore_Fast
```

3. Install & Create a virtual environment:

```CMD
pip install virtualenv
virtualenv venv
```

4. Activate the virtual environment:
```CMD
windows : venv/scripts/activate
mac/linux : source venv/bin/activate
```

5. Install the dependencies: 

```CMD
pip install -r requirements.txt
```

6. Setup .env file in root directory with the following variables:
```
DB_URL=postgresql://user:password@server/db
```

7. Create a PostgreSQL database and connect it by entering credentials in .env file, once connected run the migrate command:
```CMD
alembic upgrade head
```

8. Run the backend server on localhost:

```CMD
uvicorn api.main:app --reload
```

You can access the endpoints from your web browser following this url:
```url
http://127.0.0.1:8000
```

For interactive documentation, go to:
```url
http://127.0.0.1:8000/docs
```


# <p align = "center"> Key Features </p>

### <p align = "center"> Add a new book </p>
### <p align = "center"> Retrieve the details of a specific book </p>
### <p align = "center"> Update the details of a specific book </p>
### <p align = "center"> Delete a specific book </p>
### <p align = "center"> Retrieve details of all books </p>
### <p align = "center"> Retrieve details of all books sorted by their average ratings, highest first </p>
### <p align = "center"> Add a new rating for a book (a user can only rate a book once) </p>
### <p align = "center"> Retrieve all ratings for a specific book </p>