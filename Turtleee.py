from turtle import *

#http://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters
def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)
#shape('turtle')
def korduste_töötlus(inputStr):
    command_string = ''
    #delimiters = ":"
    #colon_count = 0
    for el in inputStr:
        if el == ':': #colon_count += 1
            index1 = inputStr.index(':')
            part1 = inputStr[:index1]
            #print('Part1   '+ part1)
            if '.' in inputStr:
                index2 = inputStr.index('.')
                part2 = inputStr[index1+1:index2]
                #print('Part2   '+ part2)
                part3 = inputStr[index2+1:]
                #print('Part3   '+ part3)
            else:
                part2 = inputStr[index1+1:]
                part3 = ''
    #input_list = split(delimiters,inputStr)
    #print(input_list)
    #i=0
    #while i<colon_count:
    for el in part1.split():
            #print(input_list[i])
            #print(el)
        if el.isdigit():
            kordaja = int(el)
        elif el.startswith('-') and el[1:].isdigit():
            kordaja = int(el[1:])*(-1)
        #print(kordaja)
    string = part2
    korratavStr = part2
        #print(string)
    j = 0
    while j<kordaja:
        j += 1
        if ':' in korratavStr:
            command_string += korratavStr + '.'
        else:
            command_string += korratavStr + ","
        #command_string += string*kordaja + ","
        #print(command_string)
        #i+=2
    #delimiters2 = ";", " ja ", ","
    #commands = split(delimiters2, command_string)
    command_string += part3
    #print(command_string)
    return command_string
## Käskluste realiseerimine
def do(word, argument):
    word=word.lower()
    if word in liigu_edasi: #== "edasi" or word.lower() == "otse":
        forward(int(argument))            
    if word in liigu_tagasi: #== "tagasi" or word.lower() == "tagurpidi":
        backward(int(argument))
        #if x== "2 sammu edasi":
    if word in paremale: #== "paremale" or word.lower() == "päripäeva":
        right(int(argument))
    if word.lower() in vasakule: #== "vasakule" or word.lower() == "vastupäeva":
        left(int(argument))
    if word in lõpeta: #== "lõpeta":
        exitonclick()
    if word == "kiirus":
        speed(int(argument))
    #pliiats üles ja alla paremad märksõnad?
    if word == "üles":
        up()
    if word == "alla":
        down()
    if word == "suurus" or word=='paksus':
        pensize(int(argument))
    ## VÄRVID
    if word in värvid:
        pencolor(värvid.get(word))
    ## Kilpkonna nähtavus
    if word == "nähtav":
        showturtle()
    if word == "nähtamatu":
        hideturtle()
    ## Ilmakaared
    if word in ilmakaared:
        setheading(ilmakaared.get(word))
    ## Ekraani puhastamine
    if word in puhasta:
        reset()

## korduste_töötlus kaotab ära korduskäsklusele eelnevad käsud
## executeCommands hakkab käske algusest täitma, kuni jõuab korduskäsuni
def executeCommands(inputStr):
    delimiters = ";", " ja ", "," , "."
    commandslist = split(delimiters, inputStr)
    for command in commandslist:
        shape('turtle')
        words = command.split()
        argument = 0
        for word in words:
            if word.isdigit():
                argument = word
            elif word.startswith('-') and word[1:].isdigit():
                argument = int(word[1:])*(-1)
        if ':' in command:
            executeCommands(korduste_töötlus(inputStr))
            return  ## funktsiooni töö võib peatada
        for word in words:
            ## Eitused
            if word in eitused:
                break
            else:
                do(word, argument)            
    argument = 0
        


liigu_edasi = ['edasi', 'otse', 'otsejoones', 'silmalt', 'silmmnäolt', 'otseteed', 'õkva']
liigu_tagasi = ['tagasi', 'tagurpidi']
paremale = ['paremale', 'päripäeva']
vasakule = ['vasakule', 'vastupäeva']
lõpeta = ['lõpeta', 'lõpetan', 'quit', 'exit', '']
eitused = ['ära', 'mitte', 'ei']
värvid = {'punane':'red', 'oranž':'orange', 'kollane':'yellow', 'roheline':'green' ,'sinine': 'blue'}
ilmakaared = {'põhja': 90, 'lõunasse': 270, 'itta':0, 'läände': 180, 'kirdesse': 45, 'kagusse': 315, 'edelasse': 225, 'loodesse': 135}
puhasta = ['puhasta', 'taasta', 'puhtaks']

while True:
    x=input("Anna käsklus: ")
    if x.lower() in lõpeta:
        break
    #if x.split(':') != [x]:
        #x=korduste_töötlus(x)
    #delimiters = ";", " ja ", ","
    #commands = split(delimiters, x)
    #commands=x.split(";")
    #print('-20'.isdigit())
    #print(commands)
    executeCommands(x)

exitonclick()
