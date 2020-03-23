import json
from pyecharts import Line, Bar, Pie, EffectScatter
from pyecharts.engine import create_default_environment
#from snapshot_selenium import snapshot as driver
#from pyecharts.render import make_snapshot
attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
line = Line('折线图')
line.add('商家A', attr, v1, mark_point=['max'])
line.add('商家B', attr, v2, mark_point=['min'], is_smooth=True)
#line.show_config()
env = create_default_environment("png")
env.render_chart_to_file(line, path='line.png')
#line.render(path='./test.html')
