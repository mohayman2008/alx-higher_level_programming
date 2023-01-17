#!/usr/bin/python3
'''This script list the most recent 10 commits of the GitHub repository \
using GitHub API, the repo name and the owner name should be passed as \
arguments'''
from sys import argv

import requests


def main():
    '''Main function'''
    if len(argv) < 3:
        return None

    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)
    try:
        commits = response.json()
        if commits and not isinstance(commits, list):
            return None
        out_lst = []
        count = min(10, len(commits))
        for i in range(count):
            sha = commits[i]
            sha = sha.get('sha', None)
            commit_meta = commits[i].get('commit', None)
            if commit_meta is not None:
                author = commit_meta.get('author', None)
                if author is not None:
                    author_name = author.get('name', None)
                    date = author.get('date', None)
            out_lst.append((date, sha, author_name))
        out_lst.sort(reverse=True)
        for commit in out_lst:
            # date = commit[0]
            sha = commit[1]
            author_name = commit[2]
            print(f'{sha}: {author_name}')
            # print(f'{sha}: {author_name} {date}')
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
