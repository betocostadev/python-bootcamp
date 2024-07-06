# Python FastAPI - Workout API

A simple API to track workouts

## Running it

There is a Makefile in the root folder to keep the commands simples.

To start the API run `make run` or use `uvicorn workout_api.main:app --reload` from the workout main folder

Then you can access the [docs here](http://127.0.0.1:8000/docs)


### Run the Container

Run the commands in the application folder
Build the Docker Image

```docker build --pull -t workout .```


With the image create you can just use Dockercompose

```docker compose up```

Then, open another terminal window and run Postgres

```docker compose exec db psql -U postgres```