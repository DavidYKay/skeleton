{% include "header.base" %}

{% block imports %}{% endblock %}

class {{ class_name }} {% block superclass %}{% endblock %}:
  """ This class is all about ___
  """
  def __init__(self, *args, **kwargs):
    {% block constructor %}
    pass
    {% endblock %}

  {% block methods %}{% endblock %}
