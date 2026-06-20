#!/usr/bin/env python3

from app import app
from models import *
from datetime import date

with app.app_context():

	WorkoutExercise.query.delete()
	Workout.query.delete()
	Exercise.query.delete()

	db.session.commit()

	squat = Exercise(name = 'Barbell Squat', category = 'Strength', equipment_needed = True)
	run = Exercise(name = 'Treadmill Run', category = 'Cardio', equipment_needed = True)

	db.session.add_all([squat, run])

	db.session.commit()

	workout_1 = Workout(date = date(2024, 6, 1), duration_min = 60, notes = 'morning workout')
	workout_2 = Workout(date = date(2024, 6, 3), duration_min = 90, notes = 'night workout')

	db.session.add_all([workout_1, workout_2])

	db.session.commit()

	workout_exercise_1 = WorkoutExercise(workout_id = workout_1.id, exercise_id = squat.id, sets = 3, reps = 10)
	workout_exercise_2 = WorkoutExercise(workout_id = workout_2.id, exercise_id = run.id, duration_sec = 2000)

	db.session.add_all([workout_exercise_1, workout_exercise_2])

	db.session.commit()

	print("🌱 Seeded 🌱")
