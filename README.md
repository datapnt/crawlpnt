# CrawlPNT 🤖🕸️

**Precision Navigation Tool for Dependency-Free, AI-Ready Web Crawling**  
*A deterministic, rules-based web crawler built for scalability and structured data extraction.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/datapnt/crawlpnt/actions/workflows/tests.yml/badge.svg)](https://github.com/datapnt/crawlpnt/actions)
[![PyPI Version](https://img.shields.io/pypi/v/crawlpnt)](https://pypi.org/project/crawlpnt/)

---

## Features

- 🎯 **Rule-Based Crawling**: Define limits (`max_depth`, `max_pages`) and targets (`target_url`, `exclude_url`).
- 🚫 **Zero Dependencies**: Built entirely with Python’s standard library.
- 🤖 **Deterministic Behavior**: Configurable rules ensure predictable, repeatable crawls.
- 📂 **Structured Output**: Extract HTML content, URLs, or metadata into `.txt`, `.json`, or `.csv`.

---

## Quick Start

### Installation
```bash
pip install crawlpnt
```

### Basic Usage
```python
from crawlpnt import CrawlPNT

crawler = CrawlPNT(
    entry_urls=["https://example.com"],
    max_depth=2,
    target_url=r"^https://example\.com/blog/",
    politeness_delay=1.5,
)

crawler.run(output_dir="./data")
```

### Configuration
```yaml
# config.yml
entry_urls:
  - https://example.com
max_depth: 3
exclude_url: \.pdf$
output_format: json
```

```bash
crawlpnt --config config.yml
```

---

## Why CrawlPNT?

|                | Traditional Crawlers          | CrawlPNT                          |
|----------------|-------------------------------|------------------------------------|
| **Dependencies** | Often require Scrapy/BS4      | **Zero third-party dependencies** |
| **Focus**      | Broad coverage                | **Precision targeting**           |
| **Output**     | Raw HTML                      | **Structured, AI-ready data**     |
| **Complexity** | Steep learning curve          | **Simple YAML/CLI configuration** |

---

## Contributing

We welcome contributions! Please read our:
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

Check out the [ROADMAP](ROADMAP.md) to see our future plans and the [CHANGELOG](CHANGELOG.md) for recent updates.

---

## License

MIT License © 2025 [DataPNT](https://datapnt.com).  
*Free for open-source and commercial use.*
