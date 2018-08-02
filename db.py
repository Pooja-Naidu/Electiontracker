import time
import pymysql

def updatedb():
  db = pymysql.connect("localhost", "root", "", "electiontracker")
  cur = db.cursor()
  print ('\nStateNo   Statename   Ruling Party   \tPercentage  ')    
  cur.execute("select * from main;")
  for i in cur.fetchall():
    ttl=((i[5]*15)+(i[6]*8)+(i[7]*15)+(i[8]*5)+(i[9]*13)+(i[10]*11)+(i[11]*7)+(i[12]*4)+(i[13]*12)+(i[14]*10))/10
    if(ttl<= 30):
      print(i[0], i[1],"|",i[4],"|",ttl,"|","Poor\n")
    elif(ttl>30 and ttl<=50):
      print(i[0], i[1],"|",i[4],"|",ttl,"|","Average\n")
    # break
    elif(ttl>50 and ttl<=70):
      print(i[0], i[1],"|",i[4],"|",ttl,"|","Good\n")
    # break
    elif(ttl>70 and ttl<90):
      print(i[0], i[1],"|",i[4],"|",ttl,"|","Very good\n")
    # break
    elif(ttl>90 and ttl<=100):
      print(i[0], i[1],"|",i[4],"|",ttl,"|","Excellent\n")
     #break 
  cur.close()
  db.close()
#schedule.every(1).minute.do(updatedb)
while(1):
    time.sleep(60)
    updatedb()