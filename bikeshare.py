import time
import pandas as pd
import numpy as np
import sys
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    conver_to_lower = [month.lower() for month in months]
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    conver_to_lower_day = [day.lower() for day in days]

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input(
            "Would you like to see data for Chicago, New York, or Washington? "))
        if city in cities:
            break
        else:
            print('That\'s not a valid input')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input(
            'Which month - January, February, March, April, May, or June you want to see the data? '))
        if month in conver_to_lower:
            break
        else:
            print('That\'s not a valid input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input(
            'Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday you want to see the data? '))
        if day in conver_to_lower_day:
            break
        else:
            print('That\'s not a valid input')

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

# TO DO: convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# To DO: extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

# TO DO:  filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
# TO DO: filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

# TO DO: Display more raw data


def moreData(city):
    df = pd.read_csv(CITY_DATA[city])
    start = 0
    end = 5
# TO DO: prompt the user whether they would like want to see the raw data.
    while True:
        rowData = str(
            input("would like want to see the raw data? Enter yes or no.\n "))
        if(rowData == 'yes'):
            print(df.iloc[start:end])
            start += 5
            end += 5
        else:
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    common_month = df['month'].mode()[0]
    print('The most common month', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day', common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]

    print('The most common hour', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The moset Commonly used start station',
          df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print('The most commonly used end station', df['End Station'].mode()[0])
    groub_station_and_trip = df.groupby(['Start Station', 'Trip Duration'])
    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip',
          groub_station_and_trip.size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration']
    print('The total travel time', total.sum())

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration']
    print('The mean travel time', mean_travel.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

#   TO DO: Condidtion to show a user data info only for chicago and new york
    if city == 'chicago' or city == 'new york city':
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('Gender counts', gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year'].min()
        birth_year_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The earliest year of birth', birth_year)
        print('The most recent year of birth', birth_year_recent)
        print('The most common year of birth', most_common)

    elif city == 'washington':
        print('no Data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        moreData(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
