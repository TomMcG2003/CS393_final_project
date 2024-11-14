from pybaseball import statcast

thing = statcast(start_dt='2019-06-24', end_dt='2019-06-25').columns

print(thing)
