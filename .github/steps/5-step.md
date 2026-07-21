## Paso 5: Usando GitHub Copilot dentro de un pull request

¡Felicitaciones! Has terminado de programar en este ejercicio (y en VS Code). Ahora es momento de fusionar nuestro trabajo. :tada: Para cerrar, aprendamos sobre dos funciones de Copilot de acceso limitado que pueden agilizar nuestros pull requests.

### 📖 Teoría: GitHub Copilot para pull requests

#### Resúmenes de pull request de Copilot

Normalmente, revisarías tus notas y mensajes de commit para luego resumirlos en la descripción de tu pull request. Esto puede tomar tiempo, especialmente si los mensajes de commit son inconsistentes o el código no está bien documentado. Por suerte, Copilot puede considerar todos los cambios del pull request y ofrecer los puntos más importantes, ¡con referencias incluidas!

#### Revisión de código de Copilot

Siempre es útil tener más ojos sobre nuestro trabajo, así que pidámosle a Copilot que haga una primera pasada antes de realizar el proceso normal de revisión entre pares. Copilot es muy bueno detectando errores comunes que se corrigen con ajustes simples, pero recuerda usarlo de forma responsable.

> [!NOTE]
> Estas funciones solo están disponibles en los planes de pago de **GitHub Copilot**. [[documentación]](https://docs.github.com/en/copilot/get-started/plans)

### :keyboard: Actividad: Resume y revisa un PR con Copilot

Tanto los **resúmenes de pull request de Copilot** como la **revisión de código de Copilot** tienen acceso limitado, por lo que esta actividad es mayormente opcional. Si no tienes acceso, omite los pasos opcionales de esta actividad.

1. En un navegador web, abre otra pestaña y navega a tu repositorio del ejercicio.

1. Es posible que notes un **banner de notificación** sugiriendo crear un nuevo pull request. Haz clic en él o usa la pestaña **Pull Requests** en la parte superior para **crear un nuevo pull request**. Usa los siguientes detalles:

   - **base:** `main`
   - **compare:** `accelerate-with-copilot`
   - **title:** `Improve student activity registration system`

1. (Opcional) En la barra de herramientas de la descripción del PR, haz clic en el ícono de **Copilot** y en la acción **Summary**. Después de un momento, Copilot agregará una descripción basada en tus cambios. :memo:

   <img alt="Botón de resumen de Copilot" width="450px" src="../images/copilot-summarize-button.png">

1. (Opcional) En el panel de información del lado derecho, en la parte superior, ubica la sección **Reviewers** y haz clic en el botón **Request** junto al ícono de **Copilot**. Espera un momento a que Copilot agregue un comentario de revisión a tu pull request.

   <img alt="Botón de revisión de Copilot" width="300px" src="../images/copilot-review-button.png">

   > 💡 **Consejo:** Observa que aparece un registro indicando que se solicitó una revisión a Copilot.

1. En la parte inferior, presiona el botón **Merge pull request**. ¡Buen trabajo! ¡Ya terminaste! :tada:

1. Espera un momento a que Mona revise tu trabajo, te dé retroalimentación y publique una revisión final de este ejercicio.
