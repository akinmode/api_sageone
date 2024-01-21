#!/usr/bin/python3
"""
"""
import requests, json

from url import SageOneUrls


if __name__ == "__main__":
    with open("access.json", "r") as read_file:
        data = json.load(read_file)
        testaccess = SageOneUrls()
        testaccess.setRequestUrl("Customer", "Get", data['options'], 5)
        print(testaccess.getRequestUrl())
