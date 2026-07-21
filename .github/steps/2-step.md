## Paso 2: Avanzando en el trabajo con Copilot

En el paso anterior, GitHub Copilot nos ayudó a familiarizarnos con el proyecto. Eso por sí solo ya ahorra mucho tiempo, ¡pero ahora vamos a ponernos a trabajar!

:bug: **HAY UN ERROR EN EL SITIO WEB** :bug:

Descubrimos que algo no está bien en el flujo de inscripción.
¡Los estudiantes actualmente pueden registrarse en la misma actividad **más de una vez**! Veamos hasta dónde puede llevarnos Copilot para descubrir la causa y construir una solución limpia.

Antes de continuar, un breve repaso de cómo funciona Copilot. 🧑‍🚀

### 📖 Teoría: Cómo funciona Copilot

En resumen, puedes pensar en Copilot como un compañero de trabajo muy especializado. Para ser eficaz con él, necesitas darle contexto (información de fondo) y una dirección clara (prompts). Además, distintas personas son mejores en distintas cosas debido a sus experiencias particulares (modelos).

- **¿Cómo proporcionamos contexto?:** En nuestro entorno de programación, Copilot considerará automáticamente el código cercano y las pestañas abiertas. Si estás usando el chat, también puedes hacer referencia explícita a archivos.

- **¿Qué modelo deberíamos elegir?:** Para nuestro ejercicio, no debería importar demasiado. ¡Experimentar con distintos modelos es parte de la diversión! ¡Esa es otra lección! 🤖

- **¿Cómo elaboro los prompts?:** Ser explícito y claro ayuda a Copilot a hacer el mejor trabajo posible. Pero a diferencia de algunos sistemas tradicionales, siempre puedes aclarar tu dirección con prompts de seguimiento.

> [!TIP]
> Existen otras formas de complementar el conocimiento y las capacidades de Copilot, como los [chat participants](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-participants), las [chat variables](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#chat-variables), los [slash commands](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet?tool=vscode#slash-commands-1) y las [herramientas MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

### :keyboard: Actividad: Usa Copilot para corregir nuestro error de registro :bug:

1. Pidamos a Copilot que sugiera de dónde podría venir nuestro error. Abre el panel de **Copilot Chat** en **Ask mode** y pregunta lo siguiente.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Los estudiantes pueden registrarse dos veces en una actividad.
   > ¿De dónde podría venir este error?
   > ```

1. Ahora que sabemos que el problema está en el archivo `src/app.py`, dentro del método `signup_for_activity`, sigamos la recomendación de Copilot y vayamos a corregirlo (de forma semi-manual). Comenzaremos con un comentario y dejaremos que Copilot termine la corrección.
   1. Abre el archivo `src/app.py`.

      > 💡 **Consejo:** Si Copilot mencionó `src/app.py` en el chat, puedes hacer clic directamente en el archivo dentro de la vista de chat para abrirlo.

   1. Cerca de la parte inferior del archivo, busca la función `signup_for_activity`.

   1. Busca la línea de comentario que describe cómo agregar un estudiante. Justo arriba de esta parece lógico hacer nuestra verificación de registro.

   1. Ingresa el siguiente comentario y presiona enter para pasar a la siguiente línea. Después de un momento, aparecerá un texto sombreado temporal con una sugerencia de Copilot. ¡Genial! :tada:

      Comentario:

      ```python
      # Validate student is not already signed up
      ```

      <img width="700" alt="sugerencia de texto sombreado de Copilot en el editor" src="../images/shadow-text.gif" />

   1. Presiona `Tab` para aceptar la sugerencia de Copilot y convertir el texto sombreado en código.

   <details>
   <summary>Resultados de ejemplo</summary><br/>

   Copilot mejora cada día y puede que no siempre produzca los mismos resultados. Si no estás conforme con las sugerencias obtenidas, aquí tienes un ejemplo de un resultado válido que obtuvimos al preparar este ejercicio. Puedes usarlo para continuar.

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### :keyboard: Actividad: Deja que Copilot genere datos de ejemplo 📋

En proyectos nuevos, suele ser útil contar con datos ficticios realistas para hacer pruebas. Copilot es excelente en esta tarea, así que agreguemos algunas actividades de ejemplo adicionales e introduzcamos otra forma de interactuar con Copilot usando **Inline Chat**.

**Inline Chat** y el panel de **Copilot Chat** son similares, pero se diferencian en su alcance: Copilot Chat maneja preguntas más amplias, exploratorias o de varios archivos; Inline Chat es más rápido cuando quieres ayuda puntual sobre la línea o el bloque exacto que tienes frente a ti.

1. Cerca de la parte superior del archivo `src/app.py` (alrededor de la línea 23), busca la variable `activities`, donde están configuradas nuestras actividades extracurriculares de ejemplo.

1. Resalta todo el diccionario `activities` haciendo clic y arrastrando el mouse desde el inicio hasta el final del diccionario. Esto ayudará a darle contexto a Copilot para nuestro siguiente prompt.

   <img width="700" alt="Diccionario de actividades resaltado antes de abrir el inline chat" src="../images/activities-dict-highlighted.png" />


1. Abre el inline chat de Copilot usando el atajo de teclado `Ctrl + I` (Windows) o `Cmd + I` (Mac).

   > 💡 **Consejo:** Otra forma de abrir el inline chat de Copilot es: `clic derecho` sobre cualquiera de las líneas seleccionadas -> `Open Inline Chat`.

1. Ingresa el siguiente texto de prompt y presiona enter o el botón **Send** a la derecha.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Agrega 2 actividades más relacionadas con deportes, 2 actividades
   > artísticas más y 2 actividades intelectuales más.
   > ```

1. Después de un momento, Copilot comenzará a realizar cambios directamente en el código. Los cambios se mostrarán con un estilo diferente para que sea fácil identificar las adiciones y eliminaciones. Tómate un momento para inspeccionar y verificar los cambios, y luego presiona el botón **Keep**.

   <details>
   <summary>Resultados de ejemplo</summary><br/>

   Copilot mejora cada día y puede que no siempre produzca los mismos resultados. Si no estás conforme con las sugerencias obtenidas, aquí tienes un resultado de ejemplo que obtuvimos al preparar este ejercicio. Puedes usarlo para continuar si tienes problemas.

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. Ahora puedes ir a tu sitio web y verificar que las nuevas actividades sean visibles.

### :keyboard: Actividad: Usa Copilot para describir nuestro trabajo 💬

¡Buen trabajo corrigiendo ese error y ampliando las actividades de ejemplo! Ahora hagamos commit de nuestro trabajo y publiquémoslo en GitHub, de nuevo con la ayuda de Copilot.

1. En la barra lateral izquierda, selecciona la pestaña `Source Control`.

   > 💡 **Consejo:** Abrir un archivo desde el área de control de versiones mostrará las diferencias respecto al original en lugar de simplemente abrirlo.

1. Busca el archivo `app.py` y presiona el signo `+` para agrupar tus cambios en el área de staging.

   ![imagen](../images/staging-changes-icon.png)

1. Encima de la lista de cambios preparados (staged), busca el cuadro de texto **Message**, pero **no escribas nada** por ahora.
   - Normalmente, escribirías aquí una breve descripción de los cambios, ¡pero ahora tenemos a Copilot para ayudarnos!

1. A la derecha del cuadro de texto **Message**, busca y haz clic en el botón **Generate Commit Message** (ícono de destellos).

1. Presiona el botón **Commit** y luego el botón **Sync Changes** para publicar tus cambios en GitHub.

1. Espera un momento a que Mona revise tu trabajo, te dé retroalimentación y comparta la siguiente lección.

<details>
<summary>¿Tienes problemas? 🤷</summary><br/>

Si no recibes retroalimentación, aquí hay algunas cosas para revisar:

- Asegúrate de haber publicado los cambios del archivo `src/app.py` en la rama `accelerate-with-copilot`.

</details>
