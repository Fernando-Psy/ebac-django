from django.http import HttpResponse
from django.views import generic
from blog.models.models import Post

class HomeView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'home.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'