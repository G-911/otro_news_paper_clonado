from django.views.generic import ListView
from django.shortcuts import render
from .models import Article
# Create your views here idiot.

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"