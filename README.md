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
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/6c216c96-4a52-42a2-b110-6a3b9b3b7a2b)

### <p align = "center"> Retrieve the details of a specific book </p>
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/1299fbc6-8c20-41aa-9232-50ea8f9bd20b)

### <p align = "center"> Update the details of a specific book </p>
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/b9dfe56c-3780-472b-9caf-66a96dd96c0c)

### <p align = "center"> Delete a specific book </p>
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/0464fbeb-014e-42e4-b5d9-2d077862a08a)

### <p align = "center"> Retrieve details of all books </p>
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/51a40927-59d5-44df-acc9-3a17e077b058)

### <p align = "center"> Retrieve details of all books sorted by their average ratings, highest first </p>
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/cad7b1f5-dbf1-4da1-9166-567b015674f6)

### <p align = "center"> Add a new rating for a book (a user can only rate a book once) </p>
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/d4a3754f-20b8-4004-a99b-3c6ad0c9f002)
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/6e9d0f9e-2a5e-492a-a1b4-ebe803339a8f)

### <p align = "center"> Retrieve all ratings for a specific book </p>
![image](https://github.com/anshumannandan/BookStore_Fast/assets/93365821/e9b407df-f480-4293-8357-9f73b7dab790)
