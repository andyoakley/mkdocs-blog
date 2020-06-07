import pytest
import mkdocs_blog.cleaner as cleaner

def test_simple():
    assert cleaner.clean("hello") == "hello"

def test_jinja_normal():
    assert cleaner.clean(r"{{ x }}") == r"{{ x }}"

def test_jinja_javascript():
    s = cleaner.clean(r"<script>{{ null; }}</script>")
    assert s == r"<script>{ { null; } }</script>"

@pytest.mark.skip(reason="Too hard")
def test_jinja_javascript_and_not():
    s = cleaner.clean(r"{{ x }}<script>{{ null; }}</script>")
    assert s == r"{{ x }}<script>{ { null; } }</script>"

def test_jinja_javascript_big():
    data = """
      "            <script type=\"text/javascript\">\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n"
        </script>
    """
    s = cleaner.clean(data)
    assert '{{' not in s
    assert '}}' not in s