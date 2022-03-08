# Historical Data Extraction from Binance
<br/>
Code directory for pulling Historical Data of a pair from Binance with API and backtesting on downloaded data

<br/>

You can run the code by typing your ApiKey and SecretKeys into the config file. 

<br/>

Pulls data for any pair you type into **symbolList = ["BTCUSDT"]** 
<br/>
Since csv name will be needed in backtesing, this part should be paid attention to.

<br/>

When specifying the date range you want to extract, you should specify it like this: **"1 January, 2022", "3 March, 2022"**

<br/>

The data is exported as **".csv"**

<br/>

Finally, the longer your date range, the longer the processing time will be, you should wait a bit.
