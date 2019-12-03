import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to explore data of Chicago, New York City or Washington?')
    city = input('Enter name of city:')
    city = city.lower()
    while city not in CITY_DATA:
        city = input('Wrong input!!!. Please re-enter one of the cities mentioned (Chicago, New York City and Washington): ')
    print('Great! We are checking data for', city)

    
    # TO DO: get user input for month (all, january, february, ... , june)
    monthes = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('Which month would you like to see data for?')
    month = input('Please enter a month between january and june only or select "all" for all: ')
    month = month.lower()
    while month not in monthes:
        print('Oops! Missing!')
        month = input('Please re-enter a chosen month mentioned or "all" for all: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayz = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('Which day of the week would you like to see data for?')
    day = input('Enter day of the week or "all" for all days:')
    day = day.lower()
    while day not in dayz:
        print('Oops! Missing!')
        day = input('Please re-enter a correct day of the week or "all" for all: ')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = (df['Start Time']).dt.month

    popular_month = (df['month']).mode()[0]

    print('Most Common Month of Travel is', popular_month)



    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = (df['Start Time']).dt.weekday_name
    popular_day = (df['day_of_week']).mode()[0]
    print('Most Common Day of Travel is', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = (df['Start Time']).dt.hour
    popular_hour = (df['hour']).mode()[0]
    print('Most Common Hour of Travel is', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print()

    # TO DO: display most commonly used start station
    popular_startstation = df.loc[:,"Start Station"].mode()
    print('Most Commonly Used Start Station is', popular_startstation)
    print()

    # TO DO: display most commonly used end station
    popular_endstation = df.loc[:,"End Station"].mode()
    print('Most Commonly Used End Station is', popular_endstation)
    print()

    # TO DO: display most frequent combination of start station and end station trip
    startend_combination = ('from '+ df["Start Station"] + ' to ' + df["End Station"]).mode()[0]
    print('Most Common Combination of Start Station and End Station trip is', startend_combination)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print()
    # TO DO: display total travel time
    total_traveltime = df["Trip Duration"].sum()
    total_timestamp = str(datetime.timedelta(seconds=int(total_traveltime)))
    print('The total travel time was', total_timestamp)

    print()

    # TO DO: display mean travel time
    mean_traveltime = df["Trip Duration"].mean()
    mean_timestamp = str(datetime.timedelta(seconds=int(mean_traveltime)))
    print('The average travel time was', mean_timestamp)

    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Types of users:\n', user_types)
    print()
    
    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print('Gender of users:\n', gender)
    else:
        print('Gender column does not exist in this dataset')

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest, most_recent, most_common = df.loc[:,"Birth Year"].min(), df.loc[:,"Birth Year"].max(), df.loc[:,"Birth Year"].mode()
        print('The oldest user was born in the year ', int(earliest))
        print()
        print('The youngest user was born in the year ', int(most_recent))
        print()
        print('The year group that ride the most are people born in ', int(most_common))
        print()
    else:
        print('Birth Year column does not exist in this dataset')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 5
        #df.shape[0] gives the number of rows
        while(i< df.shape[0]):
            rawdata = input('Hey! The complete data of this analysis is avaiable for you. Enter "yes" if you would like to explore more. \nEnter "no" if you\'ve seen enough:   ')
            if rawdata == 'yes' :
                print(df.head(i))
                i+=5#increment 5

            else :
             #if input is not 'yes' end loop
                break;

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
