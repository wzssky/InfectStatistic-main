import argparse

def get_parser():
    parser = argparse.ArgumentPaeser(description="National epidemic statistics")
    subparsers = parser.add_subparsers(help='sub-command help')
    list_parser = subparsers.add_parser('list',help='list help')
    list_parser.add_argument('-log', help='Specify directory location', required=True)
    list_parser.add_argument('-out', help='Specify output file path', required=True)
    list_parser.add_argument('-date', help='Appointed date')
    list_parser.add_argument('-type', help='')
    list_parser.add_argument('-province', help='Designated provinces')
    _parser = parser.parse_args()
    return _parser

class InfectStatistic:









