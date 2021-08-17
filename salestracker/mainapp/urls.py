from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    

]