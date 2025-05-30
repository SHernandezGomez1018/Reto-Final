class VistaComedores:
    # Esta clase maneja TODO lo que el usuario ve en pantalla

    def mostrar_menu_principal(self):
        print("\n=== SISTEMA DE COMEDORES COMUNITARIOS ===")
        print("""¡Bienvenid@ al sistema de gestión de comedores comunitarios! 
A continuación sigue las instrucciones para poder registrarte en el comedor de tu preferencia.""")
        print("\nSelecciona una opción:")
        print("[1] Registrar beneficiario")
        print("[2] Registrar asistencia") 
        print("[3] Generar listado diario")
        print("[4] Salir")

    def obtener_opcion(self):
        while True:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            if opcion in ["1", "2", "3", "4"]:
                return opcion
            print("Opción inválida. Intente nuevamente.")

    def mostrar_mensaje(self, mensaje, es_error=False):
        print(f"\n[{'ERROR' if es_error else 'INFO'}] {mensaje}")

    def pausar(self):
        input("\nPresione Enter para continuar...")

    def mostrar_beneficiarios(self, beneficiarios):
        if not beneficiarios:
            print("\nNo hay beneficiarios registrados")
            return
            
        print("\nLISTA DE BENEFICIARIOS:")
        for i, ben in enumerate(beneficiarios, 1):
            print(f"{i}. {ben.nombre} - Doc: {ben.documento} - {ben.poblacion}")

    def mostrar_comedores(self, comedores):
        print("\nCOMEDORES DISPONIBLES:")
        for i, comedor in enumerate(comedores, 1):
            print(f"{i}. {comedor.nombre} - {comedor.direccion} (Cupo: {comedor.cupo_diario}, Asignados: {len(comedor.beneficiarios_asignados)})")

    def mostrar_listado_completo(self, comedores_con_listados, fecha):
        print(f"\n=== LISTADO GENERAL DE COMEDORES - {fecha} ===")
        
        for comedor, listado in comedores_con_listados:
            print(f"\n● {comedor.nombre} ({len(listado)} beneficiarios):")
            if not listado:
                print("  No hay beneficiarios asignados")
            else:
                for i, ben in enumerate(listado, 1):
                    print(f"  {i}. {ben.nombre} - Asistencias: {len(ben.asistencias)}")
        
        print("\n" + "="*50)
        print(f"Total comedores: {len(comedores_con_listados)}")

    def solicitar_datos_beneficiario(self):
        print("\nREGISTRO DE NUEVO BENEFICIARIO")

        # Solicitar documento
        while True:
            documento = input("Documento de identidad: ").strip()
            if documento.isdigit() and len(documento) >= 6:
                break
            self.mostrar_mensaje("Documento inválido. Debe contener solo números y al menos 6 dígitos.", True)
            if input("¿Desea intentarlo de nuevo? (s/n): ").strip().lower() != 's':
                return None

        # Solicitar nombre
        while True:
            nombre = input("Nombre completo: ").strip()
            if len(nombre) >= 3:
                break
            self.mostrar_mensaje("Nombre inválido. Debe tener al menos 3 caracteres.", True)
            if input("¿Desea intentarlo de nuevo? (s/n): ").strip().lower() != 's':
                return None

        # Solicitar edad
        while True:
            try:
                edad = int(input("Edad: "))
                if 1 <= edad <= 120:
                    break
                else:
                    self.mostrar_mensaje("Edad inválida. Debe estar entre 1 y 120 años.", True)
            except ValueError:
                self.mostrar_mensaje("Edad inválida. Debe ser un número entero.", True)
            if input("¿Desea intentarlo de nuevo? (s/n): ").strip().lower() != 's':
                return None

        # Seleccionar tipo de población
        while True:
            print("\nTipo de población:")
            print("1. Niño")
            print("2. Adulto")
            print("3. Adulto mayor")
            print("4. Persona con discapacidad")
            opcion = input("Seleccione (1-4): ").strip()
            poblacion = {
                "1": "Niño",
                "2": "Adulto",
                "3": "Adulto Mayor",
                "4": "Persona con discapacidad"
            }.get(opcion)

            if poblacion:
                break
            self.mostrar_mensaje("Opción inválida. Debe seleccionar un número entre 1 y 4.", True)
            if input("¿Desea intentarlo de nuevo? (s/n): ").strip().lower() != 's':
                return None

        return documento, nombre, edad, poblacion
