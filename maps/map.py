import os
import pandas as pd
import plotly.express as px
import plotly
import json
from GoberApi.controllers import GobernorOriginInternal


def mexMap():
    # Get gobernor origin data from internal functions or test data
    call_json = GobernorOriginInternal()
    if call_json[1] != 200:
        df = pd.read_json(
            os.path.join("tests", "origins_data.json"),
            orient="index",
        )
    else:
        df = pd.DataFrame.from_dict(call_json[0], orient="index")

    # Formatting and map visualization
    df = df.reset_index(level=0)
    df["Main_country"] = ""
    row: pd.DataFrame
    for i, row in df.iterrows():
        dftmp = pd.DataFrame(
            list((d["jurisdiction"], float(d["percent"])) for d in row.countries),
            columns=["Country", "Percent"],
        )
        row.Main_country = dftmp.loc[dftmp.Percent == dftmp.Percent.max(), "Country"][0]

    with open(os.path.join("maps", "states.geojson"), encoding="utf-8") as handle:
        state_geo = json.loads(handle.read())
    fig = px.choropleth(
        data_frame=df,
        geojson=state_geo,
        locations=df["index"],
        color="Main_country",
        featureidkey="properties.state_name",
        hover_name="Main_country",
        custom_data=[
            "forename",
            "surname",
            "secondsurname",
            df["index"],
            df["Main_country"],
        ],
    )
    fig.update_geos(
        showcountries=True, showcoastlines=True, showland=True, fitbounds="locations"
    )
    # Custom hover states description
    fig.update_traces(
        hovertemplate="Gobernador de %{customdata[3]}:<br>%{customdata[0]} %{customdata[1]} %{customdata[2]}<br>Origen del nombre: %{customdata[4]}"
    )
    # Custom hover states styles
    fig.update_layout(
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Rockwell")
    )

    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return plot_json
