from django.shortcuts import render
from django.template.context import RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect , get_object_or_404
from django.utils import six
from itertools import product,chain
from .models import item,UserProfile
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


def main(request):
	return HttpResponse('<h1> Bye </h1>')

def home(request):
	return render(request,'BuyandSell/main.html')


def test(request,username):
	print("hi whats up")
	print(UserProfile.user)
	print("Hii This is sourav")
	print(username)
	u = get_object_or_404(User, username=username)
	me=UserProfile.objects.filter(user=u)
	return render(request,'BuyandSell/seller_info.html',{'obj': me})


def login_user(request):
	if not request.user.is_authenticated():
		if request.method == "POST":
			username = request.POST['name']
			password = request.POST['password']
			user = authenticate(username=username , password=password)
			login(request,user)
			if request.user.is_authenticated():
				return redirect('BuyandSell:items')
			else:
				return render(request, 'BuyandSell/login.html', {'error_message': 'Invalid login'})
		else:
			return render(request, 'BuyandSell/login.html', {'error_message': 'Invalid login'})
	else:
		return redirect('BuyandSell:items')

def logOut(request):
	logout(request)
	return redirect('BuyandSell:login_user')


def sell(request,username):
	print("i am one man of army "+ username)
	if request.method == "POST":
		item_name=request.POST['name']
		item_id=request.POST['id']
		price = request.POST["price"]
		username = request.POST['username']
		description=request.POST['description']
		image=request.FILES['image']
		obj2=item(item_name = item_name , item_id= item_id ,price=price, username= username,description=description,image=image)
		obj2.save()
	else:
		return render(request, 'BuyandSell/sell_form.html', {'username': username})
	return redirect('BuyandSell:items')


def profile(request,username):
	print("we are in profile now ")
	result =item.objects.filter(username =username)
	u = get_object_or_404(User, username=username)
	me=UserProfile.objects.filter(user=u)
	return render(request,'BuyandSell/profile.html' ,{'obj2':me,'obj' :result}) 

def search(request):
	if request.method==POST:
		item_name = request.POST['data']
		result=item.objects.filter(item_name=item_name)
		return render(request,'BuyandSell/search.html' ,{'obj' :result}) 
		
from django.contrib.auth.decorators import login_required
@login_required(login_url='BuyandSell:login_user')
def items(request):
	context = {}
	context['username'] = request.user.username
	context['items'] = item.objects.all()
	return render(request,'BuyandSell/home.html',context)

def about(request):
	return render(request,'BuyandSell/about.html')