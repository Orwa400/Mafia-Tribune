from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    date = dt.date.today()

    # Function to convert date object to find the exact day
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
    '''
    return HttpResponse(html)

def convert_dates(date):
    # Function that gets the weekday number for the date.
    day_number = date.weekday()  # Use the date object directly to get the weekday
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day
