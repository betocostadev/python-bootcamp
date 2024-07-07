# Python FastAPI Mongo DB TDD Project

Study repository used to create a FastAPI backend following TDD Practices.

Based on DIO Python AI Backend developer course.

## Run this project

This project was created using [Poetry](https://python-poetry.org/docs/)

This application was created using MongoDB with a DB deployed on [MongoDB Atlas](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.mongodb.com/cloud/atlas/register&ved=2ahUKEwiE78e62pWHAxUiq5UCHQNGAWkQFnoECBsQAQ&usg=AOvVaw3mU3hWr0cPxZD5dJY86xtR). To run the application and execute the tests, you'll need to create a DB, and add a `.env` file in the application root with the following environment variable:

```shell
DATABASE_URL="mongodb+srv://user-your-mongodb-url/?uuidRepresentation=standard"
```

Then, you'll use Docker to run you DB instance connected to MongoDB Cloud.
If you want to use only a local instance, feel free to use it.

To start run `poetry shell` to select the environment.

It should select the tdd project environment

Then run `poetry install` to install the project dependencies.

After you've set up the installation, run the project with:

```
make container up
```
This will run the docker container with MongoDB (Using an instance compatible with Macs using Apple Sillicon)

Then run in another instance of the terminal:

```
make test
```
