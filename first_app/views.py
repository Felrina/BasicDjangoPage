from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AcessRecord, Topic, Webpage
# Create your views here.


def index(request):
    webpages_list = AcessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    # my_dict = {'insert_me':"Hello I am from views.py!"}
    return render(request, 'first_app/index.html', context=date_dict)