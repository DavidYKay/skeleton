//
//  {{ file_name }}
//  {{ project_name }}
//
//  Created by {{ author }} on {{ date }}.
//  Copyright (c) {{ date.year }} {{ company_name }}. All rights reserved.
//

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
