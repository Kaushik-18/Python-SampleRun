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
blocked_days_map = {'Sunday': ['nitin'],
                    'Monday': ['gaurang'],
                    'Tuesday': ['nitin','sagar', 'jay', 'kaushik', 'gaurang', 'aditya'],
                    'Wednesday': ['kaushik', 'gaurang', 'aditya','nitin'],
                    'Thursday': ['aditya', 'nitin', 'jay','sagar'],
                    'Friday': [],
                    'Saturday': []}

# map to maintain number of turns for each person.
names_map = {'gaurang': 0, 'kaushik': 0, 'jay': 0, 'sagar': 0,
             'nitin': 0, 'aditya': 0, 'swapnil': 0,'tanmay':0,'durvesh':0}
names_list = sorted(list(names_map))
# range of days
days_range = int(input('enter day range '))
# getting current date and updating by 1
time = datetime.datetime.now()
time += datetime.timedelta(days=1)
name_list_length = len(names_map)
# writing to a file
s_file = open('schedule.txt', 'w')

for i in range(days_range):
    day = calendar.day_name[time.weekday()]
    valid_names = [name for name in names_list if name not in blocked_days_map.get(day)]
    # obtains a list of count of turns , take lowest 2 values from list and find the names from valid set
    # corresponding to the two values
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

    s_file.write('{0} {1} {2}'.format(time.date(), *name_set))
    s_file.write('\n')
    time += datetime.timedelta(days=1)

s_file.close()
# print final count of to confirm
print(names_map)
