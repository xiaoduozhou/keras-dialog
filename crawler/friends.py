#-*- coding:utf-8 -*-

"""
Fetched from https://en.m.wikiquote.org/wiki/Friends_(TV_series)
author: duzhikang
"""

import requests
from bs4 import BeautifulSoup


def crawl_dialogs(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    titles = soup.find_all('h3', 'section-heading')
    contents = soup.find_all('div', 'collapsible-block')
    all_titles = []
    all_dialogs = []
    for i in range(len(titles)):
        title = titles[i].find('span', 'mw-headline').text
        all_titles.append(title)

        dls = contents[i].find_all('dl')
        dialogs = []
        for dl in dls:
            dds = dl.find_all('dd')
            dd_t = []
            for dd in dds:
                if dd.find('b'):
                    dd_t.append(dd.text)
                else:
                    dd_t.append('Narrator: ' + dd.text)
            dialogs.append(dd_t)
        all_dialogs.append(dialogs)
    return all_titles, all_dialogs


def write_to_file(filename, titles, dialogs, cnt_scene):
    with open(filename, 'a', encoding='utf-8') as f:
        for j in range(len(titles)):
            f.write('Scene #' + str(cnt_scene) + '\n')
            f.write('Title: ' + titles[j] + '\n\n')
            dialog = dialogs[j]
            cnt_dialog = 1
            for dl in dialog:
                f.write('Dialog #' + str(cnt_dialog) + '\n')
                for x in dl:
                    f.write(x + '\n')
                f.write('\n')
                cnt_dialog += 1
            cnt_scene += 1
    return cnt_scene

if __name__ == '__main__':
    url = 'https://en.m.wikiquote.org/wiki/Friends_(season_{})'
    cnt_scene = 1
    for i in range(1, 11):
        titles, dialogs = crawl_dialogs(url.format(i))
        cnt_scene = write_to_file('friends.txt', titles, dialogs, cnt_scene)
        print('Done, url: ' + url.format(i))
    print('Total Scenes: %d' % cnt_scene)
