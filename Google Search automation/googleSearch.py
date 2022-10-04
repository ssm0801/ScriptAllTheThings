'''
Google Search automation

- Solution to deal with repetitive google searching.

Author : Hershil Piplani

Date   : 4/10/2022
'''
from googlesearch import search
results = search(term="Python Development", num_results=10, lang="en")
results = list(results)
print(results)
