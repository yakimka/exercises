import configparser
import csv

import click


@click.command()
@click.argument('ini_file', type=str)
@click.argument('csv_file', type=str)
@click.option("--collapsed", is_flag=True, help="Collapse output")
def run(ini_file, csv_file, collapsed):
    ini2csv = INI2CSV(ini_file, csv_file, collapsed)
    ini2csv.write()


class INI2CSV:
    def __init__(self, in_file, out_file, collapsed):
        self.in_file = in_file
        self.out_file = out_file
        self.collapsed = collapsed

        self.ini = configparser.ConfigParser()
        self.ini.read(self.in_file)

    def write(self):
        with open(self.out_file, 'w') as out:
            if self.collapsed:
                rows = self.get_rows_collapsed()
                writer = csv.DictWriter(out, fieldnames=rows[0].keys())
                writer.writeheader()
            else:
                rows = self.get_rows()
                writer = csv.writer(out)

            writer.writerows(rows)

    def get_rows(self):
        result = []
        for section, item in self.ini.items():
            for key, value in item.items():
                result.append([section, key, value])

        return result

    def get_rows_collapsed(self):
        return [{'header': section, **item}
                for section, item in self.ini.items()
                if item]


if __name__ == '__main__':
    run()
