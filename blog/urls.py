from django.urls import path
from blog.views.views import HomeView, PostDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]