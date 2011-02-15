from django.db import models
from hashlib import md5

class SignupRequest(models.Model):
	active = models.BooleanField(default=True, help_text='Deactivate requests that should be ignored.')
	email = models.EmailField(unique=True)
	invitation_sent = models.BooleanField(default=False, help_text='Has an invitation been sent to this recipient?')
	signed_up = models.BooleanField(default=False, help_text='Has this user signed up?')
	date_added = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	referred_by = models.ForeignKey('self', blank=True, null=True)
	ip_address = models.IPAddressField(blank=True, null=True)
	hash_value = models.TextField(unique=True)
	
	def __unicode__(self):
		return "SignupRequest for %s" % self.email
		
	def save(self):
		hash_value = md5('%s_%s' % (self.id, self.email)).hexdigest()
		if self.hash_value != hash_value:
			self.hash_value = hash_value
		super(SignupRequest, self).save()