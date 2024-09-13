import pandas as pd
import json

uuidToRelatedCards = {}
uuidToName = {}
def related_cards_to_uuid(row):
	try:
		uuidToName[row["uuid"]] = row["name"] 
		for name in json.loads(row["relatedCards"])["reverseRelated"]:
			name = name.strip()
			uuidToRelatedCards[name] = uuidToRelatedCards.get(name, [])
			uuidToRelatedCards[name].append(row["uuid"].strip())
	except:
		pass

df = pd.read_csv("ParsedCSV/tokens.csv")
df.apply(related_cards_to_uuid, axis=1)
uuidToRelatedCardsFile = open("relatedTokens.txt", "w")
uuidToRelatedCardsFile.write(json.dumps(uuidToRelatedCards))
uuidToNameFile = open("uuidToName.txt", "w")
uuidToNameFile.write(json.dumps(uuidToName))