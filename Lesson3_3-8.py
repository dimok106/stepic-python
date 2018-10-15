import sys
import re



for line in sys.stdin:
    line = line.rstrip()
    pattern = r".*\bcat\b.*"
    match_pattern = re.match(pattern, line)
    if match_pattern:
        print(line)
