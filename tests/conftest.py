import pytest
import os.path

from mkdocs import config
from mkdocs.commands import build

@pytest.fixture()
def mkdocs_site(tmpdir):
    mkdocs_root = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'test_data'
    )

    cfg = config.load_config(os.path.join(mkdocs_root, 'mkdocs.yml'))
    cfg['site_dir'] = tmpdir
    build.build(cfg)