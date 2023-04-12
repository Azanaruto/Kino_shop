from django.urls import path
from . import views 

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from store.views import*



app_name = 'store'

urlpatterns = [
	path('', views.index, name = "index"),
	path('login', views.signin, name="signin"),
	path('logout', views.signout, name="signout"),
	path('registration', views.registration, name="registration"),
	path('book/<int:id>', views.get_book, name="book"),
	path('books', views.get_books, name="books"),
	path('category/<int:id>', views.get_book_category, name="category"),
	path('writer/<int:id>', views.get_writer, name = "writer"), 
	
	path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),

	path('update/<int:pk>', views.UserUpdate.as_view()),
	path('delete/<int:pk>', views.UserDelete.as_view()),
	path('create/<int:pk>', views.UserCreate.as_view()),
	
	#path('users/', views.UserUpdate.as_view()),
	#path('delete/', views.UserDestroy.as_view()),
    #path('delete/<int:pk>', views.UserDestroy.as_view()),
    #path('update/', views.UserUpdate.as_view()),
    #path('update/<int:pk>', views.UserUpdate.as_view()),
	#path('users/', views.UserAPILIst.as_view()),
	# path('destroy/<int:pk>', views.RetrieveDestroyAPIView.as_view()),
	#path('users/<int:pk>/', views.UserUpdate.as_view(), name='user-update'),
]



urlpatterns = format_suffix_patterns(urlpatterns)
