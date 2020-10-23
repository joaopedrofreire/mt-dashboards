import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

student_outcomes = pd.DataFrame({
    "names": ["Passou", "Falhou", "Pulou", "Sem tentativas"],
    "values": [60, 10, 5,25],
})
class_outcomes = pd.DataFrame({
    "names": ["Passou", "Falhou", "Pulou", "Sem tentativas"],
    "values": [50, 5, 5,40],
})

colors =['limegreen','red','yellow','rgb(222,226,230)']

fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]], column_widths=[0.7, 0.3])

fig.add_trace(go.Pie(labels=student_outcomes["names"],
                             values=student_outcomes["values"], 
                             title=dict(
                                text="Você",
                                font=dict(family="Nunito", size=40, color='rgb(76,83,90)')),
                             textinfo="none",
                             hole=.9,
                             marker=dict(colors=colors),
                             hoverinfo='percent'),1,1)

fig.add_trace(go.Pie(labels=class_outcomes["names"],
                             values=class_outcomes["values"], 
                             title=dict(
                                text="Sua turma",
                                font=dict(family="Nunito", size=17, color='rgb(76,83,90)')),
                             textinfo="none",
                             hole=.9,
                             marker=dict(colors=colors),
                             hoverinfo='percent'),1,2)

fig.update_layout(autosize=True,
                  margin=dict(
                      l=10,
                      r=30,
                      b=0,
                      t=0,
                      pad=4
                  ),
                  legend=dict(
                      orientation="h",
                      xanchor='center',
                      x=0.5,
                      font=dict(family="Nunito",
                                size=16,
                                color='rgb(76,83,90)')),
                   hoverlabel=dict(bgcolor='white',
                                   font_size=15,
                                   font_family='Nunito')) 

fig.write_html("exercicios-chart.html")

aulas = [1,2,3,4,5,6,7,8,9,10,11,12]
erros = [8,6,7,3,5,5,2,4]
erros_turma = [6,6,5,5,4,5,4,4]

colors = []
for i in range(len(erros)):
  if erros[i] == erros_turma[i]:
    colors.append('#2196F3');
  elif erros[i] < erros_turma[i]:
    colors.append('limegreen')
  else:
    colors.append('red')
#2196F3
#64B5F6

fig2 = go.Figure()

fig2.add_trace(go.Scatter(name='Sua turma',
                          x=aulas,
                          y=erros_turma,
                          line_shape='linear',
                          line = dict(color='rgb(200,200,200)', width=5),
                          marker = dict(size=15, color='rgb(200,200,200)'),
                          hoverinfo='y'))

fig2.add_trace(go.Scatter(name='Você',
                          x=aulas,
                          y=erros,
                          line_shape='linear',
                          line = dict(color='#2196F3', width=5),
                          marker = dict(size=15, color=colors),
                          hoverinfo='y'))

fig2.update_layout(autosize=True,
                   margin=dict(
                      l=10,
                      r=10,
                      b=10,
                      t=0,
                      pad=4
                   ),
                   legend=dict(
                      traceorder='reversed',
                      yanchor="top",
                      y=0.99,
                      xanchor="right",
                      x=0.99,
                      orientation="h",
                      font=dict(size=16)
                   ),
                   plot_bgcolor='white',
                   xaxis_title='Aula',
                   yaxis_title='Erros',
                   font=dict(family="Nunito",
                             size=14,
                             color='rgb(76,83,90)'),
                   hoverlabel=dict(bgcolor='white',
                                   font_size=15,
                                   font_family='Nunito'))

fig.write_html("exercicios-chart.html", config={'displayModeBar': False})
fig2.write_html("aulas-chart.html", config={'displayModeBar': False})