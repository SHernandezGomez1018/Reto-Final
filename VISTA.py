class VistaComedores:
    # Esta clase maneja TODO lo que el usuario ve en pantalla
    
    def mostrar_menu_principal(self):
        # Muestra el menú principal con las opciones
        print("\n=== SISTEMA DE COMEDORES COMUNITARIOS ===")
        print("[1] Registrar beneficiario")
        print("[2] Registrar asistencia") 
        print("[3] Generar listado diario")
        print("[4] Salir")

    def obtener_opcion(self):
        # Pide al usuario que seleccione una opción y valida que sea correcta
        while True:
            opcion = input("\nSeleccione una opción (1-4): ")
            if opcion in ["1", "2", "3", "4"]:  # Solo acepta estas opciones
                return opcion
            print("Opción inválida. Intente nuevamente.")

    def mostrar_mensaje(self, mensaje, es_error=False):
        # Muestra mensajes en pantalla (normales o de error)
        print(f"\n[{'ERROR' if es_error else 'INFO'}] {mensaje}")

    def pausar(self):
        # Hace una pausa esperando que el usuario presione Enter
        input("\nPresione Enter para continuar...")

    def mostrar_beneficiarios(self, beneficiarios):
        # Muestra la lista de personas registradas
        if not beneficiarios:
            print("\nNo hay beneficiarios registrados")
            return
            
        print("\nLISTA DE BENEFICIARIOS:")
        for i, ben in enumerate(beneficiarios, 1):  # enumera desde 1
            print(f"{i}. {ben.nombre} - Doc: {ben.documento} - {ben.poblacion}")

    def mostrar_comedores(self, comedores):
        # Muestra la lista de comedores con su información
        print("\nCOMEDORES DISPONIBLES:")
        for i, comedor in enumerate(comedores, 1):
            print(f"{i}. {comedor.nombre} - {comedor.direccion} (Cupo: {comedor.cupo_diario}, Asignados: {len(comedor.beneficiarios_asignados)})")

    def mostrar_listado_completo(self, comedores_con_listados, fecha):
        """Muestra todos los comedores con sus beneficiarios en una sola vista"""
        print(f"\n=== LISTADO GENERAL DE COMEDORES - {fecha} ===")
        
        for comedor, listado in comedores_con_listados:
            print(f"\n● {comedor.nombre} ({len(listado)} beneficiarios):")
            if not listado:
                print("  No hay beneficiarios asignados")
            else:
                for i, ben in enumerate(listado, 1):
                    print(f"  {i}. {ben.nombre} - Asistencias: {len(ben.asistencias)}")
        
        print("\n" + "="*50)  # Línea separadora
        print(f"Total comedores: {len(comedores_con_listados)}")

    def solicitar_datos_beneficiario(self):
        # Pide los datos para registrar una nueva persona
        print("\nREGISTRO DE NUEVO BENEFICIARIO")
        
        # Validación del documento (debe tener al menos 6 dígitos)
        documento = input("Documento de identidad: ").strip()
        if not documento.isdigit() or len(documento) < 6:
            self.mostrar_mensaje("Documento inválido", True)
            return None
            
        # Validación del nombre (al menos 3 letras)
        nombre = input("Nombre completo: ").strip()
        if len(nombre) < 3:
            self.mostrar_mensaje("Nombre inválido", True)
            return None
            
        # Validación de la edad (entre 1 y 120 años)
        try:
            edad = int(input("Edad: "))
            if edad <= 0 or edad > 120:
                self.mostrar_mensaje("Edad inválida", True)
                return None
        except ValueError:
            self.mostrar_mensaje("Edad inválida", True)
            return None
            
        # Menú para seleccionar tipo de población
        print("\nTipo de población:")
        print("1. Niño")
        print("2. Adulto mayor") 
        print("3. Persona con discapacidad")
        
        poblacion = {"1": "Niño", "2": "Adulto mayor", "3": "Persona con discapacidad"}.get(input("Seleccione (1-3): "))
        if not poblacion:
            self.mostrar_mensaje("Opción inválida", True)
            return None
            
        # Si todo está correcto, devuelve los datos
        return documento, nombre, edad, poblacion