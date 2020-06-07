import re

def clean(html):
    if '<script' in html:
        return html.replace('{{', '{ {').replace('}}', '} }')
    else:
        return html