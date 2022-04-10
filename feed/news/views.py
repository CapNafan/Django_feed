from django.shortcuts import render
from django.contrib import admin
from .models import NewsItem
from .forms import NewsForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def list_news(request):
    per_page = request.GET.get('per_page', 10)
    items = NewsItem.objects.order_by("-publish_date")
    paginator = Paginator(items, per_page)
    page_number = request.GET.get('page')

    try:
        paginated = paginator.get_page(page_number)
    except PageNotAnInteger:
        paginated = paginator.get_page(1)
    except EmptyPage:
        paginated = paginator.page(paginator.num_pages)

    return render(request, 'news/list.html', context={'items': paginated, 'per_page': per_page})


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
