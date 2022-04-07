from django.shortcuts import render
from django.contrib import admin
from .models import NewsItem
from .forms import NewsForm
from django.http import HttpResponseRedirect


def list_news(request):
    items = NewsItem.objects.order_by("-publish_date")
    return render(request, 'news/list.html', context={'items': items})


def add_news(request):
    submitted = False
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_news?submitted=True')
    else:
        form = NewsForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'news/add_news.html', {'form': form, 'submitted': submitted})
