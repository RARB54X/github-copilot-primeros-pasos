## Paso 3: Activa la hipervelocidad - Copilot Agent Mode 🚀

### 📖 Teoría: ¿Qué es Copilot Agent Mode?

El [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) de Copilot es la siguiente evolución en la programación asistida por IA. Actuando como un compañero de programación autónomo, realiza tareas de programación de varios pasos siguiendo tus indicaciones.

Copilot Agent Mode responde a errores de compilación y de lint, monitorea la salida de la terminal y de las pruebas, y se autocorrige en un ciclo hasta completar la tarea.

#### Agent Mode (de un vistazo)

| Aspecto | 👩‍🚀 Agent Mode |
| --- | --- |
| Autonomía y planificación | Divide solicitudes de alto nivel en trabajo de varios pasos e itera hasta que la tarea esté completa. |
| Recolección de contexto | Usa tu contexto actual y puede descubrir archivos relevantes adicionales cuando sea necesario. |
| Uso de herramientas | Selecciona e invoca herramientas automáticamente; también puedes dirigir herramientas con menciones como `#codebase`. |
| Aprobación y controles de seguridad | Las acciones sensibles pueden requerir aprobación antes de ejecutarse, ayudándote a mantener el control. |

#### 🧰 Herramientas de Agent Mode

Agent mode usa herramientas para realizar tareas especializadas mientras procesa una solicitud del usuario. Ejemplos de estas tareas son:

- Encontrar los archivos relevantes para completar tu prompt
- Obtener el contenido de una página web
- Ejecutar pruebas o comandos de terminal

> [!TIP]
> Aunque VS Code ofrece muchas herramientas integradas, también puedes darle a Agent Mode capacidades más específicas del dominio mediante **herramientas MCP**.
>
> Lee más sobre los [servidores MCP](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) y el [GitHub MCP Server](https://github.com/github/github-mcp-server)

Ahora, ¡probemos **Agent Mode**! 👩‍🚀

### :keyboard: Actividad: Usa Copilot para agregar una nueva funcionalidad :rocket:

Nuestro sitio web muestra las actividades, pero mantiene en secreto la lista de inscritos 🤫

Usemos Copilot para modificar el sitio web y mostrar los estudiantes inscritos debajo de cada actividad.

1. En la parte inferior de la ventana de Copilot Chat, usa el menú desplegable para cambiar al modo **Agent**.

   <img width="350" alt="imagen" src="../images/agent-mode-dropdown.png" />

1. Abre los archivos relacionados con nuestra página web y arrastra cada ventana de editor (o archivo) al panel de chat, indicándole a Copilot que los use como contexto.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **Nota:** Agregar archivos como contexto es opcional. Si omites este paso, Copilot Agent Mode aún puede usar herramientas como `#codebase` para buscar archivos relevantes según tu prompt. Agregar archivos específicos ayuda a orientar a Copilot en la dirección correcta, lo cual es especialmente útil en bases de código más grandes.

   <img width="400" alt="imagen mostrando archivos agregados al contexto" src="../images/files-added-to-context.png" />

   > 💡 **Consejo:** También puedes usar el botón **Add Context...** para agregar otras fuentes de contexto, como un issue de GitHub o el resultado de una ventana de terminal.

1. Pídele a Copilot que actualice nuestro proyecto para mostrar los participantes actuales de las actividades. Espera un momento a que lleguen las sugerencias de edición y se apliquen.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hola Copilot, ¿puedes editar las tarjetas de actividad para agregar una sección de participantes?
   > Debe mostrar qué participantes ya están inscritos en esa actividad, en una lista con viñetas.
   > ¡Recuerda que se vea bien!
   > ```

   Cuando Copilot termine el trabajo, tú tienes el control sobre qué cambios se conservan.

   Usando los botones **Keep** que se muestran a continuación, puedes aceptar/descartar todos los cambios o revisar y decidir cambio por cambio. Esto se puede hacer desde la vista del panel de chat o mientras inspeccionas cada archivo editado.

      <img width="900" alt="botones para conservar o descartar cambios" src="../images/review-changes-buttons.png" />


1. Antes de simplemente aceptar los cambios, revisa nuevamente nuestro sitio web y verifica que todo se haya actualizado como se esperaba.

   Aquí tienes un ejemplo de una tarjeta de actividad actualizada. Es posible que debas reiniciar la aplicación o actualizar la página.

   <img width="350" alt="Tarjeta de actividad con información de participantes" src="../images/activity-card-with-participants.png" />

   > 🪧 **Nota:** Tu tarjeta de actividad puede verse diferente. Copilot no siempre produce los mismos resultados.

   <details>
   <summary>¿Necesitas ayuda? 🤷</summary><br/>
   Si el sitio web no carga, aquí hay algunas cosas para revisar.

   - Reinicia el depurador de VS Code para asegurarte de que se sirva la última versión del sitio web.
   - Si olvidaste la url, o cerraste la ventana, por favor revisa el paso 1.
   - Intenta hacer un refresco forzado de la página o abrirla en una ventana privada para que descargue una copia nueva.

   </details>

1. Ahora que confirmamos que nuestros cambios son correctos, usa el panel para recorrer cada edición sugerida y presiona **Keep** para aplicar el cambio.

   > 💡 **Consejo:** Puedes aceptar los cambios directamente, modificarlos o dar instrucciones adicionales para refinarlos usando la interfaz de chat.

### :keyboard: Actividad: Usa Agent mode para agregar botones funcionales de "dar de baja"

Probemos algunas solicitudes más abiertas que agregarán más funcionalidad a nuestra aplicación web.

Si no obtienes los resultados deseados, puedes probar otros modelos o dar retroalimentación de seguimiento para refinar los resultados.

1. Asegúrate de que Copilot siga en modo **Agent**.

   <img width="250" alt="agent mode" src="../images/agent-mode-dropdown.png" />

1. Haz clic en el ícono de **Tools** y explora todas las herramientas actualmente disponibles para Copilot Agent Mode.

   <img width="250"  alt="ícono de herramientas" src="../images/tools-icon.png" />

1. ¡Hora de nuestra prueba! Pidámosle a Copilot que agregue la funcionalidad para eliminar participantes.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Por favor agrega un ícono de eliminar junto a cada participante y oculta las viñetas.
   > Al hacer clic, se debe dar de baja a ese participante de la actividad.
   > ```

   Copilot usa la herramienta `#codebase` para encontrar archivos y fragmentos de código relevantes para la tarea en cuestión.

   > 🪧 **Nota:** En este laboratorio incluimos explícitamente la herramienta `#codebase` para obtener los resultados más repetibles.
   > Siéntete libre de probar el prompt **sin** `#codebase` y observar si Agent Mode decide reunir por su cuenta un contexto más amplio del proyecto.

1. Cuando Copilot termine, inspecciona los cambios en el código y los resultados en el sitio web. Si te gustan los resultados, presiona el botón **Keep**. Si no, intenta darle a Copilot retroalimentación para refinar los resultados.

   > 🪧 **Nota:** Si no ves actualizaciones en el sitio web, es posible que necesites reiniciar el depurador.

1. Pídele a Copilot que corrija un error de registro.

   > 💡 **Consejo:** Recomendamos probar tú mismo/a el flujo de registro para que puedas ver claramente el comportamiento antes/después de los cambios.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > He notado que parece haber un error.
   > Cuando se registra un participante, hay que actualizar la página para ver el cambio en la actividad.
   > ```

1. Cuando Copilot termine, inspecciona los resultados y valida el flujo de registro en el sitio web.

   Si te gustan los resultados, presiona el botón **Keep**. Si no, intenta darle a Copilot retroalimentación.

1. Haz **commit** y **push** de todos tus cambios a la rama `accelerate-with-copilot`.

1. Espera a que Mona revise tu trabajo y comparta el siguiente paso.
