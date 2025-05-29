# Clase base para herencia simple
class Persona:
    def __init__(self, documento, nombre, edad):
        self.documento = documento
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} (Doc: {self.documento})"

# Clase para herencia múltiple
class Registrable:
    def registrar(self):
        return f"{self.nombre} registrado correctamente."

# Clase que representa a una persona que recibe ayuda del comedor
class Beneficiario(Persona, Registrable):
    def __init__(self, documento, nombre, edad, poblacion):
        # Datos básicos del beneficiario
        super().__init__(documento, nombre, edad)
        self.nombre = nombre        # Nombre completo
        self.edad = edad            # Edad en años
        self.poblacion = poblacion  # Tipo: niño, adulto mayor, etc.
        self.asistencias = []       # Aquí se guardan las fechas que asistió

    # Muestra el nombre y documento cuando se imprime el objeto
    def __str__(self):
        return f"{self.nombre} (Doc: {self.documento})"


# Clase que representa un comedor comunitario
class Comedor:
    def __init__(self, nombre, direccion, localidad, cupo_diario):
        # Información del comedor
        self.nombre = nombre          # Ej: "Comedor Perdomo"
        self.direccion = direccion    # Dirección física
        self.localidad = localidad   # Barrio o sector
        self.cupo_diario = cupo_diario  # Máximo de personas por día
        # Lista de beneficiarios que pueden comer aquí
        self.beneficiarios_asignados = []  

    # Muestra nombre, dirección y cupo al imprimir
    def __str__(self):
        return f"{self.nombre} - {self.direccion} (Cupo: {self.cupo_diario})"


# Clase principal que maneja todo el sistema
class SistemaComedoresModelo:
    def __init__(self):
        self.beneficiarios = []  # Aquí se guardan TODOS los beneficiarios
        
        # Lista de comedores disponibles (se crean automáticamente al iniciar)
        self.comedores = [
            Comedor("Perdomo", "AV VILLAVICENCIO No. 60B-05 SUR", "Ciudad Bolívar", 10),
            Comedor("Los Luceros", "Plaza de Mercado de Los Luceros", "Ciudad Bolívar", 10),
            Comedor("Jerusalen Canteras", "CARRERA 47D # 68G-08SUR", "Ciudad Bolívar", 10),
            Comedor("Estrella del sur", "CLL 74 No. 18 BIS-18", "Ciudad Bolívar", 10),
            Comedor("Santa Viviana", "CALLE 75D SUR No. 75C-03 SUR", "Ciudad Bolívar", 10),
            Comedor("Arborizadora", "CRA 40 No. 63I-25 SUR", "Ciudad Bolívar", 10),
        ]

    # Agrega un nuevo beneficiario y lo asigna a un comedor
    def agregar_beneficiario(self, documento, nombre, edad, poblacion, indice_comedor):
        # Verifica que los datos obligatorios no estén vacíos
        if not documento or not nombre or not poblacion:
            return False  # Indica que falló

        # Busca si ya existe alguien con ese documento
        if not self.buscar_beneficiario(documento):
            nuevo = Beneficiario(documento, nombre, edad, poblacion)
            # Intenta asignarlo al comedor seleccionado
            if self.asignar_beneficiario(nuevo, indice_comedor):
                self.beneficiarios.append(nuevo)  # Lo agrega al sistema
                return True  # Éxito!
        return False  # Si falla en algún paso

    # Busca un beneficiario por su número de documento
    def buscar_beneficiario(self, documento):
        return next((ben for ben in self.beneficiarios if ben.documento == documento), None)

    # Asigna un beneficiario a un comedor específico
    def asignar_beneficiario(self, beneficiario, indice_comedor):
        # Verifica que el índice del comedor sea válido
        if 0 <= indice_comedor < len(self.comedores):
            comedor = self.comedores[indice_comedor]
            # Revisa si el comedor tiene cupo disponible
            if len(comedor.beneficiarios_asignados) < comedor.cupo_diario:
                comedor.beneficiarios_asignados.append(beneficiario)
                return True  # Asignación exitosa
        return False  # No se pudo asignar

    # Obtiene la lista de beneficiarios de un comedor
    def generar_listado_diario(self, indice_comedor, fecha):
        if 0 <= indice_comedor < len(self.comedores):
            return self.comedores[indice_comedor].beneficiarios_asignados
        return []  # Si el índice es inválido, devuelve lista vacía

    # Registra la asistencia de un beneficiario en una fecha
    def registrar_asistencia(self, indice_comedor, fecha, documento):
        beneficiario = self.buscar_beneficiario(documento)
        # Verifica que exista y esté asignado a ese comedor
        if beneficiario and any(ben.documento == documento for ben in self.comedores[indice_comedor].beneficiarios_asignados):
            beneficiario.asistencias.append(fecha)  # Agrega la fecha de asistencia
            return True  # Registro exitoso
        return False  # No se pudo registrar