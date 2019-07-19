import csv

with open('/Users/jenny/Desktop/citibike/2013-07-CitiBiketripdata.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # print(citibike)

    customer_count = 0
    subscriber_count = 0

    for row in reader:
        for usertags in row:
            if usertags == "Customer" :
                customer_count +=1
            else: 
                # usertags == "Subscriber"
                subscriber_count +=1
    print (f'Customer count: {customer_count}, Subscriber count: {subscriber_count}')