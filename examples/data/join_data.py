import csv
import pprint


pp = pprint.PrettyPrinter(indent=4)
pros_by_id = {}

with open('pro_fav_food.csv', 'r') as fav_food:
    data = csv.DictReader(fav_food)
    for row in data:
        pro_id = int(row['pro_id'])
        pros_by_id[pro_id] = {
            'favorite_food': row['favorite_food']
        }


with open('pro_region.csv', 'r') as fav_food:
    data = csv.DictReader(fav_food)
    for row in data:
        pro_id = int(row['pro_id'])
        region = row['region']
        pros_by_id[pro_id]['region'] = region 

pp.pprint(pros_by_id)

