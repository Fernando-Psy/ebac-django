from django.http import HttpResponse
from django.views import generic

class HomeView(generic.View):
    def get(self, request):
        return HttpResponse("Hello, world! This is the home page.")