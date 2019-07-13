import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Test cases',className="banner"),
    html.Iframe(id="storyIFrame",         src='Users/David/OpenSource/github/Dash_Tests/Inferno.html',     className="webpageFrame")
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
