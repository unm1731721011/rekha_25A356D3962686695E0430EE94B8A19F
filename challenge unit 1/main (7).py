 " "
4==0
100!=0
400==0

" "
def isleapyear(year):
  if(year % 4==0 and year % 100!=0)or year % 400==0:
    return True
  else:
    return false

year=int(input("Enter a year:"))
if isleapyear(year):
  print ('{}is leap year.'.format(year))
else:
  print('{}is not a leap year.'.format(year))
  
  
  
  
  


  
   
   

