from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader = PackageLoader('app', 'email_templates'),
    autoescape = select_autoescape(['html', 'xml'])
)
template = env.get_template('email.html')

def generate_html_report(verbs, nouns, text):
    html = template.render(verbs=verbs, nouns=nouns, text=text)
    return html