import pandas as pd
import pickle
import os
import glob

os.chdir('/Users/graallen/Documents/Personal Docs/Grad School/fall_2024/ds_785/capstone')

# Find all files matching the pattern
file_list = glob.glob('lineup_dict_*.pkl')

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def nested_dict_to_dataframe(nested_dict):
    rows = []
    for season, games in nested_dict.items():
        for game, game_data in games.items():
            base_info = {
                'season': season,
                'game': game,
                'home_team': game_data['home_team'],
                'away_team': game_data['away_team']
            }
            for play, plays_data in game_data['plays'].items():
                flat_dict = flatten_dict(plays_data)
                flat_dict.update(base_info)
                flat_dict['play'] = play
                rows.append(flat_dict)
    return pd.DataFrame(rows)

# Find all files matching the pattern
file_list = glob.glob('/Users/graallen/Documents/Personal Docs/Grad School/fall_2024/ds_785/capstone/lineup_dict_*.pkl')

# Initialize an empty list to store DataFrames
lineups = []

# Iterate over the list of files
for file in file_list:
    with open(file, 'rb') as f:
        lineup_dict = pickle.load(f)
        
        # Convert the dictionary to a DataFrame (assuming the dictionary can be directly converted)
        df = nested_dict_to_dataframe(lineup_dict)
        
        # Append the DataFrame to the list
        lineups.append(df)

# Concatenate all DataFrames into a single DataFrame
lineups_df_raw = pd.concat(lineups, ignore_index=True)

lineups_df_raw['unique_players'] = lineups_df_raw['players'].apply(lambda x: len(set(x)))

# only deal with data in the first 4 quarters and get rid of 1996
lineups_df = lineups_df_raw[(lineups_df_raw['period']<=4) & (lineups_df_raw['season']>21997)]

# Identify games where unique_players does not equal 10
games_to_filter = lineups_df[(lineups_df['unique_players'] != 10) | (lineups_df['points'] < 0)]['game'].unique()

# Filter out the identified games from the DataFrame
lineups_df = lineups_df[~lineups_df['game'].isin(games_to_filter)]

# Group by lineup and possession and sum points to sum things like free throws on the same possession
lineups_df['players'] = lineups_df['players'].apply(tuple)
lineups_df = lineups_df.groupby(['season','game','home_team','away_team','players','game_possession','home_possession'])['points'].sum().reset_index()