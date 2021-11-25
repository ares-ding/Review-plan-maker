import Charge
import datetime
import Patch_1

while True:
    print('——————复习计划——————')

    print('1.该天该笔记往后的复习计划')
    print('2.该月该笔记往后的复习计划')
    print('3.查询某天的笔记复习计划')

    choice=int(input(':'))
    if choice ==1 :
        date01 = datetime.date.today()
        plan=Charge.review_time(str(date01.month)+'-'+str(date01.day))
        print('复习计划如下：\n',plan)
        break
    elif choice ==2:
        month=datetime.date.today()
        months=str(month.month)+'-'
        print('复习计划如下：')
        for i in range(1,Patch_1.day()+1):
            plan=Charge.review_time(months+str(i))
            print(plan)
        break
    elif choice ==3:
        date02=input('请输入笔记的日期(格式：12-07)：')
        print('复习计划如下：')
        plan=Charge.review_time(date02)
        print(plan)
        break
    else:
        print('不存在的编号，请重新输入！\n\n\n')


