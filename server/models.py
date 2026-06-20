from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here

class Excercise(db.Model):

    __tablename__ = 'excercise'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    category = db.Column(db.String, nullable = False)
    equipment_needed = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return f"<Exercise id={self.id} name={self.name}>"

class Workout(db.Model):

    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable = False)
    duration_min = db.Column(db.Integer, nullable = False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"<Workout id={self.id} date={self.date} duration={self.duration_min}>"

class WorkoutExercise(db.Model):

    __tablename__ = 'workout_exercise'

    id = db.Column(db.Integer, primary_key = True)
    workout_id = db.Column(db.Interger, db.ForeignKey('workouts.id'), nullable = False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable = False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_sec = db.Column(db.Integer)

    def __repr__(self):
        return f"<WorkoutExercise workout={self.workout_id} excercise={self.exercise_id}>"