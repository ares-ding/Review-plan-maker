#判断闰年和平年
import datetime
def day():

    year01=datetime.date.today()
    year=year01.year
    if year%4==0 and year%100!=0 or year%400==0:
    #print('今年的年份是：'+str(year)+',闰年')
        month01=datetime.date.today()
        month=month01.month
        if month==1 or month==3 or month==5 or month==7 or month ==8 or month== 10 or month==12:
            days=31
        #print('该月份是'+str(month)+'有：'+str(days)+'天.')
        elif month==2:
            days=29
        #print('该月份是'+str(month)+'有：'+str(days)+'天.')
        else:
            days=30
        #print('该月份是'+str(month)+'有：'+str(days)+'天.')
    
    else:
    #print('今年的年份是：'+str(year)+',平年')
        month01=datetime.date.today()
        month=month01.month
        if month==1 or month==3 or month==5 or month==7 or month ==8 or month== 10 or month==12:
            days=31
        #print('该月份是'+str(month)+'有：'+str(days)+'天.')
        elif month==2:
            days=28
        #print('该月份是'+str(month)+'有：'+str(days)+'天.')
        else:
            days=30
        #print('该月份是'+str(month)+'有：'+str(days)+'天.')
    return days
    