import xml.etree.ElementTree as ET
import re


def find_by_tag(tag, path):
    tree = ET.parse(path)
    root = tree.getroot()
    return [item.text for item in root.findall(tag)]


def contains_score(item):
    # pattern = re.compile(r'([a-zA-Z]+)\s*-\s*([a-zA-Z]+)')

    pattern = re.compile(r'(\d+)\s*-\s*(\d+)')
    item_title = item.find('.//title')
    if not ((item_title is None) or (item_title.text is None)):
        if pattern.search(item_title.text):
            return True
    item_description = item.find('.//description')
    if not ((item_description is None) or (item_description.text is None)):
        if pattern.search(item_description.text):
            return True
    return False


def parse_rss(text):
    rss_xml = ET.fromstring(text)
    items = [txt for txt in rss_xml.findall('.//item')]
    filtered_items = [i for i in items if contains_score(i)]
    return filtered_items


def write_xml(items, path):
    sport_results = ET.Element('results')
    for i in items:
        # ET.SubElement(sport_results, 'item').insert(0, i)
        sport_results.insert(0, i)
    tree = ET.ElementTree(sport_results)
    tree.write(path)




