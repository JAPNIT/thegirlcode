
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

#Home Page
def home(request):
    return render(request, 'TheGirlCode/landingpage.html')
