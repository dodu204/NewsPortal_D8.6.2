from django.urls import path
from django.contrib.auth.views import LogoutView
from allauth.account.views import LoginView, LogoutView, SignupView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ProfileUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(template_name='registration/signup.html'), name='signup'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]