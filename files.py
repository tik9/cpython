from pathlib import Path
import os,sys
import json
import pretty_csv

home = str(Path.home())
doc = "$HOME/documents/"
dw = home+'downloads/'


def main():
    '''main'''
    # print(home)
    # print(f_values())
    pretty_csv.pretty_file("shares.csv", header=False, border=False, delimiter="|")


def f_values():
    file='shares.csv'
    with open(file) as file:
        vals = file.read()
    return vals


def js_values():
    '''get values from json'''
    vals = {}
    file = 'income.json'

    with open(file) as json_file:
        vals = json.load(json_file)
    return vals



if __name__ == "__main__":
    main()
