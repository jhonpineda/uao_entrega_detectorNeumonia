Herramienta de detección de Neumonía

Integrantes:

Nombre: Jhon Harold Pineda Dorado
Cédula: 97435193
Código: 2220156

Nombre: Harold Muñoz
Cédula: 97397310
Código: 2221845


Definición: Herramienta para la detección rápida de neumonía con base en imagenes radiológicas.

Requerimientos para el funcionamiento:

	
git clone:

https://github.com/jhonpineda/uao_entrega_detectorNeumonia

Descargar modelo desde la siguiente ruta:

wget: http://208.76.80.10/WilhemNet_86.h5

Instalar aplicacion desde Dockerfile.

----------------------------------------------------------------------------------

Uso de la herramienta:

- Ingrese la cédula del paciente
- Presione el botón 'Cargar Imagen', y realice atachment.
- Presione el botón 'Predecir'
- Presione el botón 'Guardar' para almacenar en archivo .csv
- Presione el botón 'PDF' para descargar reporte
- Presión el botón 'Limpiar' para cargar nueva imagen
