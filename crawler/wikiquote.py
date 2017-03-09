#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

def quote_without_title(url, series, filename):
    cnt_dialog = 1
    for i in range(1, series + 1):
        r = requests.get(url.format(i))
        soup = BeautifulSoup(r.content, 'lxml')
        with open(filename, 'a', encoding='utf-8') as f:
            for x in soup.find_all('dl'):
                f.write('Dialog #' + str(cnt_dialog) + '\n')
                cnt_dialog += 1
                for y in x.find_all('dd'):
                    text = y.text
                    if ':' not in text:
                        text = 'Narrator: ' + text
                    f.write(text + '\n')
                f.write('\n')

if __name__ == '__main__':
    # url_thrones = 'https://en.m.wikiquote.org/wiki/Game_of_Thrones/Season_{}'
    # quote_without_title(url_thrones, 6, 'game_of_thrones_no_title.txt')
    url_friends = 'https://en.m.wikiquote.org/wiki/Friends_(season_{})'
    quote_without_title(url_friends, 10, 'friends_no_title.txt')
