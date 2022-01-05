from flask import *

app = Flask(__name__)

@app.route("/")
def bokeh_plot():
    import pandas as pd
    import numpy as np

    from bokeh.layouts import layout,WidgetBox
    from bokeh.plotting import figure, show
    from bokeh.models import HoverTool, Title, Div, RangeSlider, Spinner, Dropdown, CustomJS
    from bokeh.embed import components
    from bokeh.resources import CDN

    def cdn_js():
        return CDN.js_files

    def line_plot(movie,title_mov):
        # create a new plot with a title and axis labels
        p = figure(x_range=(0, 10),
                title=title_mov,
                x_axis_label="Rating", 
                y_axis_label="Number of Reviewer", 
                width=1200,
                sizing_mode="scale_both")
        p.add_layout(Title(text="Rating  Rotten Tomatoes",align = 'center'), 'above')

        p.vbar(x=movie['rating'], top=movie['val_rating'], width=0.5, bottom=0, color="red")

        p.xgrid.visible = False
        p.ygrid.visible = False

        hover = HoverTool(tooltips=[('Rating', '@x'),
                                    ('Number of Reviewer', '@top')],
                        mode='vline')

        # Style plot
        p.title.align = 'center'
        p.title.text_font_size = '20pt'
        p.title.text_font = 'serif'

        # Axis titles
        p.xaxis.axis_label_text_font_size = '14pt'
        p.xaxis.axis_label_text_font_style = 'bold'
        p.yaxis.axis_label_text_font_size = '14pt'
        p.yaxis.axis_label_text_font_style = 'bold'

        # Tick labels
        p.xaxis.major_label_text_font_size = '12pt'
        p.yaxis.major_label_text_font_size = '12pt'

        # Add the hover tool and styling
        p.add_tools(hover)

        range_slider = RangeSlider(
            title="Adjust rating range",
            start=0,
            end=10,
            step=1,
            value=(p.x_range.start, p.x_range.end),
        )
        range_slider.js_link("value", p.x_range, "start", attr_selector=0)
        range_slider.js_link("value", p.x_range, "end", attr_selector=1)

        controls = WidgetBox(range_slider, margin = (0, 0, 0, 457))
        # show the results
        layouts = layout(
            [
                [p],
                [controls],
            ]
        )

        # show result
        script_comp, div_comp = components(layouts)

        return script_comp, div_comp

    def spiderman():
        dat = pd.read_csv('data/spiderman_spider_verse.csv')
        val_sc = dat.review_score.value_counts().to_list()
        rat_sc = dat.review_score.value_counts().index.to_list() 
        movie_dat = {'rating':rat_sc,
                     'val_rating':val_sc
        }
        return line_plot(movie_dat,"Spider-Man: Into the Spider-Verse")
        
    def wolfows():
        dat = pd.read_csv('data/wolf_of_wallstreet.csv')
        val_sc = dat.review_score.value_counts().to_list()
        rat_sc = dat.review_score.value_counts().index.to_list() 
        movie_dat = {'rating':rat_sc,
                     'val_rating':val_sc
        }
        return line_plot(movie_dat,"The Wolf of Wall Street")

    def zootopia():
        dat = pd.read_csv('data/zootopia.csv')
        val_sc = dat.review_score.value_counts().to_list()
        rat_sc = dat.review_score.value_counts().index.to_list() 
        movie_dat = {'rating':rat_sc,
                     'val_rating':val_sc
        }
        return line_plot(movie_dat,"Zootopia")

    script1,div1 = zootopia()
    script2,div2 = wolfows()
    script3,div3 = spiderman()

    script = [script1,script2,script3]
    div = [div1,div2,div3]

    return render_template('index.html',
                            script=script,
                            div=div,
                            cdn=cdn_js())

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)