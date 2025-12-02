Tarea 4: Pruebas Automatizadas con Selenium
Este proyecto contiene la suite de pruebas automatizadas "End-to-End" (E2E) desarrollada para la asignatura de Calidad de Software. Las pruebas validan el funcionamiento de la aplicación web OrangeHRM utilizando Selenium WebDriver.

Nombre: Angel Morillo 
Matrícula: 2024-1780
Asignatura: Programación 3

Lenguaje: Python 3.14 
Framework de Pruebas: PytestHerramienta de Automatización: Selenium WebDriverNavegador: Microsoft EdgeReportes: Pytest-HTML

Escenarios de Prueba.
(Historias de Usuario) El script ejecuta 5 casos de prueba obligatorios: Login Exitoso: Verifica que un usuario válido pueda acceder al sistema.
Login Fallido (Prueba Negativa): Valida que el sistema bloquee el acceso y muestre error con credenciales incorrectas.
Crear Empleado (CRUD - Create): Simula el flujo de añadir un nuevo registro al sistema.
Buscar Empleado (CRUD - Read): Verifica que el buscador filtre correctamente los registros existentes.
Validación de Campos Vacíos (Prueba de Límites): Comprueba que el sistema maneje intentos de envío de formularios vacíos.

1. Instalación y Ejecución; PrerrequisitosTener instalado Python y Ms Edge.
2. Instalación de Dependencias; Ejecutar en la terminal:py -m pip install selenium pytest pytest-html webdriver-manager
3. Ejecución de las Pruebas; Para correr las pruebas y generar el reporte HTML, pues usamos el siguiente comando: py -m pytest test_tarea4.py --html=reporte.html --self-contained-html
