from django.views.generic import TemplateView

from tkinter_web.models import Script, ExecutionLog


class TkinterHomeView(TemplateView):
    template_name = 'tkinter_web/home.html'

    def get_context_data(self, **kwargs):
        scripts = Script.objects.all()
        logs = ExecutionLog.objects.all()
        kwargs['scripts'] = scripts
        kwargs['logs'] = logs
        return super().get_context_data(**kwargs)
