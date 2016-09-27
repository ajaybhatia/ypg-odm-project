from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions


class ODMForm(forms.Form):
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
	soc_vendor = forms.ChoiceField(choices=VENDOR_SOC_CHOICES, initial='MediaTek')
	odm = forms.CharField(required=False)
	android_version = forms.ChoiceField(choices=ANDROID_VERSION_CHOICES, initial='L-5.1.1')
	build_type = forms.ChoiceField(choices=BUILD_TYPE_CHOICES, initial='OTA')

	def __init__(self, *args, **kwargs):
		super(ODMForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)
		self.helper.layout.append(Div(Submit('save', 'save', css_class="btn-lg btn-primary"), css_class="pull-right"))