import folium
import pandas as pd
from folium.plugins import HeatMap
import numpy as np
import webbrowser

data=pd.read_csv('demosite.csv',engine='python')
del data['site']
list1=data.values.tolist()



China_map = folium.Map(
tiles = 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7',
attr='高德-常规图',
location = [33.67,113.87],                  # location 经纬度 [纬度,经度]
zoom_start =7,
# control_scale=True                         # 初始地图大小
)

HeatMap(list1).add_to(China_map)

China_map.save('chart.html')              # 保存为HTML
webbrowser.open('chart.html')