# Hint:  use Google to find python function
import datetime as dt

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'
start = dt.datetime.strptime(date_start, '%m-%d-%Y')
end = dt.datetime.strptime(date_stop, '%m-%d-%Y')
print((end - start).days)

####b)  
date_start = '12312013'  
date_stop = '05282015'
start = dt.datetime.strptime(date_start, '%m%d%Y')
end = dt.datetime.strptime(date_stop, '%m%d%Y')
print((end - start).days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'
start = dt.datetime.strptime(date_start, '%d-%b-%Y')
end = dt.datetime.strptime(date_stop, '%d-%b-%Y')
print((end - start).days)

