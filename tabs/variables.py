import pandas as pd
import numpy as np


nba_year_keys=[1992, 1995, 2000, 2005, 2010, 2015, 2020]
nba_year_values=['1992', '1995', '2000', '2005', '2010', '2015', '2020']
query_tab_sql_ph='''You can write your SQL query here.
Not sure how the data looks like or the column names? Click on one of the tables to find out...
Here is an example of a query to get you going:
SELECT * FROM statsbomb.competition_information LIMIT 50;'''

dict_columns = ['TACTICS','PASS', 'CARRY', 'UNDER_PRESSURE', 'BALL_RECEIPT', 'COUNTERPRESS',
                'INTERCEPTION', 'DRIBBLE', 'GOALKEEPER', 'SHOT', 'OUT', 'DUEL', 'BALL_RECOVERY',
                'CLEARANCE', 'OFF_CAMERA', 'FOUL_WON', 'FOUL_COMMITTED', 'SUBSTITUTION',
                'INJURY_STOPPAGE', 'MISCONTROL', '50_50', 'BAD_BEHAVIOUR', 'BLOCK', 'PLAYER_OFF',
                'HOME_COUNTRY', 'AWAY_COUNTRY', 'STADIUM_COUNTRY', 'REFEREE_COUNTRY']
button_dict={
    'button_1':'nba_reference.player_overall_seasons',
    'button_2':'nba_reference.player_stats_by_game',
    'button_3':'statsbomb.competition_information',
    'button_4':'statsbomb.match_information'
    }

intro_dict={
    'statsbomb.competition_information':
        '''
        The following table consists of the public data provided by Statsbomb. The table consists of the competition information,
        which can be found in the following links:
         - https://github.com/statsbomb/open-data/blob/master/data/competitions.json
         - https://github.com/statsbomb/open-data/tree/master/data/matches
        ''',
    'statsbomb.match_information':
        '''
        The following table consists of the public data provided by Statsbomb. The table consists of the events of the matches listed in
        statsbomb.competition_information, a total of 799 games. You can access the original data right here:
        - https://github.com/statsbomb/open-data/tree/master/data/events
        ''',
    'nba_reference.player_overall_seasons':
        '''
        The following table consists of data collected from basketball-reference.com. You will be able to view a collection of players'
        overall season stats, spanning their career. An example of a table is the following link:
        - https://www.basketball-reference.com/players/s/siakapa01.html
        ''',
    'nba_reference.player_stats_by_game':
        '''
        The following table consists of data collected from basketball-reference.com. You will be able to view a collection of players'
        stat line by game, spanning their career. An example of a table is the following link:
        - https://www.basketball-reference.com/players/s/siakapa01/gamelog/2020/
        '''
}

filtering_string_dict={
    'nba':['''
           #### A Little Insight

           The following graph allows you to have an idea on the background of the players.''',
           'You can adjust the period of the players you are interested in by playing with Range Slider below the Graph.'],
    'statsbomb':['''
                #### A Little Insight

                The following graphs allows you to see a background of the Statsbomb data by leagues.''',
                'You can further filter your data before exporting the leagues and/or seasons you are interested in.']
}

table_string='''
             #### Advanced filtering

             You can choose to explore the data furthermore using the features available with the Data Table selected.

             Whenever you are ready hit that export button, enjoy your explorations :)
             '''

bad_table_string='''
             #### Advanced filtering

             Due to some technical difficulties, the data you requested was not able to be made for you. Apologies in advance, the issue
             is being addressed. In the mean time, enjoy the throwback data to 1990s, 2000s hoopers.

             You can still interact with the data using the SQL interaction.

             Whenever you are ready, hit that export button! enjoy your explorations :)
             '''
