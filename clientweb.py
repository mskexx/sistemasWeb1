#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple client web per descarregar de udl.cat

@author: marcos.susin.mzn@gmail.com
'''
import urllib2
import bs4

class Client(object):

    def get_webpage(self, page):
        """ obtener plano web """
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    def search_data(self, html):
        """ buscar datos """
        bs = bs4.BeautifulSoup(html, "lxml")
        caixa = bs.find("div", "sg-featuredlink")
        items = caixa.find_all("div", "featured-links-item")
        results = []
        
        for item in items:
            time = item.find('time')["datetime"]
            text = item.find('span', 'flink-title').text
            results.append((time, text))

        return results


    def main(self):
        webpage = self.get_webpage('http://www.udl.cat')
        results = self.search_data(webpage)

        print results
        print len(results)
        # imprimir resultados

if __name__ == "__main__":
    cw = Client()
    cw.main()
