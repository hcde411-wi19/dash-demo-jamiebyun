import dash
import dash_core_components as dcc
import dash_html_components as html


Category_in_order = ['Engine_Size(l)', 'Cyl', 'HP', 'City', 'MPG', 'Hwy', 'MPG', 'Weight',	'Wheel', 'Base', 'Len', 'Width', 'Net']
Acura_RL_4dr = [3.5, 6,	225, 18, 24, 3880, 115, 197, 72, 10.8353331]
Acura_RL_wNavigation_4dr =[3.5, 6, 225, 18, 24, 3893, 1151, 197, 72, 10.84598698]
Acura_MDX = [3.5, 6, 265, 17, 23, 4451, 106, 189, 77, 9.765868182]
Acura_TL_4dr = [3.2, 6, 270, 20, 28, 3575, 108, 186, 72, 8.724205453]


app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a HCDE 411 Exercise 2
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': Category_in_order, 'y': Acura_RL_4dr, 'type': 'bar', 'name': 'Acura_RL_4dr'},
                {'x': Category_in_order, 'y': Acura_RL_wNavigation_4dr, 'type': 'bar', 'name': 'Acura_RL_wNavigation_4dr'},
                {'x': Category_in_order, 'y': Acura_MDX, 'type': 'bar', 'name': 'Acura_MDX'},
                {'x': Category_in_order, 'y': Acura_TL_4dr, 'type': 'bar', 'name': 'Acura_TL_4dr'},

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Acura Model Car Characteristics Comparison '
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)

