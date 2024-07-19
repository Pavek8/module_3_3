def print_params(a,b,c):
    print(a,b,c)


print_params(1,2,True)
print_params(1,5,'Privet')
#print_params(1,2)
#print_params()
#print_params(1,2,3,4)
#print_params(b = 25)
#print_params(c = [1,2,3])
print_params('Copybara',55,'User')
values_list=[100,'Pavel Kostin',False]
print_params(*values_list)
values_dict={ 'a':33, 'b':44, 'c':55}
print_params( **values_dict )

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

