import requests
import sys

with open('input.txt') as f:
    content = f.readlines()
f.close()

#length = len(content)
#print(length)

#content = ['http://www.apertus.com.tw/','http://www.google.com.t','http://www.yahoo.com.w']
length = len(content)
num = 0

f = open('errorLog', 'w')
while num < length:
  try:  
    r = requests.get(''+str(content[num].rstrip('\n')))
  #except requests.exceptions.ConnectionError:    
  #  errMess = 'Connect Error in: ' + str(content[num])
  #  print( errMess.rstrip('\n') )
  #  f.write( errMess )
  except:
    e = sys.exc_info()[0]
    print(e)
    f.write(str(e))
    errMess = 'Error in [' + str(num) + ']: ' + str(content[num])
    print( errMess.rstrip('\n') )
    f.write( errMess )
  else: #r.status_code === 200
    print('Processing in [' + str(num) + ']..', end='\r')
  num+=1
f.close()
