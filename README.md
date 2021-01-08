# Autoattendance-Cognitive

## Librerias a utilizar
- NumPy .- NumPy is the fundamental package for array computing with Python.(numpy)
- Microsoft cognitive services .- Python SDK for the Cognitive Face API (cognitive-face)
- dlib .- A toolkit for making real world machine learning and data analysis applications(dlib)
- openpyxl .- A Python library to read/write Excel 2010 xlsx/xlsm files(openpyxl)
- OpenCv .- Wrapper package for OpenCV python bindings. (opencv-python)
- peewee .- ORM para la conexion con base de datos

      pip install openpyxl
      pip install numpy
      pip install cognitive-face
      pip install opencv-python
      pip install dlib
      pip install peewee


## Description
Propiedades de la base de datos en sqlite
    
    db identifier
    ID: identificador en base de datos
    Name: Person name, nombre de la persona
    Codigo: codigo de estudiante
    Person Guid: generated from cognitive faces(CF)
    personId: generated from cognitive faces(CF)




Archivo	Desc
--------------------------------------------------------------------------------
Face-DataBase	Base
Dataset	(Un conjunto de datos) contiene dir con caras de cada estudiante
add_student.py	hacer conjunto de datos y entrada en DB
create_person.py	generar personId desde el servidor de microsoft
add_person_faces.py	generar faceIds para cada cara en el conjunto de datos
train.py	entrena el modelo en el servidor de microsoft
get_status.py	mostrar el estado actual
spreadsheet.py	hace hoja xls llamado informes.xlsx
detect.py	detectar caras en la imagen de prueba y los cultivos y ponerlos en Cropped_faces directorio
identify.py	identificar cada rostro y marca la asistencia




Url reference article
With nodeJs
https://www.codemag.com/Article/1805031/Identify-Faces-with-Microsoft-Cognitive-Services
Example python, with request lib 
https://medium.com/@rachit.bedi1/microsoft-face-apis-using-python-e16775622e3b

#### Install env Steps
- Install python3, pip3 and add to path
- Install cmake and add to path
- Install c/c++ compiler (gcc/g++ in linux or visual c++ cmake tool windows for windows) for build "dlib"

- Optional, install virtualenv, create env and activate
- Install required packages
- Optional install pylint

- Create azure cf apikeys

Steps for use azure cognitive faces
- Create person group
- Create persons, add image face to persons
- Train person group
- Identify


Para  ejecutar scripts
- Crear db
- Registrar persona
- Identificar personas


---

Instalacion de programas necesarios


Python, interprete para ejecutar los scripts en Python
Visual c++, compilador de c++, necesarios para instalar compilar e instalar , DLIB
Cmake, sistema de compilacion, necesarios para instalar compilar e instalar , DLIB
agrear los 3 programas al path





Primero se crea en CF, para la api key en el portal de azure.


Crea un grupo de personas.
Agrear personas en el grupo, se crea una persona en CF , y se agrega caras a esa persona, por cada una de las personas que quieras reconocer 
Finalmente se hace el entrenamiendo.
---------------------------------------------------------------------

Reconocer