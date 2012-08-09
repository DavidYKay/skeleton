{% include "header.base" %}

{% block imports %}{% endblock %}

/**
 * 
 */
public class {{ class_name }} {% block superclass %}{% endblock %}{% block interfaces %}{% endblock %} {
  {% block fields %}{% endblock %}
  public {{ class_name }}() {
    {% block constructor %}{% endblock %}
  }
  {% block methods %}{% endblock %}
}
