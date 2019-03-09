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
    
while True:
       city = input('Pick a city! Chicago, New York or Washington. \n> ').lower()
       if city in CITIES:
           break
    
       
    # TO DO: get user input for month (all, january, february, ... , june)
    month = get_user_input('Next, pick a month!'\
                    'to pick no month say\'all\'. \n(e.g. all, january, february, march, april, may, june) \n> ', MONTHS)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_user_input('Next, provide a day of the week!'\
                   ' to pick no month say \'all\'. \n(e.g. all, monday, sunday) \n>', DAYS)

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most commonly chosen month:", common_month)

    # TO DO: display the most common day of week
   common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most commonly chosen day of week is :", common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].value_counts().idxmax()
    print("The most commonly chosen start hour is:", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("The start station people used most was:", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The end station people used most was:", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("People most frequently used this combination of start station and end station: {}, {}"\
            .format(common_start_end_station[0], common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()


    # TO DO: Display counts of gender
    print("Counts of gender:\n")
    gender_count = df['gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    most_recent = birth_year.max()
    print("We determined the most recent birth year to be:", most_recent)
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)

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
