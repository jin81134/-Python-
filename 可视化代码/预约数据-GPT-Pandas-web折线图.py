# coding:utf-8
import os
import pandas as pd
import plotly.graph_objects as go

# 只需改动以下参数即可
current_dir = os.getcwd()  # 获取当前目录
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  # 获取上一目录
file_name = parent_dir + r'\数据\合并预约人数.csv'
output_name = parent_dir + r'\预约数据.html'

# 读取 CSV 文件
data = pd.read_csv(file_name)

# 将第一列作为 X 轴
x = data.iloc[:, 0]

# 创建一个 Figure 对象
fig = go.Figure()

# 遍历数据列并将它们添加到图形中
for col in data.columns[1:]:
    y = data[col]
    fig.add_trace(go.Scatter(x=x, y=y, name=col))

# 设置图形的标题和坐标轴标签
fig.update_layout(title="全网预约详情<br>双击右侧图例可以打开单条折线，点击右上工具可缩放<br>PS:主要是看每分钟人数的差值", xaxis_title="时间", yaxis_title="预约人数")

# 添加注释
fig.add_annotation(x="2023/4/7 0:00", y=0, text="2023/4/7 0:00<br>此时官网“阴兵上线”", showarrow=True, arrowhead=1)
fig.add_annotation(x="2023/4/12 18:06", y=147071, text="2023/4/12 18:06<br>官网预约人数在此时切换成为<br>官网人数+Bili人数+Tap人数",
                   showarrow=True, arrowhead=1)
fig.add_annotation(x="2023/4/23 8:56", y=1000015, text="2023/4/23 8:56<br>全网预约”人数“100万", showarrow=True, arrowhead=1)
fig.add_annotation(x="2023/4/25 10:57", y=334074, text="2023/4/25 10:57<br>官网人数突增约3000人", showarrow=True, arrowhead=1)
fig.add_annotation(x="2023/5/10 13:19", y=1507651, text="2023/5/10 13:19<br>由于CMD卡住数据未获取到", showarrow=True, arrowhead=1)

# 将图表保存为 HTML 文件
fig.write_html(output_name)
fig.show()
