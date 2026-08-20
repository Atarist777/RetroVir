from pelican import signals
from datetime import date
import hashlib
from pelican import contents, signals
import logging

logger = logging.getLogger(__name__)
path_filters: set[str] = set([
    '/viruses/'
])
article_of_the_day = None

def choose_article_of_the_day(generator):

    global article_of_the_day

    # collect candidate articles
    candidates = []
    for article in generator.hidden_articles:
        # skip drafts or explicitly excluded articles
        if getattr(article, 'Status', '').lower() == 'draft':
            continue
        if getattr(article, 'Exclude_from_aotd', False):
            continue

        for path in path_filters:
            if path in str(article):
                candidates.append(article)
                break

    chosen = None
    if candidates:
        today: str = date.today().isoformat()
        site_name = generator.settings.get('SITENAME', '') or ''
        seed = (today + site_name).encode('utf-8')
        idx: int = int(hashlib.sha256(seed).hexdigest(), 16) % len(candidates)
        chosen = candidates[idx]

    article_of_the_day = chosen

    
def insert_aotd(instance) -> None:

    global article_of_the_day
    
    if type(instance) != contents.Page:
        logger.info("[aotd] Skipped: Content is not of type Page")
        return

    if instance.metadata.get('show_aotd', "").lower() == "true":
        logger.info(f"[aotd] Setting AotD variable for {instance.metadata}")
        instance.article_of_the_day =  article_of_the_day


def register() -> None:
    signals.article_generator_finalized.connect(choose_article_of_the_day)
    signals.content_object_init.connect(insert_aotd)
