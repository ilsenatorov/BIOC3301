import pandas as pd
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-i", help="Input mapping tsv file", type=str)
parser.add_argument("-o", help="Output mapping file", type=str)
args = parser.parse_args()

df = pd.read_csv(args.i, sep='\t')
df = df[df['env_material'] == 'soil']
df = df[['#SampleID', 'Description', 'country', 'env_feature']]
df['SourceSink'] = pd.Series('source', index=df.index)
df.to_csv(args.o, sep='\t')
