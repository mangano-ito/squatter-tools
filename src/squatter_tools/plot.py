import plotly.graph_objects as go

def main():
    fig = go.FigureWidget()
    y = list(range(0, 100))
    fig.add_trace(
        go.Scatter(y=y),
    )
    fig.show(renderer="chrome")
