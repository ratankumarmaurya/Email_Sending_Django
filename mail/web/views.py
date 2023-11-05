# from django.shortcuts import render,redirect
# from .utils import send_email_client
# # Create your views here.
#
# def send_email(request):
#     send_email_client()
#     return redirect("/")
#
# def index(request):
#     return render(request,'index.html')
#

from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmailForm

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')

            from_email = 'your_email@gmail.com'
            recipient_list = [recipient]

            if attachment:
                email = EmailMessage(subject, message, from_email, recipient_list)
                email.attach(attachment.name, attachment.read(), attachment.content_type)
                email.send()
            else:
                send_mail(subject, message, from_email, recipient_list)

            # return HttpResponse("Email sent successfully!")
            return render(request,'show.html')
    else:
        form = EmailForm()

    return render(request, 'index.html', {'form': form})