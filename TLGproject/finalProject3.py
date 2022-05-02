#!/usr/bin/env python3
""" ECMelander | TLG at Alta3
    Filtering and displaying data for veterans in apprenticeships
    Data from data.wa.gov"""

import pandas as pd
from sodapy import Socrata
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def totalGB(df_gb) :
    ### unstacking the groupby
    #df_V = df_V.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    #df_V = df_V.unstack()
    #df_V.columns = ['__'.join(col).strip() for col in df_V.columns.values]
    #df_V = df_gb.rename(columns={'veteran__Non-vet':'Non-Vet', 'veteran__Not Specified':'Not Specified', 'veteran__Veteran':'Veteran'})

    #print(df_gbU_copy)

    ### unstacking the groupby
    #print(df.groupby(['year' , 'veteran']).size())
    #sns.countplot(x='year', hue='veteran', data=df)

    sns.countplot(x='year', hue='veteran', data=df_gb).set(title='Annual Apprenticeship Totals')
    #plt.set_title('Apprenticeship Totals')
    #plt.set_xlabel('Annual Participation')
    plt.savefig('/home/student/static/Apprentice_Totals.png')  

    df_gb = df_gb.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_gb = df_gb.unstack()
    df_gb.columns = ['__'.join(col).strip() for col in df_gb.columns.values]
    df_gb = df_gb.rename(columns={'veteran__Non-vet':'Non-Vet', 'veteran__Not Specified':'Not Specified', 'veteran__Veteran':'Veteran'})
    #df_gb.Index.to_series(name='Year')

    return df_gb



def totalVets(df_V) :
    ### unstacking the groupby
    df_V = df_V.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_V = df_V.unstack()
    df_V.columns = ['__'.join(col).strip() for col in df_V.columns.values]
    df_V = df_V.rename(columns={'veteran__Non-vet':'Non-Vet', 'veteran__Not Specified':'Not Specified', 'veteran__Veteran':'Veteran'})

    #print(df_gbU_copy)

    df_V['total'] = df_V.sum(axis=1)
    #print(df_V)
    #input()
    df_V['Percentage'] = (df_V['Veteran'] / df_V['total']) * 100
    #df_V['Percentage'] = pd.Series(['{:.2f}%'.format(val * 100) for val in df_V['Percentage']], index = df_V.index)
    df_V['Veterans'] = df_V['Veteran'].astype(int)
    #print(df_gbU_copy)
    df_V = df_V[['Veterans', 'Percentage']]
    #print(f"\nTotal Veteran Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    #print(df_V)

    df_Vi = df_V.reset_index()
    #print(df_Vi)
    #input()
    
    fig, ax1 = plt.subplots()
    #sns.barplot(data=df_Vi, x='year', y='Veterans') #, ax=ax1)
    #ax2 = ax1.twinx()
    #sns.lineplot(data=df_V['Percentage'], ax=ax2)
    ax2 = ax1.twinx()
    ax1.set_ylabel('Veteran Apprentices')
    ax2.set_ylabel('as Percentage of Total Apprentices')
    ax1.set_title('Annual Veteran Apprentice Totals')

    
    df_V['Veterans'].plot(kind='bar', color='green', ax=ax1)
    df_Vi['Percentage'].plot(kind='line', marker='d', color='blue', ax=ax2)
    #plt.twinx()
    #df_V['Percentage'].plot(kind='line', marker='d', secondary_y=True)
    plt.savefig('/home/student/static/Veteran_Totals.png')    

    return df_V

def femaleVets(df_F) :
    sex_filter = df_F['sex'] == 'Female'                                             # setting filter variable
    df_F = df_F.loc[sex_filter, ['year', 'sex', 'veteran']]       # applying filter variable
    ####
    df_F = df_F.groupby(['year' , 'veteran']).agg({'veteran' : 'count'})
    df_F = df_F.unstack()
    #df_F['Female_Vet'] = df_F[[('veteran', 'Veteran')]]
    df_F.columns = ['__'.join(col).strip() for col in df_F.columns.values]
    df_F['Female_Vet'] = df_F['veteran__Veteran']
    ####
    #df_F.columns = ['__'.join(col).strip() for col in df_F.columns.values]
    #df_F['Percent_Change'] = df_F['veteran__Non-vet'].pct_change()    
    #print(df_F.pct_change())
    #input()

    df_F=df_F.rename(columns={'Veteran':'Female_Vet'})
    df_F['Percent_Change'] = df_F['Female_Vet'].pct_change(fill_method='ffill') * 100
    #df_F['Percent_Change'] = pd.Series(['{:.2f}%'.format(val * 100) for val in df_F['Percent_Change']], index = df_F.index)
    #df_F['Female_Vet'] = df_F['Female_Vet'].astype(int)
    #df_F['Percent_Change'] = df_F.pct_change([('veteran', 'Non-vet')])
    df_F = df_F[['Female_Vet', 'Percent_Change']]
    #print(f"\nFemale Veteran Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    #print(df_F)

    #df_F['Female_Vet'].plot(kind='bar')
    #df_F['Percentage_Change'].plot(kind='line', secondary_y=True)
    #plt.savefig('/home/student/static/Female_Veteran.png')  

    df_Fi = df_F.reset_index()
    #print(df_Vi)
    #input()
    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.set_ylabel('Female Veteran Apprentices')
    ax2.set_ylabel('Percentage Change from Prior Year')
    ax1.set_title('Annual Female Veteran Totals')  

        
    df_F['Female_Vet'].plot(kind='bar', color='green', ax=ax1)
    df_Fi['Percent_Change'].plot(kind='line', marker='d', color='blue', ax=ax2)
    plt.savefig('/home/student/static/Female_Veterans.png')

    return df_F



def main() :

    global yrMax
    global yrMin


    jsonFile = "/home/student/static/mcr6-ujqw.json"
    df= pd.read_json(jsonFile)    

    # importing data
    #client = Socrata("data.wa.gov", None)               # define variable for location of source data
    #results = client.get("mcr6-ujqw", limit=200000)     # import source data as results
    #df = pd.DataFrame.from_records(results)             # Convert to pandas DataFrame as df

    ###for debugging###
    print(f"\nStarting number of rows:  {len(df)}")

    # Cleaning data
    df.sort_values(['registration_date'], inplace=True)                     # sorting by date
    df.drop_duplicates(['apprentice_id'], inplace=True)                     # removing duplicates
    df.set_index(['apprentice_id'], inplace=True)                           # setting index
    df.replace( 'Other than Vietnam era vet' , 'Veteran' , inplace = True)  # standardizing veteran designation
    df.replace( 'Vietnam era vet' , 'Veteran' , inplace = True)             # standardizing veteran designation
    df['registration_date'] = pd.to_datetime(df['registration_date'])       # converting object to date
    df["year"] = df["registration_date"].dt.year                            # adding column for year

    # setting variable to filter by year
    yrList = list(df['year'].unique())          # creating list for validating user input
    yrMax = max(yrList)
    yrMin = 0
    print("\nEnter desired start year:")
    while yrMin not in yrList :               # while loop to ensure valid input
        try :
            yrMin = int(input('> '))
        except :
            print("Please enter a valid year")

    # filter according to specified year
    year_filter = df['year'] >= yrMin                                             # setting filter variable
    #df = df.loc[year_filter, ['last_name', 'first_name', 'year', 'sex', 'veteran']] # applying filter and selecting relevent columns
    df = df.loc[year_filter, ['year', 'sex', 'veteran']] # applying filter and selecting relevent columns


    ###for debugging###
    #print(df.veteran.unique())
    #print(df[[ 'last_name' , 'first_name' , 'year' , 'veteran' , 'sex' ]].head(30))
    #print(df.sex.unique())
    print(f"\nResulting number of rows:  {len(df)}")
    #print(df.dtypes)
    #rint(df.head())


    ### unstacking the groupby
    #df_gb = df.groupby(['year' , 'veteran','sex']).agg({'veteran' : 'count'})
    #df_gb = df_gb.unstack()
    #print(df_gbU)

    #df_gbU_copy = df_gbU.copy()
    #df_gb.columns = ['__'.join(col).strip() for col in df_gb.columns.values]
    #df_gb = df_gb.rename(columns={'veteran__Non-vet':'Non-Vet', 'veteran__Not Specified':'Not Specified', 'veteran__Veteran':'Veteran'})
    #print(df_gb)


    print(f"\nTotal Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    df_gbm = totalGB(df)
    print(df_gbm)
    input("\n (press enter to continue)\n")


    print(f"\nVeteran Participation as Percentage of Total Apprentices\n      from {yrMin} to {yrMax}\n")    
    df_Vm = totalVets(df)
    print(df_Vm)
    input("\n (press enter to continue)\n")

    print(f"\nFemale Veteran Apprenticeship Participation\n      from {yrMin} to {yrMax}\n")    
    df_Fm = femaleVets(df)
    print(df_Fm)
    input("\n (press enter to continue)\n")

    #dataPrint(df_gbm, df_Vm, df_Fm)



    input('stop')

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(f"/home/student/static/Apprenticeship_Data_{yrMin}-{yrMax}.xlsx", engine='xlsxwriter')

    # Write each dataframe to a different worksheet.
    df_gbm.to_excel(writer, sheet_name='Sheet1')
    df_Vm.to_excel(writer, sheet_name='Sheet2')
    df_Fm.to_excel(writer, sheet_name='Sheet3')

    # Get the xlsxwriter workbook and worksheet objects.
    #workbook  = writer.book
    #worksheet1 = writer.sheets['Sheet1']


    # Get the dimensions of the dataframe.
    (max_row, max_col) = df_gbm.shape
    writer.sheets['Sheet1'].insert_image(0, max_col + 2, '/home/student/static/Apprentice_Totals.png' )

    (max_row, max_col) = df_Vm.shape
    writer.sheets['Sheet2'].insert_image(0, max_col + 2, '/home/student/static/Veteran_Totals.png' )

    (max_row, max_col) = df_Fm.shape
    writer.sheets['Sheet3'].insert_image(0, max_col + 2, '/home/student/static/Female_Veterans.png' )    

    # Configure the series of the chart from the dataframe data.
    #chart.add_series({'values': ['Sheet1', 1, 1, max_row, max_col]})
    #chart.add_series({'values': ['Sheet1', 1, 2, max_row, max_col]})
    #chart.add_series({'values': ['Sheet1', 1, 3, max_row, max_col]})

    # Insert the chart into the worksheet.
    #worksheet.insert_chart(0, max_col + 2, chart)


    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

    #input("\n (press enter to continue)\n")
    #print(df.groupby(['year' , 'veteran']).size())
    #sns.countplot(x='year', hue='veteran', data=df)
    #plt.savefig('/home/student/static/countPlot2.png')

if __name__ == '__main__' :
    main()