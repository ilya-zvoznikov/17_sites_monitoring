import requests
import whois
import os
import datetime
import argparse
import sys


def get_path_to_urls():
    parser = argparse.ArgumentParser(
        description='The app checks status of URLs from file')
    parser.add_argument('input', help='path to file with URLs list')
    args = parser.parse_args()
    return args.input


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as file_handler:
        lines = file_handler.readlines()
        return [line.strip() for line in lines if line.strip() != '']


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
    except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.MissingSchema,
    ):
        return False

    if response.status_code == 200:
        return True
    else:
        return False


def get_domain_expiration_date(domain_name):
    try:
        response = whois.whois(domain_name)
        expiration_date = response['expiration_date']
    except:
        return None
    if type(expiration_date) is list:
        return expiration_date[0]
    else:
        return expiration_date


def is_exp_date_is_more_than(days, exp_date):
    period = datetime.timedelta(days=days)
    today = datetime.datetime.today()
    if exp_date is None:
        return False
    else:
        return (exp_date - today) >= period


def print_url_status(url, is_server_responds_with_200, is_exp_date_more):
    print(url)
    print('Server responds with HTTP 200: {}'.format(
        is_server_responds_with_200))
    print('Domain was paid by more than 1 month: {}'.format(
        is_exp_date_more))
    print()


if __name__ == '__main__':
    period_in_days = 30
    path = get_path_to_urls()
    urls_list = load_urls4check(path)
    if not urls_list:
        sys.exit('Incorrect URLs file')
    for url in urls_list:
        exp_date = get_domain_expiration_date(url)
        print_url_status(
            url,
            is_server_respond_with_200(url),
            is_exp_date_is_more_than(period_in_days, exp_date),
        )
