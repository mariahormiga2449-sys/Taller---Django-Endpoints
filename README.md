# Taller: Creación de endpoints en Django nativo

**Docente:** Jose Javier Torres Vanstrahlen  
**Curso:** Desarrollo de Aplicaciones Web I – 4E  
**Estudiante:** Maria Hormiga

## 1. Creación de endpoints en Django nativo

Django permite crear endpoints de manera nativa mediante vistas que reciben solicitudes HTTP y devuelven respuestas al cliente.

Para este desarrollo se utiliza una vista basada en clase, heredando de `View`, que permite implementar los métodos `get()`, `post()`, `put()` y `delete()`.

Las rutas se definen en el archivo `urls.py` y se conectan con la vista mediante `path()` y `as_view()`.

En este proyecto se utilizan las siguientes rutas:

- `/proyectos/`: permite consultar todos los proyectos y crear uno nuevo.
- `/proyectos/<id>/`: permite consultar, actualizar o eliminar un proyecto específico.

## 2. Manejo de los cuatro verbos HTTP

**GET – Consultar**

Permite obtener información sin modificar los datos almacenados.

En el proyecto, el método `get()` permite consultar todos los proyectos o buscar uno específico mediante su identificador.

**POST – Crear**

Permite enviar información al servidor para crear un nuevo registro.

En el proyecto, el método `post()` recibe el nombre y la descripción de un proyecto en formato JSON y lo guarda en la base de datos.

**PUT – Actualizar**

Permite actualizar un recurso existente.

En el proyecto, el método `put()` busca un proyecto mediante su identificador, recibe los nuevos datos y guarda los cambios.

**DELETE – Eliminar**

Permite solicitar la eliminación de un recurso.

En el proyecto, el método `delete()` busca el proyecto mediante su identificador y lo elimina de la base de datos.

## 3. Relación entre los verbos HTTP y CRUD

CRUD representa las cuatro operaciones básicas para administrar información:

| Operación CRUD | Verbo HTTP | Función en el proyecto |
|---|---|---|
| Create (Crear) | POST | Registrar un proyecto. |
| Read (Leer) | GET | Consultar proyectos. |
| Update (Actualizar) | PUT | Modificar un proyecto. |
| Delete (Eliminar) | DELETE | Eliminar un proyecto. |

## 4. Módulos, funciones y decoradores utilizados

| Elemento | Descripción |
|---|---|
| `json` | Módulo de Python utilizado para trabajar con datos JSON. |
| `json.loads()` | Convierte los datos JSON recibidos en un objeto de Python. |
| `django.http.JsonResponse` | Permite devolver respuestas HTTP en formato JSON. |
| `django.views.View` | Clase base utilizada para crear vistas basadas en clases. |
| `django.urls.path` | Permite definir las rutas de la aplicación. |
| `as_view()` | Convierte la vista basada en clase en una vista que Django puede ejecutar. |
| `dispatch()` | Identifica el método HTTP recibido y dirige la solicitud al método correspondiente. |
| `method_decorator` | Permite aplicar un decorador a una vista basada en clase. |
| `csrf_exempt` | Excluye la vista de la protección CSRF de Django. |
| `get()` | Método que permite consultar proyectos. |
| `post()` | Método que permite crear proyectos. |
| `put()` | Método que permite actualizar proyectos. |
| `delete()` | Método que permite eliminar proyectos. |
| `Proyecto.objects.all()` | Recupera todos los proyectos de la base de datos. |
| `Proyecto.objects.get()` | Busca un proyecto específico. |
| `Proyecto.objects.create()` | Crea y guarda un nuevo proyecto. |
| `save()` | Guarda los cambios realizados en un objeto. |
| `delete()` | Elimina un objeto de la base de datos. |

## 5. Fuentes consultadas

**Django Software Foundation.** Class-based views. Documentación oficial de Django.  
https://docs.djangoproject.com/en/6.1/topics/class-based-views/

**Django Software Foundation.** Base views. Documentación oficial de Django.  
https://docs.djangoproject.com/en/6.1/ref/class-based-views/base/

**Django Software Foundation.** URL dispatcher. Documentación oficial de Django.  
https://docs.djangoproject.com/en/6.1/topics/http/urls/

**Django Software Foundation.** Cross Site Request Forgery protection. Documentación oficial de Django.  
https://docs.djangoproject.com/en/6.1/ref/csrf/
