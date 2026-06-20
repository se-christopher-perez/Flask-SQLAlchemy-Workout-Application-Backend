from marshmallow import Schema, fields

from models import Excercise, Workout, WorkoutExercise

class ExcerciseSchema(Schema):
    
    id = fields.Int(dump_only = True)
    name = fields.Str(required = True)
    category = fields.Str(required = True)
    equipment_needed = fields.Bool(load_default = False)

class WorkoutExerciseSchema(Schema):

    id = fields.Int(dump_only = True)
    workout_id = fields.Int(dump_only = True)
    excercise_id = fields.Int(dump_only = True)
    reps = fields.Int(load_default = None)
    sets = fields.Int(load_default = None)
    duration_sec = fields.Int(load_default = None)
    excercise = fields.Nested(lambda: ExcerciseSchema(only = ('id', 'name', 'category')), dump_only = True)

class WorkoutSchema(Schema):
    id = fields.Int(dump_only = True)
    date = fields.Date(required = True)
    duration_min = fields.Int(required = True)
    notes = fields.Str(load_default = None)
    workout_exercise = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only = True)
    excercises = fields.List(fields.Nested(ExcerciseSchema(only = ('id', 'name', 'category'))), dump_only = True)
