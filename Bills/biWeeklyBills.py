#!/usr/bin/env python
# coding: utf-8

# In[35]:


from IPython.display import clear_output
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime as DT
import pandas as pd
import numpy as np


class bills(object):
    
    def __init__(self , startingPayDate):
        self.startingPayDate = startingPayDate
        
    def getMonthly(self , month , year = 2020 ):     
        # Input year and month number
        year = year
        month = month
        month = DT.datetime(year ,  month , 1 , 0 , 0  )
        clear_output() ; print( "--> Script running for:  " , month.strftime( '%m-%d-%Y' ) )

        # Finding all possible pay dates Then finding the pay daytes for hte month entered.
        startingPayDate = self.startingPayDate
        payDates = [] # All the possible pay dates until 2050.
        for i in range(800):
            payDates.append( startingPayDate + DT.timedelta( days = i*14 ) )
        times = pd.DataFrame( payDates )
        payDatesThisMonth = times[ ( times >= month ) & ( times < month + DT.timedelta( days = 30 ) ) ].dropna()
        print("--> Paydates this month: " , payDatesThisMonth[0].map( lambda x: x.strftime( '%m-%d-%Y' ) ).values )


        # Imported Excel Sheet
        importSheet = pd.read_excel( 'input.xls' , sheet_name = "Bill Input" )

        # Making the dates in excel sheet match inputed month, year
        billDates = []
        for i in importSheet['Day']:
            billDates.append(month + DT.timedelta( days = i - 1 ) )
        importSheet['Day'] = billDates
        importSheet.index = importSheet['Bill'] ; importSheet.drop( ['Bill'] , axis = 1 , inplace = True )
        both_dfs = importSheet[importSheet['Both'] == True]
        notBoth = importSheet[importSheet['Both'] == False]
        both_names = both_dfs.index.values


        # replacing all the True ones with the date of the pay day
        store = []
        for i in payDatesThisMonth[0]:
            for j in range( len(both_dfs) ):
                store.append( i )      
        payArrays = np.array(store)

        #Concatenating 2 or 3 ( how many paychecks are recieved this month ) together then using payArrays to reassign all the dates.
        new_df = both_dfs
        for i in range( payDatesThisMonth.shape[0] -1 ):
            new_df = pd.concat( [ new_df , both_dfs ] )
        new_df['Day'] = payArrays

        # Building Final df
        final = pd.concat( [ notBoth , new_df ] )
        final.drop(['Both'] , axis = 1 , inplace = True)

        # Checking Rent Can be three paychecks
        if final.loc['Rent'].shape[0] != 2:

            print("-//-> ERROR: Change Rent in input sheet! Should be: " ,                  ( final.loc['Rent']['Amount'] * (2 / final.loc['Rent'].shape[0]) ).mean() )

        # Creating Paycheck Dataframes
        first = final[ final['Day'] < payDatesThisMonth[0].values[0] ]
        second = final[ final['Day'] < payDatesThisMonth[0].values[1] ]
        after_second = final[ final['Day'] > payDatesThisMonth[0].values[1] ]

        try:
            third = final[ final['Day'] < payDatesThisMonth[0].values[2] ]
            after_third = final[ final['Day'] > payDatesThisMonth[0].values[2] ]
            return [ first , second , after_second , third , after_third]
            print("--> Three Paychecks")
        except:
            return [ first , second , after_second]
            print("--> Only Two Paychecks")
        print('--')
        
    def multipleMonths(self , monthStart , monthEnd , year=2020):
        month1 = self.getMonthly(monthStart)
        month2 = self.getMonthly(monthEnd)
        
        mid = pd.concat( [ month1[-1] , month2[0] ] )
        return [month1 , month2 , mid]

