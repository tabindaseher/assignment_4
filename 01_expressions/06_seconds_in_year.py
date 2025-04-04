
def main():
 # Constants
 DAYS_IN_YEAR = 365         # Number of days in a year
 HOURS_IN_DAY = 24          # Number of hours in a day
 MINUTES_IN_HOUR = 60       # Number of minutes in an hour
 SECONDS_IN_MINUTE = 60     # Number of seconds in a minute

# Calculate the total number of seconds in a year
 seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

# Print the result in a nice format
 print(f"There are {seconds_in_year} seconds in a year!")



if __name__ == '__main__':
 main()