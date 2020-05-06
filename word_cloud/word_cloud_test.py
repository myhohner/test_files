#https://www.cnblogs.com/wkfvawl/p/11585986.html
import jieba
from wordcloud import WordCloud

# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio
import io,sys
mk = imageio.imread(r"C:\Users\user\Desktop\test_files\word_cloud\America.jpg")#图片尽量小否则溢出

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# 从外部.txt文件中读取大段文本，存入变量txt中
with open(r'C:\Users\user\Desktop\test_files\word_cloud\test.txt','r+') as f:
    txt= f.read()
res=jieba.lcut(txt)
string=' '.join(res)

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = WordCloud(width=5000,height=350,background_color='white',font_path='simhei.ttf',mask=mk,scale=20) #增加清晰度,字体是电脑中的字体


# 将txt变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file(r'C:\Users\user\Desktop\test_files\word_cloud\output3-sentence.png')
