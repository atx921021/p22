import time
import pandas as pd
import numpy as np

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
    while city == 'chicago'or 'new york city'or 'washington' :
       
        filename = CITY_DATA(city)
        df = pd.read_csv(filename)
    

    # TO DO: get user input for month (all, january, february, ... , june)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        if day != 'all':
            day = df[df['day_of_week'] == day.title()]


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
    while city == 'chicago'or 'new york city'or 'washington' :
        
        filename = CITY_DATA(city)
        df = pd.read_csv(filename)
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    while city == 'chicago'or 'new york city'or 'washington' :
       
        filename = CITY_DATA(city)
        df = pd.read_csv(filename)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode()[0]


    # TO DO: display the most common day of week
        df['day'] = df['Start Time'].dt.weekday_name
        popular_day = df['day'].mode()[0]


    # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    while city == 'chicago'or 'new york city'or 'washington' :
       
        filename = CITY_DATA(city)
        df = pd.read_csv(filename)
        df['start station'].value_counts()
        most commonly used start station = df['start station'].value_counts()


    # TO DO: display most commonly used end station
        most commonly used end station = df['end station'].value_counts()


    # TO DO: display most frequent combination of start station and end station trip
        df1 = df['start station'].join(df['end station'],on=col1,how='inner')
        df1.value_counts()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    while city == 'chicago'or 'new york city'or 'washington' :
       
        filename = CITY_DATA(city)
        df = pd.read_csv(filename)
        total travel time = df['Trip Duration'].sum()


    # TO DO: display mean travel time
        mean travel time = df['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    filename = CITY_DATA(city)
    df = pd.read_csv(filename)
    user_types = df['User Type'].value_counts()


    # TO DO: Display counts of gender
    counts of gender = df['Gender'].value_counts()


    # TO DO: Display earliest, most recent, and most common year of birth
    most common year of birth = df['Birth Year'].mode()[0]
    earliest = df['Birth Year'].min()
    most recent = df['Birth Year'].max()
    


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
