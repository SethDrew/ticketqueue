import csv

# Yeild dictionaries line-by-line from a csv file in the data folder
def get_entities(url):
    with open("{}".format(url)) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row;


