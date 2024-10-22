from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date,})

def convert_dates(date):
    # Function that gets the weekday number for the date.
    day_number = date.weekday()  # Use the date object directly to get the weekday
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request, past_date):

    try:

        # Convet data from the string Url
        date = dt.datetime.strptime(past_date, '%d-%m-%Y').date()


    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date":date, "news":news}) 

def news_today(request):
    date = dt.date.today()
    news = Article.today_news()
    return render(request, 'all-news/today-news.html', {"date": date, "news":news})