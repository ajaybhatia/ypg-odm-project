from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ODMForm

@login_required
def index(request):
	return render(request, 'odm_builder/index.html', {'form': ODMForm()})