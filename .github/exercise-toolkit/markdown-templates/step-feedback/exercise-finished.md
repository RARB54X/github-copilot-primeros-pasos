<img src="https://octodex.github.com/images/welcometocat.png" align="left" height="150px" />

¡Felicidades @{{ login }}! ¡Terminaste el ejercicio! 🎉🎉🎉
{% if readme_updated %}
¡Actualizamos el repositorio con algunos cambios para destacar tu logro!

Vuelve a la página de [inicio del repositorio](/{{ repo_full_name }}) para ver tu progreso!
{%- else %}
Completaste todos los pasos con éxito. ¡Bien hecho!
{%- endif %}
