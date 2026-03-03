# WebSearch.py
import googlesearch as gs

def searchTerm(term):
    print('Searching for "', term, '" ...', sep="")
    domains = gs.search(term, verify_ssl=False, stop=10)
    return domains

def stringifyResult(term, domains, domainString):
    i = 0
    while True:
        try:
            domain = next(domains)
        except StopIteration:
            break
        domainSplit = domain.rsplit("//")
        domain = domainSplit[1]
        domainSplit = domain.rsplit("/")
        domain = domainSplit[0]
        if domainString.find(domain) == -1:
            domainString = domainString + "\n" + domain
            i = i + 1
    if i == 0:
        print("No domains", end="")
    elif i == 1:
        print("One domain", end="")
    elif i == 10:
        print("Search stopped after ten domains", end="")
    else:
        print(i, "domains", end="")
    print(' found for search term "', term, '".', sep="")
    return domainString

print("Welcome to Web Search")
term  = input("Enter search term: ")
result = searchTerm(term)
resultString = ""
resultString = stringifyResult(term, result, resultString)
print(resultString)
print("\nEnd of Web Search")
