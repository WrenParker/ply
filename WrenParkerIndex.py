import ply.lex as lex
import csv

tokens = (
    'WORD', 'WORK_BREAK'
)

t_WORD = r'[A-Za-zÀ-ÖØ-öø-ÿ-°³º¡]+'
t_WORK_BREAK = r'[\.| |,|;|:|"|\n]+'



def generatePrecedingWords(index, arr):
    precedingWords = list()
    index-=1
    while(index>=0 and len(precedingWords)<5):
        precedingWords.append(arr[index])
        index-=1
    precedingWords.reverse()
    return precedingWords

def generateAntecedingWords(index, arr):
    precedingWords = list()
    index+=1
    while(index<len(arr) and len(precedingWords)<5):
        precedingWords.append(arr[index])
        index+=1
    return precedingWords

def buildTable(table, chapterNum, sorted=False):
    print('|---------------------|--------|-----|-----------------------------------------------|-----------------------------------------------|')
    print('|Current Word         |Chapter#|Index|Previous 5 Words                               |Following 5 Words                              |')

    with open('./Chapter'+str(chapterNum)+("_sorted" if sorted else "")+'.csv', 'w', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        for entry in table:
            print('|---------------------|--------|-----|-----------------------------------------------|-----------------------------------------------|')
            print("|", end="")
            key = ""
            for tmpKey in entry.keys():
                print(tmpKey, end=" ")
                key = tmpKey
                for space in range(20-len(tmpKey)):
                    print(" ", end="")
            print("|", end=" ")

            print("2", end=" ")
            print("     |", end=" ")

            print(entry[key]['index'], end=" ")
            for space in range(3-len(str(entry[key]['index']))):
                print(" ", end="")
            print("|", end=" ")

            preceding = ""
            for word in entry[key]['precedingWords']:
                preceding+=word+" "
            print(preceding, end=" ")
            for space in range(45-len(preceding)):
                print(" ", end="")
            print("|", end=" ")
            anteceding= ""
            for word in entry[key]['antecedingWords']:
                anteceding+=word+" "
            print(anteceding, end=" ")
            for space in range(45-len(anteceding)):
                print(" ", end="")
            print("|")
            csvwriter.writerow([key, chapterNum, entry[key]['index'], preceding, anteceding])
        print('|---------------------|--------|-----|-----------------------------------------------|-----------------------------------------------|')

def tokenize(chapter):
    arr = list()
    with open(chapter) as f:
        text  = f.read()
        lexer = lex.lex()
        lexer.input(text)
        tok = lexer.token()
        while(tok!=None):
            if(tok.type=="WORD"):
                arr.append(tok.value)

            tok = lexer.token()
    return arr

table = list()
firstChapter = tokenize('Chapter1.txt')
for pos in range(len(firstChapter)):
    table.append({firstChapter[pos]: {'index': pos,'precedingWords': generatePrecedingWords(pos, firstChapter),'antecedingWords': generateAntecedingWords(pos, firstChapter)}})

buildTable(table,1)
print("\n\n")
buildTable(sorted(table, key= lambda entry : list(entry.keys())[0].lower()),1, True)

table = list()
secondChapter = tokenize('Chapter3.txt')
for pos in range(len(secondChapter)):
    table.append({secondChapter[pos]: {'index': pos,'precedingWords': generatePrecedingWords(pos, secondChapter),'antecedingWords': generateAntecedingWords(pos, secondChapter)}})

buildTable(table,3)
print("\n\n")
buildTable(sorted(table, key= lambda entry : list(entry.keys())[0].lower()),3, True)
