import pandas as pd
import pyecharts.options as opts
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, WordCloud
from pyecharts.globals import SymbolType, ThemeType

#读取和转换部分
name,count =[],[]
data_jd = pd.read_csv('K:\学习\channel627\get_jd627.csv')
data = data_jd.values.tolist()
for i in range(len(data)):
    now = data[i]
    name.append(now[0])
    count.append(now[1])

#绘制基本柱状图
bar = Bar(init_opts=opts.InitOpts(width="1000px"))
bar.add_xaxis(name)
bar.add_yaxis('购买人数',count)
bar.set_global_opts(title_opts=opts.TitleOpts(title="Chanel-627", subtitle=" "))
bar.set_global_opts(legend_opts=opts.LegendOpts(type_=None # 'plain'：普通图例。缺省就是普通图例。 
                                                               # 'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。                                                     
                                                    ,pos_left='left' #图例横向的位置,right表示在右侧，也可以为百分比
                                                    ,pos_top='down'#图例纵向的位置，middle表示中间，也可以为百分比
                                                    ,orient='vertical'#horizontal #图例方式的方式
                                                   ))
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render('bar_627.html')

#绘制富文本饼图
c = (
    Pie(init_opts=opts.InitOpts(width="1000px"))
    .add(
        "",
        [list(z) for z in zip(name, count)],
        radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    #加侧面标签
    .set_global_opts(
        title_opts=opts.TitleOpts(title=" "),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #.set_global_opts(title_opts=opts.TitleOpts(title=" "))
    .render("pie_channel.html")
)

#绘制玫瑰图
c1 = (
    Pie(init_opts=opts.InitOpts(width="1800px"))
    .add(
        "",
        [list(z) for z in zip(name, count)],
        
        radius=["30%", "75%"],
        center=["25%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title=" "),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("channel_rosetype.html")
)

#绘制词云图
c2 = (
    WordCloud()
    .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_colors(['red',"blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Chanel-627"))
    .render("wordcloud_channel.html")
)
