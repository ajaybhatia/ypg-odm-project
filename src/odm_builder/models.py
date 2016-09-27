from django.db import models

class Build(models.Model):
	VENDOR_SOC_CHOICES = (
		('MediaTek', 'MTK'),
		('QualComm', 'QCOM'),
		('Spreadtrum', 'Spreadtrum'),
	)

	ODM_CHOICES = (
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
	odm = models.CharField(max_length=100, blank=True)
	android_version = models.CharField(max_length=20, choices=ANDROID_VERSION_CHOICES, default='L-5.1.1')
	build_type = models.CharField(max_length=10, choices=BUILD_TYPE_CHOICES, default='OTA')