from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.conf import settings

from launch.models import SignupRequest

from launch.forms import SignupForm

from django.core.mail import EmailMultiAlternatives

def signup(request, template='launch/signup_page.html'):
	if "POST" == request.method:
		signup_form = SignupForm(data=request.POST)
		if signup_form.is_valid():
			#If an email has already been entered, let's pull the data from the original request and use that
			try:
				signuprequest = SignupRequest.objects.get(email=signup_form.cleaned_data['email'])
			except:
				signuprequest = signup_form.save(commit=False)
				signuprequest.save()
				subject = render_to_string('launch/email_subject.txt')
				text_body = render_to_string('launch/email_text.txt')
				email = EmailMultiAlternatives(subject, text_body, settings.DEFAULT_FROM_EMAIL, [signuprequest.email])
				email.attach_alternative(render_to_string('launch/email_html.html'), "text/html")
				email.send()
				
			request.session['signup_id'] = signuprequest.id
			return HttpResponseRedirect(reverse('launch_page_success_with_id', args=[signuprequest.id]))
	else:
		signup_form = SignupForm()
	context = {
		'signup_form' : signup_form,
	}
	return render_to_response(template, context, context_instance=RequestContext(request))

def success(request, requestid = None, template='launch/signup_complete.html'):
	context = {}
	context['requestid'] = requestid
	return render_to_response(template, context, context_instance=RequestContext(request))