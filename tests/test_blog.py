import pytest
import os.path

from datetime import datetime

from mkdocs import config
from mkdocs.commands import build


@pytest.fixture
def processed_config(tmpdir):
    mkdocs_root = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'test_data'
    )

    cfg = config.load_config(os.path.join(mkdocs_root, 'mkdocs.yml'))
    cfg['site_dir'] = tmpdir

    files = build.get_files(cfg)
    nav = build.get_navigation(files, cfg)
    nav = cfg['plugins'].run_event('nav', nav, config=cfg, files=files)

    return cfg


def test_chronological(processed_config):
    data = processed_config.data

    assert 'chronological' in data
    assert len(data['chronological']) == 2

    d2019 = datetime(2019, 1, 1)
    assert d2019 in data['chronological']
    assert len(data['chronological'][d2019]) == 2

    d2020 = datetime(2020, 1, 1)
    assert d2020 in data['chronological']
    assert len(data['chronological'][d2020]) == 1


def test_ordered(processed_config):
    data = processed_config.data

    assert 'ordered' in data
    assert len(data['ordered']) == 3

    prev = datetime(1980, 1, 1)
    for entry in data['ordered']:
        page, year, month, mtime = entry
        this = datetime(year, month, 1)

        assert this >= prev
        prev = this
