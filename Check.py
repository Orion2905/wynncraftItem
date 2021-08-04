

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
            #print(1, checkDict)
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

    #print(2, checkDict)
    sum = 0
    for f in checkDict:
        sum = sum + checkDict[f]

    #print(sum)
    if sum == 9:
        print("COMBO DONE!")
        return True
    else:
        return False


def customFile():
    with open("config/custom_file.txt", "r") as f:
        file = f.read()
        if len(file) > 0:
            #print("sii")
            return file
        else:
            return False


def customCSVFile():
    with open("config/custom_csv_file.txt", "r") as f:
        file = f.read()
        if len(file) > 0:
            #print("sii")
            return file
        else:
            return False


def openFile(file, mode, text=""):
    with open(file, mode, encoding="utf-8") as f:
        if mode == "r":
            value = f.readlines()
            return value
        else:
            f.writelines(text)
