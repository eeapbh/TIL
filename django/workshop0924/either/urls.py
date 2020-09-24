from django.urls import path
from . import views
app_name = 'either'
urlpatterns = [
    path('',views.index, name='index'),
    path('create_question/', views.create_question, name='create_question'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('<int:question_pk>/create_comment/', views.create_comment, name='create_comment'),
]
