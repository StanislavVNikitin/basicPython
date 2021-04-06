
var_list = [False, 1, 1.2,'stroka',[1,2,3],('1',2,'3.1'),{1,2,3},{1:'1',2:'2',3:'3'}]
i = 0
print(var_list)
len_list = len(var_list)
while(len_list > i):
    print('Значение: ',var_list[i],' тип данных:',type(var_list[i]))
    i+=1
