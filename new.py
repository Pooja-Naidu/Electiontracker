import datetime
import time
#import random
import pymysql
    
def updatedb():
  db = pymysql.connect("localhost", "root", "", "electiontracker") 
  cur = db.cursor()
  cur.execute("select * from main;")
  
  for i in cur.fetchall():
   # n = [x for x in range(10)]
    #random.shuffle(n)
    #cur.execute("update main set Administration=%s,Corruption=%s,Schemes=%s,Literacy=%s,Employment=%s,RuralDevelopment=%s,budget=%s,lawandjustice=%s,infrastructure=%s,others=%s where SNo=%s",(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],id ))
    ttl=((i[5]*15)+(i[6]*8)+(i[7]*15)+(i[8]*5)+(i[9]*13)+(i[10]*11)+(i[11]*7)+(i[12]*4)+(i[13]*12)+(i[14]*10))/10
    now = datetime.datetime.now()
    if(ttl<= 30):
        cur.execute("INSERT INTO updatetable(updatedate, SNo, total,status) VALUES (%s, %s, %s,%s)",(now,i[0],ttl,"Poor"))
    elif(ttl>30 and ttl<=50):
       cur.execute("INSERT INTO updatetable(updatedate, SNo, total,status) VALUES (%s, %s, %s,%s)",(now,i[0],ttl,"Average"))
    elif(ttl>50 and ttl<=70):
       cur.execute("INSERT INTO updatetable(updatedate, SNo, total,status) VALUES (%s, %s, %s,%s)",(now,i[0],ttl,"good"))
    elif(ttl>70 and ttl<90):
       cur.execute("INSERT INTO updatetable(updatedate, SNo, total,status) VALUES (%s, %s, %s,%s)",(now,i[0],ttl,"Very Good"))
    elif(ttl>90 and ttl<=100):
      cur.execute("INSERT INTO updatetable(updatedate, SNo, total,status) VALUES (%s, %s, %s,%s)",(now,i[0],ttl,"Excellent"))
  print("done")
  cur.close()
  db.close()
#schedule.every(1).minute.do(updatedb)
while(1):
   # rnumber()
    updatedb()
    time.sleep(60)

