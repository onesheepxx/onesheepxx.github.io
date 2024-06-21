#加载情感分析模块
from snownlp import SnowNLP
#from snownlp import sentiment
import pandas as pd
import matplotlib.pyplot as plt
#导入数据
aa ="Swigo\comments\choupchg.xlsx"
#读取文本数据
df=pd.read_excel(aa)
#提取所有数据
df1=df.iloc[:,0]
#遍历每条评论进行预测
values=[SnowNLP(i).sentiments for i in df1]
#输出积极的概率，大于0.5积极的，小于0.5消极的
#myval保存预测值
myval=[]
good=0
bad=0
for i in values:
   if (i>=0.5):
       myval.append("正面")
       good=good+1
   else:
       myval.append("负面")
       bad=bad+1
df['预测值']=values
df['评价类别']=myval

rate=good/(good+bad)

# 计算图表的显示范围，以便确定好评率文本的位置
y_min, y_max = min(values), max(values)
y_text_pos = y_max # 假设好评率文本放在图表底部上方10%的高度位置

# 作图
y=values
plt.rc('font', family='SimHei', size=10)
plt.plot(y, marker='o', mec='#558B2F', mfc='w', color='#9CCC65', label=u'评价分值')

# 添加好评率文本到图表
plt.text(270, y_text_pos, f'好评率：{rate*100:.1f}%', fontsize=12, ha='center', va='center', color='black') 

plt.xlabel('用户')
plt.ylabel('评价分值')

plt.title('臭屁醋火锅评价情感分析', family='SimHei', size=14)
plt.savefig('Swigo\comments\臭屁醋火锅评价情感分析.png')
plt.show()
