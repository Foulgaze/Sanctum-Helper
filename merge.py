import pandas as pd


cards = pd.read_csv("Files/cards.csv")
tokens = pd.read_csv("Files/tokens.csv")

allCards = cards.merge(tokens, how='outer')
allCards.head(5)
allCards.to_csv("Files/merge.csv")
