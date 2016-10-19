from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions

from .models import Build

class ODMForm(forms.ModelForm):
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
	soc_vendor = forms.ChoiceField(choices=VENDOR_SOC_CHOICES, initial='MediaTek')
	odm = forms.ChoiceField(choices=ODM_CHOICES, initial='Tinno')
	android_version = forms.ChoiceField(choices=ANDROID_VERSION_CHOICES, initial='L-5.1.1')
	build_type = forms.ChoiceField(choices=BUILD_TYPE_CHOICES, initial='OTA')

	# Uploads
	target_file = forms.FileField()
	buildprop_file = forms.FileField()

	def __init__(self, *args, **kwargs):
		super(ODMForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.layout.append(Div(Submit('begin_sign', 'Begin Sign', css_class="btn-lg btn-primary"), css_class="pull-right"))

	class Meta:
		model = Build
		exclude = ['user']