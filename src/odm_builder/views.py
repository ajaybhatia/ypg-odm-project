from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ODMForm
from .models import Build

from subprocess import call

@login_required
def index(request):
	if request.method == 'POST':
		form = ODMForm(request.POST, request.FILES)
		if form.is_valid():
			build = form.save(commit=False)
			build.user = request.user
			
			# Main Logic goes here
			build_file_name = build.target_file
			target_file_name = build.buildprop_file
			'''
			export target_file_name="p7201-target_files-1474857792.zip"
			export mmx_key_path="/home/gursimran/YUClosed/vendor/yuos/security/yuos_keys"
			export path_of_target_file="/home/gursimran/ODM/tinno/dist"
			export new_path_of_signed_target_files="/home/gursimran/YUClosed"
			export OS_Android_version="MM-6.0.1"
			export Build_ID="MMB30K"
			export mmx_build_version="MMXMR1.0"
			export target_product="jalebi"
			'''

			build.save()
			return redirect('/builder/home/')
	else:
		form = ODMForm()

	return render(request, 'odm_builder/index.html', {'form': form})