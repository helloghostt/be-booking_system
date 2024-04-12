from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Court

@login_required
def court_list(request):
    courts = Court.objects.all()
    return render(request, 'courts/court_list.html', {'courts': courts})