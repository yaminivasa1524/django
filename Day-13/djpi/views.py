from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def he(request):
	print("hello welcome")
	return HttpResponse("hiii welcome to django internship")

def hlp(request,n):
	return HttpResponse("Hiii {} welcome  to django internship".format(n))

def yam(request,t):
	y= []
	for p in range(1,11):
		u = "{} x {:02} = {:02}".format(t,p,t*p)+"<br/>"
		y.append(u)
	print(y)
	return HttpResponse(y)

def record(request,age,name,sal=2000):
	return HttpResponse("hii your name is: {}<br/>your age is :{}<br/>your age is :{}".format(name,age,str(sal)))

def student(request,prc,name,age):
	t="<h5 style='background-color:green;color:white;font-size:20px'>hiii welcome {}</h5>".format(age)
	u="<h2>your age is:{} </h4>".format(age)
	return HttpResponse("<script>alert('hello')</script>")

def rcde(request,name,a):
	return HttpResponse("<h3 style='margin-left:30%;background-color:yellow;margin-right:20%'>hii wecome <span style='color:green'>{}</span> and your age is<span style='background:red'> {}</span></h3>".format(name,a))

def emp(request,sal,empid,empname):
	return render(request,'prjc/sample.html',{"n":empname,"i":empid,"u":sal})

def reg(request):
	if request.method == "POST":
		name = request.POST['n']
		age = request.POST['a']
		usname = request.POST['uname']
		pasd = request.POST['pwd']
		print(name,age,usname,pasd)
		return render(request,'prjc/display.html',{"na":name,"ag":age,"username":usname,"psd":pasd})
	return render(request,'prjc/register.html')

def lg(request):
	if request.method == "POST":
		u = request.POST['uname']
		p = request.POST['pwd']
		if u == "yamini":
			if p == "170":
				return HttpResponse("Hi Welcome {}".format(u))
			return HttpResponse("Invalid password")
		return HttpResponse("Invalid Username")
	return render(request,'prjc/login.html')


 