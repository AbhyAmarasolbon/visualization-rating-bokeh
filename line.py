import pandas as pd
import numpy as np

from bokeh.plotting import figure, show
from bokeh.models import HoverTool, Title
from bokeh.embed import components
from bokeh.resources import CDN

def line_plot(movie):
    # create a new plot with a title and axis labels
    p = figure(title="Spider-Man: Into the Spider-Verse",
               x_axis_label="Rating", 
               y_axis_label="Number of Reviewer", 
               height=400,
               sizing_mode="stretch_width")
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

    # show the results
    script_comp, div_comp = components(p)

    return script_comp, div_comp