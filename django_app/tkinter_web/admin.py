from django.contrib import admin

from tkinter_web.models import ExecutionLog, Script

admin.site.register([Script, ExecutionLog])
