from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import AuthorList, AuthorDetail, BookList, BookDetail

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/authors/', AuthorList.as_view(), name='author_list'),
    path('api/authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]
