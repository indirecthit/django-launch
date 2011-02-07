from django import forms

from launch.models import SignupRequest

class SignupForm(forms.ModelForm):
	referred_by_id = forms.CharField(widget=forms.HiddenInput(), required=False)
	class Meta:
		model = SignupRequest
		exclude = (
			'active', 
			'invitation_sent', 
			'signed_up',
			'referred_by'
		)

	#We want to silently fail on emails that have already been entered
	def validate_unique(self):
		pass

	def save(self, commit=True):
		referred_by = self.cleaned_data['referred_by_id']
		try:
			referred_by = SignupRequest.objects.get(pk=referred_by)
			self.instance.referred_by = referred_by
		except:
			pass

		return super(SignupForm, self).save(commit=commit)
