import csv
import os.path

#buscar clientes
def find_client():
	pass

#Total de usuarios por empresa
def total_users():
	pass

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
	
	CAMPOS = ['Nombre', 'Direccion', 'Documento', 'Fecha Alta', 'Correo Electronico', 'Empresa']

	while True:
		print("Elija una opcion: \n 1.Buscar cliente \n 2.Total de usuarios por empresa \n 3.Consultar montos por empresa")
		print(" 4.Consultar total de viajes y monto por DNI \n 5. Salir\n")
		opcion = input("")
		
		if opcion == "5":
			exit()
		if opcion == "1":
			find_client()
		if opcion == "2":
			total_users()
		if opcion == "3":
			company_amounts()
		if opcion == "4":
			amounts_travels_dni()
		else:
			print("Por favor elija una opcion valida")
	
menu()
