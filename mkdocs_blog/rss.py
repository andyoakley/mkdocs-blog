from jinja2 import Environment
import pkgutil
import os.path
import urllib.parse

from . import jinja_filters
from . import cleaner

def generate(nav, config, files):
    env = Environment()
    env.filters['strftime'] = jinja_filters.strftime
    env.globals['urljoin'] = urllib.parse.urljoin

    template = pkgutil.get_data(__package__, 'rss.xml')

    output = env.from_string(template.decode('utf-8')).render(
        config=config,
        nav=nav,
        files=files
    )

    output_path = os.path.join(
        config.data['site_dir'],
        'rss.xml'
    )

    os.makedirs(config.data['site_dir'], exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(output)
