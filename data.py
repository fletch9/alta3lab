#!/usr/bin/env python3
  
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
                                      #filename is one.txt, not one.csv
    df = pd.read_csv("/home/student/mycode/one.txt", index_col=1)
    df.drop_duplicates(inplace=True)
    df.drop(df.columns.difference(["average_rating","name"]), 1, inplace=True)
    sorted_by_name = df.sort_values(["average_rating"], ascending=False)
    sorted_by_name.set_index("name")
    
# indentation problems
# because lines 17-20 are not indented 4 spaces to the right, they aren't part of the main function, so it has no idea what "sorted_by_name" is
    print(sorted_by_name.head(10))


if __name__ == "__main__":

        main()
