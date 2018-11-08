#GovRptWordCloudV1.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("feiluo.jpg")
excludes = {}
f = open("zgtsshzy.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "msyh.ttc",\
                        width = 1000,\
                        height = 700,\
                        background_color = "white",\
                        mask=mask)
w.generate(txt)
w.to_file("grwordcloudf.png")
