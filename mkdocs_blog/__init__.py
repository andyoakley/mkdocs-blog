__version__ = '0.1.0'

from mkdocs.plugins import BasePlugin
import os.path
import datetime


class Blog(BasePlugin):
    def parse_url(self, url):
        try:
            pieces = url.split('/')
            year = int(pieces[1])
            month = int(pieces[2])
            return (year, month)
        except ValueError:
            return None

    def on_nav(self, site_navigation, config):
        # ordered by time
        ordered = []
        # nested by year and month
        chronological = {}

        for page in site_navigation.walk_pages():
            parsed = self.parse_url(page.abs_url)
            if parsed:
                year, month = parsed

                yeartime = datetime.datetime(year, 1, 1)
                monthtime = datetime.datetime(year, month, 1)
                mtime = os.path.getmtime(page.abs_input_path)

                ordered.append((page, year, month, mtime))

                if not yeartime in chronological:
                    chronological[yeartime] = {}
                if not monthtime in chronological[yeartime]:
                    chronological[yeartime][monthtime] = {}
                chronological[yeartime][monthtime][mtime] = page

        ordered.sort(key=lambda tup: (tup[1], tup[2], tup[3]))

        config['ordered'] = ordered
        config['chronological'] = chronological

        return site_navigation

