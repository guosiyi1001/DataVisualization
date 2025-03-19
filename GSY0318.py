#!/usr/bin/env python
# coding: utf-8

# In[21]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['Kai Ti']  
plt.rcParams['font.family'] = 'Times New Roman'  
plt.rcParams['font.size'] = 10  
plt.rcParams['axes.unicode_minus'] = False   

# 1. 在同一张图中叠加柱状图和折线图
def plot_bar_line():
    data = {'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
            'Sales Volume': [120, 150, 180, 200],
            'Profit': [20, 30, 35, 40]}
    df = pd.DataFrame(data)

    fig, ax1 = plt.subplots()  

    ax1.bar(df['Quarter'], df['Sales Volume'], color='palegoldenrod', alpha=0.6, label='Sales Volume')
    ax1.set_xlabel('Quarter')
    ax1.set_ylabel('Sales Volume', color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    ax2 = ax1.twinx()

    ax2.plot(df['Quarter'], df['Profit'], color='steelblue', marker='o', linestyle='-', linewidth=2, label='Profit')
    ax2.set_ylabel('Profit', color='black')
    ax2.tick_params(axis='y', labelcolor='black')

    plt.title("Chart of sales and profit trends")
    fig.tight_layout()
    plt.show()

plot_bar_line()


# In[19]:


# 2. 在同一张图中绘制具有多个“盒子”的箱线图
def plot_boxplot():
    data = {'Mark': [65, 70, 75, 80, 85, 90, 55, 60, 65, 70, 75, 80, 85, 90, 95],
            'Course': ['Maths', 'Maths', 'Maths', 'Maths', 'Maths', 'Maths', 'Chinese', 'Chinese', 'Chinese', 'Chinese', 'Chinese', 'Chinese', 'English', 'English', 'English']}
    df = pd.DataFrame(data)

    plt.figure()
    sns.boxplot(x='Course', y='Mark', data=df)
    plt.xlabel('Course')
    plt.ylabel('Mark')
    plt.title("Box chart of score distribution for each course")
    plt.show()

plot_boxplot()


# In[14]:


# 3. 使用“子图”（subplots）绘制多个雷达图
labels = ['Sales Volume', 'Profit', 'Cost', 'Market share']
values1 = [80, 70, 60, 90]
values2 = [70, 80, 75, 85]
values3 = [60, 65, 70, 75]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

fig, axs = plt.subplots(1, 3, figsize=(15, 5), subplot_kw=dict(polar=True))

def plot_radar(ax, values, title):
    ax.plot(angles, values, color='b', linewidth=2, label='Index')
    ax.fill(angles, values, color='b', alpha=0.25)
    ax.set_xticks(angles)  # 设置刻度位置
    ax.set_xticklabels(labels)  # 设置刻度标签
    ax.set_title(title)
    ax.legend(loc='upper right')

plot_radar(axs[0], values1, 'Company A')
plot_radar(axs[1], values2, 'Company B')
plot_radar(axs[2], values3, 'Company C')

plt.show()  


# In[17]:


# 4. 绘制热力图，显示图例
def plot_heatmap():
    data = {'Monday': [30, 25, 20],
            'Tuesday': [35, 30, 25],
            'Wednesday': [40, 35, 30],
            'Thursday': [45, 40, 35],
            'Friday': [50, 45, 40]}
    df = pd.DataFrame(data, index=['Product A', 'Product B', 'Product C'])

    plt.figure()
    sns.heatmap(df, annot=True, fmt="d", cmap="YlGnBu", cbar=True)
    plt.title("Product sales heat map")
    plt.show()

plot_heatmap()


# In[18]:


# 5. 绘制气泡图，根据数值大小设置气泡大小
def plot_bubble_chart():
    np.random.seed(0)
    x = np.random.rand(10) * 10
    y = np.random.rand(10) * 10
    sizes = np.random.rand(10) * 100

    plt.figure()
    plt.scatter(x, y, s=sizes, alpha=0.6, cmap='viridis')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Bubble diagram")
    plt.show()

plot_bubble_chart()

