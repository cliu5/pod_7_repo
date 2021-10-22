from django.urls import path
from myapp.views import hello
from myapp.views import goodbye

urlpatterns = [
    path('', goodbye, name='goodbye'),
    # myapp/
    path('', hello, name='hello'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name')
]