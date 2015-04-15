from news_parser.single_thread import *
import urllib2
from news_parser.multi_thread import *
from time import time

file_path = "/Users/aleksejfilobok/PycharmProjects/untitled2/sportnews.xml"

final_res = []
urls = find_by_tag('url', file_path)
t0 = time()
for url in urls:
    obj = urllib2.urlopen(url)
    byte_arr = obj.read(-1)
    temp = parse_rss(byte_arr)
    final_res.extend(temp)
t1 = time()
write_xml(final_res, "single_thread.xml")
t2 = time()
results = multi_thread_parse(urls)
t3 = time()
write_xml(results, "multi_thread.xml")
print(t1 - t0)
print(t3-t2)