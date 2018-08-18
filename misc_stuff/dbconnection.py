import mysql.connector
from datetime import date, datetime, timedelta

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'database': 'test',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

print('Now selecting and printing ...')
query = ("SELECT id, firstname, lastname, startdate, enddate FROM test.pythondemo")
cursor.execute(query)

for (id, firstname, lastname, startdate, enddate) in cursor:
  print(f'{firstname} has id no: {id} and period is from {startdate} to {enddate}')

print("Now inserting ...")
tomorrow = datetime.now().date() + timedelta(days=1)
nextweek = datetime.now().date() + timedelta(days=8)

insert_stmt = ("INSERT INTO `test`.`pythondemo` (`firstname`,`lastname`,`startdate`,`enddate`)VALUES(%s,%s,%s,%s)")
insert_stmt2 = ("INSERT INTO `test`.`pythondemo` (`firstname`,`lastname`,`startdate`,`enddate`)VALUES(%(firstname)s,%(lastname)s,%(startdate)s,%(enddate)s)")
data1 = ('Hassan', 'Hasani', tomorrow, date(2020,11,13))
data2 = {'firstname': 'Hanne', 'lastname':'Hansen', 'startdate':date(2002,4,3),'enddate':nextweek }

cursor.execute(insert_stmt, data1)
lastID = cursor.lastrowid
print(f'Last id generated by the server:{lastID}')

cursor.execute(insert_stmt2, data2) # Just to show an alternative way.
cnx.commit()
cursor.close()
cnx.close()