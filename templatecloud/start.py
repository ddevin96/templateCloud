import os
from time import time
import numpy as np 
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    print("hello from plugin")
    print(time())
    c = np.zeros([3, 3])
    print("\nMatrix c : \n", c)
    response = requests.get("https://www.google.com")
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        continue
    else
        print(f"response: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)