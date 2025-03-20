
from django.contrib import admin
from django.urls import path
from restapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('starterpage/', views.starterpage, name='starter-page'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('chefs/', views.chefs, name='chefs'),
    path('specials/', views.specials, name='specials'),
    path('events/', views.events, name='events'),
    path('login/', views.login_view, name='login'),
    path('', views.register, name='register'),
    path('contact/', views.contact1, name='contact'),
    path('table/', views.table1, name='table'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),






]
