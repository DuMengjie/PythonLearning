# ScrapJDItem.py
import requests
url = "https://www.amazon.cn/dp/B07J35QDDP/ref=pd_sbs_14_1?_encoding=UTF8&pd_rd_i=B07J35QDDP&pd_rd_r=efbad784-e0d7-11e8-a0d9-c57af29329d8&pd_rd_w=EBojS&pd_rd_wg=2af62&pf_rd_i=desktop-dp-sims&pf_rd_m=A1AJ19PSB66TGU&pf_rd_p=2d9f2e80-85a0-476d-89d7-9e61ddceb885&pf_rd_r=PJX7PJTESK3RGVHXFZ33&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=PJX7PJTESK3RGVHXFZ33"
try:
    r = requests.get(url)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")