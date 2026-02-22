from django.shortcuts import render
from news.models import News
# Create your views here.
def index(request):
    latest_news = News.objects.filter(
        is_published=True
    ).order_by('-date')[:5]

    context = {
        "latest_news": latest_news,
    }
    return render(request, 'core/index.html', context)