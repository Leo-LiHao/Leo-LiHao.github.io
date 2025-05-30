# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Hao Li's academic personal website built with Jekyll using the "Academic Pages" template. It's a static site generator for creating academic portfolio websites with support for publications, talks, teaching, and CV management.

## Development Commands

### Local Development
```bash
# Install Ruby dependencies
bundle install

# Serve site locally with live reload
jekyll serve -l -H localhost
# Alternative with bundle exec
bundle exec jekyll serve -l -H localhost

# Build JavaScript assets
npm run build:js
npm run watch:js  # Watch for changes
```

### Docker Development
```bash
# Run site in Docker container
docker compose up
# Site will be available at localhost:4000
```

### Content Generation
```bash
# Convert markdown CV to JSON format
./scripts/update_cv_json.sh

# Generate publication/talk pages from TSV files
cd markdown_generator
python3 publications.py  # Generate from publications.tsv
python3 talks.py         # Generate from talks.tsv
```

## Architecture

### Jekyll Collections Structure
- `_publications/` - Academic papers with PDF/BibTeX links
- `_talks/` - Conference presentations and talks  
- `_teaching/` - Teaching experience entries
- `_portfolio/` - Project portfolio items
- `_posts/` - Blog posts (standard Jekyll)
- `_pages/` - Static pages (about, CV, etc.)

### Content Management
- **Publications**: Individual markdown files in `_publications/` with YAML frontmatter
- **Files**: PDFs and BibTeX files stored in `files/` directory
- **CV Dual Format**: Maintain both `_pages/cv.md` (markdown) and `_data/cv.json` (structured data)

### Theme Architecture
- **Base**: Academic Pages theme (fork of Minimal Mistakes)
- **Styling**: Modular SCSS in `_sass/` with theme variants (default/dark)
- **JavaScript**: Minified bundle with jQuery, plugins, and custom scripts

### Configuration
- `_config.yml` - Main site configuration (author info, collections, SEO)
- `_config_docker.yml` - Docker-specific overrides
- `_data/cv.json` - Structured CV data (auto-generated from markdown)

## Content Workflows

### Adding Publications
1. Create markdown file in `_publications/` with YAML frontmatter
2. Add PDF and BibTeX files to `files/` directory
3. Reference files in frontmatter: `paperurl`, `citation`

### Bulk Content Generation
1. Edit TSV files in `markdown_generator/` (publications.tsv, talks.tsv)
2. Run corresponding Python scripts to generate markdown files
3. Review and commit generated files

### CV Management
1. Edit primary CV in `_pages/cv.md`
2. Run `./scripts/update_cv_json.sh` to generate JSON version
3. JSON version enables alternative CV layouts and export formats

## Key Files
- `_config.yml` - Site configuration and author profile
- `_pages/about.md` - Homepage with research focus
- `scripts/cv_markdown_to_json.py` - CV format converter
- `markdown_generator/` - Bulk content generation tools

## Deployment
Site auto-deploys to GitHub Pages from master branch. No manual build process required for production.