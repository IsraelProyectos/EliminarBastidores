import accesoOracle

class deleteBastidores():
	def __init__(self, textAreaBastidores, textAreaTransactionID):
		self.textAreaBastidores=textAreaBastidores
		self.textAreaTransactionID=textAreaTransactionID
		
	def delete(self):
		#self.connectionString='WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH'
		connectionString='DRUGO73/lokomotiv1970@127.0.0.1/xe'
		ao=accesoOracle.connectToOracle(connectionString)
		if ao.connect():
			print("Conexion establecida")
			ao.disConnect()
		else:
			print("Conexion rechazada")

    	