# Importamos las clases necesarias de otros archivos
from MODELO import SistemaComedoresModelo    # Donde están los datos
from VISTA import VistaComedores            # Lo que ve el usuario
from CONTROLADOR import ControladorComedores # El "cerebro" del programa

def main():
    # 1. Creamos el modelo (la base de datos del sistema)
    modelo = SistemaComedoresModelo()
    
    # 2. Creamos la vista (la interfaz que verá el usuario)
    vista = VistaComedores()
    
    # 3. Creamos el controlador y le pasamos modelo y vista
    controlador = ControladorComedores(modelo, vista)
    
    # 4. Iniciamos el programa ejecutando el controlador
    controlador.ejecutar()

# Esto asegura que el programa solo se ejecute cuando se abre directamente este archivo
if __name__ == "__main__":
    main()
