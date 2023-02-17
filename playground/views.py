#from django.core.mail import send_mail, EmailMessage, BadHeaderError, mail_admins
from django.shortcuts import render
from django.core.cache import cache
#from templated_mail.mail import BaseEmailMessage
import requests
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import logging
import requests

logger = logging.getLogger(__name__) 

class HelloView(APIView):
        def get(self, request):
             
            try:
                logger.info('Calling httpbin')
                response = requests.get('https://httpbin.org/delay/2')
                logger.info('Received the response')
                data = response.json()
            except requests.ConnectionError:
                logger.critical('httpbin is offline')
            return render(request, 'hello.html', {'name': 'Vinu'})





        
#return render(request, 'hello.html', {'name': 'Mosh'})
""""
def say_hello(request):
    try:
        message = BaseEmailMessage(
           template_name='emails/hello.html',
           context={'name': 'Mosh'}
       )
        message.send(['Vinu@hero.com'])
       
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
"""
"""
 message = EmailMessage('subject', 'message', 'from@domain.com', ['kumar@gmail.com'])
        message.attach_file('playground/static/images/sach1.jpg')
        message.send()
        #mail_admins('subject', 'message', html_message = 'message')
"""