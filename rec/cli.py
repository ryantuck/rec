from pprint import pprint

import click

from . import rec


@click.command('rec')
@click.argument('csv-path-1')
@click.argument('csv-path-2')
def cli(csv_path_1, csv_path_2):
    results = rec.reconcile_csvs(csv_path_1, csv_path_2)
    for k, v in results.items():
        print(k.replace('_', ' ').title())
        print('-' * 50)
        pprint(v)
