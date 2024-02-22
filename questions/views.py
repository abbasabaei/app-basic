from django.http import HttpResponse
from django.shortcuts import render
from .models import Text_Question,Response,Supervisor
from django.core.mail import send_mail
from twilio.rest import Client


def index(request, questiontext=None):
    if questiontext is None:
        answer = Text_Question.objects.first()
    else:
        answer = Text_Question.objects.filter(question=questiontext)

    # option = Response.objects.filter(question=answer)
    return render(request, 'questions/index.html', {'answer': answer})

def process_response(request,questiontext):
    if request.method == 'POST':
        queryset = Response.objects.filter(question__question_text__contains=questiontext).values_list('id',flat=True)
        answernum=0
        if queryset:  # Check if the queryset is not empty
            answernum = queryset[0]
        answer=Response.objects.get(id=answernum)
        option = request.POST.get('option')
        if option=='next':
            query = Response.objects.filter(question__question_text__contains=answer.next).values_list('id',flat=True)
            answern=0
            if query:
                answern = query[0]
            check=Response.objects.get(id=answern)
            return render(request,'questions/index.html',{'answer': answer,'option':option,'check':check})
        elif option=='no':
            query = Response.objects.filter(question__question_text__contains=answer.next_no).values_list('id',flat=True)
            answern=0
            if query:
                answern = query[0]
            check=Response.objects.get(id=answern)
            return render(request,'questions/index.html',{'answer': answer,'option':option,'check':check})
        elif option=='yes':
            query = Response.objects.filter(question__question_text__contains=answer.next_yes).values_list('id',flat=True)
            answern=0
            if query:
                answern = query[0]
            check=Response.objects.get(id=answern)
            return render(request,'questions/index.html',{'answer': answer,'option':option,'check':check})
        else:
            return render(request,'questions/send_email.html')

def send_email(request,ismail,issms):
    user = request.user
    id=Supervisor.objects.filter(user=user).values_list('id',flat=True)
    if id:  # Check if the queryset is not empty
        answernum = id[0]
    supervisor_info=Supervisor.objects.get(id=answernum)
    mail=supervisor_info.mail_address
    phone=supervisor_info.phone_number
    sendermail='your_email'
    if ismail.lower() == 'true':
        ismail = True
    else:
        ismail = False

    if issms.lower() == 'true':
        issms = True
    else:
        issms = False

    if request.method == 'POST':
        if issms and ismail:
            account_sid = 'your_sid'
            auth_token = 'your_token'
            client = Client(account_sid, auth_token)
            client.messages.create(
            from_='your_number',
            body='This is a test message.',
            to=phone
            )
            send_mail(
            'Test',
            'This is a test message.',
            sendermail,
            [mail],
            fail_silently=False,
            )
            return HttpResponse('Email and SMS sent successfully.')
        elif ismail:
            send_mail(
            'Test',
            'This is a test message.',
            sendermail,
            [mail],
            fail_silently=False,
            )
            return HttpResponse('Email sent successfully.')
        elif issms:
            account_sid = 'your_sid'
            auth_token = 'your_token'
            client = Client(account_sid, auth_token)
            client.messages.create(
            from_='your_number',
            body='This is a test message.',
            to=phone
            )
            return HttpResponse('SMS sent successfully.')
    else:
        return HttpResponse('Email Failled.')
    
