# Getting Started with CrawlPNT

Welcome to CrawlPNT – the **Precision Navigation Tool for Dependency-Free, AI-Ready Web Crawling**. This guide will walk you through the installation, configuration, and basic usage of CrawlPNT.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Basic Usage](#basic-usage)
  - [Running via Python Script](#running-via-python-script)
  - [Running via the Command Line](#running-via-the-command-line)
- [Configuration](#configuration)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)
- [Further Resources](#further-resources)

---

## Overview

CrawlPNT is a deterministic, rules-based web crawler designed for:
- **Precision Targeting:** Specify exact URLs or patterns to include or exclude.
- **Zero Dependencies:** Built solely with Python’s standard library.
- **Structured Output:** Easily extract data in formats like \.txt, \.json, or \.csv.

This tool is ideal if you need a lightweight crawler without the overhead of external libraries.

---

## Prerequisites

- **Python Version:** Python 3.6 or higher
- **Package Manager:** `pip` should be installed and updated.

---

## Installation

Install CrawlPNT directly from PyPI using pip:

```bash
pip install crawlpnt
```  

After installation, verify that the package is available:

```bash
python -c "import crawlpnt; print('CrawlPNT installed successfully!')"
```  

---

## Basic Usage

There are two main ways to run CrawlPNT: using a Python script or via the command line with a configuration file.

### Running via Python Script

Create a new Python file (e.g., `example.py`) with the following code:

```python
from crawlpnt import CrawlPNT

# Initialize the crawler with your desired settings
crawler = CrawlPNT(
    entry_urls=["https://example.com"],
    max_depth=2,
    target_url=r"^https://example\.com/blog/",
    politeness_delay=1.5,  # Seconds between requests
)

# Run the crawler and store the output in the specified directory
crawler.run(output_dir="./data")
```  

Run your script:

```bash
python example.py
```  

### Running via the Command Line

1. **Create a Configuration File**

   Save the following content as `config.yml`:

   ```yaml
   entry_urls:
     - https://example.com
   max_depth: 3
   target_url: "^https://example\.com/blog/"
   exclude_url: "\.pdf$"
   output_format: json
   politeness_delay: 1.5
   ```  

2. **Execute CrawlPNT with the Config File**

   Run the following command:

   ```bash
   crawlpnt --config config.yml
   ```  

   This command will load your configuration and start the crawling process accordingly.

---

## Configuration

CrawlPNT supports a YAML-based configuration file for ease of use. Here are some of the key parameters you can set:

- **entry_urls:**  
  A list of URLs where the crawler will start.  
  *Example:*
  ```yaml
  entry_urls:
    - https://example.com
  ```  

- **max_depth:**  
  The maximum number of link-hops from the entry URLs.  
  *Example:*
  ```yaml
  max_depth: 3
  ```  

- **target_url:**  
  A regular expression to specify which URLs should be crawled.  
  *Example:*
  ```yaml
  target_url: "^https://example\.com/blog/"
  ```  

- **exclude_url:**  
  A regular expression to filter out URLs from being crawled.  
  *Example:*
  ```yaml
  exclude_url: "\.pdf$"
  ```  

- **output_format:**  
  The format of the output data (`txt`, `json`, or `csv`).  
  *Example:*
  ```yaml
  output_format: json
  ```  

- **politeness_delay:**  
  Delay (in seconds) between consecutive requests to avoid overloading servers.  
  *Example:*
  ```yaml
  politeness_delay: 1.5
  ```  

---

## Advanced Usage

- **Custom Crawling Rules:**  
  Tweak the crawler's logic by modifying configuration parameters to better suit your target websites.

- **Integrating with Other Tools:**  
  Because CrawlPNT outputs structured data, you can easily integrate it with data analysis or AI processing pipelines.

- **Extending Functionality:**  
  Advanced users can fork the repository to add new features or adapt the crawler to more complex scenarios. Check our [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

## Troubleshooting

- **Installation Issues:**  
  Ensure you are using Python 3.6+ and that your `pip` is updated. Try reinstalling if you encounter errors.

- **Configuration Errors:**  
  Double-check your YAML file for correct indentation and valid regular expressions. Use an online YAML validator if needed.

- **Unexpected Crawling Behavior:**  
  Review your `max_depth`, `target_url`, and `exclude_url` settings to ensure they are configured correctly for your target website.

If you run into any issues, feel free to open an issue on our [GitHub repository](https://github.com/datapnt/crawlpnt/issues) or reach out via our community channels.

---

## Further Resources

- [Project README](../README.md) – Overview and feature list.
- [Contributing Guide](../CONTRIBUTING.md) – How to get involved.
- [Code of Conduct](../CODE_OF_CONDUCT.md) – Community guidelines.
- [Examples Directory](../examples/) – More usage examples and advanced configurations.

Happy crawling!
