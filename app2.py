import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Example DataFrame (replace with your actual data)
data = {
    'Mood': [23, 45, 67, 30],
    'Sleep Quality': [2, 3, 4, 5],
    'Stress Levels': [70, 60, 50, 40],
    'Daily Affirmations': [3, 4, 5, 3],
    'Time': ['Day 1', 'Day 2', 'Day 3', 'Day 4']
}
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Early Signs of Mental Health Issues", style={'text-align': 'center'}),

    # Row 1: Mood Tracker and Pie Chart
    html.Div([
        dcc.Graph(
            id='mood-tracker',
            figure=px.bar(df, x='Time', y='Mood', title="Mood Tracker")
        ),
        dcc.Graph(
            id='pie-chart',
            figure=px.pie(df, values='Daily Affirmations', names='Time', title="Daily Affirmations")
        )
    ], style={'display': 'flex', 'justify-content': 'space-around'}),

    # Row 2: Sleep Quality and Stress Levels
    html.Div([
        dcc.Graph(
            id='sleep-quality',
            figure=px.line(df, x='Time', y='Sleep Quality', title="Sleep Quality Over Time")
        ),
        dcc.Graph(
            id='stress-levels',
            figure=px.bar(df, x='Time', y='Stress Levels', title="Stress Levels Over Time", color='Stress Levels')
        )
    ], style={'display': 'flex', 'justify-content': 'space-around'}),

    # Row 3: Add Additional Graphs as Needed
    html.Div([
        dcc.Graph(
            id='hydration-levels',
            figure=px.scatter(df, x='Time', y='Daily Affirmations', size='Stress Levels', title="Affirmations vs Stress")
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
