<<<<<<< HEAD
import requests,random,re,sys,io,time,asyncio
=======
import requests,random,re,sys,io
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
from selenium import webdriver
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
from selenium.webdriver.chrome.options import Options

class Search:
    weizhuang=["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"]
    headers={'User-agent':random.choice(weizhuang)}
    #pool = mp.Pool()
    
    def selenium_setup(self):
        driver_path=r'C:\Users\user\AppData\Local\Google\Chrome\Application\chromedriver.exe'
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        self.driver=webdriver.Chrome(driver_path,options=chrome_options)

<<<<<<< HEAD
    async def selenium_search(self,path):
        self.driver.get(path)
        await asyncio.sleep(3)
        html=self.driver.page_source
        return html

=======
    def selenium_search(self,path):
        self.driver.get(path)
        html=self.driver.page_source
        return html
    
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
    def crawl(self,url):
        html=requests.get(url,headers=self.headers)
        encode=html.apparent_encoding
        html.encoding = encode
        html=html.text
        return html

    def tearDown(self):
        print('finish')
        self.driver.quit()

<<<<<<< HEAD
    async def search(self,url_list,data_list):
=======
    def search(self,url_list,data_list):
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
        result_list=[]
        for url in url_list:
            try:
                html=self.crawl(url)
<<<<<<< HEAD
=======
                #html=self.pool.apply_async(crawl,args=(url,))
                #html=html.get()

                #print(html)
                #print(len(html))
                #print('*'*20)
                #print(html2)
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
                for i in data_list:
                    if re.search(i,html):
                        res=1
                        continue
                    elif not re.search(i,html) and html.strip()!='' and len(html)>20:
<<<<<<< HEAD
                        task=asyncio.create_task(self.selenium_search(url))
                        finished,unfinished=await asyncio.wait([task],return_when=asyncio.FIRST_COMPLETED)
                        for j in finished:
                            res_html=j.result()
                            #print(res_html)
                        #res_html=self.selenium_search(url)
=======
                        #res_html=self.pool.apply_async(selenium_search, args=(url,))
                        #res_html=res_html.get()
                        res_html=self.selenium_search(url)
                        #print(res_html)
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
                        if re.search(i,res_html):
                            res=1
                            continue
                        else:
                            res=2
                            break
                result_list.append(res)
            except:
                res=3
                result_list.append(res)
                continue
<<<<<<< HEAD

#        self.tearDown()
        return result_list

#��ȡ����
=======
        self.tearDown()
        return result_list

>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
    def search_test(self,url):
        try:
            html=self.crawl(url)
            tuple=(url,html)
            #html=self.pool.apply_async(crawl,args=(url,))
            #html=html.get()
            #print(html)
            #print(len(html))
            #print('*'*20)
            #print(html2)
        except:
            tuple=(url,'3')
        return tuple

<<<<<<< HEAD
#�Ƚ�����
=======
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
    def check_crawl(self,result_dict,data_list):
        for url,html in result_dict.items():
            for i in data_list:
                if re.search(i,html):
                    result_dict[url]='1'
                    continue

                elif not re.search(i,html) and html.strip()!='' and len(html)>20:
                    #res_html=self.pool.apply_async(selenium_search, args=(url,))
                    #res_html=self.selenium_search(url)
                    #print(res_html)
                    result_dict[url]='2'
                    break

                    '''
                    if re.search(i,res_html):
                        res=1
                        continue
                    else:
                        res=2
                        break
                    '''
        return result_dict

<<<<<<< HEAD
#selenium����
=======
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44
    def selenium(self,url):
        self.selenium_setup()
        res_html=self.selenium_search(url)
        self.tearDown()
        #print(res_html)
<<<<<<< HEAD
        return res_html

#��ȡ����
    async def search_async(self,self,url_list,data_list):
        result_dict={}
        needed_dict={}
        for url in url_list:
            try:
                html=self.crawl(url)
                for i in data_list:
                    if re.search(i,html):
                        result_dict.update({url,'1'})
                        continue
                    else:
                        result_dict.update({url,'2'})
                        needed_dict.update({url,'2'})
                    '''
                    elif not re.search(i,html) and html.strip()!='' and len(html)>20:
                        
                        task=asyncio.create_task(self.selenium_search(url))
                        finished,unfinished=await asyncio.wait([task],return_when=asyncio.FIRST_COMPLETED)
                        for j in finished:
                            res_html=j.result()
                            #print(res_html)
                        #res_html=self.selenium_search(url)
                        if re.search(i,res_html):
                            res=1
                            continue
                        else:
                            res=2
                            break
                result_list.append(res)
                '''
            except:
                result_dict.update({url,'3'})
                needed_dict.update({url,'2'})
                continue
        return result_list,needed

    async def check_manager(self,url,data_list):
        html=self.selenium_search(url)
        boolean=False
        for i in data_list:
            if re.search(i,html):
                boolean=True
                continue
            else:
                boolean=False
        if boolean��
            return url

    async def task_manager(self,needed_dict,data_list,result_dict):
        tasks=[self.check_manager(self,url,data_list) for url in needed_dict.keys()]
        finished, unfinished = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for j in finished:
            url=j.result()
            result_dict.update({url,'1'})
        
=======
        return res_html
>>>>>>> bf36c3b9f85edd3ea322cd6a23bedcaa967f6f44