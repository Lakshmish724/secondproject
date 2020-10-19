from django.shortcuts import render
import datetime

# Create your views here.
def Welcome(request):
	date=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg=  'Hi Bad Ass'

	if hour<12:
		msg+='Good Morning'

	elif hour<16:
		msg+='After Noon'

	elif hour<21:
		msg+='Evening'

	else:
		msg+='Night'

	my_dict = {'insert_date' : date,'insert_msg' :msg}
	return render(request=request,template_name='app10/display.html', context=my_dict)
