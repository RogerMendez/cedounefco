#encoding:utf-8
from django.core.mail import EmailMultiAlternatives
from django.contrib.contenttypes.models import ContentType

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE

from django.http import HttpResponse
from django.conf import settings
#import ho.pisa as pisa
#import cStringIO as StringIO
import cgi
import os

import random

def create_code_activation():
    li = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0']
    #51 elementos
    code = random.choice(li)
    for i in range(50):
         code += random.choice(li)
    return code


def send_email(email, html, subject = 'Codigo De Activacion'):
    text_content = 'Mensaje...nLinea 2nLinea3'
    html_content = html
    from_email = '"Prospection" <sieboliva@gmail.com>'
    to = email
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    #send_mail('Subject here', html, 'from@example.com', [], fail_silently=False)


def admin_log_addition(request, objecto, mensaje):
    LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(objecto).pk,
                object_id       = objecto.pk,
                object_repr     = u'%s'%objecto,
                action_flag     = ADDITION,
                change_message = mensaje,
            )

def admin_log_change(request, objecto, mensaje):
    LogEntry.objects.log_action(
                user_id         = request.user.pk,
                content_type_id = ContentType.objects.get_for_model(objecto).pk,
                object_id       = objecto.pk,
                object_repr     = u'%s'%objecto,
                action_flag     = CHANGE,
                change_message = mensaje,
            )

'''def generar_pdf(html):
    result = StringIO.StringIO()
    links = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-16")), dest=result, link_callback=fetch_resources)
    #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, link_callback=links)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


def fetch_resources(uri, rel):
    import os.path
    BASE_DIR = settings.BASE_DIR
    path = os.path.join(
            os.path.join(BASE_DIR, 'static'),
            uri.replace(settings.STATIC_URL, ""))
    return path
'''
def rountn(valor):
    return float('%.2f' %valor)