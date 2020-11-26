import csv
import os.path

def _read_():

	user_input = input("Ingrese el nombre del archivo para consultar: ")
	choise_file = (f"{user_input}.csv")
	
	try:
		with open (choise_file, "r", newline = '') as file:
			
			#Cargo el documento en una variable
			clientes_csv = csv.reader(file)
				
			#salteo el encabezado
			next(clientes_csv)
			
			#empiezo a leer
			clientes = next(clientes_csv, None)
		
			while clientes:
				print(clientes[0])
					
				clientes = next(clientes_csv, None)
				
	
	except IOError:
		print("hubo un error en la lectura")

_read_()
