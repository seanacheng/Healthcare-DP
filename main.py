import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasql import sqldf

df = pd.read_csv('h236.csv')


def run_query(query):
    print(sqldf(query))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", metavar="query")

    args = parser.parse_args()

    # print(df.info())
    if args.query:
        run_query(args.query)

if __name__ == "__main__":
    main()