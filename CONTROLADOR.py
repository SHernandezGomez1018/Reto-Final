from datetime import datetime  # Para trabajar con fechas

class ControladorComedores:
    def __init__(self, modelo, vista):
        # Conexión con el modelo (datos) y la vista (interfaz)
        self.modelo = modelo  # Accede a toda la lógica del sistema
        self.vista = vista    # Maneja lo que se muestra al usuario

    def ejecutar(self):
        # Bucle principal que mantiene el programa funcionando
        while True:
            try:
                self.vista.mostrar_menu_principal()  # Muestra el menú
                opcion = self.vista.obtener_opcion() # Lee la opción del usuario

                # Decide qué hacer según la opción seleccionada
                if opcion == "1":
                    self.registrar_beneficiario()    # Opción 1: Registrar persona
                elif opcion == "2":
                    self.generar_listado()           # Opción 2: Ver listado
                elif opcion == "3":
                    self.registrar_asistencia()      # Opción 3: Marcar asistencia
                elif opcion == "4":
                    self.vista.mostrar_mensaje("Saliendo del sistema...")
                    break  # Opción 4: Salir del programa

                self.vista.pausar()  # Pequeña pausa después de cada acción
            except Exception as e:
                # Si algo falla, muestra el error
                self.vista.mostrar_mensaje(f"Error: {str(e)}", True)
                self.vista.pausar()

    def registrar_beneficiario(self):
        # Pide los datos de la persona a registrar
        datos = self.vista.solicitar_datos_beneficiario()
        if datos is None:  # Si no se dieron datos, cancela
            return

        # Muestra la lista de comedores disponibles
        self.vista.mostrar_comedores(self.modelo.comedores)
        try:
            # Pide seleccionar un comedor (resta 1 porque las listas empiezan en 0)
            indice = int(input("\nSeleccione comedor para el beneficiario: ")) - 1
            
            # Intenta agregar al beneficiario (*datos expande la lista de argumentos)
            if self.modelo.agregar_beneficiario(*datos, indice):
                self.vista.mostrar_mensaje("Beneficiario registrado y asignado correctamente")
            else:
                self.vista.mostrar_mensaje("No se pudo registrar (datos repetidos o cupo lleno)", True)
        except (ValueError, IndexError):
            self.vista.mostrar_mensaje("Selección inválida", True)

    def generar_listado(self):
        # Muestra los comedores disponibles
        self.vista.mostrar_comedores(self.modelo.comedores)

        try:
            # Pide seleccionar comedor y fecha
            indice = int(input("\nNúmero de comedor: ")) - 1
            fecha = input("Fecha (DD-MM-AAAA): ")
            datetime.strptime(fecha, "%d-%m-%Y")  # Valida el formato de fecha
            
            # Obtiene el listado del modelo
            listado = self.modelo.generar_listado_diario(indice, fecha)
            nombre_comedor = self.modelo.comedores[indice].nombre
            
            # Muestra el listado usando la vista
            self.vista.mostrar_listado(listado, nombre_comedor, fecha)
        except (ValueError, IndexError):
            self.vista.mostrar_mensaje("Entrada inválida", True)

    def registrar_asistencia(self):
        # Muestra los comedores disponibles
        self.vista.mostrar_comedores(self.modelo.comedores)

        try:
            # Pide datos: comedor, fecha y documento de la persona
            indice = int(input("\nNúmero de comedor: ")) - 1
            fecha = input("Fecha (DD-MM-AAAA): ")
            documento = input("Documento del beneficiario: ")

            # Intenta registrar la asistencia
            if self.modelo.registrar_asistencia(indice, fecha, documento):
                self.vista.mostrar_mensaje("Asistencia registrada")
            else:
                self.vista.mostrar_mensaje("No se pudo registrar (verifique datos)", True)
        except (ValueError, IndexError):
            self.vista.mostrar_mensaje("Datos inválidos", True)