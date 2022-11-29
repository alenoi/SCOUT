from proxyscrape import create_collector
from selenium import webdriver
def jsonFindAttr(attr: str, jsonData):
    for k, v in jsonData.items():
        if k == attr:
            yield v
        elif isinstance(v, dict):
            for id_val in jsonFindAttr(attr, v):
                yield id_val

def getProxy():
    collector = create_collector('my-collector', 'http')
    proxy = collector.get_proxy()
    print(proxy)
    return f'{proxy.host}:{proxy.port}'

def openUrl(url: str):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    print(driver.page_source)
    return driver

openUrl("https://vm.tiktok.com/ZMFuB9Vk2/")