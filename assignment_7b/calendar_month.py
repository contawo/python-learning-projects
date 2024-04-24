import math


def day_of_week(day, month, year):
    # Zeller’s congruence expects the month values to be in the range 3 to 14 (where March is 3, April is 4, and so on
    if month < 3:
        month += 12
        year -= 1

    h = (day + math.floor((13 * (month + 1)) / 5) + year + math.floor(year / 4) - math.floor(year / 100) + math.floor(year / 400)) % 7
    return (h + 5) % 7 + 1


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
        return True
    return False


def month_num(month_name):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for i in range(0, len(months)):
        if month_name.lower() == months[i].lower():
            return i + 1

def num_days_in(month_num, year):
    days_in_months = [31, 
        29 if is_leap(year) else 28, 
    31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return days_in_months[month_num - 1]

def num_weeks(month_num, year):
    first_day = day_of_week(1, month_num, year)
    
    if month_num == 2:
        leap_year = is_leap(year)
        if leap_year:
            return 5
        else:
            return 4 if (first_day == 1) else 5
        
    else:
        days = num_days_in(month_num, year)
        if days == 30:
            return 6 if (first_day == 7) else 5
        else:
            return 6 if (first_day >= 6) else 5


def week(week_num, start_day, days_in_month):
    weekdays = 7 - (start_day - 1)
    days_left = days_in_month
    current_day = 1
    
    output = []
    
    for i in range(week_num):
        output = []
        
        for i in range(weekdays):
            if current_day <= 9:
                output.append(f" {current_day} ")
            else:
                output.append(f"{current_day} ")
            current_day = current_day + 1
            
        days_left = days_in_month - current_day
        weekdays = 7 if (days_left >= 7) else (days_left + 1)
        
    return "".join(output)

def main():
    month = input("Enter month:\n")
    year = int(input("Enter year:\n"))
    
    month_number = month_num(month)
    week_number = num_weeks(month_number, year)
    month_days = num_days_in(month_number, year)
    
    start_day = day_of_week(1, month_number, year)
    
    print(month.title())
    print("Mo Tu We Th Fr Sa Su")
    
    for w in range(1, week_number + 1):
        weeks_output = week(w, start_day, month_days)
        if w == 1:
            week_days = weeks_output.split("  ")
            spaces = 7 - len(week_days)
            
            while spaces > 0:
                print("  ", end=" ")
                spaces = spaces - 1
            
            for w_d in week_days:
                num = int(w_d.replace(" ", ""))
                print(f" {num}", end=" ")
                
            print()
        else:
            print(weeks_output)
    
if __name__=='__main__':
    main()






