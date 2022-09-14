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

Librerias

pip install tk
pip install Pillow
pip install numpy
pip install pyautogui
pip install tkcap
pip install img2pdf
pip install pydicom
pip install opencv-python
pip install keras
pip install tensorflow==2.7.0

	
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

---

## DESCRIPCION DE LOS MODULOS

## Mi_App.py

Es el disparador de la aplicación  el cual invoca al frontend para que ilustre la interfaz grafica de 
usuario.

def main();


## Frontend.py

Controla el codigo requerido para el funcionamiento de la interfaz grafica de 
usuario haciendo uso de la libreria Tkinter.

Tamben contiene los diferentes metodos para el funcionamiento de la aplicación accedido por el usuario.


## BackendReadImg.py

Es un módulo encargado de manejar la logica para el cargue de los archivos.


## BackendPredict.py

Encargado de manejar la inferencia y a su vez realiza llamados a otros modulos necesarios para 
cumplir con dicha tarea.

Es invocado desde el frontend y por lo tanto provee conexión al modelo el cual se encuentra compilado
mediante el archivo 'WilhemNet86.h5'.

## ModelpreprocessImg.py

Modulo encargado del preprocesamiento de las imagenes.

## ModelgradCam.py

Se encarga de procesa sar la imagen usando la logica del modelo y obtiene la predicción y la capa 
convolucional con las características mas importantes de la imagen.

Grad-CAM realiza el cálculo del gradiente de la salida correspondiente a la clase a visualizar con respecto a las neuronas de una cierta capa de la CNN. 







