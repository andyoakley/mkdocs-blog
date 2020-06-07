This is a list of the most recent three posts.

{% for p in config['ordered'][-3:] | reverse %}
  {% set page = p[0] %}
  {% set mtime = p[3] %}
  <a href="{{ page.url }}">
  {{ page.title }}
  </a>
  <br />
{% endfor %}
