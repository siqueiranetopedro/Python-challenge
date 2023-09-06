import csv


with open("/Users/pedrosiqueira/budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    number_of_months = 0
    total_profit = 0
    total_change_in_profit = 0
    Greatest_change_profit = 0
    Greatest_change_date = 0
    Greatest_decrease_profit = 0
    Greatest_decrease_date = 0
    for row in csvreader:
        number_of_months = number_of_months + 1
        date = row[0]
        profit = int(row[1]) #pulling the second column
        if number_of_months > 1:#calculate the profit after month number 1"skips"
            change_in_profit = profit - previous_profit
            total_change_in_profit = total_change_in_profit + change_in_profit
            if change_in_profit > Greatest_change_profit:
                Greatest_change_profit = change_in_profit
                Greatest_change_date = date
            if change_in_profit < Greatest_decrease_profit:
                Greatest_decrease_profit = change_in_profit
                Greatest_decrease_date = date
        total_profit = total_profit + profit # sum of all values in second column
        print(row)
        previous_profit = profit

    #count the line for the months
    print("number of months",number_of_months)
    
    #net total amount profit/loss
    print("profit and losses",total_profit)
    
    #change profit/loses
    print("average change in profit" , total_change_in_profit / (number_of_months - 1))
    
    #greatest increase profit
    print("date",Greatest_change_date,"greatest change profit", Greatest_change_profit)
    
    #greatest decrease profit
    print("date",Greatest_decrease_date,"greatest decrease profit", Greatest_decrease_profit)
    