import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# number of stocks for optimization and price data
num_stocks = int(input('Number of stocks for optimization analysis (max of 5 stocks):'))

if num_stocks == 0:
    print('Zero stocks for optimization')
elif num_stocks == 1:
    input_ticker1 = input('Ticker symbols in caps:')
    print(' When inputing the date please beware of IPOs ')
    input_period_start = input('Start period (ex:yyyy-mm-dd):')
    input_period_end = input('End period (ex:yyyy-mm-dd):')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
elif num_stocks == 2:
    print("2 for optimization")
    input_ticker1 = input('Ticker symbols in caps:')
    input_ticker2 = input('Ticker symbols in caps:')
    print('When inputing the date please beware of IPOs')
    input_period_start = input('Start period (ex:yyyy-mm-dd):')
    input_period_end = input('End period (ex:yyyy-mm-dd):')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
elif num_stocks == 3:
    print("3 stocks for optimization")
    input_ticker1 = input('Ticker symbols in caps:')
    input_ticker2 = input('Ticker symbols in caps:')
    input_ticker3 = input('Ticker symbols in caps:')
    print(' When inputing the date please beware of IPOs ')
    input_period_start = input('Start period (ex:yyyy-mm-dd):')
    input_period_end = input('End period (ex:yyyy-mm-dd):')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
elif num_stocks == 4:
    print("4 for optimization")
    input_ticker1 = input('Ticker symbols in caps:')
    input_ticker2 = input('Ticker symbols in caps:')
    input_ticker3 = input('Ticker symbols in caps:')
    input_ticker4 = input('Ticker symbols in caps:')
    print(' When inputing the date please beware of IPOs ')
    input_period_start = input('Start period (ex:yyyy-mm-dd):')
    input_period_end = input('End period (ex:yyyy-mm-dd):')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
elif num_stocks == 5:
    print("5 for optimization")
    input_ticker1 = input('Ticker symbols in caps:')
    input_ticker2 = input('Ticker symbols in caps:')
    input_ticker3 = input('Ticker symbols in caps:')
    input_ticker4 = input('Ticker symbols in caps:')
    input_ticker5 = input('Ticker symbols in caps:')
    print(' When inputing the date please beware of IPOs ')
    input_period_start = input('Start period (ex:yyyy-mm-dd):')
    input_period_end = input('End period (ex:yyyy-mm-dd):')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
else:   
    print('Number of stocks is higher than 5')

# Creating a list to download the price data based on number of stocks
if num_stocks == 0:
    print('Zero stocks for download')
elif num_stocks == 1:
    stocks = [(input_ticker1)]
    print(stocks)
elif num_stocks == 2:
    stocks = [(input_ticker1, input_ticker2)]
    print(stocks)
elif num_stocks == 3:
    stocks = [(input_ticker1, input_ticker2, input_ticker3)]
    print(stocks)
elif num_stocks == 4:
    stocks = [(input_ticker1, input_ticker2, input_ticker3, input_ticker4)]
    print(stocks)
elif num_stocks == 5:
    stocks = [(input_ticker1, input_ticker2, input_ticker3, input_ticker4, input_ticker5)]
    print(stocks)
else:
    print('Error')

# Getting price data
if num_stocks == 0:
    print('No stocks')
elif num_stocks > 5:
    print('Error')
else:
    for stock in stocks:
        data = yf.download(stock, start=input_period_start, end=input_period_end)
        # Download the price data
        file_name = input('File name of price data (ex: prices.csv):')
        data.to_csv(info_store+str(file_name))
        print(data)
        close_prices = data["Close"]
        # Portfolio optimization
        x = close_prices.pct_change()
        p_weights = []
        p_returns = []
        p_risk = []
        p_sharpe = []
        
        count = 10000
        for k in range(0, count):
            wts = np.random.uniform(size = len(x.columns))
            wts = wts/np.sum(wts)
            p_weights.append(wts)
            # Returns
            mean_ret = (x.mean() * wts).sum()*252
            p_returns.append(mean_ret)

            # Volatility
            ret = (x * wts).sum(axis = 1)
            annual_std = np.std(ret) * np.sqrt(252)
            p_risk.append(annual_std)
            
            # Sharpe ratio
            sharpe = (np.mean(ret) / np.std(ret))*np.sqrt(252)
            p_sharpe.append(sharpe)

    max_ind = np.argmax(p_sharpe)

    # Max Sharpe ratio
    print(p_sharpe[max_ind])

    # Max weights
    print(p_weights[max_ind])

    # This portfolio results in the maximum Sharpe ratio.
    s = pd.Series(p_weights[max_ind], index=x.columns)
    s.plot(kind="bar")

    plt.scatter(p_risk, p_returns, c=p_sharpe, cmap="plasma")  
    plt.colorbar(label="Sharpe Ratio")
    plt.scatter(p_risk[max_ind], p_returns[max_ind], color="r", marker="*", s=100)
    plt.show()

# Number of stocks for financial data download
num_of_data = int(input('Number of stock for download (max 4 stocks):'))

# Creating a list to download the financial data based on number of stocks
if num_of_data == 0:
    print('Zero stocks for download')
elif num_of_data == 1:
    print('1 stocks for download')
    ticker1 = input('Ticker symbols in caps:')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
elif num_of_data == 2:
    print('2 stocks for download')
    ticker1 = input('Ticker symbols in caps:')
    ticker2 = input('Ticker symbols in caps:')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
elif num_of_data == 3:
    print('3 stocks for download')
    ticker1 = input('Ticker symbols in caps:')
    ticker2 = input('Ticker symbols in caps:')
    ticker3 = input('Ticker symbols in caps:')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
elif num_of_data == 4:
    print('4 stocks for download')
    ticker1 = input('Ticker symbols in caps:')
    ticker2 = input('Ticker symbols in caps:')
    ticker3 = input('Ticker symbols in caps:')
    ticker4 = input('Ticker symbols in caps:')
    info_store = input('Where to store the information- input like the example (ex: Path where you want to store the CSV file\):')
else:
    print('Number of stocks for download exceeds 4')

# Getting the financial data based on num_of_data
if num_of_data == 0:
    print('Zero stocks for download')
elif num_of_data == 1:
    tickers = [yf.Ticker(ticker1)]
    print(tickers)
    for ticker in tickers: 
        print('Financials',ticker.financials)
        df1 = ticker.financials 
        file_name1 = input('File of financials name (ex: financials_tsla.csv):')
        df1.to_csv(info_store+str(file_name1))

        print('Balance sheet',ticker.balance_sheet)
        df2 = ticker.balance_sheet 
        file_name2 = input('File of balance sheet name (ex: financials_tsla.csv):')
        df2.to_csv(info_store+str(file_name2))

        print('Cash flow',ticker.cashflow)
        df3 = ticker.cashflow 
        file_name3 = input('File of cash flow name (ex: financials_tsla.csv):')
        df3.to_csv(info_store+str(file_name3))

        print('Earnings',ticker.earnings)
        df4 = ticker.earnings
        file_name4 = input('File of earnings name (ex: financials_tsla.csv):')
        df4.to_csv(info_store+str(file_name4))

        print('Dividends',ticker.dividends)
        df5 = ticker.dividends
        if len(df5.value_counts()) > 0 :
            file_name5 = input('File of dividends name (ex: financials_tsla.csv):')
            df5.to_csv(info_store+str(file_name5)) 
        else:
            print("Did not pay dividends")

        print('Recommendations',ticker.recommendations)
        df6 = ticker.recommendations
        file_name6 = input('File of recommendations name (ex: financials_tsla.csv):')
        df6.to_csv(info_store+str(file_name6)) 

        print('Sustainability',ticker.sustainability)
        df7 = ticker.sustainability
        file_name7 = input('File of sustainability name (ex: financials_tsla.csv):')
        df7.to_csv(info_store+str(file_name7)) 

        print('Earning dates',ticker.earnings_dates)
        df8 = ticker.earnings_dates
        file_name8 = input('File of earnings dates name (ex: financials_tsla.csv):')
        df8.to_csv(info_store+str(file_name8)) 

        print('Next events',ticker.calendar)
        df9 = ticker.calendar
        file_name9 = input('File of calendar name (ex: financials_tsla.csv):')
        df9.to_csv(info_store+str(file_name9)) 

        print('Analysis',ticker.analysis)
        df10 = ticker.analysis
        file_name10 = input('File of analysis name (ex: financials_tsla.csv):')
        df10.to_csv(info_store+str(file_name10)) 

        print('Institutional holders',ticker.institutional_holders)
        df11 = ticker.institutional_holders
        file_name11 = input('File of institutional holders name (ex: financials_tsla.csv):')
        df11.to_csv(info_store+str(file_name11))

elif num_of_data == 2:
    tickers = [yf.Ticker(ticker1), yf.Ticker(ticker2)]
    print(tickers)
    for ticker in tickers: 
        print('Financials',ticker.financials)
        df1 = ticker.financials 
        file_name1 = input('File of financials name (ex: financials_tsla.csv):')
        df1.to_csv(info_store+str(file_name1))

        print('Balance sheet',ticker.balance_sheet)
        df2 = ticker.balance_sheet 
        file_name2 = input('File of balance sheet name (ex: financials_tsla.csv):')
        df2.to_csv(info_store+str(file_name2))

        print('Cash flow',ticker.cashflow)
        df3 = ticker.cashflow 
        file_name3 = input('File of cash flow name (ex: financials_tsla.csv):')
        df3.to_csv(info_store+str(file_name3))

        print('Earnings',ticker.earnings)
        df4 = ticker.earnings
        file_name4 = input('File of earnings name (ex: financials_tsla.csv):')
        df4.to_csv(info_store+str(file_name4))

        print('Dividends',ticker.dividends)
        df5 = ticker.dividends
        if len(df5.value_counts()) > 0 :
            file_name5 = input('File of dividends name (ex: financials_tsla.csv):')
            df5.to_csv(info_store+str(file_name5)) 
        else:
            print("Did not pay dividends")

        print('Recommendations',ticker.recommendations)
        df6 = ticker.recommendations
        file_name6 = input('File of recommendations name (ex: financials_tsla.csv):')
        df6.to_csv(info_store+str(file_name6)) 

        print('Sustainability',ticker.sustainability)
        df7 = ticker.sustainability
        file_name7 = input('File of sustainability name (ex: financials_tsla.csv):')
        df7.to_csv(info_store+str(file_name7)) 

        print('Earning dates',ticker.earnings_dates)
        df8 = ticker.earnings_dates
        file_name8 = input('File of earnings dates name (ex: financials_tsla.csv):')
        df8.to_csv(info_store+str(file_name8)) 

        print('Next events',ticker.calendar)
        df9 = ticker.calendar
        file_name9 = input('File of calendar name (ex: financials_tsla.csv):')
        df9.to_csv(info_store+str(file_name9)) 

        print('Analysis',ticker.analysis)
        df10 = ticker.analysis
        file_name10 = input('File of analysis name (ex: financials_tsla.csv):')
        df10.to_csv(info_store+str(file_name10)) 

        print('Institutional holders',ticker.institutional_holders)
        df11 = ticker.institutional_holders
        file_name11 = input('File of institutional holders name (ex: financials_tsla.csv):')
        df11.to_csv(info_store+str(file_name11))

elif num_of_data == 3:
    tickers = [yf.Ticker(ticker1), yf.Ticker(ticker2), yf.Ticker(ticker3)]
    print(tickers)
    for ticker in tickers: 
        print('Financials',ticker.financials)
        df1 = ticker.financials 
        file_name1 = input('File of financials name (ex: financials_tsla.csv):')
        df1.to_csv(info_store+str(file_name1))

        print('Balance sheet',ticker.balance_sheet)
        df2 = ticker.balance_sheet 
        file_name2 = input('File of balance sheet name (ex: financials_tsla.csv):')
        df2.to_csv(info_store+str(file_name2))

        print('Cash flow',ticker.cashflow)
        df3 = ticker.cashflow 
        file_name3 = input('File of cash flow name (ex: financials_tsla.csv):')
        df3.to_csv(info_store+str(file_name3))

        print('Earnings',ticker.earnings)
        df4 = ticker.earnings
        file_name4 = input('File of earnings name (ex: financials_tsla.csv):')
        df4.to_csv(info_store+str(file_name4))

        print('Dividends',ticker.dividends)
        df5 = ticker.dividends
        if len(df5.value_counts()) > 0 :
            file_name5 = input('File of dividends name (ex: financials_tsla.csv):')
            df5.to_csv(info_store+str(file_name5)) 
        else:
            print("Did not pay dividends")

        print('Recommendations',ticker.recommendations)
        df6 = ticker.recommendations
        file_name6 = input('File of recommendations name (ex: financials_tsla.csv):')
        df6.to_csv(info_store+str(file_name6)) 

        print('Sustainability',ticker.sustainability)
        df7 = ticker.sustainability
        file_name7 = input('File of sustainability name (ex: financials_tsla.csv):')
        df7.to_csv(info_store+str(file_name7)) 

        print('Earning dates',ticker.earnings_dates)
        df8 = ticker.earnings_dates
        file_name8 = input('File of earnings dates name (ex: financials_tsla.csv):')
        df8.to_csv(info_store+str(file_name8)) 

        print('Next events',ticker.calendar)
        df9 = ticker.calendar
        file_name9 = input('File of calendar name (ex: financials_tsla.csv):')
        df9.to_csv(info_store+str(file_name9)) 

        print('Analysis',ticker.analysis)
        df10 = ticker.analysis
        file_name10 = input('File of analysis name (ex: financials_tsla.csv):')
        df10.to_csv(info_store+str(file_name10)) 

        print('Institutional holders',ticker.institutional_holders)
        df11 = ticker.institutional_holders
        file_name11 = input('File of institutional holders name (ex: financials_tsla.csv):')
        df11.to_csv(info_store+str(file_name11))

elif num_of_data == 4:
    tickers = [yf.Ticker(ticker1), yf.Ticker(ticker2), yf.Ticker(ticker3), yf.Ticker(ticker4)]
    print(tickers)
    for ticker in tickers: 
        print('Financials',ticker.financials)
        df1 = ticker.financials 
        file_name1 = input('File of financials name (ex: financials_tsla.csv):')
        df1.to_csv(info_store+str(file_name1))

        print('Balance sheet',ticker.balance_sheet)
        df2 = ticker.balance_sheet 
        file_name2 = input('File of balance sheet name (ex: financials_tsla.csv):')
        df2.to_csv(info_store+str(file_name2))

        print('Cash flow',ticker.cashflow)
        df3 = ticker.cashflow 
        file_name3 = input('File of cash flow name (ex: financials_tsla.csv):')
        df3.to_csv(info_store+str(file_name3))

        print('Earnings',ticker.earnings)
        df4 = ticker.earnings
        file_name4 = input('File of earnings name (ex: financials_tsla.csv):')
        df4.to_csv(info_store+str(file_name4))

        print('Dividends',ticker.dividends)
        df5 = ticker.dividends
        if len(df5.value_counts()) > 0 :
            file_name5 = input('File of dividends name (ex: financials_tsla.csv):')
            df5.to_csv(info_store+str(file_name5)) 
        else:
            print("Did not pay dividends")

        print('Recommendations',ticker.recommendations)
        df6 = ticker.recommendations
        file_name6 = input('File of recommendations name (ex: financials_tsla.csv):')
        df6.to_csv(info_store+str(file_name6)) 

        print('Sustainability',ticker.sustainability)
        df7 = ticker.sustainability
        file_name7 = input('File of sustainability name (ex: financials_tsla.csv):')
        df7.to_csv(info_store+str(file_name7)) 

        print('Earning dates',ticker.earnings_dates)
        df8 = ticker.earnings_dates
        file_name8 = input('File of earnings dates name (ex: financials_tsla.csv):')
        df8.to_csv(info_store+str(file_name8)) 

        print('Next events',ticker.calendar)
        df9 = ticker.calendar
        file_name9 = input('File of calendar name (ex: financials_tsla.csv):')
        df9.to_csv(info_store+str(file_name9)) 

        print('Analysis',ticker.analysis)
        df10 = ticker.analysis
        file_name10 = input('File of analysis name (ex: financials_tsla.csv):')
        df10.to_csv(info_store+str(file_name10)) 

        print('Institutional holders',ticker.institutional_holders)
        df11 = ticker.institutional_holders
        file_name11 = input('File of institutional holders name (ex: financials_tsla.csv):')
        df11.to_csv(info_store+str(file_name11))
else:
    print('Number of stocks exceeds 4')