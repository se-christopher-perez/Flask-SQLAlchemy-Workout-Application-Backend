# Flask-SQLAlchemy-Workout-Application-Backend

# Workout Tracker API

- A backend API for tracking workouts and exercises, built with Flask and SQLAlchemy.

- Practice building a backend architecture from scratch using Flask and SQLAlchemy.

- Apply all forms of validations to ensure clean and consistent data.

- Use Marshmallow schemas to serialize complex relationships and ensure request integrity.

- Define models, migrations, and seed data for a multi-table relational schema.

- Build API endpoints aligned with REST conventions and real-world use cases.

- Gain confidence managing app structure, commits, and GitHub repo organization.

## What it does

- Create, view, and delete workouts

- Create, view, and delete exercises

- Add exercises to workouts with sets, reps, or duration

## Tools Used

- Python 3.8.13

- Flask

- Flask-SQLAlchemy

- Flask-Migrate

- Marshmallow

- SQLite

## Installation

- git clone <your-repo-url>

- cd <your-repo-name>

## Move into the server folder and set up the database

- cd server

- pipenv run flask db upgrade head

- pipenv run python seed.py

## Start the server

- pipenv run flask run --port=5555

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | /workouts | Get all workouts |
| GET | /workouts/<id> | Get one workout |
| POST | /workouts | Create a workout |
| DELETE | /workouts/<id> | Delete a workout |
| GET | /exercises | Get all exercises |
| GET | /exercises/<id> | Get one exercise |
| POST | /exercises | Create an exercise |
| DELETE | /exercises/<id> | Delete an exercise |
| POST | /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises | Add an exercise to a workout |