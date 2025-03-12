BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"

ROBOTSTXT_OBEY = True

FEEDS = {
    'pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 0,
}
