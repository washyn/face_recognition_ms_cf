# Autoattendance-Cognitive

## Libs
- NumPy .- NumPy is the fundamental package for array computing with Python.(numpy)
- Microsoft cognitive services .- Python SDK for the Cognitive Face API (cognitive-face)
- dlib .- A toolkit for making real world machine learning and data analysis applications(dlib)
- openpyxl .- A Python library to read/write Excel 2010 xlsx/xlsm files(openpyxl)
- OpenCv .- Wrapper package for OpenCV python bindings. (opencv-python)



## Description

- Face-Database, database of students with fields, Id, FullName, Roll, PersonId
- dataset, folder with images of all students, aditionally include face expresions
- add_student, este script pide al usuario ingresar datos como nombre, id  para guardarlo en DB,
 para luego crear una carpeta para ese usaurio y almancenar ahi sus expresiones

db identifier
ID:
Person name
Name:
Enrollment id
Roll:
Person id generated from cognitive faces(CF)
personId:

- create_person .- al parecer tomas los args de la carpeta de fotos y el user id y genera un guid
que se almacena en base de datos, generar personId desde el servidor de microsoft
- add_person_faces A cada personId se le agrega las caras de la carpeta donde estan sus fotos, generar faceIds para cada cara en el conjunto de datos, el equivalente a entrenar em microsoft CF
- create_person_group .- Crea un grupo de personas. Al parecer es un scrip innecesario.
- get_status .- mostrar el estado actual ???????
- train.py	entrena el modelo en el servidor de microsoft



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



# TODOS:
- ver el video
- Crear la api key
- investigar un poco como funciona
- probar
- modificar

# Para iniciar completo
- Ver el orden de ejecucion para un entorno real, cuando se tiene todo listo

# Para iniciar agregando estudiante
- Ver el orden cuando se quiere agregar un estudiante



## add_student2.py
al ejecutar script se le pide al usuario que ingrese el nombre de una persona, el cual sera gurdado en la base de datos sqlite, y se activara la camara y se gurdaran sus expresiones, imagenes en una carpeta con un nombre generado de forma aleatoria para el entrenamiento.

## TODO:
Terminar de revisar los scripts de :
spreadsheet.py
identity.py