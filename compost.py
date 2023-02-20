from bazaarpy import bazaar as bz

baz = bz.Bazaar()
baz.updateValues()

# Define a dictionary of items and their organic matter values
item_organic_matter = {
    #Wheat 
    "WHEAT": 1,
    "ENCHANTED_BREAD":60,
    "HAY_BLOCK":9,
    "ENCHANTED_HAY_BLOCK":1296,
    "TIGHTLY_TIED_HAY_BALE":186624,
    #Carrot
    "CARROT_ITEM": 0.3,
    "ENCHANTED_CARROT":46.4,
    #Potato
    "POTATO_ITEM": 0.3,
    "ENCHANTED_POTATO": 52.8,
    "ENCHANTED_BAKED_POTATO":8448,
    #Pumpkin
    "PUMPKIN": 1,
    "ENCHANTED_PUMPKIN":160,
    "POLISHED_PUMPKIN":25600,
    #Melon
    "MELON": 0.2,
    "MELON_BLOCK":1.8,
    "ENCHANTED_MELON": 32,
    "ENCHANTED_MELON_BLOCK":5120,
    #Mushroom
    "RED_MUSHROOM": 1,
    "ENCHANTED_RED_MUSHROOM":160,
    "HUGE_MUSHROOM_2":9,
    "HUGE_MUSHROOM_1":9,
    "BROWN_MUSHROOM": 1,
    "ENCHANTED_BROWN_MUSHROOM":160,
    "ENCHANTED_HUGE_MUSHROOM_2":5184,
    "ENCHANTED_HUGE_MUSHROOM_1":5184,
    #Cocoa bean
    "INK_SACK:3": 0.4,
    "ENCHANTED_COCOA":64,
    #Cactus
    "CACTUS": 0.5,
    #Cactus green is 0.5 but not on bazaar :D
    "ENCHANTED_CACTUS_GREEN":80,
    "ENCHANTED_CACTUS":12800,
    #Netherwart
    "NETHER_STALK": 0.3,
    "ENCHANTED_NETHER_STALK":52.8,
    "MUTANT_NETHER_STALK":5448,
    #Sugarcane
    "SUGAR_CANE": 0.5,
    "ENCHANTED_SUGAR":80,
    "ENCHANTED_PAPER":96,
    "ENCHANTED_SUGAR_CANE":12800,
}

# Create a list of items and their coins per organic matter ratio
item_ratios = []
for item, organic_matter in item_organic_matter.items():
    buyPrice = baz.price(item)['buyPrice']
    ratio = buyPrice / organic_matter
    item_ratios.append((item, ratio))

# Sort the list of items by coins per organic matter ratio
sorted_items = sorted(item_ratios, key=lambda x: x[1])

# Print the top items with the best coins per organic matter ratio
print("Top items by coins per organic matter ratio:")
print("-" * 40)
for i, (item, ratio) in enumerate(sorted_items[:1000], 1):
    if item == "INK_SACK:3":
        print(f"({i}). Cocoa Bean: {ratio:.2f} Coins Per Organic Matter")
    elif item == "HUGE_MUSHROOM_1":
        print(f"({i}). Brown Mushroom Block: {ratio:.2f} Coins Per Organic Matter")
    elif item == "HUGE_MUSHROOM_2":
        print(f"({i}). Red Mushroom Block: {ratio:.2f} Coins Per Organic Matter")
    elif item == "ENCHANTED_HUGE_MUSHROOM_1":
        print(f"({i}). Enchanted Brown Mushroom Block: {ratio:.2f} Coins Per Organic Matter")
    elif item == "ENCHANTED_HUGE_MUSHROOM_2":
        print(f"({i}). Enchanted Red Mushroom Block: {ratio:.2f} Coins Per Organic Matter")
    else:
    
        separated_words = item.split('_')
        cap_words = [word.capitalize() for word in separated_words]
        joined_words = ' '.join(cap_words)
        print(f"({i}). {joined_words}: {ratio:.2f} Coins Per Organic Matter")
print("-" * 40)

