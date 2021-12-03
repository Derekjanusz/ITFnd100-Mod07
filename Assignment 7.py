#Derek Janusz
#11/30/2021
#Assignment 7, Pickling & Error Handling

#To Do:
#function, enter a baseball team
#enter number of wins predicted,
#enter number of losses predicted.
#calculate win/loss%
import pickle
objfile = 'baseball.dat'

baseballRatings = []
teamName = ''
teamWins= ''
teamlosses= ''

print("Enter a baseball team")


#how many wins will they have?
# how many world series won. etc, use error handling to prevent non numbers
#need error handling if non number is entered

def pickle_reader(objfile):
    data = []

    with open(objfile, 'rb') as file:
        while True:
            try:
                data.append(pickle.load(file))
            except:
                break

    print('Pickle file loaded!')
    return data

def fileSaver(objfile, list_of_data):
    with open(objfile, 'ab') as file:
        for each in list_of_data:
            pickle.dump(each, file)
            #save function

def baseballTeam():
    try:
        teamName = input('Enter a baseball team: ')
        teamWins = input('Enter games they will win(0-162): ')
        teamlosses = input('Enter games they will lose(0-162)')
        #get stat predictions

        # ensure they enter numnbers for record
        if teamWins.isalpha() or teamlosses.isalpha():
            raise Exception('Please enter a number for wins and losses (0-162).')
        elif ((int(teamWins) + int(teamlosses))) != 162 :
            raise TotalGames() # make sure 162 total
        else:
            percent = int(teamWins)/2
            print('Success! Rating added.\n')
            return [teamName, percent]
    except Exception as e:
        print(e)


class TotalGames(Exception):
    def __str__(self):
        return 'There are 162 games in a season, please make sure your wins and losses add to 162.'

print('Youre a baseball fan eh? enter your predictions for each team! (Data saved to \'%s\')\n' % objfile)
userInput = 'y'
while userInput.lower() != 'n':
    baseballRatings.append(baseballTeam())

    userInput = input('Continue adding baseball teams? (y/n)')
    while userInput.lower() != 'y' and userInput.lower() != 'n':
        userInput = (input('Incorrect choice. Please select either \'y\' or \'n\')'))


fileSaver(objfile, baseballRatings)
new_baseballRatings = pickle_reader(objfile)
print(new_baseballRatings)