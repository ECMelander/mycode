#!/usr/bin/env python3
""" ECMelander | TLG at Alta3
    Filtering and displaying data for veterans in apprenticeships
    Data from data.wa.gov"""

import pandas as pd
from sodapy import Socrata
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def totalGB(df_gb) :  # data for all apprentices separated by veteran status (veteran/non-veteran/not specified)

    # generating and saving chart
    sns.countplot(x='year', hue='veteran', data=df_gb).set(title='Annual Apprenticeship Totals')
    plt.savefig('/home/student/static/data/Apprentice_Totals.png')  

    # breaking veteran column into three separate columns
    df_gb = df_gb.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_gb = df_gb.unstack()
    df_gb.columns = ['__'.join(col).strip() for col in df_gb.columns.values]
    df_gb = df_gb.rename(columns={'veteran__Non-vet':'Non-Vet', 'veteran__Not Specified':'Not Specified', 'veteran__Veteran':'Veteran'})
    return df_gb

def totalVets(df_V) :  # data for only veteran apprenticeships

    # calculating veteran participation as a percentage of total apprenticeships
    df_V['total'] = df_V.sum(axis=1)
    df_V['Percentage'] = (df_V['Veteran'] / df_V['total']) * 100
    df_V['Veterans'] = df_V['Veteran'].astype(int)
    df_V = df_V[['Veterans', 'Percentage']]
    df_Vi = df_V.reset_index()
    
    # generating and saving chart
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.set_ylabel('Veteran Apprentices')
    ax2.set_ylabel('as Percentage of Total Apprentices')
    ax1.set_title('Annual Veteran Apprentice Totals')
    df_V['Veterans'].plot(kind='bar', color='green', ax=ax1)
    df_Vi['Percentage'].plot(kind='line', marker='d', color='blue', ax=ax2)
    plt.savefig('/home/student/static/data/Veteran_Totals.png')    
    return df_V

def femaleVets(df_F) :  # data for female veteran apprenticeships

    # filtering for female veterans
    sex_filter = df_F['sex'] == 'Female'
    df_F = df_F.loc[sex_filter, ['year', 'sex', 'veteran']]
    df_F = df_F.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_F = df_F.unstack()
    df_F.columns = ['__'.join(col).strip() for col in df_F.columns.values]
    df_F['Female_Vet'] = df_F['veteran__Veteran']
    df_F=df_F.rename(columns={'Veteran':'Female_Vet'})

    # calculating change in participation compared to the previous non-zero year
    df_F['Percent_Change'] = df_F['Female_Vet'].pct_change(fill_method='ffill') * 100
    df_F = df_F[['Female_Vet', 'Percent_Change']]
    df_Fi = df_F.reset_index()

    # generating and saving chart    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.set_ylabel('Female Veteran Apprentices')
    ax2.set_ylabel('Percentage Change from Prior Year')
    ax1.set_title('Annual Female Veteran Totals')  
    df_F['Female_Vet'].plot(kind='bar', color='green', ax=ax1)
    df_Fi['Percent_Change'].plot(kind='line', marker='d', color='blue', ax=ax2)
    plt.savefig('/home/student/static/data/Female_Veterans.png')
    return df_F

def main() :

    # importing data
    client = Socrata("data.wa.gov", None)              # define variable for location of source data
    results = client.get("mcr6-ujqw", limit=200000)    # import source data as results
    df = pd.DataFrame.from_records(results)            # Convert to pandas DataFrame as df

    # debugging: importing data from static file
    #jsonFile = "/home/student/static/mcr6-ujqw.json"
    #df= pd.read_json(jsonFile)
    print(f"\nStarting number of rows:  {len(df)}")    # displaying total number of rows to validate total dataset imported

    # cleaning data
    df.sort_values(['registration_date'], inplace=True)                     # sorting by date
    df.drop_duplicates(['apprentice_id'], inplace=True)                     # removing duplicates
    df.set_index(['apprentice_id'], inplace=True)                           # setting index
    df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)  # standardizing veteran designation
    df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)             # standardizing veteran designation
    df['registration_date'] = pd.to_datetime(df['registration_date'])       # converting object to date
    df["year"] = df["registration_date"].dt.year                            # adding column for year

    # setting variable to filter by year
    yrList = list(df['year'].unique())          # creating list for validating user input
    yrMax = max(yrList)                         # creating year variables for filtering and referencing date range of data 
    yrMin = 0
    print("\nEnter desired start year:")
    while yrMin not in yrList :                 # while loop to ensure valid input
        try :
            yrMin = int(input('> '))
        except :
            print("Please enter a valid year")

    # filter according to specified year
    year_filter = df['year'] >= yrMin                       # setting filter variable
    df = df.loc[year_filter, ['year', 'sex', 'veteran']]    # applying filter and selecting relevent columns
    print(f"\nResulting number of rows:  {len(df)}")        # displaying total number of rows to confirm data properly cleaned and filtered
    input("\n (press enter to continue)\n")

    # calling functions to process data and generate charts
    print(f"\nTotal Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    df_gbm = totalGB(df)
    print(df_gbm)
    input("\n (press enter to continue)\n")

    print(f"\nVeteran Participation as Percentage of Total Apprenticeships\n      from {yrMin} to {yrMax}\n")    

    df_Vm = totalVets(df_gbm)
    print(df_Vm)
    input("\n (press enter to continue)\n")

    print(f"\nFemale Veteran Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    df_Fm = femaleVets(df)
    print(df_Fm)

    # exporting data and charts to xlsx file
    writer = pd.ExcelWriter(f"/home/student/static/data/Apprenticeship_Data_{yrMin}-{yrMax}.xlsx", engine='xlsxwriter')
    df_gbm.to_excel(writer, sheet_name='Sheet1')
    df_Vm.to_excel(writer, sheet_name='Sheet2')         # writing each dataframe to a different worksheet.
    df_Fm.to_excel(writer, sheet_name='Sheet3')
    (max_row, max_col) = df_gbm.shape                   # getting dimensions of each dataframe and setting position for inserting charts
    writer.sheets['Sheet1'].insert_image(0, max_col + 2, '/home/student/static/data/Apprentice_Totals.png' )
    (max_row, max_col) = df_Vm.shape
    writer.sheets['Sheet2'].insert_image(0, max_col + 2, '/home/student/static/data/Veteran_Totals.png' )
    (max_row, max_col) = df_Fm.shape
    writer.sheets['Sheet3'].insert_image(0, max_col + 2, '/home/student/static/data/Female_Veterans.png' )    
    writer.save()

if __name__ == '__main__' :
    main()