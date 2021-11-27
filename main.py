import plotly.express as px
import pandas as pd
import os
#
#
# df = pd.read_csv('movies.csv')
# print(f'Original rows: {len(df)}')
# df = df.dropna()
# print(f'Rows without nan: {len(df)}')
#
#
# def export_csv_to_local_folder(df_to_export, export_folder='Downloads', export_file_name='Unnamed'):
#     path = os.path.join(os.path.expanduser('~'), export_folder, export_file_name)
#     df_to_export.to_csv(path, index_label=False)
#
#
# list_of_genre = df['genre'].unique()
# df_top50_movie_on_IMDb = df.sort_values(by=['score', 'votes'], ascending=False)[:50].reset_index()
# df_top10_movie_on_IMDb = df.sort_values(by=['score', 'votes'], ascending=False)[:10].reset_index()
# # export_csv_to_local_folder(df_to_export=df_top50_movie_on_IMDb,export_file_name='top50_movie_on_IMDb')
#
# # Find which type of movies is the most profitable one
# df['profit'] = df['gross'] - df['budget']
# df_sorted_by_profit_top50 = df.sort_values(by='profit', ascending=False, ignore_index=True)[:50].reset_index()
# # df_sored_by_company_year = df.groupby(by=['company', 'year'], as_index=False, sort=False)['gross', 'budget', 'profit'].sum()
# #
# # # Check which month is the most popular month to release movies
# # # df.sort_values(by='released', inplace=True)
# # df['month'] = df['released'].str.split(' ', 1).str[0]
# # df_sorted_by_month = df.groupby(by='month', as_index=False).agg({'name': 'count', 'gross': 'sum'})
# # df_sorted_by_month.sort_values(by='gross', inplace=True, ascending=False)
#
#
# # fig1 = px.scatter(df_top50_movie_on_IMDb,
# #                   x='year',
# #                   y='score',
# #                   color='name',
# #                   hover_data=['director', 'writer', 'star', 'gross', 'country'])
# # fig1.show()
#
# fig2 = px.line(df_sorted_by_profit_top50, x='year', y='profit', color='company', hover_data=['name'])
# fig2.show()

app = dash.Dash()

# app.layout = html.Div('div')


colours = {'background': '#111111', 'text': '#7FDBFF'}

# app.layout = html.Div(children=[
#             html.H1('Hello Dash!', style={'textAlign': 'center',
#                                           'color': '#7FDBFF'}),
#             html.H2('Small Hello Dash!'),
#             html.H2('H3 Hello Dash!'),
#             html.Div('Dash: Web Dashboard with Python.'),
#
# ])

app.layout = html.Div([html.H1('this is H1')])
if __name__ == '__main__':
    app.run_server()
