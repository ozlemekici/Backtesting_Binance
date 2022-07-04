from ta.trend import MACD
import pandas as pd
import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
longProcess = False
shortProcess = False
principal = 100
CountProcesses = 0
win = 0
loss = 0
lowest = principal  # Minimum amount of money
highest = principal  # Maximum amount of money
winRate = 0
longEnterTime = 0
shortEnterTime = 0
longEnterPrice = 0
longExitPrice = 0

# Extracting csv name as symbol + ".csv"
csvName = "BTCUSDT.csv"  # OR your csv file name

print("PREPARING BACKTEST...")
attributes = ["timestamp", "open", "high", "low",
              "close", "volume", "1", "2", "3", "4", "5", "6"]
df = pd.read_csv(csvName, names=attributes)

macdDiff = MACD(df["close"], 26, 12, 9)
df["Macd Diff"] = macdDiff.macd_diff()


for i in range(df.shape[0]):
    print(str(len(df.index)) + "/" + str(i),
          " Backtesting...principal:", principal)
    if i > 26:
        # BULL EVENT
        if float(df["Macd Diff"][i-1]) > 0:
            # SHORT EXIT
            if shortProcess == True:
                shortExitPrice = float(df["open"][i])
                principal = principal + \
                    (((principal / 100) * ((longExitPrice -
                     longEnterPrice) / longEnterPrice) * 100)) * -1
                #principal = principal * 0.9996
                if principal < lowest:
                    lowest = principal
                if principal > lowest:
                    lowest = lowest
                if highest < principal:
                    highest = principal
                if highest > principal:
                    highest = highest
                CountProcesses = CountProcesses + 1
                if shortExitPrice < shortEnterPrice:
                    win = win + 1
                else:
                    loss = loss + 1
                winRate = (win / CountProcesses) * 100
                shortProcess = False

            # LONG ENTER
            if longProcess == False and principal > 5:
                longEnterPrice = float(df["open"][i])
                #principal = principal * 0.9996
                longProcess = True

            if principal < 5:
                print("Insufficient Balance...")

        # BEAR EVENT
        if float(df["Macd Diff"][i-1]) < 0:

            # LONG EXIT
            if longProcess == True:
                longExitPrice = float(df["open"][i])
                principal = principal + \
                    ((principal / 100) *
                     ((longExitPrice - longEnterPrice) / longEnterPrice) * 100)
                #principal = principal * 0.9996
                if principal < lowest:
                    lowest = principal
                if principal > lowest:
                    lowest = lowest
                if highest < principal:
                    highest = principal
                if highest > principal:
                    highest = highest
                CountProcesses = CountProcesses + 1
                if longExitPrice > longEnterPrice:
                    win = win + 1
                else:
                    loss = loss + 1
                winRate = (win / CountProcesses) * 100
                longProcess = False

            # SHORT ENTER
            if shortProcess == False and principal > 5:
                shortEnterPrice = float(df["open"][i])
                shortProcess = True
                #principal = principal * 0.9996
            if principal < 5:
                print("Insufficient Balance...")

print("BACKTEST DONE. RESULTS: ")
print(csvName)
print("Total Principal: ", principal)
print("Minimum amount of money: ", lowest)
print("Maximum amount of money: ", highest)
print("Number of Completed Processes: ", CountProcesses)
print("Win: ", win, " Loss: ", loss, " Win Rate: ", winRate)
winsound.Beep(freq, duration)
