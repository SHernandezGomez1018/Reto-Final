# Proyecto: Sistema de Gestión de Comedores Comunitarios

## _Casos de Uso para el Sistema de Comedores Comunitarios_

### **1. Registrar un nuevo beneficiario**
Actor: Administrador del sistema
Descripción: Registra un nuevo beneficiario y lo asigna a un comedor comunitario disponible.
**Precondiciones:**
•	El comedor debe tener cupo disponible.
•	El documento del beneficiario no debe estar registrado previamente.

**Flujo principal:**
1.	El sistema muestra el menú principal (VistaComedores.mostrar_menu_principal).
2.	El administrador selecciona la opción 1.
3.	El sistema solicita documento, nombre, edad y tipo de población (VistaComedores.solicitar_datos_beneficiario).
4.	El administrador ingresa los datos requeridos.
5.	El sistema muestra los comedores disponibles (VistaComedores.mostrar_comedores).
6.	El administrador selecciona un comedor.
7.	El sistema valida los datos y verifica el cupo.
8.	El sistema registra al beneficiario (SistemaComedoresModelo.agregar_beneficiario).
9.	Se muestra mensaje de confirmación.

**Flujos alternativos:**
•	Datos inválidos → Mensaje de error y vuelta al menú.
•	No hay cupo disponible → Mensaje de error y vuelta al menú.
•	Documento ya registrado → Mensaje de error y vuelta al menú.

### **2. Generar listado diario de beneficiarios**
Actor: Administrador del sistema
Descripción: Muestra el listado diario de beneficiarios por comedor.
Precondiciones:
•	Debe ingresarse una fecha válida.
**Flujo principal:**
1.	El sistema muestra el menú principal.
2.	El administrador selecciona la opción 3.
3.	El sistema solicita una fecha.
4.	El sistema valida la fecha (datetime.strptime).
5.	El sistema genera el listado por comedor (SistemaComedoresModelo.generar_listado_diario).
6.	El sistema muestra el listado completo (VistaComedores.mostrar_listado_completo).

**Flujos alternativos:**
•	Fecha inválida → Mensaje de error.

### **3. Registrar asistencia de un beneficiario**
Actor: Administrador del sistema
Descripción: Registra la asistencia de un beneficiario en un comedor en una fecha específica.
**Precondiciones:**
•	El beneficiario debe estar registrado en el comedor.

**Flujo principal:**
1.	El sistema muestra el menú principal.
2.	El administrador selecciona la opción 2.
3.	El sistema muestra comedores disponibles.
4.	El administrador selecciona un comedor.
5.	El sistema solicita fecha y documento.
6.	El administrador ingresa los datos.
7.	El sistema valida y registra la asistencia (SistemaComedoresModelo.registrar_asistencia).
8.	El sistema muestra mensaje de confirmación.
   
**Flujos alternativos:**
• Beneficiario no asignado → Mensaje de error.
• Datos inválidos → Mensaje de error.

### **4. Consultar comedores disponibles**
Actor: Administrador del sistema
Descripción: Muestra la lista de comedores con su información básica.

**Flujo principal:**
1.	El sistema muestra el menú principal.
2.	El administrador elige una opción que muestre comedores.
3.	El sistema muestra nombre, dirección, cupo y beneficiarios asignados (VistaComedores.mostrar_comedores).
4. Salir del sistema
Actor: Administrador del sistema
Descripción: Finaliza el programa de forma segura.

**Flujo principal:**
1.	El sistema muestra el menú principal.
2.	El administrador selecciona "Salir".
3.	El sistema muestra un mensaje de despedida y cierra el programa.

### **Mapa de Navegación del Sistema**

![image](https://github.com/user-attachments/assets/32d41a4a-1a03-4b0a-ab3b-23d07541bf14)

 
### **Estructura General del Proyecto:**
-  **MAIN.py:** Punto de entrada. Ejecuta el controlador con modelo y vista.
-  **CONTROLADOR.py:** Coordina las acciones entre vista y modelo.
-  **MODELO.py:** Define la lógica y estructura de datos (beneficiarios y comedores).
-  **VISTA.py:** Interfaz de usuario en consola (entrada/salida).
-  
### **Descripción de las Clases:**
**1. Beneficiario (MODELO.py)**
-    Atributos: documento, nombre, edad, poblacion, asistencias
-    Metodos: __init__, __str__, registrar
-    
**2. Comedor (MODELO.py)**
-    Atributos: nombre, direccion, localidad, cupo_diario, beneficiarios_asignados
-    Métodos: __init__, __str__
-    
**3. SistemaComedoresModelo (MODELO.py)**
-    Atributos: beneficiarios, comedores
-    Métodos: agregar_beneficiario, buscar_beneficiario, asignar_beneficiario, generar_listado_diario, registrar_asistencia
-    
**4. VistaComedores (VISTA.py)**
-    Métodos: mostrar_menu_principal, obtener_opcion, mostrar_mensaje, pausar, mostrar_comedores, mostrar_listado_completo, solicitar_datos_beneficiario
-    
**5. ControladorComedores (CONTROLADOR.py)**
-    Métodos: ejecutar, registrar_beneficiario, generar_listado, registrar_asistencia

## **Justificación del Proyecto**
**Contexto:**
En Ciudad Bolívar, la gestión manual de comedores comunitarios causa ineficiencia, errores y dificultades para planear y rendir cuentas.
**Objetivo:**
Automatizar el sistema con Python para mejorar:
-    Registro de beneficiarios
-    Control de cupos
-    Reportes de asistencia
**Justificación Técnica:**
-    Python es versátil, gratuito y escalable.
-    Permite migrar a interfaces gráficas o web en el futuro.
**Impacto Esperado:**
-    Mayor eficiencia en registro y atención.
-    Transparencia en la asignación de recursos.
-    Mejor planeación con datos precisos.
**Conclusión:**
Este sistema contribuye directamente al bienestar social, modernizando la gestión de alimentos para familias en situación de vulnerabilidad.
