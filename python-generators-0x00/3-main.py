#!/usr/bin/python3
import sys
lazy_paginator = __import__('2-lazy_paginate').lazy_pagination


try:
    count = 0    
    for page in lazy_paginator(100):
        count += 1
        for user in page:
            print(user)
    print(f"count: {count}")

except BrokenPipeError:
    sys.stderr.close()