from django.shortcuts import render,  redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Categorie, Subscriber, SubscribedUsers
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import re
from django.core.mail import send_mail
from .forms import *


# Create your views here.
def index(request):    
    return render(request, 'fructs/index.html')


def about(request):
    return render(request, 'fructs/about.html')


def cart(request):
    products = Product.objects.all()
    return render(request, 'fructs/cart.html', {'products': products})


def slider(request):
    return render(request, 'fructs/index_2.html')


def news(request):
    return render(request, 'fructs/news.html')


def shop(request):
    categories = Categorie.objects.all()
    products = Product.objects.all()
    return render(request, 'fructs/shop.html', {'products': products, 'categories': categories})


def singlenews(request):
    return render(request, 'fructs/single-news.html')


def singleproduct(request, nom):
    if nom:
        pdt = Product.objects.get(name=nom)
        family = Product.objects.filter(label=pdt.label)
        return render(request, 'fructs/single-product.html', {'pdt': pdt, 'products': list(family)})
    return render(request, 'fructs/single-product.html')


def checkout(request):
    return render(request, 'fructs/single-product.html')


def contact(request):
    return render(request, 'fructs/contact.html')


def mailer(request):
    form = MailForm()
    print("my_post", request)
    if request.method == "POST":
        print('sended')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(subject, message, email, [email])
        return render(request, 'fructs/send.html')
    context = {'form': form}
    return render(request, 'fructs/mailer.html', context)


def save_email(email):
    try:
        subscribe_model_instance = SubscribeModel.objects.get(email=email)
    except ObjectDoesNotExist as e:
        subscribe_model_instance = SubscribeModel()
        subscribe_model_instance.email = email
    except Exception as e:
        logging.getLogger("error").error(traceback.format_exc())
        return False

    # does not matter if already subscribed or not...resend the email
    subscribe_model_instance.status = constants.SUBSCRIBE_STATUS_SUBSCRIBED
    subscribe_model_instance.created_date = utility.now()
    subscribe_model_instance.updated_date = utility.now()
    subscribe_model_instance.save()
    return True


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def new(request, page):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, page)
    else:
        return render(request,  page)


def validate_email(request): 
    email = request.POST.get("email", None)   
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.get(email = email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res