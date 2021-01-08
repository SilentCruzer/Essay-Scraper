import bs4,requests,pyperclip,time
from googlesearch import search 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

  
def get_content(query): 
    content = ''
    for link in search(query, tld="co.in", num=5, stop=5, pause=2): 
        res = requests.get(link+'?action=render')
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        paragraph = soup.select("p")
        url_para = ''
        for para in paragraph:
            if len(url_para)<5000:
                url_para += para.text
            else:
                content += url_para
                break
    return content

def summarize(content):
    browser = webdriver.Chrome()
    browser.get("https://resoomer.com/en/")
    enter_text = browser.find_element_by_name("contentText")
    enter_text.click()
    enter_text.send_keys(content)
    scroll = browser.find_element_by_class_name('page-scroll')
    scroll.click() 
    convert = browser.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[1]/div/form/fieldset/div/div[1]/div/ul/li[2]/input")
    browser.execute_script("arguments[0].click();", convert)

    time.sleep(10)

    doc = browser.find_element_by_css_selector("#contentTexteResoomer_3 > p > a:nth-child(4)")
    browser.execute_script("arguments[0].click();", doc)
    time.sleep(10)
    print('Downloaded essay')
    browser.close()



query = input("Enter the topic: ")
content = get_content(query)
summarize(content)


