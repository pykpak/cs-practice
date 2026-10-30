import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)
non_empty = sum(1 for l in lines if l.strip())

print(len(records))
print(non_empty - len(records))
if records:
    city = warmest_city(records)
    print(f'{average_by_city(records)[city]:.1f}')
