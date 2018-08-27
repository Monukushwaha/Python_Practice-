#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
meal_cost = float(raw_input())
tip_percent = int(raw_input())
tax_percent = int(raw_input())
def solve(meal_cost, tip_percent, tax_percent):
    if __name__ == '__main__':
        tip = meal_cost*tip_percent/100
        tax = meal_cost*tax_percent/100
        totalCost=int(round(meal_cost+tip+tax))
        print('The total meal cost is '+ str(totalCost) +' dollars.')
solve(meal_cost, tip_percent, tax_percent)

