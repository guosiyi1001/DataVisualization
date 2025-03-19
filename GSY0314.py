#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd

plt.figure()
tips = pd.read_csv('tips.csv')

# 设置字体属性
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 中文使用楷体
plt.rcParams['font.family'] = 'Times New Roman'  # 英文和数字使用Times New Roman
plt.rcParams['font.size'] = 10  # 设置字体大小适中
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

tips['tip'].plot.hist(bins=50)	#绘制直方图
tips['tip'].plot.density()		#绘制密度图


# In[44]:


# 在同一张图中叠加柱状图和折线图
fig, ax1 = plt.subplots()  # 创建图和子图轴

# 绘制柱状图
x = tips['day']  # 使用tips数据集中的'day'列作为x轴数据
y = tips['total_bill']  # 使用tips数据集中的'total_bill'列作为y轴数据
ax1.bar(x, y, color='orange', alpha=0.6, label='total_bill')
ax1.set_xlabel('day')
ax1.set_ylabel('total_bill', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# 创建第二个y轴
ax2 = ax1.twinx()

# 绘制折线图
line_x = tips['day']  # 使用tips数据集中的'day'列作为折线图x轴数据
line_y = tips['size']  # 使用tips数据集中的'size'列作为折线图y轴数据
ax2.plot(line_x, line_y, color='black', marker='o', linestyle='-', linewidth=2, label='size')
ax2.set_ylabel('size', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# 添加标题和图例
plt.title("柱状图与折线图叠加")
fig.tight_layout()  # 调整布局
plt.show()

# 在同一张图中绘制具有多个“盒子”的箱线图
plt.figure()
sns.boxplot(x='day', y='total_bill', data=tips)
plt.xlabel('day')
plt.ylabel('total_bill')
plt.title("箱线图")
plt.show()


# In[6]:


get_ipython().run_line_magic('pip', 'install seaborn')


# In[57]:


# 创建雷达图所需的角度
categories = ['总账单', '小费', '人数']
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]
ax.set_ticks(angles[:-1])  # 设置刻度位置，排除最后一个闭合点

# 准备每个子图的数据
fig, axs = plt.subplots(2, 2, figsize=(12, 10), subplot_kw=dict(polar=True))
days = ['Thur', 'Fri', 'Sat', 'Sun']

for i, day in enumerate(days):
    row = tips[tips['day'] == day]
    values = [tips['total_bill'].values[0], row['tip'].values[0], row['size'].values[0]]
    values += values[:1]  # 闭合雷达图

    # 绘制雷达图
    ax = axs[i // 2, i % 2]
    ax.plot(angles, values, color='green', linewidth=2, label=day)
    ax.fill(angles, values, color='green', alpha=0.25)
    ax.set_xticks(angles)
    ax.set_xticklabels(categories)
    ax.set_title(day)
    ax.legend(loc='upper right')

plt.tight_layout()
plt.show()


# In[32]:


# 绘制热力图，显示图例
plt.figure()
corr_matrix = tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="YlGnBu", cbar=True)
plt.title("相关性热力图")
plt.show()


# In[33]:


plt.figure()
x = tips['total_bill']
y = tips['tip']
sizes = tips['size'] * 10

plt.scatter(x, y, s=sizes, alpha=0.6, cmap='viridis')
plt.xlabel('total_bill')
plt.ylabel('tip')
plt.title("气泡图")
plt.show()


# In[29]:


# 绘制条形图
import seaborn as sns
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
tips.head()
#Seaborn条形图中的黑线是以均值为中心的置信区间，误差线
sns.barplot(x='tip_pct', y='day', data=tips, orient='h')


# In[31]:


#绘制不同分类或维度的对比图,指定row和col作为分类依据,catplot函数之前版本名字是factorplot
sns.catplot(x='day', y='tip_pct', hue='time', col='smoker', kind='bar', data=tips[tips.tip_pct < 1])


# In[15]:


sns.catplot(x='day', y='tip_pct', row='time',
               col='smoker',
               kind='bar', data=tips[tips.tip_pct < 1])


# In[16]:


sns.catplot(x='tip_pct', y='day', kind='box',
               data=tips[tips.tip_pct < 0.5])


# In[17]:


#添加网格，然后将绘图函数映射到网格上
g=sns.FacetGrid(data=tips[tips.tip_pct < 0.5],col="smoker")
g.map(plt.hist,"tip_pct")


# In[ ]:




