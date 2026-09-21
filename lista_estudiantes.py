def gestionar_sistema_academico():
    # 1. Lista: Almacena los nombres de los estudiantes en orden de llegada
    lista_estudiantes = ["Edwin", "Oscar", "Sebastian", "Oscar"]
    
    # 2. Conjunto (Set): Almacena cédulas únicas para evitar duplicados
    cedulas_unicas = {"0901234567", "0907654321", "0901234567"} # El duplicado se elimina solo
    
    # 3. Diccionario (Map): Relaciona el nombre del estudiante con su nota (clave-valor)
    notas_estudiantes = {
        "Edwin": 10,
        "Oscar": 9.5,
        "Sebastian": 6.5
    }

    print("=== SISTEMA DE GESTIÓN ACADÉMICA ===")

    # Operación: Recorrer y mostrar la lista de estudiantes
    print("\n--- Lista de Estudiantes (Permite orden y duplicados) ---")
    for estudiante in lista_estudiantes:
        print(f"- {estudiante}")

    # Operación: Recorrer el conjunto de cédulas únicas
    print("\n--- Cédulas Únicas Registradas (Conjunto) ---")
    for cedula in cedulas_unicas:
        print(f"Cédula: {cedula}")

    # Operación: Insertar un nuevo dato en el diccionario
    print("\n[Operación] Agregando nueva nota al diccionario...")
    notas_estudiantes["Carlos"] = 9.5
    print("¡Estudiante 'Carlos' agregada con éxito!")

    # Operación: Buscar / consultar un elemento en el diccionario
    print("\n[Operación] Consultando nota de un estudiante...")
    estudiante_buscado = "Sebastian"
    if estudiante_buscado in notas_estudiantes:
        print(f"La nota de {estudiante_buscado} es: {notas_estudiantes[estudiante_buscado]}")

    # Operación: Recorrer el diccionario completo (Clave y Valor)
    print("\n--- Registro Final de Notas (Diccionario) ---")
    for nombre, nota in notas_estudiantes.items():
        print(f"Estudiante: {nombre} | Nota: {nota}")

    # Operación: Eliminar un elemento del diccionario
    print("\n[Operación] Eliminando al estudiante 'Carlos' del registro...")
    del notas_estudiantes["Carlos"]
    print("Registro actualizado de notas:", notas_estudiantes)

if __name__ == "__main__":
    gestionar_sistema_academico()