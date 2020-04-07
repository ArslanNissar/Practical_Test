
# Create your views here.
from django.http import HttpResponse
from .models import Story
from django.shortcuts import render
from django.template import loader

def index(request):

    latest_news = Story.objects.order_by('-pub_date')[:5]

    template = loader.get_template('newsApp/index.html')

    context = {
            'latest_news': latest_news,
    }

    return render(request, 'newsApp/Index.html', context)
    #return HttpResponse("News")



