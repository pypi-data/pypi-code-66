
from django.urls import path

from customers import views

app_name = 'customers'


urlpatterns = [

    path('<int:customer_id>/details/', views.get_customer_detail,
         name='detail')

]
