import cx_Oracle


class connectToOracle():

	def __init__(self,connectionString,textAreaBastidores):
		self.query=query
		self.connectionString=connectionString
	def connect(self):
		try:	   
			con =  cx_Oracle.connect(self.connectionString)
			#print(con.version)
			#cur = con.cursor()
			#cur.execute(self.query)
			#cur.execute("select * from sko_exec_transactions")
			#for result in cur:
			#print(result)
			#return cur
			#cur.close()
			#con.close()

		except cx_Oracle.DatabaseError as e:
			error, = e.args
			if error.code == 24373:
				print("Se ha entregado una query vacia")
			
