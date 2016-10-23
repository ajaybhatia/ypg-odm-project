from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import ODMForm
from .models import Build

from subprocess import call, Popen, PIPE
from os.path import dirname, join, exists

# Use 12factor inspired environment variables or from a file
import environ

@login_required
def index(request):
	if request.method == 'POST':
		form = ODMForm(request.POST, request.FILES)
		if form.is_valid():
			build = form.save(commit=False)
			build.user = request.user
			build.save()

			# Main Logic goes here
			source_file_name = build.source_file.name
			build_file_name = build.buildprop_file.name
			
			env = environ.Env()
			env_file = join(dirname(__file__), 'config.env')
			if exists(env_file):
			    environ.Env.read_env(str(env_file))

			MMX_KEY_PATH = env('MMX_KEY_PATH')
			PATH_OF_SOURCE_FILE = env('PATH_OF_SOURCE_FILE')
			#NEW_PATH_OF_SIGNED_TARGET_FILES = env('NEW_PATH_OF_SIGNED_TARGET_FILES')
			NEW_PATH_OF_SIGNED_TARGET_FILES = '/mnt/ODM/' + build.odm.lower()

			MEDIA_PATH = settings.MEDIA_ROOT
			build_file = join(MEDIA_PATH, build_file_name)
			#sign_file = join(MEDIA_PATH, 'Sign.sh')

			sign_file = 'Sign.sh'
			
			import re
			build_str = open(build_file, "r")
			target_product_found = False
			for line in build_str:
				if re.match("ro.build.id", line):
					build_id = line.split('=')[1]
				if re.match("ro.build.fingerprint", line):
					build_version = line.split('=')[1].split('/')[4].split(':')[0]
				if re.match("ro.yu.device", line) and not target_product_found:
					target_product = line.split('=')[1].strip()
					target_product_found = True
					NEW_PATH_OF_SIGNED_TARGET_FILES += '/' + target_product + '/'

			# If target directory does't exists then create one
			import os
			if not os.path.exists(NEW_PATH_OF_SIGNED_TARGET_FILES):
				os.makedirs(NEW_PATH_OF_SIGNED_TARGET_FILES)

			# Move uploaded source file to /mnt/ODM/(odm name)/(device name)
			import shutil
			shutil.move(os.getcwd() + '/media/' + source_file_name, NEW_PATH_OF_SIGNED_TARGET_FILES)	

			call('export target_file_name="' + source_file_name + '"', shell=True)
			call('export mmx_key_path="' + MMX_KEY_PATH + '"', shell=True)
			call('export path_of_target_file="' + NEW_PATH_OF_SIGNED_TARGET_FILES + '"', shell=True)
			call('export new_path_of_signed_target_files="' + NEW_PATH_OF_SIGNED_TARGET_FILES + '"', shell=True)
			call('export OS_Android_version="' + build.android_version + '"', shell=True)
			call('export Build_ID="' + build_id + '"', shell=True)
			call('export mmx_build_version="' + build_version + '"', shell=True)
			call('export target_product="' + target_product + '"', shell=True)
			os.chdir("/mnt/yuos")
			call('./' + sign_file + ' ' + build.build_type, shell=True)

			return redirect('/builder/home/')
	else:
		form = ODMForm()

	return render(request, 'odm_builder/index.html', {'form': form})
