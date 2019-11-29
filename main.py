import csv
import datetime
import matplotlib.pyplot as plt
import sys

""" Tarea 1: 
Define completamente una estructura de datos (registro) ADECUADA
para guardar la información de UNA línea del fichero para poder
trabajar ADECUADAMENTE con ella. 
La estructura de datos (registro) se llamará InfoTerremoto.
Deberá incluir NECESARIAMENTE un campo de tipo Fecha 
y un campo de tipo Hora para guardar la fecha y hora del terremoto. """

class InfoTerremoto:
    def __init__(self, Year, Month, Day, Hora, Mag, Lat, Lon, Depth_km, Region, IRIS_ID, Timestamp):
        self.Year = int(Year)
        self.Month = int(Month)
        self.Day = int(Day)
        self.Hora = Hora
        self.Fecha = datetime.date(int(Year),int(Month),int(Day))
        self.Mag = float(Mag)
        self.Lat = float(Lat)
        self.Lon = float(Lon)
        self.Depth_km = float(Depth_km)
        self.Region = Region
        self.IRIS_ID = int(IRIS_ID)
        self.Timestamp = int(Timestamp)

    def show_info(self):
        print("Fecha: " + str(self.Fecha))
        print("Hora: " + str(self.Hora))
        print("Magnitud: " + str(self.Mag))
        print("Ubicacion: " + "Latitud: " + str(self.Lat) + ", Longitud: " + str(self.Lat))
        print("Profundidad: " + str(self.Depth_km))
        print("IRIS_ID: " + str(self.IRIS_ID))
        print("Region: " + self.Region)

""" Tarea 2:
Define una función AnalizaLinea que permita analizar una línea del fichero y rellenar 
y devolver UNA estructura de datos InfoTerremoto con la información de 
UNA línea del fichero pasada como parámetro.
Comprueba el correcto funcionamiento de la función creando un pequeño programa principal 
que llame a la función con una línea del fichero (str) como parámetro 
y que, a continuación, muestre la información de los diferentes campos de InfoTerremoto. """

def AnalizaLinea(linea):
    DatosLinea = linea.split(";")
    return InfoTerremoto(DatosLinea[0],DatosLinea[1],DatosLinea[2],DatosLinea[3],DatosLinea[4],DatosLinea[5],DatosLinea[6],DatosLinea[7],DatosLinea[8],DatosLinea[9],DatosLinea[10])

""" Tarea 3: 
Define una función LeerFichero que permita leer un fichero linea 
a linea con la información de los terremotos guardada en el fichero. 
A la función se le pasará el NOMBRE del fichero y devolverá una lista de elementos de tipo InfoTerremoto. 
Además, la función devolverá verdadero si se ha podido abrir el fichero 
y falso si no se ha podido abrir el fichero. """

def LeerFichero(fichero):   
    try:
        file = open("C:/Users/kuba/Desktop/python/OOP/infoTerremotos_class/" + fichero + '.csv','r') 
    except:
        print ("El fichero {} no existe.".format(fichero))
        print ("Cerrando programa.")
        sys.exit()
    else:       
        cabecera = True
        registros = []
        for linea in file.readlines():
            if cabecera == True:
                cabecera = False
            else:    
                registros.append(AnalizaLinea(linea))       
    print ("El fichero {} ha sido cargado.".format(fichero))
    file.close()
    return registros

def leerFechas():

    fecha_inicio_str = input("Introduce la fecha de inicio en formato \"dd/mm/yyyy\": ")
    fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, "%d/%m/%Y").date()

    fecha_fin_str = input("Introduce la fecha de finnal en formato \"dd/mm/yyyy\": ")
    fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%d/%m/%Y").date()

    return fecha_inicio, fecha_fin



def MaxTerremoto(registros):
    
    fecha_inicio, fecha_fin = leerFechas()
    
    maxRegister = None
    for r in registros:
        if (r.Fecha >= fecha_inicio) and (r.Fecha <= fecha_fin): 
            if maxRegister is None:
                maxRegister = r  # primer terremoto r.Mag , maxRegister.Mag
            else:
                if (maxRegister.Mag < r.Mag):
                    maxRegister = r
    return maxRegister

""" Tarea 7: 
Realiza una función ObtenerLista que nos devuelva una lista con las magnitudes de los terremotos 
producidos en un area concreta del planeta delimitada por una latitud mínima 
y una latitud máxima y por una longitud mínima y una longitud máxima. """

def ObtenerLista(registros):
    min_lat = float(input("Introduce un minima latitud: "))
    max_lat = float(input("Introduce un maxima latitud: "))
    min_lon = float(input("Introduce un minima longitud: "))
    max_lon = float(input("Introduce un maxima longitud: "))
    listaMag = []
    for r in registros:
        if ((r.Lat <= max_lat) and (r.Lon <= max_lon) and (r.Lat >= min_lat) and (r.Lon >= min_lon)):
            listaMag.append(r.Mag)
    return listaMag

""" Vamos a crear una funcion que nos devuelve objetos de terremotos producidos 
en una area concreta de la planeta """

def ObtenerListaInfo(registros):
    min_lat = float(input("Introduce un minima latitud: "))
    max_lat = float(input("Introduce un maxima latitud: "))
    min_lon = float(input("Introduce un minima longitud: "))
    max_lon = float(input("Introduce un maxima longitud: "))
    terremotos = []
    for r in registros:
        if ((r.Lat <= max_lat) and (r.Lon <= max_lon) and (r.Lat >= min_lat) and (r.Lon >= min_lon)):
            terremotos.append(r)
    return terremotos


""" Tarea 8: 
Realizar una función ObtenerRegiones que nos devuelve en 
una lista todas las regiones que aparecen en la lista de InfoTerremoto. """

def ObtenerRegiones(registros):
    Regiones = []
    for i in registros:
        if (i.Region not in Regiones): #comprobamos si region ya esta en lista Regiones, si no está añadimos 
            Regiones.append(i.Region)
    return Regiones

""" Tarea 9: 
Realizar una función TerremotosRegion que nos diga 
la magnitud media de los terremotos producidos en una región concreta entre dos fechas. 
Se pasará la región y las fechas como parámetros y nos devolverá 
el valor de la magnitud media de los terremotos.
Si la región no existiera devolverá un '-2'. 
Si no se produjeron terremotos en la región entre las fechas pasadas como parámetros, 
devolverá un '-1'.
 """

def TerremotosRegion(registros):
    region = input("Introduce una region sobre la que quieres recibir la información: ")
    regiones_disponibles = ObtenerRegiones(registros)
    if (region not in regiones_disponibles):
        return -2

    fecha_inicio, fecha_fin = leerFechas()

    sumaMag = 0
    numero_terremotos = 0
    for r in registros:
        if (r.Region == region):
            if (r.Fecha >= fecha_inicio) and (r.Fecha <= fecha_fin): 
                sumaMag += r.Mag # registros es una lista de objetos, 'r' es cada objeto, magnitud es 'r.Mag'
                numero_terremotos += 1

    if numero_terremotos > 0:
        media = sumaMag / numero_terremotos
        return round(media, 2)
    else:
        return -1

""" Guardar en un fichero la información de los terremotos entre dos fechas concretas. 
En este fichero SOLO guardaremos la fecha, la magnitud, la latitud y longitud donde se produjo el terremoto 
y la profundidad en kilómetros. 
El orden en las fechas guardadas seguirá siendo desde la fecha más antigua hasta la fecha más actual. """


def GuardarFichero(registros):

    fecha_inicio, fecha_fin = leerFechas()

    print("Introduce el nombre del fichero:")
    nombre_fichero = input() + ".csv"

    f = open(nombre_fichero,'w')
    f.write("Fecha;Magnitud;Latitud;Longitud\n")
    for r in registros:
        if (r.Fecha >= fecha_inicio) and (r.Fecha <= fecha_fin):
            f.write(str(r.Fecha) +';' + str(r.Mag) +';' + str(r.Lat) +';' + str(r.Lon) +';' + str(r.Depth_km) + "\n")
    f.close() 
    print("Su fichero {} se guardó correctamente.".format(nombre_fichero))

    
'''
Imprime el menu por pantalla
'''
def print_menu():
	print("1. Obtener el primer máximo terremoto producido entre dos fechas concretas.")
	print("2. Obtener la magnitud media de los terremotos producidos en una determinada región del planeta entre dos fechas concretas.")
	print("3. Mostrar la gráfica de las magnitudes de los terremotos en una zona del planeta a lo largo del tiempo.")
	print("4. Guardar en un fichero la información de los terremotos entre dos fechas concretas.")
	print("5. Salir del programa.")



""" Tarea 4: 
Una vez realizadas y verificadas las funciones, 
implementa un programa completo PrFinal03.py que pida el nombre de un fichero 
y cargue la información del fichero en una lista de elementos de tipo InfoTerremoto 
(no tiene que mostrar por pantalla la información cargada). """

def main():

    fichero = input("Introduzca el nombre del fichero: ")
    print ("Leyendo {}...".format(fichero)) 
    informacion = LeerFichero(fichero)

    print_menu()
    opcion = int(input("Introduzca la información deseada: ")) 

    if opcion == 1:
        print("*" * 15)
        MaxTerremoto(informacion).show_info()
    elif opcion == 2:
        
        print(TerremotosRegion(informacion))

    elif opcion == 3:
        sub_registros = ObtenerListaInfo(informacion)
        if len(sub_registros)<1:
            print("No hay registros para la ubicación indicada.")
        else:
            listaMagnitudes = []
            listaFechas = []
            for i in sub_registros:
                listaMagnitudes.append(i.Mag)
                listaFechas.append(i.Fecha)
        plt.plot(listaFechas, listaMagnitudes)
        plt.xlabel('Fecha')
        plt.ylabel('Magnitude')
        plt.show()

    elif opcion == 4:
        GuardarFichero(informacion)

    elif opcion == 5:
        print('Saliendo del programa...')

    else:
        print("Has elegido no valido. Gracias")



if __name__ == "__main__":
    
    main()

    




