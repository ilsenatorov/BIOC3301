#!/usr/bin/env python
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(dataframe, title=False, savename=False, fmt='d', annot=True, cbar=True):
    matplotlib.rcParams.update({'font.size': 25})

    fig, ax = plt.subplots(figsize=(40,30), dpi=100)
    sns.heatmap(ax=ax,
                data=dataframe,
                square=True,
                annot=annot,
                fmt=fmt,
                annot_kws={"size":8},
                cbar=cbar)
    if title:
        plt.title(title, fontsize=40)
    if savename:
        plt.savefig(savename, bbox_inches='tight')
    plt.show()

def sort_df(dataframe):
    cols = []
    for num in range(8,38):
        cols.append('515rcbc'+str(num))
    dataframe = dataframe.reindex(reversed(cols))
    return dataframe[cols]

def plot_bar(dataframe, metric, title=False, savename=False, dpi=100, ylabel=False, xlabel='SampleID'):
    matplotlib.rcParams.update({'font.size': 14})
    fig, ax = plt.subplots(figsize=(9,6))
    dataframe = dataframe.sort_values(metric, axis=0)
    plt.bar(dataframe.index, dataframe[metric], color='purple')
    plt.xticks(rotation=90)
    plt.ylabel(metric, fontsize=14)
    ax.grid(axis='y')
    ax.set_axisbelow(True)
    if title:
        plt.title(title, fontsize=18)
    if xlabel:
        plt.xlabel(xlabel, fontsize=14)
    if ylabel:
        plt.ylabel(ylabel, fontsize=14)
    if savename:
        plt.savefig(savename, dpi=dpi, bbox_inches='tight')

    plt.show()
