from googlesearch import search
results = search(term="Python Development", num_results=10, lang="en")
results = list(results)
print(results)
