#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create graphs"""

import pandas as pd

# these following two lines are for writing to file
# use this when you are not rendering to a window
import matplotlib as mpl
mpl.use('Agg')

# create some graphs
import matplotlib.pyplot as plt

def main():
    # define the name of our xls file
    excel_file = 'movies.xls'

    # Choose the first column "Title" as
    # index (index=0)
    MoviesReverse = pd.read_excel(excel_file,sheet_name=2,index_col=0)
    for i in reversed(range(0,2)):
        MoviesReverse = pd.concat([MoviesReverse,pd.read_excel(excel_file,sheet_name=i,index_col=0)])


    #MoviesReverse_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    #print(MoviesReverse_sheet3.head())

    # combine all DFs into a single DF called MoviesReverse
    #MoviesReverse = pd.concat([MoviesReverse_sheet1, MoviesReverse_sheet2, MoviesReverse_sheet3])

    # number of rows and columns (5042, 24)
    print(MoviesReverse)

    # unfortunately our data has some duplicates in it
    # we can remove them quickly with the .drop_duplicates() method
    # this returns a dataframe, or None if .drop_duplicates(inplace=True)
    MoviesReverse.drop_duplicates(inplace=True)
    
    # take a peek at how our dataframe changed after removing duplicates
    print(MoviesReverse.shape)
    
    # sort DataFrame based on Gross Earnings
    sorted_by_gross = MoviesReverse.sort_values(["Gross Earnings"], ascending=False)

    # Data is sorted by values in a column
    # display the top 10 MoviesReverse by Gross Earnings.
    # passing the 10 values to head returns the top 10 not the default 5
    print(sorted_by_gross.head(10))

    # create a stacked bar graph
    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
    # save the figure as stackedbar.png
    plt.savefig("/home/student/static/stackedbar.png", bbox_inches='tight')
    print("I make things in excel... but some people don't like that... so...")
    OutputChoice=input("What format would you like? JSON/CSV/XLS ? ")
    if OutputChoice == "JSON":
        MoviesReverse.head(5).to_json("BigMovies.json")
        print("Done in json")
    elif OutputChoice == "CSV":
        MoviesReverse.head(5).to_csv("BigMovies.csv")
        print("Done in CSV")
    else:
         MoviesReverse.head(5).to_excel("BigMovies.xls")
         print("Done in XLS")


if __name__ == "__main__":
    main()

