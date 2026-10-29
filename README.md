# Taller: Creación de endpoints en Django nativo

**Docente:** Jose Javier Torres Vanstrahlen  
**Curso:** Desarrollo de Aplicaciones Web I – 4E  
**Estudiante:** Maria Hormiga

## 1. ¿Cuál es el objetivo del taller?

Investigar y desarrollar endpoints utilizando Django nativo, sin librerías externas para la creación de los endpoints. Se implementa una vista basada en clase que maneja los métodos HTTP `GET`, `POST`, `PUT` y `DELETE`, relacionándolos con las operaciones CRUD.

## 2. ¿Qué es un endpoint?

Un endpoint es una ruta de una aplicación que permite al cliente comunicarse con el servidor para consultar o modificar información. En Django, las rutas se definen en `urls.py` y se conectan con las vistas que procesan las solicitudes.

En este proyecto se trabaja con dos rutas:

- `/proyectos/`: permite consultar los proyectos y crear uno nuevo.
- `/proyectos/<id>/`: permite consultar, actualizar o eliminar un proyecto específico.

Esta organización sigue la idea explicada en las fuentes consultadas: una URL se conecta con una vista que se encarga de procesar la solicitud.

## 3. ¿Qué es una vista basada en clase?

Una vista basada en clase permite organizar la lógica de una aplicación dentro de una clase. En lugar de manejar todos los métodos HTTP mediante condiciones dentro de una sola función, se pueden definir métodos separados para cada tipo de solicitud.

La documentación oficial de Django explica que las vistas basadas en clase permiten organizar y reutilizar código mediante la herencia. Para este taller se utiliza la clase `View` y se implementan los métodos `get()`, `post()`, `put()` y `delete()`.

Fuente: [Django — Class-based views](https://docs.djangoproject.com/en/6.1/topics/class-based-views/).

## 4. ¿Para qué sirve cada método HTTP?

### ¿Qué hace GET?

`GET` permite consultar información sin modificar los registros almacenados.

En el proyecto, `get()` devuelve todos los proyectos o consulta uno específico mediante su identificador.

### ¿Qué hace POST?

`POST` permite enviar información al servidor para crear un nuevo registro.

En el proyecto, `post()` recibe el nombre y la descripción del proyecto en formato JSON y guarda los datos en la base de datos.

### ¿Qué hace PUT?

`PUT` se utiliza para actualizar un recurso existente.

En el proyecto, `put()` busca el proyecto por su identificador, recibe los nuevos datos y guarda los cambios.

### ¿Qué hace DELETE?

`DELETE` solicita la eliminación de un recurso.

En el proyecto, `delete()` busca el proyecto indicado y lo elimina de la base de datos.

## 5. ¿Cómo se relacionan los métodos HTTP con CRUD?

CRUD es la abreviatura de las cuatro operaciones básicas que se realizan sobre los datos:

| Operación | Método HTTP | Uso en el proyecto |
|---|---|---|
| Create (crear) | POST | Registrar un proyecto |
| Read (leer) | GET | Consultar proyectos |
| Update (actualizar) | PUT | Modificar un proyecto |
| Delete (eliminar) | DELETE | Borrar un proyecto |

## 6. ¿Qué archivos se modificaron?

### `models.py`

Contiene el modelo `Proyecto`, que define los campos `nombre` y `descripcion`. Django utiliza los modelos para representar los datos almacenados en la base de datos.

### `views.py`

Contiene la clase `ProyectoView`, donde se procesa la lógica de las solicitudes HTTP y se generan las respuestas en formato JSON.

### `urls.py`

Define las rutas de la aplicación y las conecta con `ProyectoView` mediante `path()` y `ProyectoView.as_view()`.

## 7. ¿Qué módulos, funciones y decoradores se utilizaron?

| Elemento | Descripción |
|---|---|
| `json` | Módulo de Python utilizado para interpretar los datos JSON recibidos. |
| `json.loads()` | Convierte el contenido JSON en un objeto de Python. |
| `django.http.JsonResponse` | Permite devolver respuestas HTTP en formato JSON. |
| `django.views.View` | Clase base utilizada para crear una vista basada en clase. |
| `django.urls.path` | Define las rutas de la aplicación. |
| `as_view()` | Permite conectar la vista basada en clase con una ruta. |
| `dispatch()` | Dirige la solicitud al método que corresponde al verbo HTTP. |
| `csrf_exempt` | Excluye la vista de la comprobación CSRF de Django. |
| `method_decorator` | Permite aplicar un decorador a una clase o a sus métodos. |
| `get()` | Consulta los proyectos. |
| `post()` | Crea un proyecto. |
| `put()` | Actualiza un proyecto. |
| `delete()` | Elimina un proyecto. |
| `Proyecto.objects.all()` | Recupera todos los proyectos. |
| `Proyecto.objects.get()` | Busca un proyecto específico. |
| `Proyecto.objects.create()` | Crea y guarda un proyecto. |
| `save()` | Guarda los cambios realizados en un objeto. |
| `delete()` | Elimina un objeto de la base de datos. |

**Nota de seguridad:** durante las pruebas se utilizó `csrf_exempt` para facilitar el envío de solicitudes desde Thunder Client. En una aplicación de producción se debe revisar la configuración de seguridad y mantener las protecciones CSRF que correspondan.

## 8. ¿Cómo se comprobaron los endpoints?

Se utilizó Thunder Client, una extensión de Visual Studio Code que permite enviar solicitudes HTTP y revisar las respuestas del servidor.

- **GET:** se consultó la lista de proyectos.
- **POST:** se creó un proyecto enviando un nombre y una descripción.
- **PUT:** se actualizaron los datos de un proyecto existente.
- **DELETE:** se eliminó un proyecto mediante su identificador.

### Evidencias

Agregar aquí las capturas tomadas durante las pruebas:

1. ![alt text](<Captura GET.png>)
2. ![alt text](<Captura POST.png>)
3. ![alt text](<Captura PUT.png>)
4. ![alt text](<Captura DELETE.png>)

## 9. ¿Qué se concluye del taller?

Con este taller se practicó la creación de endpoints utilizando una vista basada en clase de Django. Se comprobó que los métodos HTTP permiten realizar diferentes operaciones sobre los registros de una aplicación y que las rutas definidas en `urls.py` conectan las solicitudes con la lógica implementada en `views.py`.

También se utilizaron respuestas JSON para mostrar el resultado de las operaciones y Thunder Client para verificar el funcionamiento de los endpoints.

## 10. Fuentes consultadas

1. Django Software Foundation. **Class-based views**. Documentación oficial de Django.  
   https://docs.djangoproject.com/en/6.1/topics/class-based-views/

2. Django Software Foundation. **Base views**. Documentación oficial de Django.  
   https://docs.djangoproject.com/en/6.1/ref/class-based-views/base/

3. Pypro. **Construcción de Endpoints en Django Rest**.  
   https://www.pypro.mx/app/curso/apis-con-django-rest/construccion-de-endpoints-en-django-rest

4. Sintu S@mson. **Django: post, put, get, delete requests example | Rest APIs #Chapter-19**. Medium, 31 de diciembre de 2023.  
   https://medium.com/@sinturana07/django-post-put-get-delete-requests-example-rest-apis-chapter-19-c449b6260b2a

