def saludo(nombre):
    return "Hola " + nombre# Funcion nueva en progreso
def exportar_csv(productos):
    print('Exportando a CSV...')
    for p in productos:
        print(f'{p["nombre"]},{p["cantidad"]},{p["precio"]}')
