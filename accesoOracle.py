import cx_Oracle


class connectToOracle():

	def __init__(self,connectionString):
		self.connectionString=connectionString

	def connect(self):
		try:
		    #Conexion a BBDD	   
			self.con =  cx_Oracle.connect(self.connectionString)
			
			#Retornar el objeto conexion
			return(self.con)

		except cx_Oracle.DatabaseError as e:

			#Excepciones de la conexion
			error, = e.args

			#Entrega del campo de la query vacia(Solo se utiliza para escribir directamente la query en un TextBox)
			if error.code == 24373:
				print("Se ha entregado una query vacia")
			#Error en el string de conexion	
			elif (error.code == 12154) or (error.code == 12560) or (error.code == 12541):
				print("ConexionString es erroneo")
			elif error.code == 1017:
				print("Usuario y/o contrasena incorrecta")
			elif error.code == 28000:
				print("La cuenta esta bloqueada")	
			else:
				print("No se ha  podido conectar")
	
	#Metodo para hacer commit en la BBDD y cerrar la conexion		
	def disConnect(self):
		self.con.commit()
		self.con.close()
		print("Conexion cerrada")