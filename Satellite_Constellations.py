import plotly.graph_objects as go

satellite_names = ['Starlink', 'OneWeb', 'Iridium']
latitudes = [40.0, -15.0, 30.0]
longitudes = [-100.0, 60.0, -70.0]

fig = go.Figure(data=go.Scattergeo(
    lat = latitudes,
    lon = longitudes,
    mode = 'markers',
    marker=dict(size=10),
    text = satellite_names
))

fig.update_layout(
    title = 'Satellite Constellations',
    geo_scope='world',
)

fig.show()