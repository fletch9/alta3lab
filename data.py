#!/usr/bin/env python3
"""pulls data from .txt file strips rows, prints top 20, and creates an xls file | eric.fletcher@tlgcohort.com"""
import pandas as pd
import matplotlib
import pyexcel


def main():
# opens file and sorts data
    df = pd.read_csv("/home/student/mycode/one.txt", index_col=1)
    df.drop_duplicates(inplace=True)
    df.drop(df.columns.difference(["average_rating","name"]), 1, inplace=True)
    sorted_by_name = df.sort_values(["average_rating"], ascending=False)
    sorted_by_name.set_index("name")
    
# prints sorted data

    print(sorted_by_name.head(20))
#creates xls file
    df.to_excel("top20_shows.xls")

if __name__ == "__main__":

    main()
