blocked_days_map = {'Sunday':[],
                     'Monday' : ['kaushik','aditya','gaurang','jay','swapnil','sagar','nitin'],
                    'Tuesday' :['durvesh','tanmay'],
                    'Wednesday':['gaurang','nitin'] ,
                    'Thursday':['kaushik','durvesh','tanmay'],
                    'Friday':['gaurang','nitin'],
                    'Saturday':[]}


names_map = {'durvesh':0,'tanmay':0,'jay':0,'swapnil':0,'sagar':0,'nitin':0,'gaurang':0,'aditya':0,'kaushik':0}

names_list = list(names_map)

import datetime
import calendar

time = datetime.datetime.now()
time +=datetime.timedelta(days= 1)

name_list_length = len(names_map)

prev_set = []
for i in range(31) :
 day = calendar.day_name[time.weekday()]
 valid_names = [name for name in names_list if name not in blocked_days_map.get(day)]

 time_list =[]
 for name in valid_names:
  time_list.append(names_map.get(name))

 time_list = sorted(time_list)
 low_1 ,low_2 = time_list[:2]
 name_set = []

 for k,v in names_map.items() :
     if(v == low_1 and  k in valid_names):
         name_set.append(k)
         break

 for k,v in names_map.items() :
     if(v == low_2 and k in valid_names):
         if  k not in name_set:
          name_set.append(k)
          break

 for name in name_set :
      names_map[name] += 1

 print(time.date(),*name_set )
 time += datetime.timedelta(days= 1)

print(names_map)







