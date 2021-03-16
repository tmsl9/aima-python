from csp import australia_csp, AC3, backtracking_search, MapColoringCSP
import copy

domain = {'WA': 'R', 'V': 'B',
          'SA': ['R', 'G', 'B'], 'NT': ['R', 'G', 'B'], 'Q': ['R', 'G', 'B'], 'NSW': ['R', 'G', 'B']}

good_domain = copy.copy(domain)
bad_domain = copy.copy(domain)
bad_domain['V'] = 'R'


def ac3(domains):
    print('\n\nAC3')
    australia_ac3 = copy.copy(australia_csp)
    australia_ac3.domains = domains
    consistent, checks = AC3(australia_ac3)
    print("Current domains:", australia_ac3.curr_domains)
    print("Is consistent?", consistent)
    print("Checks:", checks)


def bs(domains):
    print('\n\nBS')
    australia_bs = copy.copy(australia_csp)
    australia_bs.domains = domains
    result = backtracking_search(australia_bs)
    print("Current domains:", australia_bs.curr_domains)
    print("Result:", result)


def main():
    ac3(good_domain)
    ac3(bad_domain)
    bs(good_domain)
    bs(bad_domain)
