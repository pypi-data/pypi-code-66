from iapa.preML import read
from iapa.classification import Classification
import os
import argparse

cwd = os.getcwd()

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()
csv = args.path
data_path = cwd
df = read(csv)
clf = Classification(df, "poly", data_path)
clf.execute()