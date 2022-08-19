#!/usr/bin/env python3
  
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("/home/student/mycode/one.csv", index_col=1)
    df.drop_duplicates(inplace=True)
    df.drop(df.columns.difference(["trend","season","episode","total_votes"]), 1, inplace=True)
    sorted_by_name = df.sort_values(["rank"], ascending=True)
    sorted_by_name.set_index("name")

print(sorted_by_name.head(10))

sorted_by_name.head(10).plot(kind="name")
plt.savefig("/home/student/static/sorted.txt", bbox_inches='tight')

if __name__ == "__main__":

        main()