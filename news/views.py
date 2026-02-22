from django.shortcuts import get_object_or_404, render

from .models import News

# Create your views here.
def news_list(request):
    news = News.objects.all()

    context = {
        'news_list': news
    }

    return render(request, 'news_list.html', context)

def news_detail(request, text_slug):
    news = get_object_or_404(News, url=text_slug)

    context = {
        'news': news
    }

    return render(request, 'news_detail.html', context)