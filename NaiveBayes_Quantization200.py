zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
import csv

f = open('/Users/rohanseth/Desktop/mnist_train.csv')
csv_f = csv.reader(f)
for row in csv_f:
    if (row[0] == '0'):
        zero = zero + 1
    elif (row[0] == '1'):
        one = one + 1
    elif(row[0] =='2'):
        two = two + 1
    elif(row[0] == '3'):
        three = three + 1
    elif(row[0] == '4'):
        four = four + 1
    elif(row[0] == '5'):
        five = five + 1
    elif(row[0] == '6'):
        six = six + 1
    elif(row[0] =='7'):
        seven = seven + 1
    elif(row[0] == '8'):
        eight = eight + 1
    elif(row[0] == '9'):
        nine = nine + 1

total = zero + one + two + three + four + five + six + seven + eight + nine
print("Zero", zero)        
print("One:", one)
print("Two:", two)
print("Three:", three)
print("Four:", four)
print("Five:", five)
print("Six:", six)
print("Seven:", seven)
print("Eight:", eight)
print("Nine:", nine)
print("Total", total)


#Probability of pixel n such that digit 0 has occured
x = [0]*7665
temp1 = 0
#ans = 1
#ans = [1] * 785
ans0 = [[ 1 for i in range(785)] for j in range(10)]
ans1 = [[ 1 for i in range(785)] for j in range(10)]



    
## for number 1

'''
for x in range(1, 784):
    temp10 = 0
    temp20 = 0
    temp11 = 0
    temp21 = 0
    temp12 = 0
    temp22 = 0
    temp13 = 0
    temp23 = 0
    temp14 = 0
    temp24 = 0
    temp15 = 0
    temp25 = 0
    temp16 = 0
    temp26 = 0
    temp17 = 0
    temp27 = 0
    temp18 = 0
    temp28 = 0
    temp19 = 0
    temp29 = 0
    f = open('/Users/rohanseth/Desktop/mnist_train.csv')
    csv_f = csv.reader(f)
    for row in csv_f:
        #print(csv_f.line_num,"pixel:",x)
        if (row[0] == '0'):
            if(int(row[x]) > 200):
                temp10 = temp10 + 1
            else:
                temp20 = temp20 + 1
        elif (row[0] == '1'):
            if(int(row[x]) >200):
                temp11 = temp11 + 1
            else:
                temp21 = temp21 + 1
        elif (row[0] == '2'):
            if(int(row[x]) > 200):
                temp12 = temp12 + 1
            else:
                temp22 = temp22 + 1
        elif (row[0] == '3'):
            if(int(row[x]) > 200):
                temp13 = temp13 + 1
            else:
                temp23 = temp23 + 1
        elif (row[0] == '4'):
            if(int(row[x]) > 200):
                temp14 = temp14 + 1
            else:
                temp24 = temp24 + 1
        elif (row[0] == '5'):
            if(int(row[x]) > 200):
                temp15 = temp15 + 1
            else:
                temp25 = temp25 + 1
        elif (row[0] == '6'):
            if(int(row[x]) > 200):
                temp16 = temp16 + 1
            else:
                temp26 = temp26 + 1
        elif (row[0] == '7'):
            if(int(row[x]) > 200):
                temp17 = temp17 + 1
            else:
                temp27 = temp27 + 1
        elif (row[0] == '8'):
            if(int(row[x]) > 200):
                temp18 = temp18 + 1
            else:
                temp28 = temp28 + 1
        elif (row[0] == '9'):
            if(int(row[x]) > 200):
                temp19 = temp19 + 1
            else:
                temp29 = temp29 + 1
    ans0[2][x] = ((temp12/two))
    ans0[3][x] = ((temp13/three))
    ans0[4][x] = ((temp14/four))
    ans0[5][x] = ((temp15/five))
    ans0[6][x] = ((temp16/six))
    ans0[7][x] = ((temp17/seven))
    ans0[8][x] = ((temp18/eight))
    ans0[9][x] = ((temp19/nine))
    ans0[1][x] = ((temp11/one))
    ans0[0][x] = ((temp10/zero))
    ans1[2][x] = ((temp22/two))
    ans1[3][x] = ((temp23/three))
    ans1[4][x] = ((temp24/four))
    ans1[5][x] = ((temp25/five))
    ans1[6][x] = ((temp26/six))
    ans1[7][x] = ((temp27/seven))
    ans1[8][x] = ((temp28/eight))
    ans1[9][x] = ((temp29/nine))
    ans1[1][x] = ((temp21/one))
    ans1[0][x] = ((temp20/zero))
    print("Pixel",x)

myFil0 = open('/Users/rohanseth/Desktop/mnist_conditional_p_200_a0_v2.csv', 'w')  
with myFil0:  
   writer = csv.writer(myFil0)
   writer.writerows(ans0)        
#print(ans[1])

myFil1 = open('/Users/rohanseth/Desktop/mnist_conditional_p_200_a1_v2.csv', 'w')  
with myFil1:  
   writer = csv.writer(myFil1)
   writer.writerows(ans1)        
#print(ans[1])
'''

i = 0
h = open('/Users/rohanseth/Desktop/mnist_conditional_p_200_a0_v2.csv')
csv_h = csv.reader(h)
for row in csv_h:
    ans0[i] = row
    i=i+1;
i=0
n = open('/Users/rohanseth/Desktop/mnist_conditional_p_200_a1_v2.csv')
csv_n = csv.reader(n)
for row in csv_n:
    ans1[i] = row
    i=i+1;

loss = 0
g = open('/Users/rohanseth/Desktop/mnist_test.csv')
csv_g = csv.reader(g)

for row in csv_g:
    accum0 = 1.0
    accum1 = 1.0
    accum2 = 1.0
    accum3 = 1.0
    accum4 = 1.0
    accum5 = 1.0
    accum6 = 1.0
    accum7 = 1.0
    accum8 = 1.0
    accum9 = 1.0
    for x in range(1, 784):
        if  ((int(row[x])>50)):
            accum0 = accum0 * float(ans0[0][x])
            accum1 = accum1 * float(ans0[1][x])
            accum2 = accum2 * float(ans0[2][x])
            accum3 = accum3 * float(ans0[3][x])
            accum4 = accum4 * float(ans0[4][x])
            accum5 = accum5 * float(ans0[5][x])
            accum6 = accum6 * float(ans0[6][x])
            accum7 = accum7 * float(ans0[7][x])
            accum8 = accum8 * float(ans0[8][x])
            accum9 = accum9 * float(ans0[9][x])
        else:
            accum0 = accum0 * float(ans1[0][x])
            accum1 = accum1 * float(ans1[1][x])
            accum2 = accum2 * float(ans1[2][x])
            accum3 = accum3 * float(ans1[3][x])
            accum4 = accum4 * float(ans1[4][x])
            accum5 = accum5 * float(ans1[5][x])
            accum6 = accum6 * float(ans1[6][x])
            accum7 = accum7 * float(ans1[7][x])
            accum8 = accum8 * float(ans1[8][x])
            accum9 = accum9 * float(ans1[9][x])
            

    accum0 = ((accum0*zero)/total)
    accum1 = ((accum1*one)/total)
    accum2 = ((accum2*two)/total)
    accum3 = ((accum3*three)/total)
    accum4 = ((accum4*four)/total)
    accum5 = ((accum5*five)/total)
    accum6 = ((accum6*six)/total)
    accum7 = ((accum7*seven)/total)
    accum8 = ((accum8*eight)/total)
    accum9 = ((accum9*nine)/total)
    
    if accum0 > max(accum1, accum2, accum3, accum4, accum5, accum6, accum7, accum8, accum9):
        if(row[0] == '0'):
            loss = loss + 0
            #print("I predicted rightly, 0")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 0")
    if accum1 > max(accum0, accum2, accum3, accum4, accum5, accum6, accum7, accum8, accum9):
        if(row[0] == '1'):
            loss = loss + 0
            #print("I predicted rightly, 1")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 1")


    if accum2 > max(accum1, accum0, accum3, accum4, accum5, accum6, accum7, accum8, accum9):
        if(row[0] == '2'):
            loss = loss + 0
            #print("I predicted rightly, 2")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 2")

    if accum3 > max(accum1, accum2, accum0, accum4, accum5, accum6, accum7, accum8, accum9):
        if(row[0] == '3'):
            loss = loss + 0
            #print("I predicted rightly, 3")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 3")

    if accum4 > max(accum1, accum2, accum3, accum0, accum5, accum6, accum7, accum8, accum9):
        if(row[0] == '4'):
            loss = loss + 0
            #print("I predicted rightly, 4")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 4")

    if accum5 > max(accum1, accum2, accum3, accum4, accum0, accum6, accum7, accum8, accum9):
        if(row[0] == '5'):
            loss = loss + 0
            #print("I predicted rightly, 5")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 5")

    if accum6 > max(accum1, accum2, accum3, accum4, accum5, accum0, accum7, accum8, accum9):
        if(row[0] == '6'):
            loss = loss + 0
            #print("I predicted rightly, 6")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 6")

    if accum7 > max(accum1, accum2, accum3, accum4, accum5, accum6, accum0, accum8, accum9):
        if(row[0] == '7'):
            loss = loss + 0
            #print("I predicted rightly, 7")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 7")

    if accum8 > max(accum1, accum2, accum3, accum4, accum5, accum6, accum7, accum0, accum9):
        if(row[0] == '8'):
            loss = loss + 0
            #print("I predicted rightly, 8")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 8")

    if accum9 > max(accum1, accum2, accum3, accum4, accum5, accum6, accum7, accum8, accum0):
        if(row[0] == '9'):
            loss = loss + 0
            #print("I predicted rightly, 9")
        else:
            loss = loss + 1
            #print("I predicted wrongly, 9")
print("loss",loss)

