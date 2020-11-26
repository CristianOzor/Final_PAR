import csv
import os.path
import datetime



#Voy a leer el archivo para alojar todos los datos en una lista
def _read_():
	os.system('cls')
	
	user_input = input("Ingrese el nombre del archivo para consultar: ")
	choise_file = (f"{user_input}.csv")
	
	listado_clientes = []
	
	try:
		with open (choise_file, "r", newline = '') as file:
			
			#Cargo el archivo en una variable
			clientes_csv = csv.reader(file)
				
			#salteo el encabezado
			next(clientes_csv)
			
			#empiezo a leer el archivo
			clientes = next(clientes_csv, None)
		
			while clientes:
				if (not clientes or clientes[0] != clientes[0]):
					print("\tNo hay un cliente registrado")
				else:
					listado_clientes.append([clientes[0], clientes[1], clientes[2], clientes[3], clientes[4], clientes[5]])
					
										
					
				clientes = next(clientes_csv, None)
				
	
	except IOError:
		print("hubo un error en la lectura")
	
	return listado_clientes
		
	


def find_client(listado, palabra, campos):
	localizado = 0                             
	
	os.system('cls')
	
	print(campos)
	print("---------------------------------------------------------------------------------------------------------------------------------------------------")
	                        
	for cliente in listado:                        
		if palabra in cliente[0]:
			
			print(f"{cliente[0]}, {cliente[1]}, {cliente[2]}, {cliente[3]}, {cliente[4]}, {cliente[5]}\n")
			localizado += 1       
	
	print("---------------------------------------------------------------------------------------------------------------------------------------------------\n\n")		
	if localizado == 0:                               
		print("La busqueda no arrojó ningún resultado\n\n")
	   
	
	

#Busqueda por empresa. Total de usuarios por empresa
def find_company(listado, palabra, campos):
	localizado = 0                             
	company = ""
	clientes = []
	os.system('cls')
        
	for empresa in listado:                        
		if palabra in empresa[5]:
			
			#print(f"{cliente[0]}, {cliente[1]}, {cliente[2]}, {cliente[3]}, {cliente[4]}, {cliente[5]}\n")
			company = empresa[5]
			clientes.append([empresa[0], empresa[1], empresa[2], empresa[3], empresa[4], empresa[5]])
			localizado += 1       
			
			
	if localizado == 0:                               
		print("La busqueda no arrojó ningún resultado\n\n")
		
	print("---------------------------------------------------------------------------------------------------------------------------------------------------")
	print(f"Empresa: {company}\nTotal de usuarios: {localizado}")
	print("---------------------------------------------------------------------------------------------------------------------------------------------------")
	print(campos)
	for item in clientes:
		print(f"{item}\n")
	
#Consultar montos por empresa
def company_amounts():
	pass

#Consultar total de viajes y monto por DNI
def amounts_travels_dni():
	pass

#guardar consulta
def save_query():
	pass

#ver consultas
def inquiries():
	pass


def menu():
	
	CAMPOS = ['Nombre', 'Dirección', 'Documento', 'Fecha Alta', 'Correo Electrónico', 'Empresa']

	while True:
		print("Elija una opcion: \n 1.Buscar cliente \n 2.Total de usuarios por empresa \n 3.Consultar montos por empresa")
		print(" 4.Consultar total de viajes y monto por DNI \n 5. Salir\n")
		opcion = input("")
		
		if opcion == "5":
			exit()
		if opcion == "1":
			os.system('cls')
			palabra_recibida = input("Ingrese el nombre completo o parcial de la persona a buscar: ")
			find_client(_read_(), palabra_recibida, CAMPOS)
		if opcion == "2":
			os.system('cls')
			palabra_recibida = input("Ingrese el nombre completo o parcial de la empresa a consultar: ")
			find_company(_read_(), palabra_recibida, CAMPOS)
		if opcion == "3":
			company_amounts()
		if opcion == "4":
			amounts_travels_dni()
		else:
			print("Por favor elija una opcion valida")
	
menu()




