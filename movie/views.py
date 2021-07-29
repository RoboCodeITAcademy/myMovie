from django.shortcuts import render
from django.views.generic import  (
    TemplateView,
    ListView
    )
from .models import Rubrics, Movie
# Create your views here.
def get_all_rubrics(request):
    context = {
        'rubrics':Rubrics.objects.all()
    }
    return context

class MovieListView(ListView):
    model = Movie
    template_name = 'index.html'