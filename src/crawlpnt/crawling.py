"""
crawling.py

Core implementation of CrawlPNT – a deterministic, rules-based web crawler.
Built solely with Python’s standard library.
Version: 0.1.0
"""

import re
import time
import os
import json
import csv
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    """
    A simple HTML parser that extracts URLs from anchor tags.
    """
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            for attr, value in attrs:
                if attr.lower() == "href":
                    self.links.append(value)

class Crawler:
    """
    A deterministic, rules-based web crawler.

    Parameters:
        entry_urls (list or str): The starting URL(s) for the crawl.
        max_depth (int): Maximum number of link-hops from the entry URL(s).
        target_url (str): A regular expression to filter URLs that should be crawled.
                          Only URLs matching this pattern will be considered.
        politeness_delay (float): Seconds to wait between requests.
        user_agent (str): The User-Agent header to use for requests.
        output_format (str): Format of the output file. Options: "txt", "json", "csv".
    """
    def __init__(self, entry_urls, max_depth=2, target_url=None, politeness_delay=1.0, user_agent="CrawlPNT", output_format="txt"):
        if isinstance(entry_urls, str):
            self.entry_urls = [entry_urls]
        else:
            self.entry_urls = entry_urls
        self.max_depth = max_depth
        self.target_url = re.compile(target_url) if target_url else None
        self.politeness_delay = politeness_delay
        self.user_agent = user_agent
        self.output_format = output_format
        self.visited = set()
        self.found_urls = set()

    def fetch_page(self, url):
        """
        Fetches the HTML content of the given URL.
        Returns:
            A string containing the HTML content or an empty string if an error occurs.
        """
        try:
            req = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
            with urllib.request.urlopen(req) as response:
                content_type = response.getheader("Content-Type", "")
                if "text/html" in content_type:
                    return response.read().decode("utf-8", errors="ignore")
        except Exception as e:
            print(f"Error fetching {url}: {e}")
        return ""

    def extract_links(self, html, base_url):
        """
        Extracts and returns a list of absolute URLs found in the HTML content.

        Parameters:
            html (str): The HTML content as a string.
            base_url (str): The base URL used to resolve relative links.

        Returns:
            A list of absolute URLs.
        """
        parser = LinkParser()
        parser.feed(html)
        links = []
        for link in parser.links:
            # Resolve relative URLs.
            absolute_link = urllib.parse.urljoin(base_url, link)
            # Consider only HTTP and HTTPS URLs.
            if absolute_link.startswith("http"):
                links.append(absolute_link)
        return links

    def crawl(self):
        """
        Executes the crawling process using a breadth-first strategy.
        Returns:
            A list of visited URLs.
        """
        queue = [(url, 0) for url in self.entry_urls]
        while queue:
            url, depth = queue.pop(0)
            if url in self.visited:
                continue
            self.visited.add(url)
            print(f"Crawling: {url} (depth: {depth})")
            html = self.fetch_page(url)
            if html:
                new_links = self.extract_links(html, url)
                for link in new_links:
                    # If a target_url pattern is specified, only add matching URLs.
                    if self.target_url and not self.target_url.search(link):
                        continue
                    if link not in self.visited and depth < self.max_depth:
                        queue.append((link, depth + 1))
                    self.found_urls.add(link)
            time.sleep(self.politeness_delay)
        return list(self.visited)

    def run(self, output_dir):
        """
        Runs the crawler and writes the visited URLs to a file in the specified output format.
        The file is saved in the output_dir with a name based on the output format:
            - txt: crawled.txt
            - json: crawled.json
            - csv: crawled.csv
        Returns the list of visited URLs.
        """
        visited = self.crawl()
        os.makedirs(output_dir, exist_ok=True)
        if self.output_format == "txt":
            filename = os.path.join(output_dir, "crawled.txt")
            with open(filename, "w", encoding="utf-8") as f:
                for url in visited:
                    f.write(url + "\n")
        elif self.output_format == "json":
            filename = os.path.join(output_dir, "crawled.json")
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(visited, f, indent=2)
        elif self.output_format == "csv":
            filename = os.path.join(output_dir, "crawled.csv")
            with open(filename, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                for url in visited:
                    writer.writerow([url])
        else:
            raise ValueError(f"Unsupported output format: {self.output_format}")
        return visited
