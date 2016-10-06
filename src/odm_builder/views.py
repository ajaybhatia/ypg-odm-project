from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ODMForm
from .models import Build

@login_required
def index(request):
	if request.method == 'POST':
		form = ODMForm(request.POST, request.FILES)
		if form.is_valid():
			print(form)
			build_file_name = request.FILES['buildprop_file']
			target_file_name = request.FILES['target_file']
			build = form.save(commit=False)
			build.user = request.user
			build.save() 
			return redirect('/')
	else:
		form = ODMForm()

	return render(request, 'odm_builder/index.html', {'form': form})