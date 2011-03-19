from django.db import models
from launch.encoder import UrlEncoder

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
		if self.id is None:
			super(SignupRequest, self).save()
		encoder = UrlEncoder()
		hash_value = encoder.encode_url(int(self.id))
		if self.hash_value != hash_value:
			self.hash_value = hash_value
		super(SignupRequest, self).save()
		
def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """Convert positive integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    # Special case for zero
    if number == 0:
        return '0'

    base36 = ''

    sign = ''
    if number < 0:
        sign = '-'
        number = - number

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36