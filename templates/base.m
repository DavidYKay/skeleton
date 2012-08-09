//
//  {{ file_name }}
//  {{ project_name }}
//
//  Created by {{ author }} on {{ date }}.
//  Copyright (c) {{ date.year }} {{ company_name }}. All rights reserved.
//

#import "{{ header_name }}"

{% block imports %}{% endblock %}

/**
 * {{ class_name }}
 */
@implementation {{ class_name }}

{% block synthesizers %}{% endblock %}

#pragma mark - Initialization

- (id)init {
  if (self = [super init]) {

  }
  return self;
}

#pragma mark - Main Methods
  
{% block methods %}{% endblock %}

#pragma mark - Private Methods


#pragma mark - Cleanup

- (void)dealloc {

}

@end
