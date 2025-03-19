score = input('please input score(1-100) ...\n')
intValue = int(score)
if  90<= intValue <=100 :
    print('A')
elif 80 < intValue < 90:
    print('B')
elif 70< intValue < 80:
    print('C')
elif intValue <=0 or intValue >100 :
    print('input invalid')
else:
    print('D')