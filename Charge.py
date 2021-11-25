import datetime
def review_time(today):
    delta_list = [1,1,2,2,3,4,5,5] # 每两天复习的间隔
    review_day = []
    new_day = datetime.datetime.strptime(today, '%m-%d')
    for day in delta_list:
        new_day = datetime.datetime.strptime(new_day.strftime('%m-%d'),'%m-%d') + datetime.timedelta(days=day)
        review_day.append(new_day.strftime('%m.%d'))
    print('Today is ', today, 'review days are', review_day)
