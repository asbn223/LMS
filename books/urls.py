from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books import views

# router = DefaultRouter()
# router.register('books', views.BookViewSet)
app_name = 'books'

urlpatterns = [
    path('book/', views.BookList.as_view()),
    path('book/create/', views.BookCreate.as_view()),
    path('book/<int:id>/', views.BookRetrieveUpdateDestroy.as_view()),
    path('user-login/',views.CreateTokenView.as_view()),
    # path('', include(router.urls)),
]