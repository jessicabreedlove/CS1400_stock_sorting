global overall_max, overall_min, min_date, min_symbol, max_date, max_symbol
def main():
    global overall_max, overall_min, min_date, min_symbol, max_date, max_symbol
    stocks_data = open("stocks_data.csv", "r")
    stocks = {"AAPL" : [], "IBM": [], "MSFT": []}
    stocks_data.readline()

    for line in stocks_data:
        symbol, date, price = line.strip().split(",")
        stocks[symbol].append((date, float(price)))

    overall_max, overall_min = 0, 999999
    max_date, min_date = "", ""
    max_symbol, min_symbol = "", ""
    
    def find_max_min_ave (sym, stocks):
        global overall_max, overall_min, min_date, min_symbol, max_date, max_symbol
        max_aapl = max(stocks[sym], key = lambda x: x[1])
        if max_aapl[1] > overall_max:
            overall_max = max_aapl[1]
            max_date = max_aapl[0]
            max_symbol = sym
        min_aapl = min(stocks[sym], key = lambda x: x[1])
        if min_aapl[1] < overall_min:
            overall_min = min_aapl[1]
            min_date = min_aapl[0]
            min_symbol = sym
        aapl_prices = []
        for stock in stocks[sym]:
            aapl_prices.append(stock[1])
        aapl_sum = sum(aapl_prices)
        aapl_length = len(aapl_prices)
        aapl_average = aapl_sum/aapl_length
        return_dic = {"Max:": max_aapl, "Min:": min_aapl, "Average:": aapl_average}
        return(return_dic)        
    
    #write to text file

    file = open('stock_summary.txt', 'w')

    file.writelines( "\nAAPL \n--------\n")
    aapl = (find_max_min_ave ("AAPL", stocks))
    file.writelines(f'Max: ${aapl["Max:"][1]:.2f}, {aapl["Max:"][0]}\n')
    file.writelines(f'Min: ${aapl["Min:"][1]:.2f}, {aapl["Min:"][0]}\n')
    file.writelines(f'Average: ${aapl["Average:"]:.2f}\n')

    file.writelines( "\nIBM \n--------\n")
    ibm = find_max_min_ave ("IBM", stocks)
    file.writelines(f'Max: ${ibm["Max:"][1]:.2f}, {aapl["Max:"][0]}\n')
    file.writelines(f'Min: ${ibm["Min:"][1]:.2f}, {aapl["Min:"][0]}\n')
    file.writelines(f'Average: ${ibm["Average:"]:.2f}\n')

    file.writelines( "\nMSFT \n--------\n")
    msft = find_max_min_ave ("MSFT", stocks)
    file.writelines(f'Max: ${msft["Max:"][1]:.2f}, {aapl["Max:"][0]}\n')
    file.writelines(f'Min: ${msft["Min:"][1]:.2f}, {aapl["Min:"][0]}\n')
    file.writelines(f'Average: ${msft["Average:"]:.2f}\n\n')

    file.writelines(f"Highest:  {max_symbol}, {overall_max}, {max_date}\n")
    file.writelines(f"Lowest:  {min_symbol}, {overall_min}, {min_date}")

    file.close()
    
    #print to console
    
    print( "\nAAPL \n--------\n")
    print(f'Max: ${aapl["Max:"][1]:.2f}, {aapl["Max:"][0]}\n')
    print(f'Min: ${aapl["Min:"][1]:.2f}, {aapl["Min:"][0]}\n')
    print(f'Average: ${aapl["Average:"]:.2f}\n')

 
    print( "\nIBM \n--------\n")
    print(f'Max: ${ibm["Max:"][1]:.2f}, {aapl["Max:"][0]}\n')
    print(f'Min: ${ibm["Min:"][1]:.2f}, {aapl["Min:"][0]}\n')
    print(f'Average: ${ibm["Average:"]:.2f}\n')


    print( "\nMSFT \n--------\n")
    print(f'Max: ${msft["Max:"][1]:.2f}, {aapl["Max:"][0]}\n')
    print(f'Min: ${msft["Min:"][1]:.2f}, {aapl["Min:"][0]}\n')
    print(f'Average: ${msft["Average:"]:.2f}\n\n')

    print(f"Highest:  {max_symbol}, {overall_max}, {max_date}\n")
    print(f"Lowest:  {min_symbol}, {overall_min}, {min_date}")
    
if __name__ =="__main__":
    main()
