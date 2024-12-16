import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from bizzzapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from bizzzapp.forms import bookingForm, ImageUploadForm
from bizzzapp.models import Book, seats, details, ImageModel


# Create your views here.

def home(request):
    if request.method == 'POST':
        if details.objects.filter(
            name=request.POST['name'],
            password=request.POST['password'],
        ).exists():
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
       subv=seats.objects.all(
           name=request.POST['name'],
           email=request.POST['email'],
           subject=request.POST['subject'],
           message=request.POST['message'],
       )
       subv.save()
       return redirect('/contact')
    else:
        return render(request,'contact.html')


def edit(request):
    editinformation = Book.objects.get(id=id)
    return render(request,'edit.html')

def quote(request):
    if request.method == 'POST':
        few=Book.objects.all(
            departure=request.POST['departure'],
            destination=request.POST['destination'],
            traveldate=request.POST['traveldate'],
            buses=request.POST['buses'],
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        few.save()
        return redirect('/show')
    else:
        return render(request,'get-a-quote.html')


def login(request):
    return render(request,'login.html')

def pricing(request):
    return render(request,'pricing.html')

def register(request):
    if request.method == 'POST':
        init=details.objects.all(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        init.save()
        return redirect('login')
    else:
        return render(request,'register.html')





def details(request):
    return render(request,'service-details.html')

def services(request):
    return render(request,'services.html')

def show(request):
    allinit = Book.objects.all()
    return render(request,'show.html',{'koob':allinit})

def showcontact(request):
    allshows = seats.objects.all()
    return render(request,'showcontact.html',{'oob':allshows})

def starterpage(request):
    return render(request,'starter-page.html')

def delete(request,id):
    df = Book.objects.get(id=id)
    df.delete()
    return redirect('/show')

def update(request,id):
    updateinfo = Book.objects.get(id=id)
    inside= bookingForm(request.POST,instance=updateinfo)
    if inside.is_valid():
        inside.save()
        return redirect('/show')
    else:
        form = inside
        return render(request,'edit.html')




def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def token(request):
    consumer_key = '9Roj30muMYAE2Y7wTf4KusQ4ntvoSluDAyPGCw61C84aUhAm'
    consumer_secret = 'GPB267hWUd0vwGf2TRRs2Zf5B6WCJQtPKRU9csAOuODYi89ztHGH83VMVLQ8Y2Ck'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Enter you pin on your  phone")
