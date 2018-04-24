#!/usr/bin/python3

import gmplot
import pandas as pd
import numpy as np

class Map_Plotter(object):

    def __init__(self, filename):
        self.filename = filename
        df = None
        self.html_color_codes = {
            'aliceblue': '#F0F8FF',
            'antiquewhite': '#FAEBD7',
            'aqua': '#00FFFF',
            'aquamarine': '#7FFFD4',
            'azure': '#F0FFFF',
            'beige': '#F5F5DC',
            'bisque': '#FFE4C4',
            'black': '#000000',
            'blanchedalmond': '#FFEBCD',
            'blue': '#0000FF',
            'blueviolet': '#8A2BE2',
            'brown': '#A52A2A',
            'burlywood': '#DEB887',
            'cadetblue': '#5F9EA0',
            'chartreuse': '#7FFF00',
            'chocolate': '#D2691E',
            'coral': '#FF7F50',
            'cornflowerblue': '#6495ED',
            'cornsilk': '#FFF8DC',
            'crimson': '#DC143C',
            'cyan': '#00FFFF',
            'darkblue': '#00008B',
            'darkcyan': '#008B8B',
            'darkgoldenrod': '#B8860B',
            'darkgray': '#A9A9A9',
            'darkgreen': '#006400',
            'darkkhaki': '#BDB76B',
            'deepskyblue': '#00BFFF',
            'red' : '#FF0000',
            'green' : '#00FF00',
            'blue' : '#0000FF'}



    def get_data(self):
        df = pd.read_csv(self.filename+'.csv')[['SampleLongitude', 'SampleLatitude', 'Description']]
        df = df.dropna()
        self.df = df
        return df



    def plot_map(self):
        gmap = gmplot.GoogleMapPlotter(self.df['SampleLongitude'].iloc[0], self.df['SampleLatitude'].iloc[0], 12)
        for long, lat, name, color in zip(self.df.SampleLongitude.values, self.df.SampleLatitude.values, self.df.Description.values, self.html_color_codes.keys()):
            try:
                gmap.marker(float(long), float(lat), color=color, title=name+ " , " + str(long) + " , " + str(lat))
            except Exception as e:
                print(e)
        gmap.draw(self.filename+'.html')
