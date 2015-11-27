from itertools import chain
import json
import time

from crawler import __all__ as all_crawlers
from crawler import *
all_crawlers = [globals()[crawler] for crawler in all_crawlers]

from utils import matchfile
    
while True:
    pool = []
    for match in chain(*[crawler.crawl_full() for crawler in all_crawlers]):
        pool.append(match)
        with matchfile(match) as fw:
            print(match)
            fw.write(str(match) + '\n')
    time.sleep(5)
