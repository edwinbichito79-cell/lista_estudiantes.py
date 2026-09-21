def gestionar_tienda():
    # 1. Diccionario: Relaciona el nombre del producto con su precio
    inventario = {
        "Manzana": 0.50,
        "Leche": 1.20,
        "Pan": 0.30,
        "Arroz": 1.50,
        "Maíz": 1.20
    }
    
    # 2. Conjunto (Set): Almacena categorías únicas sin repetir
    categorias = {"Frutas", "Lácteos", "Panadería", "Granos"}
    
    # 3. Lista: Almacena el historial de productos vendidos en orden de venta
    ventas_del_dia = []

    print("=== SISTEMA DE GESTIÓN DE TIENDA ===")
    
    # Mostrar inventario inicial (Diccionario)
    print("\n--- Inventario Inicial ---")
    for producto, precio in inventario.items():
        print(f"- {producto}: ${precio:.2f}")

    # Mostrar categorías (Conjunto)
    print("\n--- Categorías Disponibles ---")
    for categoria in categorias:
        print(f"- {categoria}")

    # Operación de Inserción / Agregar nuevos datos
    print("\n[Operación] Agregando nuevo producto y categoría...")
    inventario["Café"] = 2.50
    categorias.add("Bebidas")
    print("¡Producto 'Café' y categoría 'Bebidas' agregados con éxito!")

    # Operación básica adicional: Buscar un elemento en el diccionario
    print("\n[Operación] Buscando un producto en el inventario...")
    producto_a_buscar = "Leche"
    if producto_a_buscar in inventario:
        print(f"Sí tenemos '{producto_a_buscar}' y cuesta ${inventario[producto_a_buscar]:.2f}")
    else:
        print(f"El producto '{producto_a_buscar}' no está disponible.")

    # Operación básica adicional: Registrar ventas (Insertar en Lista) y recorrer
    print("\n[Operación] Registrando ventas del día...")
    ventas_del_dia.append("Manzana")
    ventas_del_dia.append("Pan")
    ventas_del_dia.append("Leche")
    ventas_del_dia.append("Maíz")

    print("\n--- Historial de Ventas (Lista) ---")
    for i, venta in enumerate(ventas_del_dia, start=1):
        print(f"Venta {i}: {venta}")

    # Operación básica adicional: Eliminar un elemento de la lista
    print("\n[Operación] Eliminando el último registro del historial de ventas...")
    producto_eliminado = ventas_del_dia.pop()
    print(f"Se ha removido '{producto_eliminado}' de las ventas recientes.")

    print("\n--- Estado Final del Historial de Ventas ---")
    print(ventas_del_dia)

if __name__ == "__main__":
    gestionar_tienda()