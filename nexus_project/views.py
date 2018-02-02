from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.template import Template
from django.http import HttpResponse,Http404,HttpResponseRedirect
from nexus_project.models import Login,Signup,Verify_email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.

def index(request):
	template = loader.get_template('project_home_page.html')
	context={"title":"Add Task"}
	return HttpResponse(template.render(context,request))

def signup_page(request):
	template = loader.get_template('project_sign_up.html')
	context={"title":"Add Task"}
	return HttpResponse(template.render(context,request)) 

def login_page(request):
	template = loader.get_template('project_login_page.html')
	context={"title":"Add Task"}
	return HttpResponse(template.render(context,request))

def logout(request):
	template = loader.get_template('project_home_page.html')
	context={"title":"Add Task"}
	return HttpResponse(template.render(context,request))


def confrm_email(request):
	template = loader.get_template('Verify_email.html')
	context={"title":"Add Task"}
	return HttpResponse(template.render(context,request))


def verify(request):
	verification = request.POST.getlist('checks')

	l_id = request.session.get('login_id')
	print l_id
	log= Login.objects.get(id=l_id)
	try:
		# bool_send_email_exist = Verify_email.objects.filter(login = log).exists()
   
		# if bool_send_email_exist == False:

			mail= Verify_email(login=log,check=verification)
			mail.save()
			template =loader.get_template('project_login_page.html')
			context ={}
		# else:
		# 	template =loader.get_template('Verify_email.html')
		# 	context ={}
	except Exception, e:    
		template = loader.get_template('Verify_email.html')
		print("************************")
		print e
		context ={}
	return HttpResponse(template.render(context,request))

def registration(request):
	name = request.POST.get('txt_name') 
	email = request.POST.get('txt_email') 
	password = request.POST.get('txt_pswd') 
	confrm_pswd = request.POST.get('txt_cnfrm_pswd') 
	print name
	print email
	print password
	print confrm_pswd

	try:
		bool_check_email_exist = Login.objects.filter(login_username= email).exists()
   
		if bool_check_email_exist == False:
        
			a=Login(login_username=email,login_password= password)
			a.save()
			fk_id = a.id
			print (fk_id)
            #--- b is the object created here ---------
			c =Login.objects.get(id =fk_id)
			#create session
			request.session['login_id']=fk_id



			b= Signup(Name=name,registration=c)
			b.save()
			fk_id1 = b.id  

			# me == my email address
			# you == recipient's email address
			me = "piyars1234@gmail.com"
			you = email

			# Create message container - the correct MIME type is multipart/alternative.
			msg = MIMEMultipart('alternative')
			msg['Subject'] = "Link"
			msg['From'] = me
			msg['To'] = you

			# Create the body of the message (a plain-text and an HTML version).
			text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
			html = """\
			<html>
			  <head></head>
			  <body>
			  	<p><font color="Blue"><h1>Thank you for signing up in NEXUS<h1></font><br>
        		<h2><font color="Blue">This is the verification message....</font></h2><br>
        		<h2><font color="Black">Click to verify :</font></h2>	
			    <button type="button"><a href="http://127.0.0.1:8000/nexus_project/confrm_email/">link</a></button>
			  </body>
			</html>
			"""

			# Record the MIME types of both parts - text/plain and text/html.
			part1 = MIMEText(text, 'plain')
			part2 = MIMEText(html, 'html')

			# Attach parts into message container.
			# According to RFC 2046, the last part of a multipart message, in this case
			# the HTML message, is best and preferred.
			msg.attach(part1)
			msg.attach(part2)

			# Send the message via local SMTP server.
			s = smtplib.SMTP('smtp.gmail.com',587)

			s.starttls()
			s.login(me,'Piyars@123')
			# sendmail function takes 3 arguments: sender's address, recipient's address
			# and message to send - here it is sent as one string.
			s.sendmail(me, you, msg.as_string())
			s.quit()

          
			template =loader.get_template('project_login_page.html')
			context ={"confrm_email" :"Please verify your email address...!!!"}
		else:
			template =loader.get_template('project_sign_up.html')
			context ={"Erroremail" :"Email already exist"}
	except Exception, e:    
		template = loader.get_template('project_sign_up.html')
		context ={}
		print("************************")
		print e
	return HttpResponse(template.render(context,request))


def login(request):
	username = request.POST.get('txt_email')
	password = request.POST.get('txt_pswd')

	print username
	print password
	context={}
	template = loader.get_template('project_login_page.html')
	try:
		obj_login =Login.objects.get(login_username =username)
		send_mail = Verify_email.objects.get(login = obj_login.id)

		if(obj_login.login_username == username and obj_login.login_password == password):

			if(send_mail.login.id==obj_login.id):
				print "hi"
				template=loader.get_template('project_welcome_page.html') 
				context={}
		else:
			template=loader.get_template('project_login_page.html')
			context={"confrm_email" :"Please verify your email address...!!!"}
	except Exception, e:    
		template = loader.get_template('project_login_page.html')
		context={"confrm_email" :"Please verify your email address...!!!"}
		print("************************")
		print e
		      

	return HttpResponse(template.render(context,request))

       