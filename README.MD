# Calculadora de liquidación definitiva.

El proyecto consiste en desarrollar una aplicación en Python
que permuita el cálculo de liquidaciones laborales. Permite determinar los diferentes conceptos que deben pagarse a un trabajador cuando se finaliza su relación laboral, como indemnización, vacaciones, cesantías, intereses sobre cesantías, prima de servicios y retención en la fuente. La aplicación recibe datos como el salario básico, las fechas de inicio y fin de labores, y los días acumulados de vacaciones, y realiza los cálculos correspondientes de acuerdo a las fórmulas y normativas vigentes. Además, permite configurar el valor de la Unidad de Valor Tributario (UVT) utilizado en el cálculo de la retención en la fuente. Este tipo de herramienta es fundamental en el ámbito de la gestión de recursos humanos y nómina, donde se requiere calcular de manera precisa los diferentes conceptos de la liquidación laboral cuando un empleado se retira de una organización.

## Integrantes del grupo:
- David Santiago Rodriguez Ruiz.
- Victor Manuel Monsalve Aguilar.

## Estructura del proyecto:
- src: En esta carpeta se encuentra la lógica y la interfaz de usuario.
- tests: En esta carpeta se encuentran las pruebas unitarias.

## ¿Cómo se usa?
Para hacer uso del aplicativo primero debe clonar el repositorio en su dispositivo local. Luego de clonarlo copie, pegue y ejecute el siguiente comando dentro de la consola de comandos: set PYTHONPATH=[ruta de la carpeta donde se clonó el repositorio].
Asegurese de tener instalada la librería Kivy en su sistema, para ello ejecute el siguiente comando en la raiz de la carpeta: 'pip install Kivy'.
- Si desea correr la interfaz de usuario, a través de la consola, debe ubicarse dentro de la carpeta 
haciendo uso del siguiente comando: cd [ruta del archivo]. Posteriormente ubicarse en la ruta src/view 
y ejecutar la interfaz gráfica con el comando 'python consola.py:'.
- Si desea correr la interfaz del controlador, a través de la consola dentro de la carpeta haciendo uso del siguinete comando: cd [ruta del archivo]. Posteriormente ubicarse en la ruta src/view y ejecutar la interfaz de controlador con el comando 'python consolacontrolador.py'.
- Si desea ejecutar las pruebas unitarias del siga el mismo procedimiento anterior y ubicarse en la carpeta test.
Una vez en la carpeta test ejecutar el comando 'python controllertest.py'.
- Si desea ejecutar las pruebas unitarias de la base de datos siga el mismo procedimiento anterior y ubicarse en la carpeta test.
Una vez en la carpeta test ejecutar el comando 'python testbasedatos.py'.