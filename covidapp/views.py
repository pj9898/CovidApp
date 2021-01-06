from django.shortcuts import render
from .models import User
from django.db.models import Q
import requests
import json



url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "9c9f99cb0amsh66de796d237637cp1124d6jsnc34af42aef47",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


#print(response.text)
# Create your views here.   
def CovidStats(request):
	def get_ip(request):
		adress=request.META.get('HTTP_X_FORWARDED_FOR')
		if adress:
			ip=adress.split(',')[-1].strip()
		else:
			ip=request.META.get('REMOTE_ADDR')
		return ip
	ip=get_ip(request)
	u= User(user=ip)
	print(ip)
	result1=User.objects.filter(Q(user__icontains=ip))
	if len(result1)==1:
		print("User Exist")
	elif len(result1)>1:
		print("user exist more than one.......")
	else:
		u.save()
		print("user is unique")
	Count=User.objects.all().count()
	print("total user is",Count)
	slectedCountry=""
	new=0
	active=0
	critical=0
	recovered=0
	total=0
	deaths=0
	noofresluts =int(response['results'])
	mylist = []
	for x in range(0,noofresluts):
		mylist.append(response['response'][x]['country'])
	mylist.sort()
	if request.method=="POST":
		slectedCountry = request.POST.get('selected')
		noofresluts =int(response['results'])
		for x in range(0,noofresluts):
			if slectedCountry==response['response'][x]['country']:
				new =response['response'][x]['cases']['new']
				active =response['response'][x]['cases']['active']
				critical =response['response'][x]['cases']['critical']
				recovered =response['response'][x]['cases']['recovered']
				total =response['response'][x]['cases']['total']
				deaths =response['response'][x]['deaths']['total']
	context ={'mylist':mylist,'slectedCountry':slectedCountry,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths,'Count':Count}

	return render(request,'Helloworld.html',context)
