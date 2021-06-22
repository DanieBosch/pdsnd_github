import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input('Would you like to see data for chicago, new york, or washington?: ').lower()
        if city not in ('chicago', 'new york', 'washington'):
            print('Not an appropriate choice, please try again.')
        else:
            break
    

    # get user input for month (all, january, february, ... , june)
    
    while True:
        month = input('For which month do you want to see the data (all, january, february, ... , june): ').lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Not an appropriate choice.')
        else:
            break
    
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input('What day of the week do you want to look at (all, monday, tuesday, ... sunday)?: ').lower()        
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Not an appropriate choice.')
        else:
            break


    print('-'*40)
    return city, month, day


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
    #Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #extract month, day of week, and start hour from start time to create new columns
    #convert the month data to lower case to filter by the month name
    df['month'] = df['Start Time'].dt.month_name()
    df['month'] = df['month'].str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]
    
    #filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel based on your filter...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    
    print('Most common month: ', most_common_month)
    
    
    #I want to include a loop here to print something else if all is not selected???
    
    #while(month == 'all'):
        #print('Most common month:', most_common_month)
        #break
    #else:
        #print('Not applicable : Same as selected month')
    
  

    # display the most common day of week    
    
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    
    print('Most common day of week:', most_common_day_of_week)
    
    #I want to include a loop here to print something else if all is not selected???
    
    #while(day == 'all'):
        #print('Most common day of week:', most_common_day_of_week)
        #break
    #else:
        #print('Not applicable : Same as selected day')

    # display the most common start hour
    
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Frequent Start Hour:', popular_hour)
        
    
    #display count based on filter & plots  
    
    #count_month = df['month'].value_counts()
    #count_day = df['day_of_week'].value_counts()
    
    ##Need to position the output better???
    #print('Month Count:', count_month)
    
    #print('Day Count:', count_day) 
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    #while True:
        #q1 = input('Would you like to see some station statistics: yes or no? ').lower()
        #if q1 not in ('yes', 'no'):
            #print('Not an appropriate choice.')
        #else:
        #    #if q1.lower()=='yes':
                #break 
            #else:
                #restart = input('Would you like to restart? Enter yes or no. ')
                #if restart.lower() != 'yes':
                    #quit()  
        


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    start_station = df['Start Station'].mode()[0]
    print('Most common Start Station:', start_station)

    # display most commonly used end station
    
    end_station = df['End Station'].mode()[0]
    print('Most common End Station:', end_station)


    # display most frequent combination of start station and end station trip
    df['start_end_station_combo'] = df['Start Station'] + ' : ' + df['End Station']

    start_end_station_combo = df['start_end_station_combo'].value_counts().idxmax()
    print('Most frequent combination of start station and end station trip: ', start_end_station_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # display total travel time
    df['Duration'] = df['End Time']-df['Start Time']
    total_travel_time = df['Duration'].sum()
    print('Total travel time based on inputs: ', total_travel_time)
    

    # display mean travel time
    mean_travel_time = df['Duration'].mean()
    print('Mean travel time based on inputs: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(gender)


    # Display youngest, oldest, and most common age
    from datetime import date
    current_year = date.today().year

    youngest_birth_year = df['Birth Year'].max()
    oldest_birth_year = df['Birth Year'].min()
    most_common_birth_year = df['Birth Year'].value_counts().idxmax()


    yongest_age = current_year - youngest_birth_year
    oldest_age = current_year - oldest_birth_year
    most_common_age = current_year - most_common_birth_year  


    print('Yongest age: ', yongest_age)
    print('Oldest age: ', oldest_age)
    print('Most common age: ', most_common_age)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def look_at_data(df):
    pd.set_option('display.max_columns',200)
    look_at_data = input('Would you like to see the first 5 rows of the dataset? Enter y or n: ').lower()
    start_loc = 0
    while (look_at_data in ['yes','y']):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        look_at_data = input('Do you wish to see more? Enter y to see the next 5 rows: ').lower()
        continue
        
    
    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        look_at_data(df)
        station_stats(df)
        look_at_data(df)
        trip_duration_stats(df)
        look_at_data(df)
        user_stats(df)
        look_at_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
