import sys
import re



for line in sys.stdin:
    line = line.rstrip()
    pattern = ".*z.{3}z.*"
    match_pattern = re.match(pattern, line)
    if match_pattern:
        print(line)
