# ACTIVIDAD 1: Crear archivo con productos iniciales y mostrarlos

productos = [
    ("manzana", 1500, 20),
    ("banana", 1200, 30),
    ("naranja", 1000, 25),
]

# Guardar productos en archivos
with open("productos.txt", "w") as archivo:
    for nombre, precio, cantidad in productos:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

# Leer y mostrar productos
with open("productos.txt", "r") as archivo:
    print("\n--- ACTIVIDAD 1: Productos del archivo ---")
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}")

# ACTIVIDAD 2: Agregar productos desde teclado

# Abrir en modo append para no sobrescribir
with open("productos.txt", "a") as archivo:
    while True:
        nombre = input("\nIngrese el nombre del producto que desea agregar (o escriba 'salir' para terminar): ")
        if nombre.lower() == "salir":
            break
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        archivo.write(f"{nombre},{precio},{cantidad}\n")

# Leer y mostrar productos actualizados
with open("productos.txt", "r") as archivo:
    print("\n--- ACTIVIDAD 2: Productos actualizados ---")
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}")

# ACTIVIDAD 3: Cargar productos en lista de diccionarios

productos_dict = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            if len(datos) == 3:
                try:
                    producto = {
                        "nombre": datos[0].strip(),
                        "precio": int(datos[1].strip()),
                        "cantidad": int(datos[2].strip())
                    }
                    productos_dict.append(producto)
                except ValueError:
                    print(f"Línea inválida ignorada: {linea}")

print("\n--- ACTIVIDAD 3: Lista de diccionarios ---")
print(productos_dict)

# ACTIVIDAD 4: Validación avanzada al cargar productos

productos_validos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for num_linea, linea in enumerate(archivo, start=1):
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(",")
        if len(partes) != 3:
            print(f"Línea {num_linea} con formato incorrecto: {linea}")
            continue
        nombre = partes[0].strip()
        precio_str = partes[1].strip()
        cantidad_str = partes[2].strip()
        try:
            precio = float(precio_str)
            cantidad = int(cantidad_str)
        except ValueError:
            print(f"Error al convertir datos numéricos en línea {num_linea}: {linea}")
            continue
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos_validos.append(producto)

print("\n--- ACTIVIDAD 4: Productos cargados con validación ---")
for p in productos_validos:
    print(p)


# ACTIVIDAD 5: Buscar un producto por nombre

buscar_producto = input("\nIngrese el nombre del producto a buscar: ").strip().lower()
encontrado = False

for producto in productos_validos:
    if producto["nombre"].lower() == buscar_producto:
        print("\n--- ACTIVIDAD 5: Producto encontrado ---")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nEl producto no existe en la lista.")


# ACTIVIDAD 6: Manejo de errores y limpieza al cargar productos

productos_final = []

try:
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        for num_linea, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) != 3:
                print(f"Línea {num_linea} con formato incorrecto: {linea}")
                continue
            nombre = partes[0].strip()
            precio_str = partes[1].strip().replace("$", "").replace(" ", "").replace(",", ".")
            cantidad_str = partes[2].strip()
            try:
                precio = float(precio_str)
                cantidad = int(cantidad_str)
            except ValueError:
                print(f"Error en conversión numérica (línea {num_linea}): {linea}")
                continue
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos_final.append(producto)
except FileNotFoundError:
    print("No se encontró el archivo productos.txt.")

print("\n--- ACTIVIDAD 6: Productos finales cargados correctamente ---")
for p in productos_final:
    print(p)