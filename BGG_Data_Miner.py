from boardgamegeek import BGGClient
import requests
import lxml.html as lh
import pandas as pd
import csv

class BGGGame:
    def __init__(self, BGGRank, title, year, geekRating, aveRating, numVoters):
        self.BGGRank = BGGRank
        self.title = title
        self.year = year
        self.geekRating = geekRating
        self.aveRating = aveRating
        self.numVoters = numVoters

    def __iter__(self):
        return iter([self.BGGRank, self.title, self.year, self.geekRating, self.aveRating, self.numVoters])

bgg = BGGClient()
MechCount = (['Dice Rolling', 0], ['Roll / Spin and Move', 0], ['Hand Management', 0],
             ['Set Collection', 0], ['Variable Player Powers', 0], ['Card Drafting', 0],
             ['Hex-and-Counter', 0], ['Cooperative Play', 0], ['Modular Board', 0], ['Tile Placement', 0],
             ['Action Point Allowance System', 0], ['Simulation', 0], ['Memory', 0], ['Point to Point Movement', 0],
             ['Area Control / Area Influence', 0], ['Simultaneous Action Selection', 0], ['Auction/Bidding', 0],
             ['Area Movement', 0], ['Grid Movement', 0], ['Trading', 0], ['Player Elimination', 0], ['Deck / Pool Building', 0], ['Partnerships', 0],
             ['Pattern Building', 0], ['Role Playing', 0], ['Pattern Recognition', 0], ['Take That', 0], ['Press Your Luck', 0], ['Storytelling', 0],
             ['Campaign / Battle Card Driven', 0], ['Worker Placement', 0], ['Pick-up and Deliver', 0],
             ['Betting/Wagering', 0], ['Secret Unit Deployment', 0], ['Action / Movement Programming', 0], ['Paper-and-Pencil', 0], ['Voting', 0],
             ['Route/Network Building', 0], ['Trick-taking', 0], ['Acting', 0], ['Variable Phase Order', 0],
             ['Stock Holding', 0], ['Area Enclosure', 0], ['Commodity Speculation', 0], ['Chit-Pull System', 0], ['Rock-Paper-Scissors', 0],
             ['Line Drawing', 0], ['Time Track', 0], ['Singing', 0], ['Area-Impulse', 0], ['Crayon Rail System'])
yearLog = []
countMech = False
importList = True
weirdYears = []
BGGList = []

if not importList:

    pages = int(input("How Many Pages? "))

    for page in range(1, pages):
        print('Page ' + str(page) + ': Searching....')
        url = 'https://boardgamegeek.com/browse/boardgame/page/' + str(page) + '?sort=rank&sortdir=asc'
        page = requests.get(url)
        doc = lh.fromstring(page.content)
        tr_elements = doc.xpath('//tr')

        for entry in range(101):
            if entry + 57 < len(tr_elements):
                for idx, t in enumerate(tr_elements[entry + 57]):

                    buildRow = ''
                    buildList = []
                    letters = True
                    if idx == 2:
                        wholeRow = tr_elements[entry+57].text_content().strip().replace("\t","")

                        for cidx, char in enumerate(wholeRow):
                            if letters and char != "\n":
                                buildRow += char
                            elif letters and char == "\n":
                                buildList.append(buildRow)
                                buildRow = ''
                                letters = False
                            elif not letters and char != "\n":
                                letters = True
                                buildRow += char

                        BGGList.append(BGGGame(buildList[0], buildList[1] ,buildList[2][1:-1] ,buildList[3], buildList[4], buildList[5]))

                        '''
                        try:
                            if int(year) >= 2100:
                                weirdYears.append([name, year])
                        except:
                            pass
                        
                        try:
                            game = bgg.game(name)
                            print(y + 1, name)
                        except:
                            print('%s was skipped. idk why' % (name))
                        '''
                        yearLog.append(year)
                        if not countMech:
                            break

                        else:

                            if 'Dice Rolling' in game.mechanics:
                                MechCount[0][1] += 1
                            if 'Roll / Spin and Move' in game.mechanics:
                                MechCount[1][1] += 1
                            if 'Hand Management' in game.mechanics:
                                MechCount[2][1] += 1
                            if 'Set Collection' in game.mechanics:
                                MechCount[3][1] += 1
                            if 'Variable Player Powers' in game.mechanics:
                                MechCount[4][1] += 1
                            if 'Card Drafting' in game.mechanics:
                                MechCount[5][1] += 1
                            if 'Hex-and-Counter' in game.mechanics:
                                MechCount[6][1] += 1
                            if 'Cooperative Play' in game.mechanics:
                                MechCount[7][1] += 1
                            if 'Modular Board' in game.mechanics:
                                MechCount[8][1] += 1
                            if 'Tile Placement' in game.mechanics:
                                MechCount[9][1] += 1
                            if 'Action Point Allowance System' in game.mechanics:
                                MechCount[10][1] += 1
                            if 'Simulation' in game.mechanics:
                                MechCount[11][1] += 1
                            if 'Memory' in game.mechanics:
                                MechCount[12][1] += 1
                            if 'Point to Point Movement' in game.mechanics:
                                MechCount[13][1] += 1
                            if 'Area Control / Area Influence' in game.mechanics:
                                MechCount[14][1] += 1
                            if 'Simultaneous Action Selection' in game.mechanics:
                                MechCount[15][1] += 1
                            if 'Auction/Bidding' in game.mechanics:
                                MechCount[16][1] += 1
                            if 'Area Movement' in game.mechanics:
                                MechCount[17][1] += 1
                            if 'Grid Movement' in game.mechanics:
                                MechCount[18][1] += 1
                            if 'Trading' in game.mechanics:
                                MechCount[19][1] += 1
                            if 'Player Elimination' in game.mechanics:
                                MechCount[20][1] += 1
                            if 'Deck / Pool Building' in game.mechanics:
                                MechCount[21][1] += 1
                            if 'Partnerships' in game.mechanics:
                                MechCount[22][1] += 1
                            if 'Pattern Building' in game.mechanics:
                                MechCount[23][1] += 1
                            if 'Role Playing' in game.mechanics:
                                MechCount[24][1] += 1
                            if 'Pattern Recognition' in game.mechanics:
                                MechCount[25][1] += 1
                            if 'Take That' in game.mechanics:
                                MechCount[26][1] += 1
                            if 'Press Your Luck' in game.mechanics:
                                MechCount[27][1] += 1
                            if 'Storytelling' in game.mechanics:
                                MechCount[28][1] += 1
                            if 'Campaign / Battle Card Driven' in game.mechanics:
                                MechCount[29][1] += 1
                            if 'Worker Placement' in game.mechanics:
                                MechCount[30][1] += 1
                            if 'Pick-up and Deliver' in game.mechanics:
                                MechCount[31][1] += 1
                            if 'Betting/Wagering' in game.mechanics:
                                MechCount[32][1] += 1
                            if 'Secret Unit Deployment' in game.mechanics:
                                MechCount[33][1] += 1
                            if 'Action / Movement Programming' in game.mechanics:
                                MechCount[34][1] += 1
                            if 'Paper-and-Pencil' in game.mechanics:
                                MechCount[35][1] += 1
                            if 'Voting' in game.mechanics:
                                MechCount[36][1] += 1
                            if 'Route/Network Building' in game.mechanics:
                                MechCount[37][1] += 1
                            if 'Trick-taking' in game.mechanics:
                                MechCount[38][1] += 1
                            if 'Acting' in game.mechanics:
                                MechCount[39][1] += 1
                            if 'Variable Phase Order' in game.mechanics:
                                MechCount[40][1] += 1
                            if 'Stock Holding' in game.mechanics:
                                MechCount[41][1] += 1
                            if 'Area Enclosure' in game.mechanics:
                                MechCount[42][1] += 1
                            if 'Commodity Speculation' in game.mechanics:
                                MechCount[43][1] += 1
                            if 'Chit-Pull System' in game.mechanics:
                                MechCount[44][1] += 1
                            if 'Rock-Paper-Scissors' in game.mechanics:
                                MechCount[45][1] += 1
                            if 'Line Drawing' in game.mechanics:
                                MechCount[46][1] += 1
                            if 'Time Track' in game.mechanics:
                                MechCount[47][1] += 1
                            if 'Singing' in game.mechanics:
                                MechCount[48][1] += 1
                            if 'Area-Impulse' in game.mechanics:
                                MechCount[49][1] += 1
                            if 'Crayon Rail System' in game.mechanics:
                                MechCount[50][1] += 1

    with open('BGGGameList.csv', 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        for game in BGGList:
            try:
                wr.writerow(list(game))
            except:
                continue
else:
    with open('BGGGameList.csv', 'r') as csv_file:
        rr = csv.reader(csv_file, delimiter=',')
        for row in rr:
            BGGList.append(BGGGame(BGGRank=row[0],title=row[1],year=row[2],geekRating=row[3],aveRating=row[4],numVoters=row[5]))

YearRatingList = []

for game in BGGList:

    if game.year not in [o[0] for o in YearRatingList]:
        YearRatingList.append([game.year, game.aveRating, 1])
    else:
        currentRating = float(YearRatingList[[o[0] for o in YearRatingList].index(game.year)][1])
        newRating = ((currentRating + float(game.aveRating)) / 2)
        YearRatingList[[o[0] for o in YearRatingList].index(game.year)][1] = newRating
        YearRatingList[[o[0] for o in YearRatingList].index(game.year)][2] += 1


with open('BGGGameYearRatings.csv', 'w', newline='') as csv_file:
    wr = csv.writer(csv_file, delimiter=',')
    for yearRating in YearRatingList:
        try:
            wr.writerow(list(yearRating))
        except:
            continue
'''
if countMech:
    for i in range(len(MechCount) - 1):
        print('%d   %s' % (MechCount[i][1], MechCount[i][0]))



yearLog.sort()
yearCountList = []
yearCountSet = []

for year in yearLog:
    yc = yearLog.count(year)
    yearCountList.append([year, yc])

for x in yearCountList:
        # check if exists in unique_list or not
        if x not in yearCountSet:
            yearCountSet.append(x)

print(weirdYears)

with open('yearCount2.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(yearCountSet)
'''