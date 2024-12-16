
from django.contrib import admin
from django.urls import path
from bizzzapp import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('index/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('quote/', views.quote, name='quote'),
    path('pricing/', views.pricing, name='pricing'),
    path('details/', views.details, name='details'),
    path('services/', views.services, name='services'),
    path('starterpage/', views.starterpage, name='starterpage'),
    path('show/', views.show, name='show'),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]
