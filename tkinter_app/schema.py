from peewee import Model, CharField, ForeignKeyField, DateTimeField, FloatField

from configs import db


class Script(Model):
    name = CharField()
    content = CharField()

    class Meta:
        database = db
        db_table = 'script'


class ExecutionLog(Model):
    script = ForeignKeyField(Script, backref='executions')
    output = CharField()
    execution_started_at = DateTimeField()
    execution_completed_at = DateTimeField()
    execution_time = FloatField()

    class Meta:
        database = db
        db_table = 'execution_log'