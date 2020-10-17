# Import necessary functionalities

import sys
import os 
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
import datetime as dt
from ipywidgets import widgets

print(__name__) if __name__ != '__main__' else None

rangeselector = dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )

def save_plot(plot, file, mode = 'static', **kwargs):
    ''' Save a plot into external file, based on selected mode: option "static" exports plot as .png file,
    option "interactive" exports plot as html file.

        Parameters
        ----------
        plot: plotly.graph_objects.Figure
        file: str of filepath including file extension
        mode: str of 'interactive' or 'static'
        kwargs: kwargs passed on to write_image() for static plots and 
            to write_html() for interactive plots

        Returns
        -------
        None
    '''

    if mode == 'static':
        if 'width' not in kwargs.keys():
            kwargs['width'] = 1600
        if 'height' not in kwargs.keys():
            kwargs['height'] = 900
        if 'scale' not in kwargs.keys():
            kwargs['scale'] = 1.5            
        
        if file.split('.')[-1] == 'html':
            error_msg = ('mode was set to static but file extenstion was set to .html. \n'
                         'see plotly.graph_pbjects.Figure.write_image() for more information'
            raise ValueError(error_msg)
        else:
            plot.write_image(file = file, **kwargs)
            return None
    elif mode == 'interactive':
        if 'autoplay' not in kwargs.keys():
            kwargs['auto_play'] = False
        plot.write_html(file = file, **kwargs)
        return None
    else:
        raise ValueError('Mode must be either "static" or "interactive".')


def multiplot(layers = None, nrows = None, ncols = None, fig = None, 
              colorway = px.colors.colorbrewer.Set2,
              **kwargs):

    ''' 
    Creates a plot with multiple sub plots.
    Parameters
    ----------
    layers: This is an array-like of layeritems which are passed one-by-one to autoplot()
            positions can be skipped by setting that layer item to None
            e.g. [[layers_for_autoplot], None, [layers_for_autoplot]]
    **kwargs: keyword arguments passed onto fig.update_layout()

    Note
    ----
    In the case of axis kwargs, all subplots have two y-axes. 
    kwargs for multiplots are therefore for example: 
        xaxis3_title_text (for the 3rd xaxis)
        yaxis4_title_font for the fourth y axis in figure (2nd yaxis of 2nd subplot)
    '''

    # fig should probably be none
    # if ncols is not provided then the default is 4 and the number of rows is determined accordingly

    if fig is None: # in case a pre-existing multiplot has not been provided
        nsubplots = len(layers)
        if (nrows is None) and (ncols is None) and (len(layers) > 4): 
            # sets a limit of 4 columns if data contains more than 4 subplots
            ncols = 4
            nrows = ((nsubplots-1) // ncols) + 1 # calculating nrows from ncols and nsubplots
        elif (nrows is None) and (ncols is None) and (len(layers) <= 4):
            ncols = len(layers)
            nrows = ((nsubplots-1) // ncols) + 1 # calculating nrows from ncols and nsubplots
        
        if (nrows is not None) and (ncols is None):
            ncols = ((nsubplots-1) // nrows) + 1 # calculating ncols from nrows and nsubplots

        specs = np.full((nrows,ncols),{'secondary_y':True}).tolist()
        fig = make_subplots(rows = nrows, cols = ncols, 
                            specs=specs)
    
    for i in range(len(layers)):
        if layers[i] is not None:
        # find the position of the plot (the +1 converts form zero- to one-indexing)
            row = (i // ncols) + 1
            col = (i % ncols) + 1
            #row, col = np.unravel_index(i,(nrows,ncols)) # this does the same as the 2 lines above
            fig = autoplot(layers = layers[i], fig = fig, row = row, col = col)

    fig = fig.update_layout(**kwargs, colorway = colorway)

    return fig


def multiplot_for_insights(layers = None, nrows = None, ncols = None, fig = None, 
              colorway = px.colors.colorbrewer.Set2, subplot_titles = None, external_specs = None,
              shared_xaxes = False, shared_yaxes = False,
              vertical_spacing = 0.02, horizontal_spacing = None, **kwargs):

    ''' 
    Creates a plot with multiple sub plots.
    layers: This is a list of layer-items which are passed one-by-one to autoplot()
            positions can be skipped by setting that layer item to None
            e.g. [[layers_for_autoplot()], None, [layers_for_autoplot()]]
    **kwargs are keyword arguments passed onto fig.update_layout()
    Note: in the case of kwargs. All subplots have two y-axes. kwargs for multiplots are therefore
    for example: xaxis3_title_text (for the 3rd xaxis) or 
                 yaxis4_title_font for the fourth y axis in figure (2nd yaxis of 2nd subplot)
    '''

    # fig should probably be none
    # if ncols is not provided then the default is 4 and the number of rows is determined accordingly

    if fig is None: # in case a pre-existing multiplot has not been provided
        nsubplots = len(layers)
        if (nrows is None) and (ncols is None) and (len(layers) > 4): # sets a limit of 4 columns if data contains more than 4 subplots
            ncols = 4
        elif (nrows is None) and (ncols is None) and (len(layers) <= 4):
            ncols = len(layers)
        
        if (nrows is None) and (ncols is not None): # if ncols was not specified above (because either ncols or nrows is specified)
            nrows = ((nsubplots-1) // ncols) + 1 # calculating nrows from ncols and nsubplots
        elif (nrows is not None) and (ncols is None):
            ncols = ((nsubplots-1) // nrows) + 1 # calculating ncols from nrows and nsubplots

        if external_specs is not None:
            specs = external_specs
        else:     
            specs = np.full((nrows,ncols),{'secondary_y':False}).tolist() 
            
        fig = make_subplots(rows = nrows, cols = ncols, 
                            specs=specs, subplot_titles = subplot_titles,
                            shared_xaxes=shared_xaxes, shared_yaxes = shared_yaxes,
                            vertical_spacing = vertical_spacing, horizontal_spacing = horizontal_spacing)
            
    for i in range(len(layers)):
        if layers[i] is not None:
        # find the position of the plot (the +1 converts form zero- to one-indexing)
            
            row = (i // ncols) + 1
            col = (i % ncols) + 1
            #print('i', i, 'row', row, 'col', col)
            fig = autoplot(layers = layers[i], fig = fig, row = row, col = col)

    fig = fig.update_layout(kwargs, colorway = colorway)

    return fig

def autoplot(layers= None, data=None, x = None, y = None, fig = None, row = None, col = None, 
             colorway = px.colors.colorbrewer.Set2, **kwargs):
    '''
    Creates one (sub)plot
    Parameters
    ----------
    layers: a list of lists (or array-like)
        - the inner lists hold details of the individual layers
        Each inner list must contain:
            0) the layer type either as a full word or one letter:
                - s(catter)
                - l(ine)
                - (bo)x
                - b(ar)
                - h(ist)
            1) the x axis column to be taken from data (if not specified as kwarg)
                OR a pandas.Series/numpy.ndarray/list of data
            2) the y axis column to be taken from data (if not specified as kwarg)
                OR a pandas.Series/numpy.ndarray/list of data
            3) a dict of keyword arguments to be passed to go.Functions() 
                e.g.  dict(connectgaps=True, opacity = 0.5)
               also accepts secondary_y parameter passed to add_trace()
    data: pandas.DataFrame
    x: (str) a column name from 'data' or an array-like to be used on all layers.
        x must then NOT be specified as part of the 'layers' argument
    y: (str) a column name from 'data' or an array-like to be used on all layers.
        y must then NOT be specified as part of the 'layers' argument
    fig: a predefined plotly.graph_objects.Figure on which to append the plot
    row: int (must also be specified if fig is specified)
    col: int (must also be specified if fig is specified)
    kwargs: keyword arguments passed onto fig.update_layout()
    '''
    if fig is None: # This is necessary because even if autplot only creates one plot, 
                    # you might be adding layers to an existing figure
        n_row = 1
        n_col = 1
        specs = np.full((n_row,n_col),{'secondary_y':True}).tolist()
        fig = make_subplots(rows = n_row, cols = n_col, 
                            specs=specs)
    if row is None:
        row = 1
    if col is None:
        col = 1
    
    if x is not None:
        if isinstance(x,str):
            x = data[x]
        elif not (isinstance(x, np.ndarray, pd.Series, list)):
            ValueError('x argument must be a column name from "data" or a series/array/list')
    if y is not None:
        if isinstance(y,str):
            y = data[y]
        elif not ( (isinstance(y, np.ndarray)) or (isinstance(y, pd.Series)) or (isinstance(y,list)) ):
            ValueError('y argument must be a column name from "data" or a series/array/list')

    for layer in layers:
        fig = add_layer(data = data, x = x, y = y, layer = layer, fig = fig, row = row, col = col)
    
    fig = fig.update_layout(kwargs, colorway = colorway)

    return fig

def add_layer(data = None, x = None, y = None, layer = None, fig = None, row = None, col = None): 
    ''' Adds a layer to an existing figure'''

    layer = layer + [None] # padder to allow the line below to work
    if x is not None:
        layer = layer[0:1]+[x]+layer[1:] # adding the kwarg to the layers list
    if y is not None:
        layer = layer[0:2]+[y]+layer[2:] # adding the kwarg to the layers list

    # defining layer
    mode = layer[0]
    x = layer[1]
    if isinstance(x,str):
        x = data[x]

    y = layer[2]
    if isinstance(y,str):
        y = data[y]
    
    if not (isinstance(layer[3], dict) or (layer[3] is None)):
        raise ValueError('Item [3] in the list must be a dict or None')

    if isinstance(layer[3], dict):
        kwargs = layer[3]
    elif layer[3] is None:
        kwargs = dict()

    if ('name' not in kwargs.keys()) and isinstance(y, pd.Series):
        kwargs['name'] = y.name

    if ('name' not in kwargs.keys()) and (not isinstance(y, pd.Series)): 
        # setting name to empty string if not prespecified
        kwargs['name'] = '' # avoids the names trace 1,2,3 etc
    
    if 'secondary_y' in kwargs.keys(): # setting secondary_y argument to add_trace() if not prespecified
        secondary_y = kwargs['secondary_y']
        kwargs.pop('secondary_y')
    else:
        secondary_y = False

    # adding trace
    if mode[0] == 's': # to find scatter
        if 'mode' not in kwargs.keys(): # setting scatter mode if not prespecified
            kwargs['mode'] = 'markers'
        fig = fig.add_trace(go.Scatter(x = x, y = y, **kwargs),
                            row = row, col = col, 
                            secondary_y = secondary_y)
    elif mode[0] == 'l': # to find line
        if 'connectgaps' not in kwargs.keys(): # setting connectgaps if not prespecified
            kwargs['connectgaps'] = True
        fig = fig.add_trace(go.Scatter(x = x, y = y, **kwargs),
                            row = row, col = col, 
                            secondary_y = secondary_y)
    elif mode[-1] == 'x': # to find box
        fig = fig.add_trace(go.Box(x = x, y = y, **kwargs),
                            row = row, col = col,  
                            secondary_y = secondary_y)
    elif mode[0] == 'b': # to find bar
        fig = fig.add_trace(go.Bar(x = x, y = y, **kwargs),
                            row = row, col = col, 
                            secondary_y = secondary_y)
    elif mode[0] == 'h': # to find line
        fig = fig.add_trace(go.Histogram(x = x, y = y, **kwargs),
                            row = row, col = col, 
                            secondary_y = secondary_y)
    return fig
