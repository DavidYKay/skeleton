{% include "header.base" %}

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
