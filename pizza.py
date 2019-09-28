#!/usr/bin/env python3

# Created by DJ Watson
# Created on September 2019
# This program calculates the cost of a pizza given the diameter


import constants


def main():
    # input
    diameter = int(input("enter diameter of pizza: "))

    # process
    subtotal = constants.LABOR + constants.RENT + (diameter * constants.CPI)
    total = subtotal + (subtotal * constants.HST)

    # output
    print("")
    print("cost of {0} inch pizza: ${1:,.2f}".format(diameter, total))


if __name__ == "__main__":
    main()
