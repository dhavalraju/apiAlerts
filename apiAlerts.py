#!/usr/bin/env python3
import argparse
import sys
from datetime import datetime
import pprint
import json
from collections import OrderedDict
timestamp = datetime.now()
print(timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f%z') + '  - AlertingTool - INFO - Parsing args')
def usage():
    print("usage: apiAlerts.py [-h] [-c CURRENCY] , [-d DEVIATION]")



parser = argparse.ArgumentParser(description='Runs checks on API' )
parser.add_argument('-c', '--currency', help="The currency trading pair, or ALL", required=True, default=None)
parser.add_argument('-d', '--deviation', help="standard deviation threshold. eg. 1 or 0", required=True, default=None)


args = parser.parse_args()

currency=args.currency

deviation=args.deviation

if (deviation) == "0":
    deviation = False
else:
    deviation = True
   

timestamp=datetime.now()
if (len(sys.argv) != 5):
    usage()
    sys.exit()


log_output = {}
log_output["timestamp"] = timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
log_output["level"] = "INFO"
log_output["trading_pair"] = currency
log_output["deviation"] =  deviation
log_output["data"] = {}
if (currency) == "btcusd":
    log_output["data"]["last_price"] = "64381.98"
    log_output["data"]["average"] = "65196.09"
    log_output["data"]["change"] = "765.67"
    log_output["data"]["sdev"] = "1.2"
elif (currency) == "ethusd":
    log_output["data"]["last_price"] = "4607.69"
    log_output["data"]["average"] = "4661.36"
    log_output["data"]["change"] = "53.67"
    log_output["data"]["sdev"] = "1.1"

result = json.dumps(OrderedDict(log_output), indent=4)

print(result)







