from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class MediaFileSystemStorage(FileSystemStorage):
	def get_available_name(self, name, max_length=None):
		if max_length and len(name) > max_length:
			raise(Exception("name's length is greater than max_length"))
		return name

	def _save(self, name, content):
		if self.exists(name):
			# if the file exists, do not call the superclasses _save method
			return name
		# if the file is new, DO call it
		return super(MediaFileSystemStorage, self)._save(name, content)


class Build(models.Model):
	VENDOR_SOC_CHOICES = (
		('MediaTek', 'MTK'),
		('QualComm', 'QCOM'),
		('Spreadtrum', 'Spreadtrum'),
	)

	ODM_CHOICES = (
		('Tinno', 'Tinno'),
		('Huaqin', 'Huaqin'),
		('IMG', 'IMG'),
		('Ragentek', 'Ragentek'),
		('Wingtech', 'Wingtech'),
		('Coolpad', 'Coolpad'),
		('Amer', 'Amer'),
		('Sprocomm', 'Sprocomm'),
		('Topwisez', 'Topwisez'),
	)

	ANDROID_VERSION_CHOICES = (
		('L-5.1.1', 'L-5.1.1'),
		('M-6.0', 'M-6.0'),
		('M-6.0.1', 'M-6.0.1'),
		('N-7.0', 'N-7.0'),
	)

	BUILD_TYPE_CHOICES = (
		('OTA', 'OTA'),
		('Factory', 'Factory'),
	)

	# Drop-downs
	soc_vendor = models.CharField(max_length=20, choices=VENDOR_SOC_CHOICES, default='MediaTek')
	odm = models.CharField(max_length=20, choices=ODM_CHOICES, default='Tinno')
	android_version = models.CharField(max_length=20, choices=ANDROID_VERSION_CHOICES, default='L-5.1.1')
	build_type = models.CharField(max_length=10, choices=BUILD_TYPE_CHOICES, default='OTA')

	# Uploads
	source_file = models.FileField(storage=MediaFileSystemStorage())
	buildprop_file = models.FileField()

	# Timestamp
	uploaded_at = models.DateTimeField(auto_now_add=True, auto_now=False)

	# User
	user = models.ForeignKey(settings.AUTH_USER_MODEL)