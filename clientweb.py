#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple client web per descarregar de udl.cat

@author: marcos.susin.mzn@gmail.com
'''
import urllib2

class Client(object):

    def get_webpage(self, page):
        ''' obtener plano web '''
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage


    def main(self):
        webpage = self.get_webpage('http://www.udl.cat')

        print webpage
        # buscar datos
        # imprimir resultados

if __name__ == "__main__":
    cw = Client()
    cw.main()
