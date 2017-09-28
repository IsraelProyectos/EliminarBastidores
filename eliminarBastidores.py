import accesoOracle

class deleteBastidores():
	def __init__(self, textAreaBastidores, textAreaTransactionID):
		self.textAreaBastidores=textAreaBastidores
		self.textAreaTransactionID=textAreaTransactionID
		
	def delete(self):
		#self.__cursor.callproc("PKG_HR.FIND_EMPLOYEES"
		#self.connectionString='BDC_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH'
		connectionString='SKO_BDC_RELAY/@bvn002b.bbdo.local/PRDBATCH'
		#connectionString='DRUGO73/lokomotiv1970@127.0.0.1/xe'

		#LLamada a la clase de conexion a BBDD pasandole el connectionString
		ao=accesoOracle.connectToOracle(connectionString)

		try:
		
		#if ao.connect():
			#print("Conexion establecida")
		#else:
			#print("Conexion rechazada")
			ao.connect()

		#Recorrido de los dos TextBox	
			for transactionID in self.textAreaTransactionID.split():
				
				transactionID = int(transactionID)

				for bastidor in self.textAreaBastidores.split():
					print(transactionID, bastidor)

					#Creando cursor para poder ejecutar la procedure
					cursor = ao.connect().cursor()

					#LLamada al procedure para borrar el registro pasandole el transactionID y el bastidor como parametros
					#Al enviar numeros al procedure debe recibirlos como INTEGER no como NUMBER 
					cursor.callproc("deleteBastidoresFF", [transactionID, bastidor])
					
					#Cerrando cursor
					cursor.close()

					#LLamada al metodo para cerrar conexiones
					ao.disConnect()
		except:
			print("Error de conexion")

    	