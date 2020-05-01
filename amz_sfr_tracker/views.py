from django.shortcuts import render



def index(request):
    return render(request, 'amz_sfr_tracker/index.html')
