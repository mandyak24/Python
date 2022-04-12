import datetime as dt

now = dt.datetime.now()
exit_time = now.replace(hour=19, minute=0,second=0)

if exit_time <now:
    print("Fuera de horario laboral")
else:
    horasRestantes=exit_time-now
    print(horasRestantes)