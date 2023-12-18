"""Generate sales report showing total melons each salesperson sold."""



def sales_report(sales):

    salespeople = [] 
    melons_sold = [] 

    with open(sales) as sales_log:
        for line in sales_log:
            line = line.strip()
            entries = line.split('|')

            salesperson = entries[0]
            melons = int(entries[2])

            if salesperson in salespeople:
                position = salespeople.index(salesperson)
                melons_sold[position] += melons
            else: 
                salespeople.append(salesperson)
                melons_sold.append(melons)
        
        for i in range(len(salespeople)):
            print(f'{salespeople[i]} sold {melons_sold[i]} melons')


sales_report("sales-report.txt")