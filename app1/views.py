from django.shortcuts import render
from django.http import HttpResponse
import datetime

def Wel_Cli(request):
	data = datetime.datetime.now()
	hour = int(data.strftime('%H'))
	msg = '<marquee><h1><font color=blue>Hey Client, Good'
	if hour<12:
		msg+='Morning'
	elif hour<16:
		msg+='Afternoon'
	elif hour<21:
		msg+='Evening'
	else:
		msg+='Night'
	msg+='</h1></font></marquee><hr>'

	msg+='<h1>Server Time: '+str(data)+'</h1>'
	return HttpResponse(msg)