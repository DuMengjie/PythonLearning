# ScrapImage.py
import os
import requests
url = "https://wx4.sinaimg.cn/mw690/89ebe1d1ly1fv6blh0x6yj20n014wthe.jpg"
root = "D://Media/Picture/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
