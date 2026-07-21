{%- set all_passed = (results_table | selectattr("passed") | length) == (results_table | length) %}

{%- if all_passed %}

## Paso {{ step_number }} - Aprobado ✅

{%- else %}

## Paso {{ step_number }} - Fallo ❌

{%- endif %}

{%- if all_passed %}
<img src="https://octodex.github.com/images/inflatocat.png" align="right" height="150px" alt="Imagen de Inflatocat indicando que el paso fue aprobado" />
{%- else %}

<img src="https://octodex.github.com/images/spidertocat.png" align="right" height="100px" alt="Imagen de Spidertocat indicando que el paso falló" />
Algunas verificaciones fallaron. Por favor revisa los resultados de abajo e inténtalo de nuevo.

¡Hora de encontrar el error! 🤔
{%- endif %}

| Estado | Descripción |
| ------ | ----------- |

{%- for row in results_table %}
| {% if row.passed -%}✅ - Aprobado{%- else -%}❌ - Fallo{%- endif %} | {{ row.description }} |
{%- endfor %}

{%- if tips and tips.length %}

### Consejos

{%- for tip in tips %}

- {{ tip }}
  {%- endfor %}

{%- endif %}
