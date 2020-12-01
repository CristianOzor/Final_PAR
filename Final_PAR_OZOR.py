import csv
import os.path
import datetime


user_input = input("Ingrese el nombre del archivo con los datos de los clientes de la empresa: ")
choise_file = (f"{user_input}.csv")

os.system('cls')

user_input2 = input("Ingrese el nombre del archivo que contienen los datos de los viajes por cliente: ")
choise_file2 = (f"{user_input2}.csv")

#Voy a leer el archivo para alojar todos los datos en una lista
def _read_(archivo_clientes):
	os.system('cls')
	
	
	listado_clientes = []
	
	try:
		with open (archivo_clientes, "r", newline = '') as file:
			
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
		
	#Para q el código no se rompa al ingresar un archivo por falta de alguna columna y ayuda en la opcion de busqueda 
	except IndexError:
		print("ERROR! Se borró alguna columna en el archivo")
		
		
	
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
		os.system('cls')                            
		print("La busqueda no arrojó ningún resultado \nSugerencia: Intente volver a poner los nombres de los archivos nuevamente.\n\n")
	   
	
	

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
			
			
	
	if (localizado > 0):	
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")
		print(f"Empresa: {company}\nTotal de usuarios: {localizado}")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")
		print(f"{campos}\n")
	
		for item in clientes:
			print(f"{item}\n")
		
	else:
		os.system('cls')                           
		print("La busqueda no arrojó ningún resultado\n\n")
	
#Consultar montos por empresa
def company_amounts(archivo_clientes, archivo_viajes):
	os.system('cls')
	
	listado_viajes = []
	
	total_empresa = 0
	empresa_localizada = ""
	flag_localizado = 0
	
	empresa_buscada = input("Ingrese el nombre de la empresa a consultar: ")	
	
	
	try:
		#Hay q abrir el archivo en utf para que corra bien el archivo viajes por la codificación que tiene el otro lo abro en modo sistema
		with open (archivo_viajes, "r" , newline = '', encoding = 'utf-8') as file1, open (archivo_clientes, "r" , newline = '') as file2:
		
			viajes_csv = csv.reader(file1)
			clientes_csv = csv.reader(file2)
		
			#salteo el encabezado
			next(viajes_csv)
			next(clientes_csv)
		
			#empiezo a leer
			viajes = next(viajes_csv, None)
			clientes = next(clientes_csv, None)
				
			while viajes:
				
				if ((len(viajes[0]) >6) and (len(viajes[0]) < 9)):
					try:
						dni = int(viajes[0])
						
							
					except ValueError:
						print("Hay un caracter no numérico")
				
				#Tuve que configurar windows para que me tome el . como separador de decimales y la , como separador de miles
				monto = viajes[2].replace(',', '.')
				monto = float(monto)
				
				dict_Viajes = {"Documento": dni, "Monto": monto}
				listado_viajes.append(dict_Viajes)
				
				viajes = next(viajes_csv, None)
			
			while clientes:
				
				if (empresa_buscada in clientes[5]):
					empresa_localizada = clientes[5]
					
					flag_localizado += 1
					
					for dni in listado_viajes:
						if dni["Documento"] == int(clientes[2]) :
							total_empresa += dni["Monto"]
				
				
				clientes = next(clientes_csv, None)	
					
	except IOError:
		print("hubo un error de lectura en alguno de los archivos. Por favor, asegurese de ingresarlos de forma correcta")
	
	except IndexError:
		print("ERROR! Se modificaron columnas en el archivo")
	except Exception as errorCode:
		print("Posiblemente ingreso los archivos al revés")
		print(errorCode)
	
	os.system('cls')
	
	if (flag_localizado > 0):		
		print("-------------------------------------------------------------------------------------------------------------")
		#formato de solo 2 decimales al float
		print(f"{empresa_localizada} ${total_empresa:10.2f}")
		print("-------------------------------------------------------------------------------------------------------------\n\n")
	
	else: 
		print("No existen registros de la empresa solicitada\n\n")
	
	#print(listado_viajes)
	
#Consultar total de viajes y monto por DNI
def amounts_travels_dni():
	pass

#guardar consulta
def save_query():
	pass

#ver consultas
def inquiries():
	pass

os.system('cls')
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
			find_client(_read_(choise_file), palabra_recibida, CAMPOS)
		if opcion == "2":
			os.system('cls')
			palabra_recibida = input("Ingrese el nombre completo o parcial de la empresa a consultar: ")
			find_company(_read_(choise_file), palabra_recibida, CAMPOS)
		if opcion == "3":
			company_amounts(choise_file, choise_file2)
		if opcion == "4":
			amounts_travels_dni()
		else:
			print("Por favor elija una opcion valida")
	
menu()




