# number of hints per difficulty level
difficulty = {
    "level": "Easy",
    "hints": 46,
}, {
    "level": "Medium",
    "hints": 34,
}, {
    "level": "Difficult",
    "hints": 28
}

# create the cells, assigning column, row, and house
cells = {}
for i in range(1, 82):
    """
        define rows and columns
        - columns are i%9 or 9 if i%9 is 0
        - rows are integer value of ((i-1)/9)+1
    """
    if i%9 != 0:
        cells[i] = {
            "cell": i,
            "value": None,
            "column": i%9,
            "row": int(((i-1)/9)+1),
            "house": 0
        }
    else:
         cells[i] = {
            "cell": i,
            "value": None,
            "column": 9,
            "row": int(((i-1)/9)+1),
            "house": 0
        }
    
    #define houses (3x3 groups of cells)
    if (cells[i]['row'] <= 3 and cells[i]['column'] <= 3):
        cells[i]['house'] = 1
    elif (cells[i]['row'] <= 3 and cells[i]['column'] > 3 and cells[i]['column'] <= 6):
        cells[i]['house'] = 2
    elif (cells[i]['row'] <= 3 and cells[i]['column'] > 6 and cells[i]['column'] <= 9):
        cells[i]['house'] = 3
    elif (cells[i]['row'] > 3 and cells[i]['row'] <= 6 and cells[i]['column'] <= 3):
        cells[i]['house'] = 4
    elif (cells[i]['row'] > 3 and cells[i]['row'] <= 6 and cells[i]['column'] > 3 and cells[i]['column'] <= 6):
        cells[i]['house'] = 5
    elif (cells[i]['row'] > 3 and cells[i]['row'] <= 6 and cells[i]['column'] > 6 and cells[i]['column'] <= 9):
        cells[i]['house'] = 6
    elif (cells[i]['row'] > 6 and cells[i]['row'] <= 9 and cells[i]['column'] <= 3):
        cells[i]['house'] = 7
    elif (cells[i]['row'] > 6 and cells[i]['row'] <= 9 and cells[i]['column'] > 3 and cells[i]['column'] <= 6):
        cells[i]['house'] = 8
    elif (cells[i]['row'] > 6 and cells[i]['row'] <= 9 and cells[i]['column'] > 6 and cells[i]['column'] <= 9):
        cells[i]['house'] = 9

def populateBoard(diffSelection):
    print(diffSelection)
    for i in range(difficulty[diffSelection]):
        pass