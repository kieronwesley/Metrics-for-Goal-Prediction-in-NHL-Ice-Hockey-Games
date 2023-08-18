import requests
import pandas as pd


def test():
    gameIds = ["%04d" % x for x in range(3, 4)]
    stats = []

    for id in gameIds:
        response = requests.get('https://statsapi.web.nhl.com/api/v1/game/202102' + id + '/boxscore').json()
        
        gameStats = []
        
        gameStats.append(id)
        # Home team stats
        gameStats.append(response['teams']['home']['team']['name'])
        for val in response['teams']['home']['teamStats']['teamSkaterStats'].values():
            gameStats.append(float(val))
        
        # Away team stats
        gameStats.append(response['teams']['away']['team']['name'])
        for val in response['teams']['away']['teamStats']['teamSkaterStats'].values():
            gameStats.append(float(val))

        stats.append(gameStats)


    # Create dataframe of stats
    teamStatsDf = pd.DataFrame(data=stats, columns=['GameId', 'Home', 'goals', 'pim', 'shots', 'powerPlayPercentage', 'powerPlayGoals', 'powerPlayOpportunities', 
                                                    'faceOffWinPercentage', 'blocked', 'takeaways', 'giveaways', 'hits',
                                                    'Away', 'goals', 'pim', 'shots', 'powerPlayPercentage', 'powerPlayGoals', 'powerPlayOpportunities', 
                                                    'faceOffWinPercentage', 'blocked', 'takeaways', 'giveaways', 'hits'])


    teamStatsDf.to_csv('teamGameStats.csv', index=False)



def getTeamInfo():
    teamInfo = []
    response = requests.get("https://statsapi.web.nhl.com/api/v1/teams").json()

    # Collect info on each team
    for team in response['teams']:
        teamInfo.append([team['id'], team['name']])

    # Create dataframe of team info
    teamInfoDf = pd.DataFrame(data=teamInfo, columns=['ID', 'Name'])

    teamInfoDf.to_csv('teamInfo.csv', index=False)






# Call relevant function:
#test()
getTeamInfo()
