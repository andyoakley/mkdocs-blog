import feedparser
import os.path

def test_rss(mkdocs_site, tmpdir):
    path = os.path.join(
        tmpdir,
        'rss.xml'
    )

    feed = feedparser.parse(path)

    assert feed.bozo == 0
    assert len(feed.entries) == 3
