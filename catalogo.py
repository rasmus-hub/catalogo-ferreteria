catalogo = {'Tornillos': 2}

#catalogo['Tuercas'] = 3

usuario = 'gustavo02'
contrasena = 'inacap2024'

def verProductos():
    listado = 0
    for producto, cantidad in catalogo.items():
        listado += 1
        print(f'[{listado}] Producto: {producto} | Cantidad: {cantidad}')
    print(f'Hay un total de {listado} producto(s) ✅')

def crearProducto(nombre, cantidad):
    catalogo[nombre] = cantidad
    print(f'Producto "{nombre}" con el valor {cantidad} ingresado correctamente ✅')

def actualizarProducto(nombre, cantidad_i):
    for producto, cantidad in catalogo.items():
        if nombre == producto:
            catalogo[nombre] = cantidad_i
            print(f'Producto "{nombre}" con el valor {cantidad_i} actualizado correctamente ✅')

def eliminarProducto(nombre):
    for producto, cantidad in list(catalogo.items()):
        if nombre == producto:
            catalogo.pop(producto)
            print(f'Producto "{nombre}" con el valor {cantidad} eliminado correctamente ✅')

def gestionFerreteria():
    op = 0
    while op != 5:
        print('\n[ Ferreteria Los Alamos 📎 ]')
        print('[1] Ver Productos\n[2] Crear Producto\n[3] Actualizar Producto\n[4] Eliminar Producto\n[5] Cerrar Sesión')
        op = int(input('Ingrese una opción listada: '))

        print('-' * 50)
        match op:
            case 1:
                verProductos()
            case 2:
                nombre = input('Ingrese nombre del producto: ')
                cantidad = int(input('Ingrese la cantidad del producto: '))
                crearProducto(nombre, cantidad)
            case 3:
                nombre = input('Ingrese nombre del producto: ')
                cantidad_i = int(input('Ingrese la cantidad del producto: '))
                actualizarProducto(nombre, cantidad_i)
            case 4:
                nombre = input('Ingrese nombre del producto: ')
                eliminarProducto(nombre)
        print('-' * 50)


while True:
    print('\n[ Ferreteria Los Alamos 📎 ]')
    usuario_i = input('Ingrese usuario: ')
    contrasena_i = input('Ingrese contraseña: ')

    if usuario_i == usuario and contrasena_i == contrasena:
        print('DATOS CORRECTOS')
        print('BIENVENIDO AL SISTEMA ✅')

        gestionFerreteria()
    else:
        print('DATOS INCORRECTOS ❌\n')
    
    print('-' * 30)