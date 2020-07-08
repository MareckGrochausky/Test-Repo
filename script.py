import math
import sys
from os import rename

import requests

# print(sys.version)f
# print(sys.executable)

name = input("Your Name? ")
print("Hello,", name)


def greet(who):
    test = "Test"
    greeting = f"Hello {who}"
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
