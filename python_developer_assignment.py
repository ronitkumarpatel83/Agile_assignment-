# ============================================================================
# ====================Leaderboard TeamWise==================================
# ============================================================================

import pandas as pd


team_data = pd.read_csv('input_ids.csv')

activity_data = pd.read_csv('ragorbuilder_raw.csv')

merged_df = pd.merge(team_data, activity_data, left_on='User ID', right_on='uid')

team_stats = merged_df.groupby('Team Name').agg({'total_statements': 'mean', 'total_reasons': 'mean'}).reset_index()

team_stats['Team Rank'] = team_stats.apply(lambda x: (x['total_statements'], -x['total_reasons']), axis=1).rank(method='dense', ascending=False).astype(int)

team_stats = team_stats[['Team Rank', 'Team Name', 'total_statements', 'total_reasons']]
team_stats = team_stats.rename(columns={'total_statements': 'Average Statements', 'total_reasons': 'Average Reasons'})
team_stats = team_stats.round(2)

final_output = team_stats.sort_values(['Average Statements', 'Average Reasons'], ascending=False).reset_index(drop=True)


print(final_output)


# ============================================================================
# ====================Leaderboard Individual==================================
# ============================================================================


df = pd.read_csv('ragorbuilder_raw.csv')
df['Total'] = df['total_statements'] + df['total_reasons']
df = df.sort_values(['Total', 'name'], ascending=[False, True])
df['Rank'] = df.reset_index().index + 1
output = df[['Rank', 'name', 'uid', 'total_statements', 'total_reasons']]
output.columns = ['Rank', 'Name', 'UID', 'No. of Statements', 'No. of Reasons']
individual_output = output.to_string(index=False)
print(individual_output)