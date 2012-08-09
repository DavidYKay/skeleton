{% include "header.base" %}

#import <UIKit/UIKit.h>
{% block imports %}{% endblock %}

/**
 * 
 */
@interface {{ class_name }} : {% block superclass %}NSObject{% endblock %} {% block interfaces %}{% endblock %} {
  {% block fields %}{% endblock %}
}

{% block property_signatures %}{% endblock %}

{% block method_signatures %}{% endblock %}

@end
