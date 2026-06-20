from marshmallow import Schema, fields, validates, ValidationError

from models import Exercise, Workout, WorkoutExercise

class ExerciseSchema(Schema):
    
    id = fields.Int(dump_only = True)
    name = fields.Str(required = True)
    category = fields.Str(required = True)
    equipment_needed = fields.Bool(load_default = False)

    @validates('name')
    def validate_name(self, value):
        if not value or value.strip() == '':
            raise ValidationError("Name can't be empty or blank")
        
    @validates('category')
    def validate_category(self, value):
        categories = ['Strength', 'Cardio', 'Flexibility', 'Balance']

        if value not in categories:
            raise ValidationError(f"Acceptable Categories: {', '.join(categories)}.")

class WorkoutExerciseSchema(Schema):

    id = fields.Int(dump_only = True)
    workout_id = fields.Int(dump_only = True)
    exercise_id = fields.Int(dump_only = True)
    reps = fields.Int(load_default = None)
    sets = fields.Int(load_default = None)
    duration_sec = fields.Int(load_default = None)
    exercise = fields.Nested(lambda: ExerciseSchema(only = ('id', 'name', 'category')), dump_only = True)

class WorkoutSchema(Schema):
    
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_min = fields.Int(required=True)
    notes = fields.Str(load_default=None)
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()