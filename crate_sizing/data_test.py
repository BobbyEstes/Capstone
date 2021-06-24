import datetime


my_data = [(datetime.date(2021, 6, 1), 28930, 'Mchafffey', 14467, '5431 Bell Rd', '', 'Auburn', 'CA', '95602', '', None, '3', '8', 'Freight Common Carrier', 'FedEx Freight Priority'), 
           (datetime.date(2021, 6, 1), 29403, 'Daffin add sample ', 14467, '5431 Bell Rd', '', 'Auburn', 'CA', '95602', '', None, '3', '8', 'Freight Common Carrier', 'FedEx Freight Priority'), 
           (datetime.date(2021, 6, 1), 30615, 'Mchafffey', 14467, '5431 Bell Rd', '', 'Auburn', 'CA', '95602', '', None, '3', '8', 'Freight Common Carrier', 'FedEx Freight Priority'), 
           (datetime.date(2021, 6, 1), 30689, 'Dunn - Add', 14467, '5431 Bell Rd', '', 'Auburn', 'CA', '95602', '', None, '3', '8', 'Freight Common Carrier', 'FedEx Freight Priority')]

new_data = []

# for l in my_data:
#     new_data.append([x.split(',') for x in l])
# print (new_data)

# for x in my_data:   
#     print (list(my_data[0])[1])
    #print (list(my_data[1])[1])
    #print (list(my_data[2])[1])
    #print (list(my_data[3])[1])

# for x in my_data:
#     new_data.append(list(x).strip()) 
    
# print(new_data) 
     
# for order in range(len(my_data)):
#     print(my_data[order][1])  
# print (my_data[0][1]) 
# print (my_data[0][2])
# print (len(my_data))
# print (my_data)

# for x in (my_data):
#     for y in x:
#         print (y[2])

for x in range(len(my_data)):
    print(my_data[x][1])
    