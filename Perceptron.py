
w0=0.0
w1=0.0
b=0.0  #bias
import csv
f = open('/Users/rohanseth/Desktop/iris_train.csv')
csv_f = csv.reader(f)
for row in csv_f:
    a = (float(row[0])*w0 + float(row[1])*w1) + b
    if ((float(row[2])*a)<=0):
        w0 = w0 + float(row[2])*float(row[0])
        w1 = w1 + float(row[2])*float(row[1])
        b = b + float(row[2])

print("W[0] is",w0)
print("W[1] is",w1)
print("b is",b)
 
