#!/usr/bin/env python3

import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    jsonFile = "/home/student/static/mcr6-ujqw.json"
    #df= pd.read_json(jsonFile, convert_dates=['registration_date'])
    df= pd.read_json(jsonFile)



    ###for debugging###
    print(f"Starting number of rows:  {len(df)}")
    #print(results_df.columns)



    # Cleaning data
    df.sort_values(['registration_date'], inplace=True)                             # sorting by date
    df.drop_duplicates(['apprentice_id'], inplace=True)                             # removing duplicates
    df.set_index(['apprentice_id'], inplace=True)                                   # setting index
    df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)          # standardizing veteran designation
    df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)                     # standardizing veteran designation
    df['registration_date'] = pd.to_datetime(df['registration_date'])               # converting object to date
    df['year'] = df['registration_date'].dt.year                                    # adding column for year

    yrList = list(df['year'].unique())
    #exists = yrValue in yrList
    #print(exists)

    yrValue = 0
    #yrValue = int(input(f"From what year would you like to display?\n > "))
    print("Enter starting year:")
    while yrValue not in yrList :
        try :
            yrValue = int(input('> '))
            print(type(yrValue))
        except :
            print("Please enter a valid year")

    input()

    year_filter = df['year'] >= yrValue                                             # setting filter variable
    df = df.loc[year_filter, ['last_name', 'first_name', 'year', 'sex', 'veteran']] # applying filter variable
    #df = df[['last_name', 'first_name', 'year', 'sex', 'veteran']]

    ###for debugging###
    #print(df.veteran.unique())
    #print(df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]].head(30))
    #print(df.sex.unique())
    print(f"Filtered rows:  {len(df)}")
    #print(df.dtypes)
    #rint(df.head())

    #input()
    print()
    #print(df.head(30))
    #print(df.groupby(['year' , 'veteran']).size())
    #sns.countplot(x='year', hue='veteran', data=df)
    #plt.savefig('/home/student/static/countPlot2.png')


    #df_vets=df[['year', 'veteran']]
    #print(df_vets)
    #vet_totals = df_vets.pivot_table(index="year", columns="veteran", aggfunc='count')
    #print(vet_totals)
    
    ### unstacking the groupby
    df_gb = df.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_gbU = df_gb.unstack()
    #print(df_gbU)

    df_gbU_copy = df_gbU.copy()
    df_gbU_copy.columns = ['__'.join(col).strip() for col in df_gbU.columns.values]
    #print(df_gbU_copy)

    df_gbU_copy['total'] = df_gbU_copy.sum(axis=1)
    df_gbU_copy['Percentage'] = df_gbU_copy['veteran__Veteran'] / df_gbU_copy['total']
    df_gbU_copy['Percentage'] = pd.Series(['{:.2f}%'.format(val * 100) for val in df_gbU_copy['Percentage']], index = df_gbU_copy.index)
    df_gbU_copy['Veterans'] = df_gbU_copy['veteran__Veteran'].astype(int)
    #print(df_gbU_copy)
    newDF = df_gbU_copy[['Veterans', 'Percentage']]
    print(newDF)


    ### export to file
    #yrMax = max(yrList)
    #df_gbU_copy.to_excel(f"{yrValue}-{yrMax}_apprentice_data.xls", index=False)



    ### dummy variable
    #print(pd.get_dummies(df, columns=['veteran']))



    #df_gbU_copy.veteran__Veteran / 


    #print(df_gb.pivot(index='year', columns='veteran'))

main()

