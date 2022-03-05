from binance import Client
import config
import csv
import winsound

duration = 1000  # milliseconds
freq = 440  # Hz

client = Client(config.apiKey, config.secretKey)
symbolList = ["BTCUSDT"]


def historical_Data_Write():
    csvFileW = open(symbol + ".csv", "w", newline='')
    klines_writer = csv.writer(csvFileW, delimiter=",")

    for candlestick in candlesticks:
        klines_writer.writerow(candlestick)

    csvFileW.close()


for symbol in symbolList:
    print("DATA ÇEKİLİYOR: ", symbol)
    candlesticks = client.get_historical_klines(
        symbol, client.KLINE_INTERVAL_1MINUTE, "1 January, 2022", "3 March, 2022")
    historical_Data_Write()

winsound.Beep(freq, duration)
