import datetime
now = datetime.datetime.now()
print( now.strftime("%a")) #name of today ex: sun
print( now.strftime("%A")) #full name of today ex: sunday
print(now.strftime("%b"))  #name of the month ex:dec
print(now.strftime("%B"))  #name of full month ex: december
print(now.strftime("%c")) #date and time ex:sun dec 03 19:15:2023
print(now.strftime("%C")) #full date and time ex:sunday december 03 19:15:2023
print(now.strftime("%d")) #print the day
print(now.strftime("%D")) #peint full name of today
print(now.strftime("h")) #print the hours in 24h
print(now.strftime("%I")) #print the time on 12 h
print(now.strftime("%j"))#number of today in the year
print(now.strftime("%m") #number of the month
print(now.strftime("%p") #this for pm or am
print(now.strftime("%S"))#this is for the seconds
print(now.strftime("%x")) # display date
print(now.strftime("%x"))#display
print(now.strftime("%i:%M:%S %"))
