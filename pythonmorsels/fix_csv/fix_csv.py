import argparse
import csv


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix your csv')
    parser.add_argument('in_file', help='In file')
    parser.add_argument('out_file', help='Out file')
    parser.add_argument('--in-delimiter', help='specify delimiter')
    parser.add_argument('--in-quote', help='specify quote')

    args = parser.parse_args()

    in_file = args.in_file
    out_file = args.out_file

    arguments = {}
    if args.in_delimiter is not None:
        arguments['delimiter'] = args.in_delimiter
    if args.in_quote is not None:
        arguments['quotechar'] = args.in_quote

    with open(in_file, 'r', encoding='unicode_escape') as in_, open(out_file, 'w') as out:
        if 'delimiter' not in arguments and 'quotechar' not in arguments:
            dialect = csv.Sniffer().sniff(in_.read(1024))
            arguments['dialect'] = dialect
            in_.seek(0)

        reader = csv.reader(in_, **arguments)

        rows = list(reader)

        writer = csv.writer(out)
        writer.writerows(rows)
