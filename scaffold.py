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
  def render(self, filename):
      raise NotImplementedError

class JavaRenderer(Renderer):
  def render(self, filename):
    file_name = filename
    class_name = filename.split('.')[0]
    params = locals()
    del params['self']
    return render_template('base.java', **params)

class PythonRenderer(Renderer):
  def render(self, filename):
    file_name = filename
    class_name = filename.split('.')[0]
    params = locals()
    del params['self']
    return render_template('base.py', **params)

class HtmlRenderer(Renderer):
  def render(self, filename, **params):
    name = 'John'
    params = locals()
    del params['self']
    return render_template('hello.html', **params)

class Scaffolding:
  def generate(self, filename):
    filetype = filename.split('.')[-1]
    if filetype == 'java':
      renderer = JavaRenderer()
    elif filetype == 'py':
      renderer = PythonRenderer()
    else:
      renderer = HtmlRenderer()
    return renderer.render(filename)

def main():
  filename = sys.argv[1] 
  scaffolding = Scaffolding()
  print scaffolding.generate(filename)

if __name__ == '__main__':
  main()
