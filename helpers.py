import csv


def read_requirements(path):
    requirements = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            requirements.append({'code': row[0], 'value': row[1], 'component': row[2]})
    return requirements
