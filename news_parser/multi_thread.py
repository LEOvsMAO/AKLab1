import gevent
from gevent import monkey
import itertools
from single_thread import *
import urllib2

monkey.patch_all()


def multi_thread_parse(urls):
    urls_tasks = [gevent.spawn(urllib2.urlopen(url).read, -1) for url in urls]
    gevent.joinall(urls_tasks)
    tasks = [gevent.spawn(parse_rss, url.value) for url in urls_tasks]
    gevent.joinall(tasks)
    # a = list(itertools.chain.from_iterable([ t.value for t in tasks]))
    return list(itertools.chain.from_iterable([ t.value for t in tasks]))
