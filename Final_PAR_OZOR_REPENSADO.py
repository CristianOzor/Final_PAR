import csv
import os.path
import datetime

user_input = input("Ingrese el nombre del archivo con los datos de los clientes de la empresa: ")
archivo_clientes = (f"{user_input}.csv")

#limpio pantalla
os.system('cls')

user_input2 = input("Ingrese el nombre del archivo que contienen los datos de los viajes por cliente: ")
archivo_viajes = (f"{user_input2}.csv")

#voy a recorrer los dos archivos y a crear listas
def listados(archivo_clientes, archivo_viajes):
	os.system('cls')
	
	listado_clientes = []
	listado_viajes = []
	empresas = []
	
	try:
		with open (archivo_clientes, "r", newline = '') as file, open (archivo_viajes, "r" , newline = '', encoding = 'utf-8') as file2:
			
			#Cargo el archivo en una variable
			clientes_csv = csv.reader(file)
			viajes_csv = csv.reader(file2)
				
			#salteo el encabezado
			next(clientes_csv)
			next(viajes_csv)
			
			#empiezo a leer el archivo
			clientes = next(clientes_csv, None)
			viajes = next(viajes_csv, None)
			
			while clientes:
				if (not clientes or clientes[0] != clientes[0]):
					print("\tNo hay un cliente registrado")
				else:
					if ((len(clientes[2]) >6) and (len(clientes[2]) < 9)):
					
						try:
							clientes[2] = int(clientes[2])
						
							
						except ValueError:
							print("Hay un caracter no numérico")
					
					else:
						print("el documento ingresado no es válido")
					listado_clientes.append([clientes[0], clientes[1], clientes[2], clientes[3], clientes[4], clientes[5]])
					
				for empresa in clientes[5]:
					if not clientes[5] in empresas:
						empresas.append(clientes[5])						
					
				clientes = next(clientes_csv, None)
				
			while viajes:
				if (not viajes or viajes[0] != viajes[0]):
					print("\tNo hay viajes registrados")
				
				else:
					if ((len(viajes[0]) >6) and (len(viajes[0]) < 9)):
					
						try:
							viajes[0] = int(viajes[0])
						
							
						except ValueError:
							print("Hay un caracter no numérico")
					
					else:
						print("el documento ingresado no es válido")
				
					#Tuve que configurar windows para que me tome el . como separador de decimales y la , como separador de miles
					viajes[2] = float(viajes[2].replace(',', '.'))
				
					
					listado_viajes.append([viajes[0], viajes[1], viajes[2]])
				
				viajes = next(viajes_csv, None)
				
	except IOError:
		print("hubo un error en la lectura")
	
	except:
		#por ejemplo si pongo viajes donde pide clientes
		print("Colocó mal los archivos\n\n")	
	
	return listado_clientes, listado_viajes, empresas


#pongo en variables globales el return de las 3 listas principales para el programa
client_list, travel_list, business_list = listados(archivo_clientes, archivo_viajes)

#print(client_list)
#print(travel_list)
#print(business_list)

#Búsqueda de clientes por nombre
def find_client(listado, palabra, campos):
	localizado = 0                             
	
	os.system('cls')
	
	print(f"[{campos[0]}, {campos[1]}, {campos[2]}, {campos[3]}, {campos[4]}, {campos[5]}]")
	print("---------------------------------------------------------------------------------------------------------------------------------------------------")
	                        
	for cliente in listado:                        
		if palabra in cliente[0]:
			
			localizado += 1
			print(f"[{cliente[0]}, {cliente[1]}, {cliente[2]}, {cliente[3]}, {cliente[4]}, {cliente[5]}]\n")
			       
	
	print("---------------------------------------------------------------------------------------------------------------------------------------------------\n\n")		
	
	
	if localizado == 0:
		os.system('cls')                            
		print("La busqueda no arrojó ningún resultado.\n\n")


#Busqueda por empresa. Total de usuarios por empresa
def find_company(listado, campos, empresas):
	localizado = 0                             
	company = ""
	clientes = []
	os.system('cls')
   
	print("Las empresas agendadas son:")
	for empresa in empresas:
		print(f"{empresa}")
    
	palabra_recibida = input("\n\nIngrese el nombre completo de la empresa a consultar: ")
      
	for empresa in listado:                        
		if palabra_recibida == empresa[5]:
			
			#print(f"{cliente[0]}, {cliente[1]}, {cliente[2]}, {cliente[3]}, {cliente[4]}, {cliente[5]}\n")
			company = empresa[5]
			clientes.append([empresa[0], empresa[1], empresa[2], empresa[3], empresa[4], empresa[5]])
			localizado += 1       
			
				
	if (localizado > 0):
		os.system('cls')
			
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")
		print(f"Empresa: {company}\nTotal de usuarios: {localizado}")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")
		print(f"[{campos[0]}, {campos[1]}, {campos[2]}, {campos[3]}, {campos[4]}, {campos[5]}]\n")
	
		for item in clientes:
			print(f"[{item[0]}, {item[2]}, {item[3]}, {item[4]}, {item[5]}]\n")
			#print(f"{item}\n")
		
	else:
		os.system('cls')                           
		print("La busqueda no arrojó ningún resultado\n\n")

def company_amounts(listado_cliente, listado_viajes, empresas):
	os.system('cls')
	

	
	total_empresa = 0
	empresa_localizada = ""
	flag_localizado = 0
	
	#printeo lista de empresas porque la empresa tiene que ser igual ya que si es busqueda parcial e
	#introduce por ejemplo una B se van a contabilizar dos empresas BYMA y la del Ministerio
	#Hay q ser precisos
	
	print("Las empresas agendadas son:")
	for empresa in empresas:
		print(f"{empresa}")
	
	empresa_buscada = input("\n\nIngrese el nombre completo de la empresa a consultar: ")	
			
	#Trabajo con los dos listados principales el de clientes y el de viajes		
	for cliente in listado_cliente:
				
		if (empresa_buscada == cliente[5]):
			empresa_localizada = cliente[5]
			#print(cliente[5])		
			flag_localizado += 1
					
			for dni in listado_viajes:
				if dni[0] == int(cliente[2]) :
					total_empresa += dni[2]
				
				
				
	os.system('cls')
	
	if (flag_localizado > 0):		
		print("-------------------------------------------------------------------------------------------------------------")
		#formato de solo 2 decimales al float
		print(f"{empresa_localizada} ${total_empresa:10.2f}")
		print("-------------------------------------------------------------------------------------------------------------\n\n")
	
	else: 
		print("No existen registros de la empresa solicitada\n\n")
		

def amounts_travels_dni(listado_clientes, listado_viajes, campos, campos2):
	identificacion = 0
	localizado = 0
	total_viajes = 0
	new_list_employee = []
	new_list_viajes = []
	
	documento = input("Ingrese el número de documento del empleado a consultar: ")
	
	if ((len(documento) >6) and (len(documento) < 9)):
					
		try:
			documento = int(documento)
						
		except ValueError:
			print("Hay un caracter no numérico\n")
					
	else:
		print("el documento ingresado no es válido\n")
	
	                        
	for dni in listado_clientes:
		#print(dni)                        
		if documento == dni[2]:
			localizado += 1  
			print(documento)
			identificacion = documento
			new_list_employee.append([dni[0], dni[1], dni[2], dni[3], dni[4], dni[5]])
			
			     
	
	
	for dni in listado_viajes:
		if identificacion == dni[0]:
			new_list_viajes.append([dni[0], dni[1], dni[2]])
			total_viajes += dni[2]
		
		
	
	if localizado > 0:
		os.system('cls')
		
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")		
		print(f"Documento: {identificacion}")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")		
		print(f"[{campos[0]}, {campos[1]}, {campos[2]}, {campos[3]}, {campos[4]}, {campos[5]}]\n")
		
		for elemento in new_list_employee:
			print(f"[{elemento[0]}, {elemento[1]}, {elemento[2]}, {elemento[3]}, {elemento[4]}, {elemento[5]}]")
		
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")		
		print(f"Total viajes: {len(new_list_viajes)}, Monto: ${total_viajes:0.2f}")
		print("---------------------------------------------------------------------------------------------------------------------------------------------------")		
		print(f"[{campos2[0]}, {campos2[1]}, {campos2[2]}]")
		
		for elemento in new_list_viajes:
			print(f"[{elemento[0]}, {elemento[1]}, {elemento[2]}]")
		
		print("\n\n")
	
	if localizado == 0:
		#os.system('cls')                            
		print("La busqueda no arrojó ningún resultado.\n\n")

#guardar archivo log leyendo pág 131 Aprendiendo a programar usando Python/ se va a usar el módulo datetime visto en w3schools
def save_log(consulta):
	
	archivo = "Taxi.log"
	
	try:
		archivo_existe = os.path.isfile(archivo)
		with open(archivo, "a", newline = '', encoding = 'utf-8') as file:
			
		   #Cargo en una variable la hora de ingreso de la consulta
			hora_actual = str(datetime.datetime.now())
		
			if not archivo_existe:
				file.writelines("Acción, Fecha\n")
				file.writelines("-----------------------------------------------------------------\n")
			
			file.writelines("..................................................................\n")
			file.write(f"{consulta}, {hora_actual}\n")
            
			return
	except IOError:
		print("Error fatal inesperado")

#ver consultas
def load_log(archivo, password):
	admin_pass = "paradigmas"

		
	if (password == admin_pass):
	
		try:
			with open(archivo, "r", newline = '', encoding = 'utf-8') as file:
			
				for linea in file:
					print(f"{linea}\n")
            
			
		except IOError:
			print("Error fatal inesperado")
	else:
		print("Acceso denegado\n\n")

#os.system('cls')
def main():
	
	CAMPOS = ['Nombre', 'Dirección', 'Documento', 'Fecha Alta', 'Correo Electrónico', 'Empresa']
	CAMPOS2 = ['Documento','fecha', 'monto']

	while True:
		consulta = "Menú"
		save_log(consulta)
		print("Elija una opcion: \n 1.Búsqueda de clientes por nombre \n 2.Búsqueda total usuarios por empresa \n 3.Consultar montos por empresa")
		print(" 4.Consultar total de viajes y monto por DNI \n 5.Recurso del administrador \n 6.Salir\n")
		opcion = input("")
		
		if opcion == "6":
			consulta = "Salir"
			save_log(consulta)
			exit()
		if opcion == "1":
			consulta = "Búsqueda de clientes por nombre"
			save_log(consulta)
			
			os.system('cls')
			palabra_recibida = input("Ingrese el nombre completo o parcial de la persona a buscar: ")
			find_client(client_list, palabra_recibida, CAMPOS)
		if opcion == "2":
			consulta = "Búsqueda total usuarios por empresa"
			save_log(consulta)
			
			os.system('cls')
			
			find_company(client_list, CAMPOS, business_list)
			
		if opcion == "3":
			consulta = "Consultar montos por empresa"
			save_log(consulta)
			
			os.system('cls')
			company_amounts(client_list, travel_list, business_list)
			
		if opcion == "4":
			consulta = "Consultar total de viajes y monto por DNI"
			save_log(consulta)
			
			os.system('cls')
			
			amounts_travels_dni(client_list, travel_list, CAMPOS, CAMPOS2)
			
			
		if opcion == "5":
			#Consulta el archivo .log
			consulta = "Recurso administrador"
			save_log(consulta)
			os.system('cls')
			
			password = input("Ingrese el código de acceso:\n")
			
			os.system('cls')
			load_log("Taxi.log", password)
		
		else:
			consulta = "Ingreso inválido al menú"
			save_log(consulta)
			
			
			print("Por favor elija una opcion valida")
			
	
main()
