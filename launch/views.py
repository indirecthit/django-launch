from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.sites.models import Site

from launch.models import SignupRequest

from launch.forms import SignupForm

from django.core.mail import EmailMultiAlternatives, EmailMessage

def signup(request, template='launch/signup_page.html'):		
	if "POST" == request.method:
		signup_form = SignupForm(data=request.POST)
		if signup_form.is_valid():
			#If an email has already been entered, let's pull the data from the original request and use that
			try:
				signuprequest = SignupRequest.objects.get(email=signup_form.cleaned_data['email'])
			except:
				#If no email, let's send the user an email and create a new signup request
				signuprequest = signup_form.save(commit=False)
				signuprequest.ip_address = request.META['REMOTE_ADDR']
				signuprequest.save()
				email_context = {
					'site' : Site.objects.get_current(),
					'signuprequest' : signuprequest
				}
				subject = render_to_string('launch/email_subject.txt', email_context)
				text_body = render_to_string('launch/email_text.txt', email_context)
				email = EmailMultiAlternatives(subject, text_body, settings.DEFAULT_FROM_EMAIL, [signuprequest.email])
				email.attach_alternative(render_to_string('launch/email_html.html', email_context), "text/html")
				email.send()
				
				launch_email = getattr(settings, 'LAUNCH_EMAIL_COPY', None)
				if launch_email is not None:
					email_context = {
						'site' : Site.objects.get_current(),
						'signuprequest' : signuprequest
					}					
					subject = render_to_string('launch/copy_email_subject.txt', email_context)
					text_body = render_to_string('launch/copy_email_text.txt', email_context)
					email = EmailMessage(subject, text_body, settings.DEFAULT_FROM_EMAIL, [launch_email])
					email.send()
				
			request.session['signup_hash'] = signuprequest.hash_value
			return HttpResponseRedirect(reverse('launch_page_success_with_id', args=[signuprequest.hash_value]))
	else:
		initial = {}
		if "referredBy" in request.GET: 
			initial['referred_by_id'] = request.GET['referredBy']
		signup_form = SignupForm(initial = initial)
	context = {
		'signup_form' : signup_form,
	}
	return render_to_response(template, context, context_instance=RequestContext(request))

def success(request, hash_value = None, template='launch/signup_complete.html'):
	signup_request = get_object_or_404(SignupRequest, hash_value=hash_value)
	context = {}
	context['signup_request'] = signup_request
	return render_to_response(template, context, context_instance=RequestContext(request))