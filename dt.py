from datetime import datetime    
import pytz 
tz_NY = pytz.timezone('Asia/Kolkata')

def time ():
	datetime_NY = datetime.now(tz_NY)  
	x=str(datetime_NY.strftime("%H:%M"))
	y=x.split(":")
	y[0]=int(y[0])
	if y[0]>12:
		y.extend('pm')
		y[0]=y[0]-12
	else:
		y.extend('am')
	y[0]=str(y[0])
	return(y)



def day ():
	x = datetime.datetime.now()
	return(x.strftime("%A"))

def year ():
	x=datetime.datetime.now()
	return x.year

def month ():
	x=datetime.datetime.now()
	return(x.strftime("%B"))
