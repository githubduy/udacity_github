import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Convert Month from text into value int.
MONTH_DATA = {
    'january': 1, 
    'february': 2, 
    'march': 3, 
    'april': 4, 
    'may': 5, 
    'june': 6, 
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 7,
}
# array day of data
DAY_DATA = {
    'monday'  : 2, 
    'tuesday' : 3, 
    'wednesday': 4, 
    'thursday' : 5, 
    'friday'   : 6, 
    'saturday' : 7, 
    'sunday'   : 8
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city  = ''
    month = ''
    day   = ''
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington)
    # HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago', 'new york city', 'washington']

    while True:
        city = input("Please enter a city (Chicago, New York City, Washington): ").lower()
        if city in valid_cities:
            break
        else:
            print(f" \'{city}\' is invalid input. Please try again with {valid_cities}")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    valid_months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Please enter a month: ").lower()
        if month.lower() == 'all':
            print ('Your choice is \'all\'. It\'s mean you dont filter by month.')
            break
        elif month.lower() in valid_months:
            #print("You entered:", month)
            break
        else:
            print(f"Invalid input. Please try again with {valid_months}.")



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day = input("Please enter a day: ").lower()
        if day == 'all':
            print ('Your choice is \'all\'. It\'s mean you dont filter by day.')
            break
        elif day in valid_days:
            print("You entered:", day)
            break
        else:
            print(f"Invalid input. Please try again with {valid_days}.")

    print(f" Your Enter is: {city} city, at {day} day, in {month} month.")
    #   print('-'*40)
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
    # Load All for the City into a DataFrame
    file_data = CITY_DATA[city]
    df_CityData = pd.read_csv(file_data)

    # Format "Start Time" column as datetime
    df_CityData['Start Time'] = pd.to_datetime(df_CityData['Start Time'])
    
    # Copy from "start time" to new column Month.
    df_CityData['Month']   = df_CityData['Start Time'].dt.month
    # Copy from "start time" to new column WeekDay.
    df_CityData['WeekDay'] = df_CityData['Start Time'].dt.dayofweek
    # Copy from "start time" to new column hour.
    df_CityData['Hour']    = df_CityData['Start Time'].dt.hour
    
    #
    # Start Filter Data
    #
    filterd_data = df_CityData
    
    if month.lower() == 'all':
        # If Month = All, dont need filter.
        pass
    else:
        # Filter Data with month.
        get_month = MONTH_DATA[month]
        filterd_data = df_CityData[df_CityData['Month'] == get_month]
    
    if day.lower() == 'all':
        # Dont need filter day special.
        pass
    else:
        # Filter Data with month.
        get_day = MONTH_DATA[day]
        filterd_data = filterd_data[filterd_data['WeekDay'] == get_day]
    #print(filterd_data)
    return filterd_data
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # The mode of a set of values is the value that appears most often. It can be multiple values.
    mode_df_month = df['Month'].mode()
    most_common_month_travel = mode_df_month[0]

    # TO DO: display the most common day of week
    mode_df_day = df['WeekDay'].mode()
    most_common_day_travel = mode_df_day[0]

    
    # TO DO: display the most common start hour
    mode_df_hour = df['Hour'].mode()
    most_common_hour_travel = mode_df_hour[0]
    
    print("Time stats,Display most time for travel!\n")
    print(f"  > Start at month: {most_common_month_travel} ")
    print(f"  > Start at day of week: {most_common_day_travel} ")
    print(f"  > Start at hour: {most_common_hour_travel} ")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input("Press Enter to continue...")


def time_stats_new(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # The mode of a set of values is the value that appears most often. It can be multiple values.
    mode_df_month = df['Month'].mode()
    most_common_month_travel = mode_df_month[0]

    # TO DO: display the most common day of week
    mode_df_day = df['WeekDay'].mode()
    most_common_day_travel = mode_df_day[0]

    
    # TO DO: display the most common start hour
    mode_df_hour = df['Hour'].mode()
    most_common_hour_travel = mode_df_hour[0]
    
    print("Time stats,Display most time for travel!\n")
    print(f"  > Start at month: {most_common_month_travel} ")
    print(f"  > Start at day of week: {most_common_day_travel} ")
    print(f"  > Start at hour: {most_common_hour_travel} ")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input("Press Enter to continue...")
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_df_used_start_station = df['Start Station'].mode()
    most_common_used_start_station = mode_df_used_start_station[0]

    # TO DO: display most commonly used end station
    mode_df_used_endstation = df['End Station'].mode()
    most_common_used_endstation = mode_df_used_endstation[0]

    # TO DO: display most frequent combination of start station and end station trip
    # Compbination start and end station into Trip column
    df['Trip'] = 'From' + df['Start Station'] + ' to ' + df['End Station']
    mode_df_trip = df['Trip'].mode()
    most_common_used_trip = mode_df_trip[0]

    print("Station_stats, we have most common station:")
    print(f" > Start station: {most_common_used_start_station}")
    print(f" > End station: {most_common_used_endstation}")
    print(f" > Top 1 Trip: {most_common_used_trip}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input("Press Enter to continue...")
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total (sum) travel time
    total_trip_duration_in_secods = df['Trip Duration'].sum()
    travel_in_hours = total_trip_duration_in_secods / 3600
    print(" > Total travel time:", travel_in_hours)
    
    # TO DO: display mean travel time
    mean_trip_duration_in_secods = df['Trip Duration'].mean()
    mean_travel_time = mean_trip_duration_in_secods  / 3600
    
    print(" > Mean travel time:", mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    input("Press Enter to continue...")
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print(f' > Count of user types: {counts_of_user_types}.')

    # TO DO: Display counts of gender
    counts_of_gender = df['Gender'].value_counts()
    print(f' > Count of user gender: {counts_of_gender}.')


    # TO DO: Display earliest, most recent, and most common year of birth
    # 1. earliest year of birth
    earliest_year_of_birth = df['Birth Year'].min()
    # 2. most recent year of birth
    most_recent_year_of_birth = df['Birth Year'].max()
    # 3. most common year of birth
    mode_df_year_of_birth =  df['Birth Year'].mode()
    most_common_year_of_birth = mode_df_year_of_birth.values[0]

    print(f" > Earliest year of birth:", earliest_year_of_birth)
    print(f" > Most recent year of birth:", most_recent_year_of_birth)
    print(f" > Most common year of birtth:", most_common_year_of_birth)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press Enter to continue...")

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
