from django.urls import path,include
from . import views
urlpatterns=[
	path('textEditor/',views.textEditor,name='textEditor'),
]