# API Alerts Script

### Run script
```
python apiAlerts.py -c currency -d 1

```
### to get help about the script 

![image](https://user-images.githubusercontent.com/24311808/153013917-83924ff5-c207-4fd9-8988-f1b0ebf8fcef.png)

### Currently I am hardcoding the values like last_price, average_price, change and sdev if we could get response from some API it would have been better.
This scripting is using **Python argparse** module to get and store arguments like **currency** and **deviation** once I store the values then I am printing JSON formatted log line that highlights the following fields:
```
Timestamp in ISO8601 format (2006-31-10T15:00:00-0500)

Log level - (ie. INFO for regular output. ERROR for upstream errors, and logical/math errors, DEBUG for extra data that is not required for user consumption)

Trading Pair: BTCUSD/ETHUSD/BTCETH/etc.

Deviation: true/false boolean indicating if there is a price deviation or not

Data: additional data regarding the log, i.e. if there was an upstream ERROR, what it was, or if there was a price deviation, what the details of that deviation were

    Last Price: a float object that indicates what the last price was

    Average Price: average price over the requested time period

    Deviation: a float object that indicates the deviation from the mean represented in standard devations

     Price change value: a float that object that indicates the deviation as a notional value

```
