# Python FastAPI Mongo DB TDD Project

Study repository used to create a FastAPI backend following TDD Practices.

Based on DIO Python AI Backend developer course.

## Run this project

This project was created using [Poetry](https://python-poetry.org/docs/)

This application was created using MongoDB with a DB deployed on [MongoDB Atlas](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.mongodb.com/cloud/atlas/register&ved=2ahUKEwiE78e62pWHAxUiq5UCHQNGAWkQFnoECBsQAQ&usg=AOvVaw3mU3hWr0cPxZD5dJY86xtR). To run the application and execute the tests, you'll need to create a DB, and add a `.env` file in the application root with the following environment variable:

```shell
DATABASE_URL="mongodb+srv://user:password@your-mongodb-url/?uuidRepresentation=standard"
```

Then, you'll use Docker to run you DB instance connected to MongoDB Cloud.

If you want to use only a local instance of MongoDB with Docker, feel free to use it.
For this, you'll need to add some configuration to `docker-compose.yml` file to add your MongoDB URL, user, and password.

To start run `poetry shell` to select the environment.

It should select the tdd project environment

Then run `poetry install` to install the project dependencies.


### Running with a local instance of MongoDB (Docker)

After you've set up the installation, if you are going to use a local instance of MongoDB, run the project with:

```
make container up
```
This will run the docker container with MongoDB (Using an instance compatible with Macs using Apple Sillicon)

### Running the application

You can run the application using:

```
make run
```

Access `http://127.0.0.1:8000/docs` to check the documentation.
There are endpoints for products like query, get by id, delete, etc.

### Running tests

Run all the tests with:

```
make test
````

Run a single test with:

````
make test-matching K=test_name
````
