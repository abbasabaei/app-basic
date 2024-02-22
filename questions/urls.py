from django.urls import path
from . import views
app_name = 'questions'
urlpatterns=[
    path('',views.index,name='index'),
    path('<questiontext>/', views.process_response, name='process_response'),
    path('send_email/<ismail>/<issms>', views.send_email, name='send_email'),
]