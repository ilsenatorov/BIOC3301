#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

class Benchmarking(object):
    def __init__(self, filename):
        self.filename = filename
        df = None
    def crunch_numbers(self, savecsv=False):
        df = pd.read_csv(self.filename+'.csv', sep=',')
        df['BEST'] = df[[col for col in df.columns if 'RUN' in col]].min(axis=1)
        df['MEAN'] = df[[col for col in df.columns if 'RUN' in col]].mean(axis=1)
        df
        df['MEAN'] = df['MEAN'].round(2)
        df['EFF_BEST'] = df[df['CORES'] == 1]['BEST'].values[0]*100/(df['CORES']*df['BEST'])
        df['EFF_BEST'] = df['EFF_BEST'].round(2)
        df['EFF_MEAN'] = df[df['CORES'] == 1]['MEAN'].values[0]*100/(df['CORES']*df['MEAN'])
        df['EFF_MEAN'] = df['EFF_MEAN'].round(2)
        if savecsv:
            df.to_csv(self.filename+'_out.csv', sep=',')
        self.df = df
        return df

    def plot_times(self, graphname=False, savegraph=False):
        plt.xticks(self.df.index.values, self.df.CORES.values)
        best = plt.plot(self.df.index, self.df['BEST'])
        mean = plt.plot(self.df.index.values, self.df['MEAN'].values)
        plt.grid()
        plt.ylabel("Time (s)")
        plt.xlabel("Number of cores")
        plt.suptitle("Benchmark plot")
        if graphname:
            plt.suptitle(graphname)
        plt.legend((best[0], mean[0]), ('Best', 'Mean'))
        if savegraph:
            plt.savefig(self.filename+'_out.png', bbox='tight')
        plt.show()
