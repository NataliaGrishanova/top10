from collections import Counter
import json
import xml.etree.ElementTree as ET

def get_top10_json():
    with open('newsafr.json', encoding='utf-8') as f:
        json_data = json.load(f)

    news_list = json_data['rss']['channel']['items']
    top10_list = []

    for news in news_list:
        new = news['description'].split()

        for word in new:
            if len(word) > 6:
                top10_list.append(word)

    print(f'ТОП-10 самых встречающихся слов в новостях: {Counter(top10_list).most_common(10)}')


get_top10_json()


def get_top10_xml():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    top_list_xml = []

    description_list = root.findall('channel/item/description')
    for description in description_list:
        all_word = description.text.split()

        for word in all_word:
            if len(word) > 6:
                top_list_xml.append(word)

    print(f'ТОП-10 самых встречающихся слов в новостях: {Counter(top_list_xml).most_common(10)}')


get_top10_xml()
