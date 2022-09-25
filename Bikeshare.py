#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'CH': 'chicago.csv',
              'NY': 'new_york_city.csv',
              'WA': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    #Getting the user's input for which city and validating the input
    while True:
        city = input('Please choose one of the cities to analyze: (Chicago: CH ,New York City: NY or Washington: WA): \n').upper()
        if city in CITY_DATA.keys():
            break
        else:
            print("That's an Invalid Choice, Please try again!\n Please remember to use the format mentioned below (CH for Chicago)")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    #getting the user's input for the month and validating
    
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    while True:
        month = input('Please choose the month (January to June or You can choose All): \n').title()
        if month in Months:
            break
        else:
            print('That\'s an invalid choise,Please try again!.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #getting the user's input for the day and validating 
    
    Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
    
    while True:
        day = input('Please choose the day (Monday to Sunday or You can choose All): \n').title()
        if day in Days:
            break
        else:
            print('That\'s an invalid choise,Please try again!.')
            

    print('_'*40)
#     return city, month, day
    return city,month,day

#____________________________

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Reading the data
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime - Same code i used in Problem #3
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of the week'] = df['Start Time'].dt.day_name()
    
    #filtering
    if month != 'All':
        
        df = df[df['Month'] == month.title()]
        
    
    if day != 'All':
        
        df = df[df['Day of the week'] == day.title()]
    
    return df

#____________________________

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    
    print("Most common month is: ", df['Start Time'].dt.month_name().mode()[0])

    # TO DO: display the most common day of week
    
    print("Most common day of the week is: ", df['Start Time'].dt.day_name().mode()[0])

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    
    print("Most common hour of the day is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*40)
    
#____________________________

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    print("Most common start station is: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
          
    print("Most common end station is: ", df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    
    trip = df['Start Station'] + " to " + df['End Station']
    
    print("Most frequent route is: ", trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*40)    

#____________________________

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # TO DO: display total travel time
    
    df['Trip Duration Time'] = df['End Time'] - df['Start Time']
    print("Total trips\'s Duration Time are: ", df['Trip Duration Time'].sum())
    
    # TO DO: display mean travel time
    
    print("Average travel time is: ", df['Trip Duration Time'].mean()) 
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*40)

#____________________________

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
        
        
    # TO DO: Display counts of user types
    print("User types: \n", df['User Type'].value_counts().to_frame())    
    
    print('_'*20)

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        if 'Gender' in df.columns and 'Birth Year' in df.columns:
            print("\nGender Count: \n", df['Gender'].value_counts().to_frame())
            
            print('_'*40)
            
            print("\nThe earliest Birth year: ", int(df['Birth Year'].min()))
            print("\nThe most recent Birth year: ", int(df['Birth Year'].max()))
            print("\nThe most common Birth year: ", int(df['Birth Year'].mode()))
            
            break
        else:
            print("\nWashington\'s 'Gender' and 'Birth Year' data are not available\n ")
            
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input(df):
    """ function to give the option to the user to show raw data from the dataframe"""
    
    start_loc = 0
    user_raw_input = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    
    while True:
        if user_raw_input == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            user_raw_input = input('\nWould you like view another 5 rows? Enter yes or no\n').lower()
#             if again_input == 'yes':
#                 continue
# #                 print(df.iloc[start_loc:start_loc+5])
#             elif again_input != 'no':
#                 print('Invalid Choise')
#             else: 
#                 break
        elif user_raw_input != 'no':
            print("Invalied Choice")
            user_raw_input = input('\nWould you like view another 5 rows? Enter yes or no\n').lower()
#             break
#             user_raw_input = input('\nWould you like view another 5 rows? Enter yes or no\n').lower()
        else:
            break
       
        


def main():
    while True:
        city, month, day = get_filters()
        print(city,month,day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
# i did some reaserach to help me finish this product, mostly the FWD community, Pandas docs and stackoverflow
#Links: 
      # https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html
      # https://nfpdiscussions.udacity.com/t/i-need-help-concerning-that-error/36006
      # https://stackoverflow.com/questions/26788854/pandas-get-the-age-from-a-date-example-date-of-birth 
      # Those are some Examples of resources that i used  


# In[4]:


df = pd.read_csv('new_york_city.csv')


df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])

# df['Trip Duration Time'] = df['End Time'] - df['Start Time']




# print(df['Trip Duration Time'].head())
# print(df['Trip Duration Time'].head())

duration = df['End Time'] - df['Start Time']

print("Trip Duration Time is: ", duration.mean())


# In[18]:


# print(df.head(5))

# print(df.sample(5))

a = 'hello World!'

print(a.lstrip())
print(a)


# In[ ]:




