import json
from collections import Counter

def checkCombo(combo):

    checkDict = {
        'weapon' : 0,
        'Leggings' : 0,
        'Necklace' : 0,
        'Bracelet' : 0,
        'Boots' : 0,
        'Ring' : 0,
        'Helmet' : 0,
        'Chestplate' : 0
    }


    is_combo = True
    for i in combo:
        #print(i)
        for x in checkDict:
            print(1, checkDict)
            #print(f"SII, {str(x)} in {i['category']}")
            if str(x) in i['category']:
                checkDict[x] += 1
            try:
                #print(f"SII, {str(x)} in {i['type']}")
                if str(x) in i['type']:
                    #print("Qui 7")
                    checkDict[x] += 1
            except:
                pass

            try:
                #print("AAA",i['accessoryType'])
                #print(f"lll, {str(x)} in {i['accessoryType']}")
                if str(x) in i['accessoryType']:
                   #print("Qui 8")
                    checkDict[x] += 1
            except:
                pass

            if checkDict['weapon'] > 1:
                print(f"FALSE: reason: {x} = {checkDict['weapon']}")
                is_combo = False
                return is_combo
            elif checkDict['Leggings'] > 1:
                print(f"FALSE: reason: {x} = {checkDict['leggings']}")
                is_combo = False
                return is_combo
            elif checkDict['Boots'] > 1:
                print(f"FALSE: reason: {x} = {checkDict['Boots']}")
                is_combo = False
                return is_combo
            elif checkDict['Necklace'] > 1:
                print(f"FALSE: reason: {x} = {checkDict['Necklace']}")
                is_combo = False
                return is_combo
            elif checkDict['Helmet'] > 1:
                print(f"FALSE: reason: {x} = {checkDict['Helmet']}")
                is_combo = False
                return is_combo
            elif checkDict['Chestplate'] > 1:
                print(f"FALSE: reason: {x} = {checkDict['Chestplate']}")
                is_combo = False
                return is_combo
            elif checkDict['Bracelet'] > 1:
                print(f"FALSE: reason: {x} = {checkDict['Bracelet']}")
                is_combo = False
                return is_combo


            if checkDict['Ring'] > 2:
                print("FALSE: reason = %s" % checkDict['Ring'])
                is_combo = False
                return is_combo

    print(2, checkDict)
    sum = 0
    for f in checkDict:
        sum = sum + checkDict[f]

    print(sum)
    if sum == 9:
        print("COMBO DONE!")
        return True
    else:
        return False


test = ({ 'name' : 'Dondasch', 'tier' : 'Legendary', 'type' : 'Chestplate', 'set' : None, 'restrictions' : 'Untradable',
          'material' : None, 'armorType' : 'Diamond', 'armorColor' : '160,101,64', 'dropType' : 'never',
          'addedLore' : 'The sheer bond between Adamastor and Urdar has manifested itself into a physical form due to their duress. Such power is not to be abused...',
          'sockets' : 0, 'health' : 3375, 'earthDefense' : 150, 'thunderDefense' : 0, 'waterDefense' : 0,
          'fireDefense' : 0, 'airDefense' : 150, 'level' : 100, 'quest' : None, 'classRequirement' : None,
          'strength' : 50, 'dexterity' : 0, 'intelligence' : 0, 'defense' : 0, 'agility' : 50, 'strengthPoints' : 20,
          'dexterityPoints' : 0, 'intelligencePoints' : 0, 'defensePoints' : 0, 'agilityPoints' : 0, 'damageBonus' : 0,
          'damageBonusRaw' : 280, 'spellDamage' : 0, 'spellDamageRaw' : 0, 'rainbowSpellDamageRaw' : 0,
          'healthRegen' : 0, 'healthRegenRaw' : 0, 'healthBonus' : 0, 'poison' : 0, 'lifeSteal' : 0, 'manaRegen' : 0,
          'manaSteal' : 0, 'spellCostPct1' : 0, 'spellCostRaw1' : 0, 'spellCostPct2' : 0, 'spellCostRaw2' : 0,
          'spellCostPct3' : 0, 'spellCostRaw3' : 0, 'spellCostPct4' : 0, 'spellCostRaw4' : 0, 'thorns' : 0,
          'reflection' : 0, 'attackSpeedBonus' : 0, 'speed' : 27, 'exploding' : 0, 'soulPoints' : 15, 'sprint' : 0,
          'sprintRegen' : 0, 'jumpHeight' : 0, 'xpBonus' : 0, 'lootBonus' : 0, 'lootQuality' : 0, 'emeraldStealing' : 0,
          'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 25, 'bonusThunderDamage' : 0,
          'bonusWaterDamage' : 0, 'bonusFireDamage' : -100, 'bonusAirDamage' : 25, 'bonusEarthDefense' : 0,
          'bonusThunderDefense' : 0, 'bonusWaterDefense' : 0, 'bonusFireDefense' : 0, 'bonusAirDefense' : 0,
          'category' : 'armor' },
        { 'name' : 'Nona', 'tier' : 'Legendary', 'type' : 'Dagger', 'set' : None, 'restrictions' : 'Untradable',
          'material' : '359:4', 'dropType' : 'never', 'addedLore' : None, 'sockets' : 3, 'damage' : '0-0',
          'earthDamage' : '62-85', 'thunderDamage' : '0-0', 'waterDamage' : '0-0', 'fireDamage' : '0-0',
          'airDamage' : '62-85', 'attackSpeed' : 'SUPER_FAST', 'level' : 95, 'quest' : None, 'classRequirement' : None,
          'strength' : 50, 'dexterity' : 0, 'intelligence' : 0, 'defense' : 0, 'agility' : 40, 'strengthPoints' : 0,
          'dexterityPoints' : 0, 'intelligencePoints' : 0, 'defensePoints' : 0, 'agilityPoints' : 13, 'damageBonus' : 0,
          'damageBonusRaw' : 100, 'spellDamage' : 0, 'spellDamageRaw' : 90, 'rainbowSpellDamageRaw' : 0,
          'healthRegen' : 0, 'healthRegenRaw' : -180, 'healthBonus' : 0, 'poison' : 0, 'lifeSteal' : 0, 'manaRegen' : 0,
          'manaSteal' : 0, 'spellCostPct1' : 0, 'spellCostRaw1' : 0, 'spellCostPct2' : 0, 'spellCostRaw2' : 0,
          'spellCostPct3' : 0, 'spellCostRaw3' : 0, 'spellCostPct4' : 0, 'spellCostRaw4' : 0, 'thorns' : 0,
          'reflection' : 0, 'attackSpeedBonus' : 1, 'speed' : 25, 'exploding' : 0, 'soulPoints' : 15, 'sprint' : 0,
          'sprintRegen' : 0, 'jumpHeight' : 0, 'xpBonus' : 10, 'lootBonus' : 0, 'lootQuality' : 0,
          'emeraldStealing' : 0, 'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 0,
          'bonusThunderDamage' : 0, 'bonusWaterDamage' : 0, 'bonusFireDamage' : 0, 'bonusAirDamage' : 0,
          'bonusEarthDefense' : 0, 'bonusThunderDefense' : 0, 'bonusWaterDefense' : 0, 'bonusFireDefense' : -100,
          'bonusAirDefense' : 0, 'category' : 'weapon' },
        { 'name' : 'Breakbore', 'tier' : 'Rare', 'type' : 'Spear', 'set' : None, 'restrictions' : 'Untradable',
          'material' : '256:4', 'dropType' : 'never', 'addedLore' : None, 'sockets' : 3, 'damage' : '90-150',
          'earthDamage' : '60-130', 'thunderDamage' : '60-130', 'waterDamage' : '0-0', 'fireDamage' : '0-0',
          'airDamage' : '0-0', 'attackSpeed' : 'SLOW', 'level' : 90, 'quest' : None, 'classRequirement' : None,
          'strength' : 35, 'dexterity' : 35, 'intelligence' : 0, 'defense' : 0, 'agility' : 0, 'strengthPoints' : 13,
          'dexterityPoints' : 0, 'intelligencePoints' : 0, 'defensePoints' : 0, 'agilityPoints' : 0, 'damageBonus' : 30,
          'damageBonusRaw' : 0, 'spellDamage' : 0, 'spellDamageRaw' : 0, 'rainbowSpellDamageRaw' : 0, 'healthRegen' : 0,
          'healthRegenRaw' : 0, 'healthBonus' : 0, 'poison' : 0, 'lifeSteal' : 0, 'manaRegen' : 0, 'manaSteal' : 0,
          'spellCostPct1' : 0, 'spellCostRaw1' : 0, 'spellCostPct2' : 0, 'spellCostRaw2' : 0, 'spellCostPct3' : 0,
          'spellCostRaw3' : 0, 'spellCostPct4' : 0, 'spellCostRaw4' : 0, 'thorns' : 0, 'reflection' : 0,
          'attackSpeedBonus' : 0, 'speed' : 0, 'exploding' : 57, 'soulPoints' : 0, 'sprint' : 0, 'sprintRegen' : 0,
          'jumpHeight' : 0, 'xpBonus' : 10, 'lootBonus' : 10, 'lootQuality' : 0, 'emeraldStealing' : 0,
          'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 0, 'bonusThunderDamage' : 20,
          'bonusWaterDamage' : 0, 'bonusFireDamage' : 0, 'bonusAirDamage' : 0, 'bonusEarthDefense' : 0,
          'bonusThunderDefense' : 0, 'bonusWaterDefense' : -20, 'bonusFireDefense' : 0, 'bonusAirDefense' : -20,
          'category' : 'weapon' },
        { 'name' : 'Eidolon', 'tier' : 'Rare', 'type' : 'Wand', 'set' : None, 'restrictions' : 'Untradable',
          'material' : '269:1', 'dropType' : 'never', 'addedLore' : None, 'sockets' : 5, 'damage' : '0-0',
          'earthDamage' : '0-0', 'thunderDamage' : '0-0', 'waterDamage' : '0-0', 'fireDamage' : '0-0',
          'airDamage' : '520-570', 'attackSpeed' : 'SUPER_SLOW', 'level' : 95, 'quest' : None,
          'classRequirement' : None, 'strength' : 0, 'dexterity' : 0, 'intelligence' : 0, 'defense' : 0, 'agility' : 45,
          'strengthPoints' : 0, 'dexterityPoints' : 0, 'intelligencePoints' : 0, 'defensePoints' : 0,
          'agilityPoints' : 15, 'damageBonus' : 0, 'damageBonusRaw' : 0, 'spellDamage' : 0, 'spellDamageRaw' : 0,
          'rainbowSpellDamageRaw' : 0, 'healthRegen' : 0, 'healthRegenRaw' : 0, 'healthBonus' : 0, 'poison' : 0,
          'lifeSteal' : 0, 'manaRegen' : 0, 'manaSteal' : 1, 'spellCostPct1' : 0, 'spellCostRaw1' : 0,
          'spellCostPct2' : 0, 'spellCostRaw2' : 0, 'spellCostPct3' : 0, 'spellCostRaw3' : 0, 'spellCostPct4' : 0,
          'spellCostRaw4' : 0, 'thorns' : 0, 'reflection' : 0, 'attackSpeedBonus' : 0, 'speed' : 30, 'exploding' : 0,
          'soulPoints' : 15, 'sprint' : 0, 'sprintRegen' : 0, 'jumpHeight' : 0, 'xpBonus' : 10, 'lootBonus' : 0,
          'lootQuality' : 0, 'emeraldStealing' : 0, 'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 0,
          'bonusThunderDamage' : 0, 'bonusWaterDamage' : 0, 'bonusFireDamage' : -20, 'bonusAirDamage' : 0,
          'bonusEarthDefense' : 0, 'bonusThunderDefense' : 25, 'bonusWaterDefense' : 0, 'bonusFireDefense' : 0,
          'bonusAirDefense' : 30, 'category' : 'weapon' },
        { 'name' : 'Back-up Plan', 'displayName' : 'Back-Up Plan', 'tier' : 'Rare', 'accessoryType' : 'Bracelet',
          'set' : None, 'restrictions' : 'Untradable', 'material' : '259:42', 'dropType' : 'never', 'addedLore' : None,
          'sockets' : 0, 'health' : 625, 'earthDefense' : 0, 'thunderDefense' : 0, 'waterDefense' : 0,
          'fireDefense' : 0, 'airDefense' : 0, 'level' : 70, 'quest' : None, 'classRequirement' : None, 'strength' : 0,
          'dexterity' : 0, 'intelligence' : 0, 'defense' : 50, 'agility' : 0, 'strengthPoints' : 0,
          'dexterityPoints' : 0, 'intelligencePoints' : 0, 'defensePoints' : 7, 'agilityPoints' : 7, 'damageBonus' : 0,
          'damageBonusRaw' : 0, 'spellDamage' : 0, 'spellDamageRaw' : 0, 'rainbowSpellDamageRaw' : 0, 'healthRegen' : 0,
          'healthRegenRaw' : 0, 'healthBonus' : 0, 'poison' : 0, 'lifeSteal' : 0, 'manaRegen' : 0, 'manaSteal' : 0,
          'spellCostPct1' : 0, 'spellCostRaw1' : 0, 'spellCostPct2' : 0, 'spellCostRaw2' : 0, 'spellCostPct3' : 0,
          'spellCostRaw3' : 0, 'spellCostPct4' : 0, 'spellCostRaw4' : 0, 'thorns' : 0, 'reflection' : 0,
          'attackSpeedBonus' : 0, 'speed' : 0, 'exploding' : 0, 'soulPoints' : 0, 'sprint' : 0, 'sprintRegen' : 0,
          'jumpHeight' : 0, 'xpBonus' : 10, 'lootBonus' : 0, 'lootQuality' : 0, 'emeraldStealing' : 0,
          'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 0, 'bonusThunderDamage' : 0,
          'bonusWaterDamage' : 0, 'bonusFireDamage' : 0, 'bonusAirDamage' : 0, 'bonusEarthDefense' : 0,
          'bonusThunderDefense' : 0, 'bonusWaterDefense' : 0, 'bonusFireDefense' : 0, 'bonusAirDefense' : 0,
          'category' : 'accessory' },
        { 'name' : 'Quick-Strike Leggings', 'tier' : 'Legendary', 'type' : 'Leggings', 'set' : None,
          'restrictions' : 'Untradable', 'material' : None, 'armorType' : 'Iron', 'armorColor' : '160,101,64',
          'dropType' : 'never', 'addedLore' : None, 'sockets' : 2, 'health' : 1525, 'earthDefense' : 0,
          'thunderDefense' : 0, 'waterDefense' : 0, 'fireDefense' : 0, 'airDefense' : 0, 'level' : 70, 'quest' : None,
          'classRequirement' : 'Assassin', 'strength' : 0, 'dexterity' : 60, 'intelligence' : 0, 'defense' : 0,
          'agility' : 0, 'strengthPoints' : 0, 'dexterityPoints' : 20, 'intelligencePoints' : 0, 'defensePoints' : 0,
          'agilityPoints' : 0, 'damageBonus' : 0, 'damageBonusRaw' : 0, 'spellDamage' : 0, 'spellDamageRaw' : 0,
          'rainbowSpellDamageRaw' : 0, 'healthRegen' : 0, 'healthRegenRaw' : 0, 'healthBonus' : 0, 'poison' : 0,
          'lifeSteal' : 0, 'manaRegen' : 0, 'manaSteal' : 0, 'spellCostPct1' : 0, 'spellCostRaw1' : 0,
          'spellCostPct2' : 0, 'spellCostRaw2' : 0, 'spellCostPct3' : 0, 'spellCostRaw3' : 0, 'spellCostPct4' : 0,
          'spellCostRaw4' : 0, 'thorns' : 0, 'reflection' : 0, 'attackSpeedBonus' : 1, 'speed' : 14, 'exploding' : 0,
          'soulPoints' : 0, 'sprint' : 0, 'sprintRegen' : 0, 'jumpHeight' : 0, 'xpBonus' : 0, 'lootBonus' : 0,
          'lootQuality' : 0, 'emeraldStealing' : 0, 'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 0,
          'bonusThunderDamage' : 0, 'bonusWaterDamage' : 0, 'bonusFireDamage' : 0, 'bonusAirDamage' : 0,
          'bonusEarthDefense' : -14, 'bonusThunderDefense' : 0, 'bonusWaterDefense' : 0, 'bonusFireDefense' : 0,
          'bonusAirDefense' : 0, 'category' : 'armor' },
        { 'name' : "Durum's Serenity", 'tier' : 'Legendary', 'accessoryType' : 'Necklace', 'set' : None,
          'restrictions' : 'Untradable', 'material' : '259:20', 'dropType' : 'never',
          'addedLore' : 'Carried by the Durum Protector, this small necklace holds but an ounce of the vibrance and life of the Durum Isles.',
          'sockets' : 0, 'health' : 30, 'earthDefense' : 7, 'thunderDefense' : 0, 'waterDefense' : 7, 'fireDefense' : 0,
          'airDefense' : 0, 'level' : 25, 'quest' : None, 'classRequirement' : None, 'strength' : 5, 'dexterity' : 0,
          'intelligence' : 10, 'defense' : 0, 'agility' : 0, 'strengthPoints' : 5, 'dexterityPoints' : 0,
          'intelligencePoints' : 7, 'defensePoints' : 0, 'agilityPoints' : 0, 'damageBonus' : 0, 'damageBonusRaw' : 0,
          'spellDamage' : 0, 'spellDamageRaw' : 0, 'rainbowSpellDamageRaw' : 0, 'healthRegen' : 0, 'healthRegenRaw' : 0,
          'healthBonus' : 0, 'poison' : 0, 'lifeSteal' : 0, 'manaRegen' : 0, 'manaSteal' : 0, 'spellCostPct1' : 0,
          'spellCostRaw1' : 0, 'spellCostPct2' : 0, 'spellCostRaw2' : 0, 'spellCostPct3' : 0, 'spellCostRaw3' : 0,
          'spellCostPct4' : 0, 'spellCostRaw4' : 0, 'thorns' : 0, 'reflection' : 0, 'attackSpeedBonus' : 0, 'speed' : 0,
          'exploding' : 0, 'soulPoints' : 12, 'sprint' : 0, 'sprintRegen' : 0, 'jumpHeight' : 0, 'xpBonus' : 10,
          'lootBonus' : 0, 'lootQuality' : 0, 'emeraldStealing' : 0, 'gatherXpBonus' : 0, 'gatherSpeed' : 0,
          'bonusEarthDamage' : 0, 'bonusThunderDamage' : 0, 'bonusWaterDamage' : 0, 'bonusFireDamage' : 0,
          'bonusAirDamage' : 0, 'bonusEarthDefense' : 0, 'bonusThunderDefense' : 0, 'bonusWaterDefense' : 0,
          'bonusFireDefense' : 0, 'bonusAirDefense' : 0, 'category' : 'accessory' },
        { 'name' : 'Crossbolt', 'tier' : 'Rare', 'type' : 'Bow', 'set' : None, 'restrictions' : 'Untradable',
          'material' : '261:2', 'dropType' : 'never', 'addedLore' : None, 'sockets' : 1, 'damage' : '60-100',
          'earthDamage' : '0-0', 'thunderDamage' : '0-0', 'waterDamage' : '0-0', 'fireDamage' : '0-0',
          'airDamage' : '0-0', 'attackSpeed' : 'SLOW', 'level' : 25, 'quest' : None, 'classRequirement' : None,
          'strength' : 0, 'dexterity' : 0, 'intelligence' : 0, 'defense' : 0, 'agility' : 0, 'strengthPoints' : 0,
          'dexterityPoints' : 0, 'intelligencePoints' : 0, 'defensePoints' : 0, 'agilityPoints' : 0, 'damageBonus' : 50,
          'damageBonusRaw' : 0, 'spellDamage' : 0, 'spellDamageRaw' : -25, 'rainbowSpellDamageRaw' : 0,
          'healthRegen' : 0, 'healthRegenRaw' : 0, 'healthBonus' : 0, 'poison' : 0, 'lifeSteal' : 0, 'manaRegen' : 0,
          'manaSteal' : 0, 'spellCostPct1' : 0, 'spellCostRaw1' : 0, 'spellCostPct2' : 0, 'spellCostRaw2' : 0,
          'spellCostPct3' : 0, 'spellCostRaw3' : 0, 'spellCostPct4' : 0, 'spellCostRaw4' : 0, 'thorns' : 0,
          'reflection' : 0, 'attackSpeedBonus' : 0, 'speed' : -5, 'exploding' : 0, 'soulPoints' : 0, 'sprint' : 0,
          'sprintRegen' : 0, 'jumpHeight' : 0, 'xpBonus' : 0, 'lootBonus' : 0, 'lootQuality' : 0, 'emeraldStealing' : 0,
          'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 0, 'bonusThunderDamage' : 0,
          'bonusWaterDamage' : 0, 'bonusFireDamage' : 0, 'bonusAirDamage' : 0, 'bonusEarthDefense' : 0,
          'bonusThunderDefense' : 0, 'bonusWaterDefense' : 0, 'bonusFireDefense' : 0, 'bonusAirDefense' : 0,
          'category' : 'weapon' },
        { 'name' : 'Temporal Cage', 'tier' : 'Rare', 'type' : 'Chestplate', 'set' : None, 'restrictions' : 'Untradable',
          'material' : None, 'armorType' : 'Leather', 'armorColor' : '160,101,64', 'dropType' : 'never',
          'addedLore' : None, 'sockets' : 0, 'health' : 0, 'earthDefense' : 0, 'thunderDefense' : 30,
          'waterDefense' : 0, 'fireDefense' : 0, 'airDefense' : 0, 'level' : 20, 'quest' : None,
          'classRequirement' : None, 'strength' : 0, 'dexterity' : 0, 'intelligence' : 0, 'defense' : 0, 'agility' : 0,
          'strengthPoints' : 0, 'dexterityPoints' : 0, 'intelligencePoints' : 0, 'defensePoints' : 0,
          'agilityPoints' : 0, 'damageBonus' : 0, 'damageBonusRaw' : 26, 'spellDamage' : 0, 'spellDamageRaw' : 20,
          'rainbowSpellDamageRaw' : 0, 'healthRegen' : 0, 'healthRegenRaw' : -7, 'healthBonus' : 0, 'poison' : 0,
          'lifeSteal' : 0, 'manaRegen' : 0, 'manaSteal' : 2, 'spellCostPct1' : 0, 'spellCostRaw1' : 0,
          'spellCostPct2' : 0, 'spellCostRaw2' : 0, 'spellCostPct3' : 0, 'spellCostRaw3' : 0, 'spellCostPct4' : 0,
          'spellCostRaw4' : 0, 'thorns' : 0, 'reflection' : 0, 'attackSpeedBonus' : 0, 'speed' : 10, 'exploding' : 0,
          'soulPoints' : 0, 'sprint' : 0, 'sprintRegen' : 0, 'jumpHeight' : 0, 'xpBonus' : 0, 'lootBonus' : 0,
          'lootQuality' : 0, 'emeraldStealing' : 0, 'gatherXpBonus' : 0, 'gatherSpeed' : 0, 'bonusEarthDamage' : 0,
          'bonusThunderDamage' : 10, 'bonusWaterDamage' : 0, 'bonusFireDamage' : 0, 'bonusAirDamage' : 0,
          'bonusEarthDefense' : 0, 'bonusThunderDefense' : 0, 'bonusWaterDefense' : 0, 'bonusFireDefense' : 0,
          'bonusAirDefense' : 0, 'category' : 'armor' })

#print(checkCombo(test))
