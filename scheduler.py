# script for scheduling cooking turns among roomates
# Requirement: Allocate turns to 2 people per day for given period of time (eg : 1 month) ,taking into account
# their availability on that day. try to allocate equal or near equal number of turns to each person

# Currently creating a hardcoded dictionary of days and names
# TODO take input directly from console for names,blocked days ,time period
# TODO current implementation needs 2-3 runs before near equality is achieved,
# TODO block by specific dates
import datetime
import calendar

# dictionary of unavailable members for each day of the week
blocked_days_map = {'Sunday': [],
                    'Monday': ['kaushik', 'aditya', 'gaurang', 'jay', 'swapnil', 'sagar', 'nitin'],
                    'Tuesday': ['durvesh', 'tanmay'],
                    'Wednesday': ['gaurang', 'nitin','swapnil'],
                    'Thursday': ['kaushik', 'durvesh', 'tanmay'],
                    'Friday': ['gaurang', 'nitin'],
                    'Saturday': []}

# map to maintain number of turns for each person.
names_map = {'durvesh': 0, 'tanmay': 0, 'jay': 0, 'swapnil': 0, 'sagar': 0, 'nitin': 0, 'gaurang': 0, 'aditya': 0,
             'kaushik': 0}

names_list = list(names_map)

days_range = 19

time = datetime.datetime.now()
time += datetime.timedelta(days=1)

name_list_length = len(names_map)

for i in range(days_range):
    day = calendar.day_name[time.weekday()]
    valid_names = [name for name in names_list if name not in blocked_days_map.get(day)]
# obtains a list of count of turns , take lowest 2 values from list and find the names from valid set corresponding to
#  the two values
    time_list = []
    for name in valid_names:
        time_list.append(names_map.get(name))

    time_list = sorted(time_list)
    low_1, low_2 = time_list[:2]
    name_set = []

    for k, v in names_map.items():
        if v == low_1 and k in valid_names:
            name_set.append(k)
            break

    for k, v in names_map.items():
        if v == low_2 and k in valid_names:
            if k not in name_set:
                name_set.append(k)
                break

    for name in name_set:
        names_map[name] += 1

    print(time.date(), *name_set)
    time += datetime.timedelta(days=1)

# print final count of to confirm
print(names_map)
