import csv
from dataclasses import dataclass


@dataclass
class Armor:
    id: int
    ilvl: int
    name: str
    damage_phys: int
    damage_mag: int
    vit: int
    main_stat: int
    ss: int
    dh: int


def main():
    job_cat = {

        'BLM': [26, 55, 63, 31, 34, 1, 56, 57],
        'WHM': [25, 53, 64, 31, 34, 1, 56, 58]
        }
    items = []
    with open('item.csv', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            items.append(row)
    f.close()
    keys = items.pop(0)
    headers = items.pop(0)
    col_types = items.pop(0)
    x = [item for item in items if
         int(item[headers.index('Level{Item}')]) >= 500
         and int(item[headers.index('ClassJobCategory')]) in job_cat['WHM']
         ]

    for row in x:
        print(row)
    #print(col_types)
    #print(headers)
    pass


if __name__ == "__main__":
    main()
