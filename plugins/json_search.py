# plugins/json_search.py
from pelican import signals
import json
import os
import logging

logger = logging.getLogger(__name__)

def generate_search_index(generator, writer=None):
    logger.info("Generating search index...")
    articles = []
    for article in generator.articles:
        tags = []
        if hasattr(article, 'tags') and article.tags is not None:
            try:
                tags = [tag.name for tag in article.tags]
            except (TypeError, AttributeError):
                tags = []
        articles.append({
            'title': article.title,
            'url': article.url,
            'summary': article.summary,
            'content': article.content,
            'date': str(article.date),
            'category': article.category.name if article.category else '',
            'tags': tags
        })
    search_data = {
        'articles': articles,
        'site_url': generator.settings.get('SITEURL', '')
    }
    output_path = generator.output_path
    file_path = os.path.join(output_path, 'search_index.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(search_data, f, ensure_ascii=False, indent=2)
    logger.info(f"Search index written to {file_path}")

def register():
    signals.article_writer_finalized.connect(generate_search_index)