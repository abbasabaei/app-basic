from django.contrib import admin
from .models import Text_Question,Response,Supervisor
class Text_QuestionAdmin(admin.ModelAdmin):
    list_display=('id','question_text')

class ResponseAdmin(admin.ModelAdmin):
    exclude=('date_created',)
    list_display=('id','question','next_yes','next_no','next','sms','mail')

class SupervisorAdmin(admin.ModelAdmin):
    list_display=('user','name','mail_address','phone_number')


admin.site.register(Text_Question,Text_QuestionAdmin)
admin.site.register(Response,ResponseAdmin)
admin.site.register(Supervisor,SupervisorAdmin)
