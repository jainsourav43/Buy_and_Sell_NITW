from django.shortcuts import render
from django.template.context import RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
#from .models import UserProfile
#from .models import Extras
#from django.views.decorators.csrf import csrf_exempt
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
	print(me[0].contactno)
	print(me[0].user)
	return render(request,'BuyandSell/seller_info.html',{'obj': me})


def login_user(request):
	if request.method == "POST":
		request.session.set_test_cookie()
		if request.session.test_cookie_worked():
			print("victory")
		request.session.delete_test_cookie()
		username = request.POST['name']
		password = request.POST['password']
		user = authenticate(username=username , password=password)
		login(request,user)
		#request.session['username'] =username
		#request.session['username'] =UserProfile.objects.get(user=request.user) 
		if request.user.is_authenticated():
			items = item.objects.all()
			if user is not None:
				if user.is_active:
					request.session.set_expiry(3000)
					print(username)
					return render(request,'BuyandSell/home.html',{'username':username,'obj': items})
				else:
					return render(request, 'BuyandSell/login.html', {'error_message': 'Your account has been disabled'})
			else:
				return render(request, 'BuyandSell/login.html', {'error_message': 'Invalid login'})
		else:
			return render(request, 'BuyandSell/login.html', {'error_message': 'Invalid login'})
	else:
		return render(request, 'BuyandSell/login.html', {'error_message': 'Invalid login'})





def sell(request,username):
	print("i am one man of army "+ username)
	if request.method == "POST":
		item_name=request.POST['name']
		item_id=request.POST['id']
		price = request.POST["price"]
		username = request.POST['username']
		description=request.POST['description']
		image=request.FILES['image']
	#	available =request.POST['available']
		obj2=item(item_name = item_name , item_id= item_id ,price=price, username= username,description=description,image=image)
		obj2.save()
	else:
		return render(request, 'BuyandSell/sell_form.html', {'username': username})
	return render(request ,'BuyandSell/login.html')


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