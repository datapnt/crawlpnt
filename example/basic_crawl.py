#!/usr/bin/env python3
"""
Basic Usage Example for CrawlPNT

This script demonstrates how to use the CrawlPNT package to perform a simple web crawl.
"""

from crawlpnt import CrawlPNT

def main():
    # Define the starting URL(s) for the crawler.
    entry_urls = ["https://example.com"]

    # Initialize the CrawlPNT instance with your desired configuration.
    crawler = CrawlPNT(
        entry_urls=entry_urls,
        max_depth=2,
        target_url=r"^https://example\.com/blog/",
        politeness_delay=1.5,  # Delay in seconds between consecutive requests
    )

    # Run the crawler. The results will be saved to the specified output directory.
    crawler.run(output_dir="./data")

    print("Crawl completed. Check the './data' directory for the output.")

if __name__ == "__main__":
    main()
