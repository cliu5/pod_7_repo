from django.urls import path
from myapp.views import hello, goodbye

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # myapp/name
    path('<str:name>', hello, name='hello_name'),
    # myapp/goodbye/name
    path('goodbye/<str:name>', goodbye, name='goodbye_name')
]
