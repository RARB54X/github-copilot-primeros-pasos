# API de Actividades de Mergington High School

Una aplicación FastAPI súper simple que permite a los estudiantes ver e inscribirse en actividades extracurriculares.

## Características

- Ver todas las actividades extracurriculares disponibles
- Inscribirse en actividades

## Primeros pasos

1. Instala las dependencias:

   ```
   pip install fastapi uvicorn
   ```

2. Ejecuta la aplicación:

   ```
   python app.py
   ```

3. Abre tu navegador y ve a:
   - Documentación de la API: http://localhost:8000/docs
   - Documentación alternativa: http://localhost:8000/redoc

## Endpoints de la API

| Método | Endpoint                                                          | Descripción                                                                    |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Obtiene todas las actividades con sus detalles y el número actual de participantes |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Inscribirse en una actividad                                                     |

## Modelo de datos

La aplicación utiliza un modelo de datos simple con identificadores significativos:

1. **Actividades** - Usa el nombre de la actividad como identificador:

   - Descripción
   - Horario
   - Número máximo de participantes permitido
   - Lista de correos electrónicos de los estudiantes inscritos

2. **Estudiantes** - Usa el correo electrónico como identificador:
   - Nombre
   - Nivel de grado

Todos los datos se almacenan en memoria, lo que significa que se reiniciarán cuando el servidor se reinicie.
