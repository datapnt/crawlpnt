import unittest
import os
import json
import csv
import tempfile
from crawlpnt.crawling import Crawler

class DummyCrawler(Crawler):
    """
    A dummy crawler that uses predefined HTML pages instead of making real HTTP requests.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define a mapping of URLs to HTML content for testing.
        self.test_pages = {
            "http://example.com": (
                '<html><body>'
                '<a href="/page1">Page 1</a>'
                '<a href="/page2">Page 2</a>'
                '</body></html>'
            ),
            "http://example.com/page1": (
                '<html><body>'
                '<a href="/page3">Page 3</a>'
                '</body></html>'
            ),
            "http://example.com/page2": (
                '<html><body>No links here</body></html>'
            ),
            "http://example.com/page3": (
                '<html><body>'
                '<a href="http://example.com">Home</a>'
                '</body></html>'
            ),
        }

    def fetch_page(self, url):
        """
        Returns predefined HTML content based on the URL.
        """
        return self.test_pages.get(url, "")

class TestCrawler(unittest.TestCase):
    def test_crawl(self):
        # Create a DummyCrawler instance to avoid external HTTP requests.
        crawler = DummyCrawler(
            entry_urls=["http://example.com"],
            max_depth=2,
            target_url="^http://example\\.com"
        )
        result = crawler.crawl()
        expected = {
            "http://example.com",
            "http://example.com/page1",
            "http://example.com/page2",
            "http://example.com/page3",
        }
        self.assertEqual(set(result), expected)

    def test_run_output_txt(self):
        crawler = DummyCrawler(
            entry_urls=["http://example.com"],
            max_depth=2,
            target_url="^http://example\\.com",
            output_format="txt",
            politeness_delay=0  # Set delay to 0 for tests
        )
        with tempfile.TemporaryDirectory() as tmpdirname:
            visited = crawler.run(tmpdirname)
            filepath = os.path.join(tmpdirname, "crawled.txt")
            self.assertTrue(os.path.exists(filepath))
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().splitlines()
            self.assertEqual(set(content), set(visited))

    def test_run_output_json(self):
        crawler = DummyCrawler(
            entry_urls=["http://example.com"],
            max_depth=2,
            target_url="^http://example\\.com",
            output_format="json",
            politeness_delay=0
        )
        with tempfile.TemporaryDirectory() as tmpdirname:
            visited = crawler.run(tmpdirname)
            filepath = os.path.join(tmpdirname, "crawled.json")
            self.assertTrue(os.path.exists(filepath))
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertEqual(set(data), set(visited))

    def test_run_output_csv(self):
        crawler = DummyCrawler(
            entry_urls=["http://example.com"],
            max_depth=2,
            target_url="^http://example\\.com",
            output_format="csv",
            politeness_delay=0
        )
        with tempfile.TemporaryDirectory() as tmpdirname:
            visited = crawler.run(tmpdirname)
            filepath = os.path.join(tmpdirname, "crawled.csv")
            self.assertTrue(os.path.exists(filepath))
            urls_from_csv = []
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        urls_from_csv.append(row[0])
            self.assertEqual(set(urls_from_csv), set(visited))

if __name__ == '__main__':
    unittest.main()
