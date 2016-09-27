from django.test import TestCase
from .forms import ODMForm

def index(request):
	return render(request, 'index.html')