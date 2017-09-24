import accesoOracle

class deleteBastidores():
	def __init__(self, textAreaBastidores, textAreaTransactionID):
		self.textAreaBastidores=textAreaBastidores
		self.textAreaTransactionID=textAreaTransactionID
		
	def delete(self):
		#self.__cursor.callproc("PKG_HR.FIND_EMPLOYEES"
		#self.connectionString='WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH'
		connectionString='DRUGO73/lokomotiv1970@127.0.0.1/xe'
		ao=accesoOracle.connectToOracle(connectionString)
		
		if ao.connect():
			print("Conexion establecida")
		else:
			print("Conexion rechazada")

		for transactionID in self.textAreaTransactionID.split():
			print(transactionID)
			for bastidores in self.textAreaBastidores.split():
				print(transactionID, bastidores)
				cur = ao.connect().cursor()
				feo='FEO'
				#cur.callproc("deleteBastidoresFF(80, FEO)")
				cur.callproc("deleteBastidoresFF", [80, 'FEO'])
				#cur.execute("UPDATE GT_ACTION_PERSONALIZATION_PROX SET BASTIDOR= 'OTRAVEZ' WHERE ID = 7")
				#cur.execute("DELETE GT_ACTION_PERSONALIZATION_PROX WHERE ID = 7")
				# for personaje in cursorData:
				# 	print(personaje)
				cur.close()
				ao.disConnect()
								

    	