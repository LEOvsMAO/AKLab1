import gevent
from gevent import monkey
import itertools
from single_thread import *
import urllib2

monkey.patch_all()


def get_urls_contents(urls):
    urls_tasks = [gevent.spawn(urllib2.urlopen(url).read, -1) for url in urls]
    # create tasks in background, which will download urls
	# in parallel
    gevent.joinall(urls_tasks)
    #wait until they're finished
    return urls_tasks


def multi_thread_parse(urls, tasks_joiner=get_urls_contents):
    urls_tasks = tasks_joiner(urls)
    # get all urls contents
    tasks = [gevent.spawn(parse_rss, url.value) for url in urls_tasks]
    # parse all pages concurrently
    gevent.joinall(tasks)
    # wait for parsing to finish
    return list(itertools.chain.from_iterable([t.value for t in tasks]))
    # transform result of each individual task
	# [[a, b, c], [d, e, f]] => [a,b,c,d,e,f]
