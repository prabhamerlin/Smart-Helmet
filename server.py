import sqlite3
import serial
import datetime

con=sqlite3.connect('database.db')
if con:
	print 'Connected to Data base succesfully'
else :
	print 'failed Database connection cahnge permission to read and write'



if con.execute(''' CREATE TABLE Datas
	        (SNO INTEGER PRIMARY KEY AUTOINCREMENT,
	         TEMP INTEGER,
		 BPM INTEGER,VAL INTEGER);'''):



	      
	print "Table created succesfully"		
else:
	print "Table already exist"
	
port=serial.Serial("/dev/ttyACM0",115200)
if port:
	print "opened port succesfully"
	
	while 1:
		
		#print 'waiting...'
		port.flushInput()




		rcv=port.read(2)
		rcv1=port.read(2)
		rcv2=port.read(2)

		#rcv3=port.read(2)

		#time.sleep(0.5)
		#rcv=rcv.strip()
		

		if len(rcv)>1:
			if len(rcv1)>1:
				if len(rcv2)>1:
					print "Temperature: " + rcv
					print "BPS: " + rcv1
					print "Button stat: 0" + rcv2

					#print "somethng:" +rcv3


		"""
		if len(rcv)>0:
			temp=int(rcv[0:2])
			print "temp is:"
			print temp
			
			#bpm=int(rcv[2:3])
			
			bpm=int(rcv[2:4])
			print "BPM is:"
			print bpm
			value=int(rcv[4:-1])
			print "Button Status:"
			print value
			

			
			value=int(rcv[2:3])
			print "Button Status:"
			print value
			bpm=int(rcv[3:-1])
			print "BPM is:"
			print bpm
		
		"""

			


		
	
		

		#con.execute("INSERT INTO Datas (TEMP,VAL,BPM) VALUES (?,?,?);",(temp,bpm,value))
		con.execute("INSERT INTO Datas (TEMP,BPM,VAL) VALUES (?,?,?);",(rcv,rcv1,rcv2))
		con.commit()

con.close()
port.close()			

		
			
		
	

