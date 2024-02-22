from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Text_Question(models.Model):
    question_text = models.CharField(max_length=255)
    date_created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text

class Response(models.Model):
    question=models.ForeignKey(Text_Question,on_delete=models.CASCADE)
    next_yes = models.ForeignKey(Text_Question, related_name='next_yes', on_delete=models.SET_NULL, null=True,blank=True)
    next_no = models.ForeignKey(Text_Question, related_name='next_no', on_delete=models.SET_NULL, null=True,blank=True)
    next = models.ForeignKey(Text_Question, related_name='next', on_delete=models.SET_NULL, null=True,blank=True)
    sms=models.BooleanField(default=False)
    mail=models.BooleanField(default=False)
    date_created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.question)
    


class Supervisor(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=50, blank=True, null=True)
    mail_address=models.EmailField(max_length=50, blank=True, null=True)
    phone_number=models.CharField(max_length=14, blank=True, null=True)
    def __str__(self):
        return str(self.user)
