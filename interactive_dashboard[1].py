
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

questions_data = {
    "Оқушылардың информатика пәніне көзқарасы": {
        "Өте қызықты": 18,
        "Қызықты, бірақ кейбір тақырыптар қиын": 10,
        "Орташа": 8,
        "Қиын, түсінбеймін": 8,
        "Өте қызықты, Қиын, түсінбеймін": 1
    },
    "Қай тақырып сіз үшін ең қиынырақ?": {
        "Python программалау тілі": 10,
        "Алгоритм және программалау": 8,
        "Массивтер": 5,
        "Электрондық кесте, деректер базасы": 4
    },
    "Сізге қандай оқу әдісі ыңғайлырақ?": {
        "Теориялық мәтіндер, Практикалық тапсырмалар": 12,
        "Практикалық тапсырмалар": 10,
        "Видео сабақтар, Ойын элементтері": 8,
        "Топтық жұмыс": 6
    },
    "Жасанды интеллектпен жасалған жүйе қызықты ма?": {
        "Иә, керемет болар еді": 25,
        "Білмеймін": 5
    },
    "Сабақ ойын түрінде болса, қызығушылық қалай өзгерер еді?": {
        "Қызығырақ болар еді, көбірек үйренер едім": 20,
        "Өзгеріс болмайды": 5,
        "Теория да қажет": 5
    }
}

app = Dash(__name__)

app.layout = html.Div([
    html.H1("9-сынып оқушыларының информатика сабағына көзқарасы", style={"textAlign": "center"}),
    html.H3("Автор: Н.Абжаппар | JOO Robotics", style={"textAlign": "center"}),
    dcc.Dropdown(
        id="question-dropdown",
        options=[{"label": k, "value": k} for k in questions_data.keys()],
        value="Оқушылардың информатика пәніне көзқарасы"
    ),
    dcc.Graph(id="bar-chart")
])

@app.callback(
    Output("bar-chart", "figure"),
    Input("question-dropdown", "value")
)
def update_chart(selected_question):
    data = questions_data[selected_question]
    df = pd.DataFrame({
        "Жауап": list(data.keys()),
        "Оқушы саны": list(data.values())
    })
    fig = px.bar(
        df,
        x="Оқушы саны",
        y="Жауап",
        orientation="h",
        text="Оқушы саны",
        title=selected_question,
        color="Жауап"
    )
    fig.update_layout(
        xaxis_title="Оқушылар саны",
        yaxis_title="Жауаптар",
        title_font_size=20,
        showlegend=False
    )
    return fig

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080)
