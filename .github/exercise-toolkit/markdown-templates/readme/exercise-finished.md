{% set socials_text -%}
{%- if exercise_title -%}
¡Acabo de completar el ejercicio práctico "{{ exercise_title }}" de GitHub Skills! 🎉
{%- else -%}
¡Acabo de completar un ejercicio práctico de GitHub Skills! 🎉
{%- endif %}

{{ repository_url }}

#GitHubSkills #OpenSource #GitHubLearn
{%- endset -%}

<div align="center">

# 🎉 ¡Felicidades {{ login }}! 🎉

<img src="https://octodex.github.com/images/welcometocat.png" height="200px" />

### 🌟 ¡Completaste el ejercicio con éxito! 🌟

## 🚀 ¡Comparte tu logro!

**¡Presume tus nuevas habilidades e inspira a otros!**

<a href="https://twitter.com/intent/tweet?text={{ socials_text | urlencode }}" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Compartir%20en%20X-1da1f2?style=for-the-badge&logo=x&logoColor=white" alt="Compartir en X" />
</a>
<a href="https://bsky.app/intent/compose?text={{ socials_text | urlencode }}" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Compartir%20en%20Bluesky-0085ff?style=for-the-badge&logo=bluesky&logoColor=white" alt="Compartir en Bluesky" />
</a>
<a href="https://www.linkedin.com/feed/?shareActive=true&text={{ socials_text | urlencode }}" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/Compartir%20en%20LinkedIn-0077b5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Compartir en LinkedIn" />
</a>

### 🎯 ¿Qué sigue?

**¡Sigue con el impulso!**

[![](https://img.shields.io/badge/Volver%20al%20Ejercicio-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)]({{ issue_url }})
[![GitHub Skills](https://img.shields.io/badge/Explora%20GitHub%20Skills-000000?style=for-the-badge&logo=github&logoColor=white)](https://learn.github.com/skills)

*¡No hay mejor manera de aprender que construyendo cosas! 🚀*

</div>
