import argparse
from random import randint

from faker import Faker

fake = Faker()

valid_tlds = [
    "com",
    "io",
    "info",
    "biz"
]

DOMAIN_WORD_COUNT_MAX = 5
DOMAIN_WORD_COUNT_MIN = 2

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help = True, description = "Generate a set of random domain names.")
    parser.add_argument('-c', "--count", type=int, help='Number of domains to generate', default=5)
    return parser.parse_args()

def build_domain_names(count:int):
    domain_names = []
    for _ in range(count):
        domain_name_len = randint(DOMAIN_WORD_COUNT_MIN, DOMAIN_WORD_COUNT_MAX)
        tld_index = randint(0, len(valid_tlds) - 1)
        domain_name = ''.join(fake.words(domain_name_len)) + '.' + valid_tlds[tld_index]
        domain_names.append(domain_name)
    return domain_names

if __name__ == '__main__':
    args = parse_args()
    names = build_domain_names(count = args.count)
    for name in names:
        print(name)
