import argparse
import os
import sys


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
    def __init__(self, log_list, out_path, date=None, display_type=None, province=None):
        self.out_path = ''
        self.log_list = {}
        self.close_date = None
        self.display_types = display_types or ['ip', 'sp', 'cure', 'dead']
        self.display_province = province or []
        self.log_data = {}

    def log_verifite(self, log_list):
        if not os.path.isdir(log_list):
            sys.exit('error-log-path')

    def out_verfite(self, out_path):
        if not os.path.isfile(out_path):
            sys.exit('error-out-path')

    def read_log(self,log_list):
        pathdir = os.listdir(log_list)
        for file in pathdir:
            self.parse_each_row(file)

    def parse_each_row(self,file):




     


















