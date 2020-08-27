from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


from tqdm import tqdm

from urllib.request import urlretrieve





import time
import os.path


p_path = os.path.dirname( os.path.abspath( __file__ ) )
driver_path = p_path+'/setting/chromedriver'
print(driver_path)



site = input('site(ex. naver, google) : ')
keyword = input('image : ')

if site == 'naver':
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(3)
    driver.maximize_window()
    url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword)
    driver.get(url)

    body = driver.find_element_by_css_selector('body')
    for _ in range(15):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(.5)

    imgs = driver.find_elements_by_css_selector('img._img')
    links=[]

    for img in imgs:
        link = img.get_attribute('src')
        print(link)
        if 'http' in link:
            links.append(link)

    if not os.path.isdir(p_path+'/images'):
        os.mkdir(p_path+'/images')
    if not os.path.isdir(p_path+'/images/{}'.format(keyword)):
        os.mkdir(p_path+'/images/{}'.format(keyword))

    filetype = 'jpg'
    for index, link in tqdm(enumerate(links),total=len(links)):
        filename = p_path+"/images/{0}/{0}{1:03d}.{2}".format(keyword,index,filetype)
        #print("crawling {0}{1:03d}.{2}".format(keyword,index,filetype))
        urlretrieve(link,filename)
    

elif site == 'google':
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(3)
    driver.maximize_window()
    url = "https://www.google.co.kr/search?hl=ko&tbm=isch&source=hp&biw=960&bih=728&ei=s5RHX_nkB43v-QaeyqyYDg&q={}".format(keyword)
    driver.get(url)

    body = driver.find_element_by_css_selector('body')
    for _ in range(15):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(.5)

    imgs = driver.find_elements_by_class_name('rg_i')
    links=[]

    for img in imgs:
        link = img.get_attribute('src')
        if link is not None:
            links.append(link)


    if not os.path.isdir(p_path+'/images'):
        os.mkdir(p_path+'/images')
    if not os.path.isdir(p_path+'/images/{}'.format(keyword)):
        os.mkdir(p_path+'/images/{}'.format(keyword))
    
    filetype = 'jpg'
    for index, link in tqdm(enumerate(links),total=len(links)):
        filename = p_path+"/images/{0}/{0}{1:03d}.{2}".format(keyword,index,filetype)
        #print("crawling {0}{1:03d}.{2}".format(keyword,index,filetype))
        urlretrieve(link,filename)
    
time.sleep(2)
driver.quit()
