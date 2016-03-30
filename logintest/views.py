#-*- coding: utf-8 -*-
from logintest.forms import LoginForm,LoggedinForm
from django.shortcuts import render,redirect
from models import Login,UserDetails

# method to check whether user is already logged in or not.
def checkLoginStatus(request):
	if request.session.has_key('uID') and request.session.has_key('uName'):
		return viewDetails(request)					# if loggedin then print details
	else:											# otherwise load the login page
		return render(request, 'login.html', {})


# method for logging in 
def login(request):
	if request.method == "POST":
		#Get the posted form
		MyLoginForm = LoginForm(request.POST)
      
		if MyLoginForm.is_valid():
			userid = MyLoginForm.cleaned_data['userid']
			passwd = MyLoginForm.cleaned_data['passwd']
			oauthid = MyLoginForm.cleaned_data['oauthid']
			if passwd == "googleLogin":
				return googleLogin(request, userid, oauthid)
			elif passwd == "fbLogin":
				return fbLogin(request, userid, oauthid)
			else:
				try:
					res = Login.objects.filter(userId = userid)
					if res[0].password == passwd:
						request.session['uID'] = res[0].id			
						request.session['uName'] = res[0].username		
						return viewDetails(request)
					else:
						return render(request, 'login.html', {"name": userid, "pswderror": "Password is incorrect..."})
				except:
					return render(request, 'login.html', {"name": userid, "usererror": "UserId does not exists..."})
	else:
		MyLoginForm = LoginForm()
	return viewDetails(request)
		

# method for facebook login handeling
def fbLogin(request, name, fbid):
	try:
		res = Login.objects.filter(fbId = fbid)
		request.session['uID'] = res[0].id
		request.session['uName'] = res[0].username
		return viewDetails(request)
	except:
		request.session['fbName'] = name
		request.session['fbId'] = fbid
		return render(request, 'oAuthSignup.html', {"error" : "", "loginType" : "fbLogin"})



# method for Google login handeling
def googleLogin(request, name, emailid):
	try:
		res = Login.objects.filter(email = emailid)
		request.session['uID'] = res[0].id
		request.session['uName'] = res[0].username
		return viewDetails(request)
	except:
		request.session['googleName'] = name
		request.session['gId'] = emailid
		return render(request, 'oAuthSignup.html', {"error" : "", "loginType" : "googleLogin"})



# method for handeling first time login through social oAuth 
# if user has already account then link the both account
def oldUserLogin(request):
	if request.method == "POST":	
		userid = request.POST['userid']
		passwd = request.POST['passwd']
		loginType = request.POST['oAuthType']
		try:
			res = Login.objects.get(userId = userid)
			if res.password == passwd:
				if loginType == "fbLogin":
					res.fbId = request.session['fbId']
				else:
					res.email = request.session['gId']
				
				request.session['uID'] = res.id
				request.session['uName'] = res.username
				res.save()
				return viewDetails(request)
			else:
				return render(request, 'oAuthSignup.html', {"error" : "Incorrect Password...", "loginType" : loginType})
		except:
			return render(request, 'oAuthSignup.html', {"error" : "Incorrect userId...", "loginType" : loginType})
	else:
		return viewDetails(request)



# method for handeling first time login through social oAuth 
# if user has not an account yet then create one
def NewUserLogin(request):
	if request.method == "POST":	
		userid = request.POST['userid']
		passwd = request.POST['passwd']
		loginType = request.POST['oAuthType']
		try:
			res = Login.objects.get(userId = userid)
			return render(request, 'oAuthSignup.html', {"error" : "userId Already Exists...", "loginType" : loginType})
		except:
			if loginType == "fbLogin":
				ins = Login(userId = userid, password = passwd, username = request.session['fbName'], fbId = request.session['fbId'])
				ins.save()
				res = Login.objects.get(fbId = request.session['fbId'])
				request.session['uID'] = res.id	
				request.session['uName'] = res.username		
				return viewDetails(request)
			else:
				ins = Login(userId = userid, password = passwd, username = request.session['goggleName'], email = request.session['gId'])
				ins.save()
				res = Login.objects.get(email = request.session['gId'])
				request.session['uID'] = res.id	
				request.session['uName'] = res.username		
				return viewDetails(request)
	else:
		return viewDetails(request)



# method for viewing details of user loggedin
def viewDetails(request):
	if request.session.has_key('uID') and request.session.has_key('uName'):
		try:
			res=UserDetails.objects.filter(uId_id = request.session['uID'])
			add=res[0].address
			city=res[0].city
			state=res[0].state
			country=res[0].country
			pin=res[0].pin
			contno=res[0].contactno
			return render(request, 'loggedin.html',{"username" : request.session['uName'], "add" : add, "city" : city, "state" : state, 					"country" : country, "pin" :  pin, "contno" : contno, "status" : "Modify"})
		except:
			return render(request, 'loggedin.html',{"username" : request.session['uName'], "add" : "", "city" : "", "state" : "", "country" : 						"", "pin" : "", "contno" : "", "status" : "Save"})
	else:
		return render(request, 'login.html', {"msg" : ""})



# method for inserting details into the mySQL db
def insertDetails(request):
	if request.method == "POST":	
		uid = request.session['uID']
		name = request.POST['uname']
		add = request.POST['add']
		cty = request.POST['city']
		stat = request.POST['state']
		cntry = request.POST.get('country', False)
		pinno = request.POST['pin']
		contno = request.POST['contactno']
		res = Login.objects.get(id = uid)
		res.username = name
		res.save()
		request.session['uName'] = name
		try:
			ins = UserDetails.objects.get(uId_id = uid)
			ins.address = add
			ins.city = cty
			ins.state = stat
			ins.country = cntry
			ins.pin = pinno
			ins.contactno = contno
			ins.save()
			return render(request, 'loggedin.html', {"username" : name, "add" : add, "city" : cty, "state" : stat, "country" : cntry, 						"pin" : pinno, "contno" : contno, "status" : "Modify", "msg" : "Data Saved Successfully..."})
		except:
			ins = UserDetails(uId_id = uid, address = add, city = cty, state = stat, country = cntry, pin = pinno, contactno = contno)
			ins.save()
			return render(request, 'loggedin.html', {"username" : name, "add" : add, "city" : cty, "state" : stat, "country" : cntry, 						"pin" : pinno, "contno" : contno, "status" : "Modify", "msg" : "Data Saved Successfully..."})
	else:
		return viewDetails(request)
			
	
# method to logout from details page	
def logout(request):
	try:
		del request.session['uID']
		del request.session['uName']
		del request.session['fbName']
		del request.session['fbId']
		del request.session['googleName']
		del request.session['gId']
	except:
		pass
	return render(request, 'login.html', {"msg" : "You are loggedout..."})
		
