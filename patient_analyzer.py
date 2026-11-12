"""Beginner portfolio project: summarize fictional healthcare visit records."""
import csv
from collections import Counter
from pathlib import Path
from statistics import mean

DATA_FILE = Path(__file__).with_name('sample_patients.csv')


def load_records(path=DATA_FILE):
    with open(path, newline='', encoding='utf-8') as file:
        records = list(csv.DictReader(file))
    for record in records:
        record['age'] = int(record['age'])
        record['visit_cost'] = float(record['visit_cost'])
    return records


def summarize(records):
    if not records:
        raise ValueError('No patient records were found.')
    return {
        'patients': len(records),
        'average_age': mean(r['age'] for r in records),
        'total_cost': sum(r['visit_cost'] for r in records),
        'average_cost': mean(r['visit_cost'] for r in records),
        'departments': Counter(r['department'] for r in records),
    }


def main():
    data = summarize(load_records())
    print('HEALTHCARE PATIENT DATA ANALYZER')
    print('(Fictional patient records — educational use only)')
    print(f"Total patients: {data['patients']}")
    print(f"Average patient age: {data['average_age']:.1f} years")
    print(f"Total visit costs: ${data['total_cost']:,.2f}")
    print(f"Average visit cost: ${data['average_cost']:,.2f}")
    print('Visits by department:')
    for department, count in sorted(data['departments'].items()):
        print(f'  {department}: {count}')


if __name__ == '__main__':
    main()
