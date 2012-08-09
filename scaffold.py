from datetime import datetime
import sys
from jinja2 import Environment, FileSystemLoader
  
def get_template_env(template_dir, *args, **kwargs):
    return Environment(loader=FileSystemLoader(template_dir or '.'), *args, **kwargs)

def render_template(template_file, **context):
    """Renders payload as a jinja template
    """
    t_env = get_template_env('templates')
    template = t_env.get_template(template_file)
    body = template.render(**context or {})
    return body

class Renderer():
  def render(self, file_name):
    context = self._create_master_context(file_name)
    return render_template(self.get_template(file_name), **context)
  
  def _create_master_context(self, file_name):
    context = self.generic_context(file_name)
    context.update(self.make_context(file_name))
    del context['self']
    return context

  def generic_context(self, file_name):
    return {
        'date': datetime.now().date(),
        'author': 'David Y. Kay',
        'company_name': 'Gargoyle Software LLC',
    }
    
  def get_template(self, file_name):
    """ This tells us which template file to render.
    """
    raise NotImplementedError

  def make_context(self, file_name):
    """ This is the main override point for our beloved Renderers. 
        Pass whatever you need into the context.
    """
    raise NotImplementedError

class AbstractObjCRenderer(Renderer):
  def get_complement(self, file_name):
    file_prefix, file_type = file_name.split('.')
    if file_type == 'm':
      complement = 'h'
    else:
      complement = 'm'
    return "%s.%s" % (file_prefix, complement)

class ObjCHeaderRenderer(AbstractObjCRenderer):
  def get_template(self, file_name):
    return 'base.h'

  def make_context(self, file_name):
    class_name = file_name.split('.')[0]
    return locals()

class ObjCRenderer(AbstractObjCRenderer):
  def get_template(self, file_name):
    return 'base.m'

  def make_context(self, file_name):
    class_name = file_name.split('.')[0]
    header_name = self.get_complement(file_name)
    return locals()

class JavaRenderer(Renderer):
  def get_template(self, file_name):
    return 'base.java'

  def make_context(self, file_name):
    class_name = file_name.split('.')[0]
    return locals()

class PythonRenderer(Renderer):
  def get_template(self, file_name):
    return 'base.py'

  def make_context(self, file_name):
    class_name = file_name.split('.')[0]
    return locals()

class HtmlRenderer(Renderer):
  def get_template(self, file_name):
    return 'base.h'

  def make_context(self, file_name):
    name = 'John'
    return locals()

class Scaffolding:
  def generate(self, file_name):
    filetype = file_name.split('.')[-1]
    if filetype == 'java':
      renderer = JavaRenderer()
    elif filetype == 'py':
      renderer = PythonRenderer()
    elif filetype == 'm':
      renderer = ObjCRenderer()
    elif filetype == 'h':
      renderer = ObjCHeaderRenderer()
    else:
      renderer = HtmlRenderer()
    return renderer.render(file_name)

def main():
  file_name = sys.argv[1] 
  scaffolding = Scaffolding()
  print scaffolding.generate(file_name)

if __name__ == '__main__':
  main()
