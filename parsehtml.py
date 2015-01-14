# encoding=utf8
from BeautifulSoup  import BeautifulSoup

import sys
reload(sys) 
sys.setdefaultencoding('utf8')
import re
import string

def ExtractReAll(rule):
    def ConcreteExtractAll(s):
        mList = list(rule[0].finditer(s))
        return "".join([m.group(rule[1]) for m in mList])
    return ConcreteExtractAll
TITLE_RULE = re.compile('>([^<>]*?)<',re.IGNORECASE|re.DOTALL|re.LOCALE|re.M)

def readFile(name = ''):
    name = '22'
    f = open(name,'r')
    text = f.read()
    f.close()
    return text

def parseHtml():
    content = readFile()
    soup = BeautifulSoup(content,fromEncoding="gb2312")
    tb =  soup.findAll('table',attrs={'style':'BORDER-COLLAPSE: collapse'})
    for item in  tb[0].findAll('tr'):
        tds = item.findAll('td')
        st = ""
        for td in tds:
             td_text = ExtractReAll((TITLE_RULE,1))(str(td))
             if str != '':
                 st = st + '\t' + td_text
             else:
                 st = td_text
        print st
    

if __name__ == "__main__":
    parseHtml()
