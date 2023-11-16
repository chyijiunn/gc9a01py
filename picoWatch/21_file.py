import time 
data = open('record','a')
now = list(time.localtime())
data.write(str(now[3])+':'+str(now[4])+':'+str(now[5])+'\n')
data.close()