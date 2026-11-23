for i in range (1,5):

    total_sales = 0

    print ("salesperson",i)

    for j in range (1,6):

        sales = int (input("enter daily sales "))

        total_sales = total_sales + sales 

    print ("total sales of salesperson",i,"=",total_sales)
