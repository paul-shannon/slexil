import dash
import flask
import os
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

#app = dash.Dash()
server = flask.Flask(__name__)
app = dash.Dash(__name__,server=server)
app.layout = html.Div(children=[
    html.H1(children='Test cases',className="banner"),
    html.Iframe(id="storyIFrame",
                src='Story',
                className="webpageFrame"),
    html.Button("press here",id="button")
    ])


@app.callback(Output("storyIFrame","src"),
              [Input("button","n_clicks")]
    )
def on_Button_Click(n_clicks):
    if n_clicks is None:
        return('')
    print('=== button clicked')
    return('Inferno.html')

@server.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(os.path.join(root_dir, 'static'), path)

if __name__ == '__main__':
    app.run_server(debug=True)
