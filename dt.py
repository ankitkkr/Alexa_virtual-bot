import datetime


def day ():
	x = datetime.datetime.now()
	return(x.strftime("%A"))

def year ():
	x=datetime.datetime.now()
	return x.year

def month ():
	x=datetime.datetime.now()
	return(x.strftime("%B"))
