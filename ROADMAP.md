# CrawlPNT Roadmap 🗺️

This document outlines the development roadmap for CrawlPNT, a deterministic, rules-based web crawler designed for AI-ready data extraction. We follow [Semantic Versioning](https://semver.org/) and prioritize backward compatibility, transparency, and community input.

---

## Current Status: **v0.1.0** (Core Engine)  
*Released: Feb 2025*  

**Focus**: Establish foundational crawling with configurable limits and targets.  

### Features Included:
✅ **Crawl Limits**  
- `max_depth` (maximum link depth from seed URLs)  
- `max_pages` (total pages to crawl)  
- `rate_limit` (requests/second)  
- `politeness_delay` (seconds between domain requests)  

✅ **Crawl Targets**  
- `target_depth` (only crawl pages at this depth)  
- `target_url` (regex pattern for URL matching)  
- `exclude_url` (regex for URLs to skip)  

✅ **Output**  
- Save crawled URLs to `urls.txt`  
- Basic HTML content extraction  

---

## Upcoming Releases  

### v0.2.0 - Advanced Targeting & Validation  
**Planned: [Month] [Year]**  
- **New Limits**: `max_content_size`, `allowed_domains`, `retry_attempts`.  
- **New Targets**: `target_content_type`, `target_status_codes`, `target_language`.  
- **Validation**: Auto-respect `robots.txt`, User-Agent rotation.  

### v0.3.0 - Structured Data Extraction  
**Planned: [Quarter] [Year]**  
- **Extraction Rules**: CSS/XPath selectors, regex patterns, metadata extraction.  
- **Output Formats**: JSON, CSV, SQLite.  
- **Persistence**: Resume crawls via `checkpoint_file`.  

### v0.4.0 - Optimization & Observability  
**Planned: [Quarter] [Year]**  
- **Parallelism**: Thread/process-based crawling.  
- **Observability**: Progress bar, logging, stats dashboard.  
- **Memory Management**: Stream results to disk.  

---

## Future Milestones  

| Version   | Focus Area                   | Key Features                                  |  
|-----------|------------------------------|-----------------------------------------------|  
| `v0.5.0`  | Extensions & Hooks           | Plugin system, proxy support, custom caching. |  
| `v0.6.0`  | Documentation & Community    | Full API docs, tutorials, Discord community.  |  
| `v1.0.0`  | Stable Release               | 100% test coverage, LTS branch, security audit. |  

---

## Versioning Principles  

| Type     | Description                                                                 | Example          |  
|----------|-----------------------------------------------------------------------------|------------------|  
| `MAJOR`  | Breaking changes (reset MINOR/PATCH to 0).                                  | `1.0.0` → `2.0.0`|  
| `MINOR`  | Backward-compatible features (reset PATCH to 0).                            | `0.1.0` → `0.2.0`|  
| `PATCH`  | Backward-compatible bug fixes.                                              | `0.1.0` → `0.1.1`|  

**Backward Compatibility**:  
- Deprecated features will be flagged for two minor versions before removal.  
- Breaking changes will only occur in `MAJOR` versions.  

---

## How to Contribute  
1. **Suggest Features**: Open a [GitHub Issue](https://github.com/datapnt/crawlpnt/issues) with the `enhancement` label.  
2. **Vote on Priorities**: React to existing issues to signal demand.  
3. **Join Development**: Follow our [Contributing Guide](CONTRIBUTING.md).  

---

**View Changelog**: [CHANGELOG.md](CHANGELOG.md)  
**Latest Stable Release**: [v0.1.0](https://github.com/datapnt/crawlpnt/releases/tag/v0.1.0)  
**License**: [MIT](LICENSE)  
