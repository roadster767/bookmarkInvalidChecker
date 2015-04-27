import requests
import sys
import re

if len(sys.argv) != 2:
  print("argv error")
  sys.exit()
textfile = open(sys.argv[1], 'r')
filetext = textfile.read()
textfile.close()
content = re.findall(r'HREF="([^"]*)"', filetext)

#with open('input.txt') as f:
#    content = f.readlines()
#f.close()

length = len(content)
num = 0

f = open('errorLog', 'w')
while num < length:
  try:  
    r = requests.get(''+str(content[num].rstrip('\n')), timeout=10.0)
  #except requests.exceptions.ConnectionError:    
  #  errMess = 'Connect Error in: ' + str(content[num])
  #  print( errMess.rstrip('\n') )
  #  f.write( errMess )
  except:
    e = sys.exc_info()[0]
    print(e)
    f.write(str(e) + '\n')
    errMess = 'Error in [' + str(num) + ']: ' + str(content[num])
    print(errMess.rstrip('\n'))
    f.write(errMess + '\n')
    f.flush()
  else: #r.status_code === 200
    print('Processing in [' + str(num) + '].. : ' + str(content[num]))
  num+=1
f.close()
