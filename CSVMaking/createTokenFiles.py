# import pandas as pd
# import json
# DEPRECATED
# import pandas as pd
# import json
# uuidToRelatedCards = {}
# uuidToName = {}
# def related_cards_to_uuid(row):
# 	try:
# 		uuidToName[row["uuid"]] = row["name"] 
# 		if(row["name"]  == "Treasure"):
# 			print("Jalapeno")
# 		for name in json.loads(row["relatedCards"])["reverseRelated"]:
# 			name = name.strip()
# 			if(row["name"]  == "Treasure"):
# 				print(name)
# 			uuidToRelatedCards[name] = uuidToRelatedCards.get(name, [])
# 			uuidToRelatedCards[name].append(row["uuid"].strip())
# 	except Exception as e:
# 		if(row["name"]  == "Treasure"):
# 			print(e)
# 		pass

# df = pd.read_csv("ParsedCSV/tokens.csv")
# df.apply(related_cards_to_uuid, axis=1)
# uuidToRelatedCardsFile = open("relatedTokens.txt", "w")
# uuidToRelatedCardsFile.write(json.dumps(uuidToRelatedCards))
# uuidToNameFile = open("uuidToName.txt", "w")
# uuidToNameFile.write(json.dumps(uuidToName))