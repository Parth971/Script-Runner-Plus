from django.db import models


class Script(models.Model):
    object = None
    name = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'script'


class ExecutionLog(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE)
    output = models.TextField()
    execution_started_at = models.DateTimeField()
    execution_completed_at = models.DateTimeField()
    execution_time = models.FloatField()


    class Meta:
        db_table = 'execution_log'
