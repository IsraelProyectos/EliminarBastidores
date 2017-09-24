import cx_Oracle


class connectToOracle():

	def __init__(self,connectionString):
		self.connectionString=connectionString
		#self.textAreaBastidores=textAreaBastidores
	def connect(self):
		try:	   
			self.con =  cx_Oracle.connect(self.connectionString)
			#for bastidor in self.textAreaBastidores.split():
				#print(bastidor)
			
			#print(con.version)
			#cur = con.cursor()
			#cur.execute(self.query)
			#cur.execute("select * from sko_exec_transactions")
			#for result in cur:
			#print(result)
			#return cur
			#cur.close()
			#con.close()
			return(self.con)

		except cx_Oracle.DatabaseError as e:
			error, = e.args
			if error.code == 24373:
				print("Se ha entregado una query vacia")
			elif error.code == 12154:
				print("ConexionString es erroneo")
				return(False)
			
	def disConnect(self):
		self.con.commit()
		self.con.close()
		print("Conexion cerrada")