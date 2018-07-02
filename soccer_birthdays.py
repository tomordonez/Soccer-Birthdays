# Soccer Birthdays
# Author: Tom Ordonez
# Tweet me @tomordonez
# Dataset is from Kaggle

import csv
from datetime import datetime, date
import time

def parse_csv():
    fname = 'fifa_2017_dataset.csv'
    with open(fname, 'r') as fh:
        players_dict = [{k:v for k,v in row.items() } for row in csv.DictReader(fh, skipinitialspace=True)]
    
    for player in players_dict:
        player['Birth_Date'] = datetime.date(datetime.strptime(player['Birth_Date'], '%m/%d/%Y'))

    return players_dict

def main():
    print('###   Soccer Birthdays   ###')
    print('')
    print("          _,...,_")
    print("        .'@/~~~\@'.")
    print("       //~~\___/~~\\")
    print("      |@\__/@@@\__/@|")
    print("      |@/  \@@@/  \@|")
    print("       \\__/~~~\__//")
    print("        '.@\___/@.'")
    print("          `.....`")
    print('\nCode: @tomordonez')
    print('Data source: Kaggle')
    print('Art: jgs\n')
    print('Processing CSV file...\n')
    time.sleep(5)
    players_dict = parse_csv()

    today = date.today()
    print('Today is: {}\n'.format(today.strftime("%A %d. %B %Y"))
)
    print('Say Happy Birthday to...\n')

    for player in players_dict:
        if player['Birth_Date'].day == today.day and player['Birth_Date'].month == today.month:
            print('{}: {}, {}'.format(player['Nationality'],player['Name'], player['Club']))



if __name__ == '__main__':
    main()
