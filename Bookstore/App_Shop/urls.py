from django.urls import path
from App_Shop import views

app_name = "App_Shop"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),  # using class based view
    path("product/<pk>",views.productDetail.as_view(), name="product_detail"),
]
