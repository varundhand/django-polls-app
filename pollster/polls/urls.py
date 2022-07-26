from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path('route', views.functionName, name="functionName")
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('myPractise', views.practise, name = 'practise'),
    path('<int:question_id>/', views.detail, name='detail')
    # path('<int:question_id>/results/',views.results,name='results')
]

# This file defines the routes/urls asscociated with the /polls route
# The second parameter (views.index) specifies the function to be run from the views file
# That function in the views file will render a template on that particular url
