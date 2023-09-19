from django.urls import path

from tkinter_web.views import TkinterHomeView

urlpatterns = [
    path('', TkinterHomeView.as_view(), name='tkinter-home'),
]
