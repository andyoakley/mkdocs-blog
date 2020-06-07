This is a list of posts, first grouped by year, then month, then sorted by age.

{% set chronological = config['chronological'] %}

{% for year in chronological|sort(reverse=True) %}
  <h3>{{ year | strftime("%Y") }}</h3>
  {% for month in chronological[year] %}
    <h4>{{ month | strftime("%B")  }}</h4>
    {% for mtime in chronological[year][month]|sort(reverse=True) %}
      {% set page = chronological[year][month][mtime] %}
      <a href="/{{ page.url }}">{{ page.title }}</a>
      <br />
    {% endfor %}
  {% endfor %}

{% endfor %}
