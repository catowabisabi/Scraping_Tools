import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

request = urllib.request.Request(url = url, headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

from lxml import etree

tree = etree.HTML(content)

result = tree.xpath('//input[@id = "su"]/@value')[0]

print(result)