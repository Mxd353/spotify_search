from bs4 import BeautifulSoup
import jieba
import requests
import re


class findKeywords():
    Keywords = []

    def __init__(self, url):
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'html.parser')
        self.findKeywords(self.saveToFile(soup.get_text()))

    def saveToFile(self, txt, filename="keywords.txt"):
        fo = open(filename, "w", encoding="utf-8")
        fo.write(txt)
        fo.close()
        return filename

    def findKeywords(self, filename):
        fo = open(filename, "r", encoding="utf-8")
        ll = fo.read()
        ll = ll.lower()
        for s in ',.\n':
            ll = ll.replace(s, ' ')
        list = ll.split()
        counts = {}
        for word in list:
            if len(word) >= 4:  # constraint length
                counts[word] = counts.get(word, 0) + 1
        sort = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        for k in sort:
            if k[1] >= 10:
                self.Keywords.append(k)
