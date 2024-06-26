#!/usr/bin/python3
"""
python scipt takes w arqumets to evaluates canidated appling for a back end
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    res = requests.get(url)
    commits = res.json()
    try:
        for x in range(10):
            print(
                "{}: {}".format(
                    commits[x].get("sha"),
                    commits[x].get("commit").get("author").get("name"),
                )
            )
    except IndexError:
        pass
