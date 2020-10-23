import requests
from lxml import etree
import csv
import json
import random
from selenium import webdriver
import re
import string
import pymysql

class newsdown:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",user="root",password="root",database="garbage_classification",charset="utf8")
        self.urls = [#"http://www.ljflw.cn/news/list.php?catid=61&page=1",
        "http://www.ljflw.cn/news/list.php?catid=61&page=2"
        ]
        useragents = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {'User-Agent':random.choice(useragents)}
    def Get_name(self,url):
        response = requests.get(url,headers=self.headers)
        return response.text
    def getxp(self,baselib):
        content = etree.HTML(baselib)
        hrefs1 = []
        times1 = []
        titles1 = []
        for icc in range(1,24):
            if icc%6 == 0:
                continue
            else:
                name = content.xpath("/html/body/div[9]/div[1]/div/ul/li["+str(icc)+"]//text()")
                time1 = str(name) 
                time = time1[2:18]
                times1.append(time)
                title = time1[22:-2]
                titles1.append(title)
                href1 = content.xpath("/html/body/div[9]/div[1]/div/ul/li["+str(icc)+"]//@href")
                hrefs1.append(href1)
        return [times1,titles1,hrefs1]
    def get_imgurl(self,fhrfs,i,imgurls):
        response1 = requests.get(fhrfs[i],headers=self.headers)
        texturlt = response1.text
        content1 = etree.HTML(texturlt)
        #text1 = content1.xpath('/html/body/div[9]/div[1]/div[2]/text()')
        #text2 = content1.xpath('//*[@class="content"]//span/text()')
        #text3 = content1.xpath('//*[@id="content"]//p/text()')
        #atext = str(text1)+'\n'+str(text2)+'\n'+str(text3)
            #print(atext)
            #print('\n')
            #print('\n')
            #print('\n')
        img1 = content1.xpath('//*[@id="article"]/p/img/@src')
        imgurl = str(img1)[1:-1]
        e22 = imgurl.split(",")
        imgurl2 = str(e22)[1:-1]
        if len(imgurl2) == 0 :
            imgurl2 = 1
            imgurls.append(imgurl2)
        else:
            imgurls.append(imgurl2)
        #print(e22[0])
        return imgurls
    def get_text(self,fhrfs,i,ftexts):
        response1 = requests.get(fhrfs[i],headers=self.headers)
        texturlt = response1.text
        content1 = etree.HTML(texturlt)
        text1 = content1.xpath('/html/body/div[9]/div[1]/div[2]/text()')
        text2 = content1.xpath('//*[@class="content"]//span/text()')
        text3 = content1.xpath('//*[@id="content"]//p/text()')
        atext = str(text1)+'\n'+str(text2)+'\n'+str(text3)
        b1 = atext.replace('[', '')
        c1 = b1.replace(']', '')
        d1 = c1.replace('"', '')
        e11 = d1.replace(',', '')
        ftexts.append(e11)
            #print(atext)
            #print('\n')
            #print('\n')
            #print('\n')
        #img1 = content1.xpath('//*[@id="article"]/p/img/@src')
        #imgurl = str(img1)
        #imgurls.append(imgurl)
        return ftexts
        
            
    
    def run(self):
        imgurls = []
        ftexts = []
        hrefs = []
        times = []
        titles = []
        types = []
        for i in range(len(self.urls)):
            url = self.urls[i]
            baselib = self.Get_name(url)
            gets11 = self.getxp(baselib)
            #print(gets11[2])
            hrefs.append(gets11[2])
            times.append(gets11[0])
            titles.append(gets11[1])
        #print(hrefs)
        strhfs = str(hrefs)
        b = strhfs.replace('[', '')
        c = b.replace(']', '')
        d = c.replace('"', '')
        e = d.split(",")
        #print(e)
        strhfs1 = str(times)
        b1 = strhfs1.replace('[', '')
        c1 = b1.replace(']', '')
        d1 = c1.replace('"', '')
        e1 = d1.split(",")
        #print(e1)
        strhfs2 = str(titles)
        b2 = strhfs2.replace('[', '')
        c2 = b2.replace(']', '')
        d2 = c2.replace('"', '')
        e2 = d2.split(",")
        #print(e2)
        fhrfs = []
        ftimes = []
        ftitles = []
        for i in range(len(e1)):
            if i == 0 :
                time1 = e1[i][1:-1]
                ftimes.append(time1)
            else:
                time1 = e1[i][2:-1]
                ftimes.append(time1)
        for i in range(len(e)):
            if i == 0 :
                href1 = e[i][1:-1]
                fhrfs.append(href1)
            else:
                href1 = e[i][2:-1]
                fhrfs.append(href1)
        for i in range(len(e2)):
            title1 = e2[i][2:-1]
            ftitles.append(title1)
        cursor = self.db.cursor()
        for i in range(len(e)):
            type1 = str("政策法规")
            types.append(type1)
        for i in range(len(e)):
            #urls = 
            self.get_imgurl(fhrfs,i,imgurls)
            self.get_text(fhrfs,i,ftexts)

        
            sql = """INSERT INTO news(imgurl,
            time,title,text,type)
            VALUES (%s,'%s', '%s',%s,'%s')"""% \
            (imgurls[i], ftimes[i],ftitles[i],ftexts[i],types[i])
            try:
                    # 执行sql语句
                cursor.execute(sql)
                        # 提交到数据库执行
                self.db.commit()
                print("1")
                
            except:
                    # 如果发生错误则回滚
                self.db.rollback()
        #print(fhrfs)
        #print(ftimes)
        #print(ftitles)
        #print(imges)
        #print(textes)
        self.db.close()

        


yunxing = newsdown()
yunxing.run()