# MultipleWebSearch.py
import WebSearch as ws  # Causes unintended search

print("Welcome to Multiple Web Search")
term = input('Enter search term ("q" to quit): ')
terms = 0
resultString = ""
while term != "q":
    terms = terms + 1
    result = ws.searchTerm(term)
    resultString = ws.stringifyResult(term, result, resultString)
    term  = input('Enter search term ("q" to quit): ')
if terms == 0:
    print("No search terms entered.")
else:
    if terms == 1:
        print("Results for the one search term entered:")
    else:
        print("Results for the", terms, "search terms entered:")
    print(resultString)
print("\nEnd of Multiple Web Search")
