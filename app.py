######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

# Fais avec Vscode, Python 3.11.1

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd


data = pd.read_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Cnockaert Jules SAE 3-01-VCOD Collecte automatisée de données Web/Data_final.csv")

# Graphics
acquisitions_par_annee = data.groupby('accessionYear').size().reset_index(name='count')
fig1 = px.line(acquisitions_par_annee, x='accessionYear', y='count', title='Évolution du nombre d\'objets acquis par année')
fig1.update_layout(xaxis_title='Année d\'acquisition', yaxis_title='Nombre d\'objets acquis', font=dict(size=14))

fig2 = px.scatter(data, x='objectBeginDate', y='objectEndDate', title='Dates de début et de fin des objets')
fig2.update_layout(xaxis_title='Date de début', yaxis_title='Date de fin', font=dict(size=14))

data2 = data.copy()
percentage = data2['period'].value_counts(normalize=True) * 100
categories_inf_1_percent = percentage[percentage < 1].index.tolist()
data2.loc[data['period'].isin(categories_inf_1_percent), 'period'] = 'Autre'
fig3 = px.pie(data2, names='period', title='Répartition des objets par période')
fig3.update_layout(
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.99,
        bgcolor='#F2F2F2',
        bordercolor='#F2F2F2',
        borderwidth=1,
    ),
    font=dict(size=14),
    uniformtext_minsize=1,
    uniformtext_mode='hide'
)

materials_count = data['medium'].value_counts()
mask = materials_count / len(data) * 100 < 1
other_materials_count = materials_count[mask]
other_materials_sum = other_materials_count.sum()
materials_count = materials_count[~mask]
materials_count['Autre'] = other_materials_sum
fig4 = px.pie(names=materials_count.index, values=materials_count.values, title='Répartition des matériaux utilisés')
fig4.update_layout(
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.99,
        bgcolor='#F2F2F2',
        bordercolor='#F2F2F2',
        borderwidth=1,
    ),
    font=dict(size=14),
    uniformtext_minsize=1,
    uniformtext_mode='hide'
)


# Initialize the app
app = Dash(__name__)


# App layout
app.layout = html.Div(children=[
    dcc.Tabs(id="tabs", value="tab1", children=[
        dcc.Tab(label="Préambule", value="tab1"),
        dcc.Tab(label="Explication des programmes", value="tab2"),
        dcc.Tab(label="Visualisation des données", value="tab3"),
    ]),
    html.Div(id='page-content')
])

# Tab 1
tab1_layout = html.Div(children=[
    html.Div([
        html.H3("Cnockaert Jules", style={"textAlign": "left", "color": "#262626"}),
        html.Div([
            html.H1(
                "SAE 3-01 Collecte de données Web",
                style={
                    "color": "#0D0D0D",
                    "marginBottom": "20px"
                }
            ),
            html.H3(
                "The Metropolitan Museum Of Art Collection API",
                style={
                    "color": "#262626"
                })
        ], style={
            "textAlign": "center",
            "marginBottom": "80px"
        }),
        html.Div([
            html.H2(
                "Table des matières", 
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.Ul([
                html.Li(html.A("Introduction", href="#intro")),
                html.Li(html.A("Histoire du musée", href="#part1")),
                html.Li(html.A("Impact des œuvres égyptiennes sur le musée", href="#part2")),
                html.Li(html.A("API du musée", href="#part3"))
            ]),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Introduction", 
                id="intro",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "Le Metropolitan Museum of Art (ou The Met), inauguré en 1872, représente l'un des musées les plus éminents et les plus vastes du monde. Situé à New York City, sur la 5e avenue, ce musée emblématique est une institution culturelle d'une importance incommensurable. Toujours avec pour mission principale l'éducation, le Met conserve ses œuvres d'art et morceaux d'histoire dans des salles séparées en catégories. Dans ce rapport, nous nous pencherons sur l'aile de l'art égyptien et son importance dans l'histoire du musée. Cette aile dédiée est une fenêtre fascinante sur la richesse de la civilisation égyptienne, offrant aux visiteurs un aperçu saisissant de l'histoire, de la mythologie et de l'art de l'Égypte ancienne.",
                style={
                    "color": "#262626"
                }
            ),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Histoire du musée", 
                id="part1",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "L'histoire du Met est intimement liée à la vision d'un groupe d'individus éclairés cherchant à établir une institution célébrant l'art et la culture à travers les âges. Fondé grâce à des dons de collections privées, le musée a rapidement élargi sa portée, acquérant des œuvres d'art du monde entier et développant des départements consacrés à diverses périodes historiques et à diverses formes d'expression artistique. Au fil des ans, le Met a connu une expansion significative, ajoutant des galeries, des collections et des programmes éducatifs qui le positionnent aujourd'hui comme un leader mondial dans le domaine de l'art et de la préservation culturelle. En ce qui concerne l'aile de l'art égyptien, le Met a commencé à acquérir ses premières pièces dès 1874, peu après la création du musée, marquant ainsi le début d'une collection égyptienne d'une richesse inestimable.",
                style={
                    "color": "#262626"
                }
            ),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Impact des œuvres égyptiennes sur le musée", 
                id="part2",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "L'Égypte ancienne a joué un rôle crucial dans la formation des collections du Met. À la fin du 19e siècle, le musée a financé et mené des expéditions archéologiques en Égypte, conduisant à l'acquisition d'une vaste gamme d'objets et d'œuvres d'art égyptiens. Les collections égyptiennes du Met comprennent des artefacts variés, des sculptures monumentales aux artefacts du quotidien, reflétant la richesse et la profondeur de la civilisation égyptienne, notamment le fameux temple de Dendur, grand temple égyptien exposé dans une vaste salle dédiée au Met, pour ne citer que lui. Ces acquisitions ont élargi la renommée du musée et ont joué un rôle crucial dans la recherche et la compréhension de cette ancienne civilisation par les historiens de l'art et les archéologues, offrant au public une immersion captivante dans l'histoire de l'Égypte ancienne.",
                style={
                    "color": "#262626"
                }
            ),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "API du musée", 
                id="part3",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "L'API du Met est une interface numérique mise en place en 2018 par le musée pour permettre un accès facilité à sa collection, toujours dans un but éducatif. Cette API fournit aux développeurs des données structurées sur les œuvres d'art du musée, y compris des images haute résolution, des informations sur les artistes, des descriptions détaillées et des informations historiques. Elle permet également des fonctionnalités de recherche avancée, permettant aux utilisateurs d'explorer la collection du Met de manière interactive. L'API du Met a ouvert de nouvelles possibilités pour les développeurs et les amateurs d'art, encourageant la création d'applications et d'outils novateurs exploitant les richesses de la collection du musée, à l'instar de ce travail que nous produisons, offrant ainsi une immersion technologique dans le patrimoine culturel du Metropolitan Museum of Art.",
                style={
                    "color": "#262626"
                }
            ),
        ])
    ], style={"width": "65%", "margin": "auto", "backgroundColor": "#F2F2F2", "padding": "20px"})
], style={
    "padding": "20px",
    "width": "100%",
    "position": "relative"
})

# Tab 2
tab2_layout = html.Div(children=[
    html.Div([
        html.H3("Cnockaert Jules", style={"textAlign": "left", "color": "#262626"}),
        html.H1(
            "Explication des programmes",
            style={
                "color": "#0D0D0D",
                "textAlign": "center",
                "marginBottom": "80px"
            }),
        html.Br(),
        html.Div([
            html.H2(
                "Table des matières", 
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.Ul([
                html.Li(html.A("Récupération des données via l'API", href="#recup")),
                html.Li(html.A("Nettoyage des données", href="#clean")),
                html.Li(html.A("Application pour la visualisation avec Dash", href="#app"))
            ]),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Récupération des données via l'API",
                id="recup",
                style={
                    "color": "#0D0D0D"
                }),
            html.Pre(
                html.Code(
                    '''
######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

import time
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

start = time.time()

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=10"
req = requests.get(url)
wb = req.json()

object_ids = wb["objectIDs"] # total 27970 données

def get_object_id(id):
    id_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
    id_req = requests.get(id_url)
    return id_req.json()

# Utilisation du ThreadPoolExecutor pour exécuter les requêtes en parallèle (réduit le temps d'execution du programme par 10x)
with ThreadPoolExecutor(max_workers=10) as executor: # limite de 80 requetes par seconde
    list_objet = list(executor.map(get_object_id, object_ids))

df = pd.DataFrame(list_objet)
selected_columns = ['objectID', 'GalleryNumber', 'title', 'accessionYear', 'objectBeginDate', 'objectEndDate', 'medium', 'period', 'dynasty', 'reign', 'country', 'region', 'subregion', 'locale']
df_selected = df[selected_columns]

# Supprimer les doublons (au cas où) 
df_selected = df_selected.drop_duplicates()

df_selected.to_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Projet/Data.csv", index=True)

end = time.time()
print("Temps d'exécution : ", end - start)

# Pour 1000 données avec 11 colonnes :  22.447643041610718 s
# Pour 10000 données avec 11 colonnes :  190.076833486557 s = 3,16794722477595 min
# Pour toutes les données (27970) avec 15 colonnes : 619.6592223644257 s = 10,3276537060737616 min
                    ''',
                    style={ 
                        "margin": 0, 
                        "padding": "10px", 
                    }
                ),
            style={
                "border": "1px solid #ccc",
                "borderRadius": "4px",
                "overflowX": "auto",
                "margin": "10px",
                "position": "relative",
                "padding": "10px"
            }),
            html.P(
                "Pour collecter des données via l'API du Met, nous avons suivi principalement les procédures enseignées en cours. Tout d'abord, nous avons créé une URL en utilisant les explications fournies dans la documentation de l'API du Met. Ensuite, nous avons effectué une requête à cette URL en utilisant la bibliothèque requests. Nous avons interprété les résultats de cette requête au format JSON. En suivant cela, nous avons créé une liste contenant les identifiants (ID) des différents objets. Ces ID ont été utilisés pour récupérer les données de chaque objet en utilisant notre fonction get_object_id(), qui nous permet de récupérer toutes les informations au format JSON pour chaque objet en fonction de son ID. Pour exécuter cette fonction plus efficacement, nous avons utilisé la bibliothèque concurrent.futures avec ThreadPoolExecutor. Cette approche nous a permis d'exécuter notre fonction plusieurs fois simultanément, réduisant ainsi considérablement le temps nécessaire pour collecter les données. Ensuite, nous avons transformé notre liste d'objets en un DataFrame à l'aide de la bibliothèque Pandas. Nous avons sélectionné les colonnes pertinentes nécessaires à la visualisation des données, en nous assurant de supprimer les doublons éventuels. Enfin, pour une utilisation ultérieure, nous avons sauvegardé notre DataFrame dans un fichier CSV, permettant ainsi de réutiliser facilement ces données dans d'autres programmes.",
                style={
                    "color": "#262626"
                })
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Nettoyage des données",
                id="clean",
                style={
                    "color": "#0D0D0D"
                }),
            html.Pre(
                html.Code(
                    '''
######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

import pandas as pd
import numpy as np

data = pd.read_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Projet/Data.csv")

for i in data.columns:
    if data[i].dtype == "object":
        data[i] = data[i].str.replace(" \(\?\)", "", regex=False)
        data[i] = data[i].fillna("Unknown")
    if data[i].dtype == "float64":
        data[i] = data[i].replace([np.inf, -np.inf], np.nan) 
        data[i] = data[i].fillna(np.nan) 
        data[i] = data[i].astype("Int64") 
    if data[i].dtype == "int64":
        data[i] = data[i].fillna(np.nan)

data.to_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Projet/Data_final.csv", index=False)
                    ''',
                    style={
                        "margin": 0, 
                        "padding": "10px",
                    }
                ),
            style={
                "border": "1px solid #ccc",
                "borderRadius": "4px",
                "overflowX": "auto",
                "margin": "10px",
                "position": "relative",
                "padding": "10px"
            }),
            html.P(
                "Pendant le processus de nettoyage des données, nous avons adopté une approche qui considère toute donnée manquante comme délibérée de la part du Metropolitan Museum of Art. En d'autres termes, nous supposons que si des données sont absentes dans une ligne (par exemple, des cellules vides), c'est parce que le musée ne possède pas cette information, et non pas en raison d'une erreur de sa part. Pour les colonnes de type 'object' (équivalent du type 'string'), nous avons principalement remplacé les valeurs manquantes par 'Unknown'. Pour les colonnes de type 'float64', nous les avons converties en 'int64'. En ce qui concerne les données de type 'int64', nous avons laissé les valeurs manquantes comme NaN (Not a Number) en utilisant la bibliothèque NumPy. Enfin, après ce processus de nettoyage, nous avons enregistré notre jeu de données dans un nouveau fichier CSV, prêt à être utilisé pour d'autres applications.",
                style={
                    "color": "#262626"
                })
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Application pour la visualisation avec Dash",
                id="app",
                style={
                    "color": "#0D0D0D"
                }),
            html.Pre(
                html.Code(
                    '''
######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

# Fais avec Vscode, Python 3.11.1

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import pandas as pd


data = pd.read_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Projet/Data_final.csv")

# Graphics
acquisitions_par_annee = data.groupby('accessionYear').size().reset_index(name='count')
fig1 = px.line(acquisitions_par_annee, x='accessionYear', y='count', title='Évolution du nombre d\'objets acquis par année')
fig1.update_layout(xaxis_title='Année d\'acquisition', yaxis_title='Nombre d\'objets acquis', font=dict(size=14))

fig2 = px.scatter(data, x='objectBeginDate', y='objectEndDate', title='Dates de début et de fin des objets')
fig2.update_layout(xaxis_title='Date de début', yaxis_title='Date de fin', font=dict(size=14))

data2 = data.copy()
percentage = data2['period'].value_counts(normalize=True) * 100
categories_inf_1_percent = percentage[percentage < 1].index.tolist()
data2.loc[data['period'].isin(categories_inf_1_percent), 'period'] = 'Autre'
fig3 = px.pie(data2, names='period', title='Répartition des objets par période')
fig3.update_layout(
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.99,
        bgcolor='#F2F2F2',
        bordercolor='#F2F2F2',
        borderwidth=1,
    ),
    font=dict(size=14),
    uniformtext_minsize=1,
    uniformtext_mode='hide'
)

materials_count = data['medium'].value_counts()
mask = materials_count / len(data) * 100 < 1
other_materials_count = materials_count[mask]
other_materials_sum = other_materials_count.sum()
materials_count = materials_count[~mask]
materials_count['Autre'] = other_materials_sum
fig4 = px.pie(names=materials_count.index, values=materials_count.values, title='Répartition des matériaux utilisés')


# Initialize the app
app = Dash(__name__)


# App layout
app.layout = html.Div(children=[
    dcc.Tabs(id="tabs", value="tab1", children=[
        dcc.Tab(label="Préambule", value="tab1"),
        dcc.Tab(label="Explication des programmes", value="tab2"),
        dcc.Tab(label="Visualisation des données", value="tab3"),
    ]),
    html.Div(id='page-content')
])

# Tab 1
tab1_layout = html.Div(children=[
    html.Div([
        html.H3("Cnockaert Jules", style={"textAlign": "left", "color": "#262626"}),
        html.Div([
            html.H1(
                "SAE 3-01 Collecte de données Web",
                style={
                    "color": "#0D0D0D",
                    "marginBottom": "20px"
                }
            ),
            html.H3(
                "The Metropolitan Museum Of Art Collection API",
                style={
                    "color": "#262626"
                })
        ], style={
            "textAlign": "center",
            "marginBottom": "80px"
        }),
        html.Div([
            html.H2(
                "Table des matières", 
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.Ul([
                html.Li(html.A("Introduction", href="#intro")),
                html.Li(html.A("Histoire du musée", href="#part1")),
                html.Li(html.A("Impact des œuvres égyptiennes sur le musée", href="#part2")),
                html.Li(html.A("API du musée", href="#part3"))
            ]),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Introduction", 
                id="intro",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "Le Metropolitan Museum of Art (ou The Met), inauguré en 1872, représente l'un des musées les plus éminents et les plus vastes du monde. Situé à New York City, sur la 5e avenue, ce musée emblématique est une institution culturelle d'une importance incommensurable. Toujours avec pour mission principale l'éducation, le Met conserve ses œuvres d'art et morceaux d'histoire dans des salles séparées en catégories. Dans ce rapport, nous nous pencherons sur l'aile de l'art égyptien et son importance dans l'histoire du musée. Cette aile dédiée est une fenêtre fascinante sur la richesse de la civilisation égyptienne, offrant aux visiteurs un aperçu saisissant de l'histoire, de la mythologie et de l'art de l'Égypte ancienne.",
                style={
                    "color": "#262626"
                }
            ),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Histoire du musée", 
                id="part1",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "L'histoire du Met est intimement liée à la vision d'un groupe d'individus éclairés cherchant à établir une institution célébrant l'art et la culture à travers les âges. Fondé grâce à des dons de collections privées, le musée a rapidement élargi sa portée, acquérant des œuvres d'art du monde entier et développant des départements consacrés à diverses périodes historiques et à diverses formes d'expression artistique. Au fil des ans, le Met a connu une expansion significative, ajoutant des galeries, des collections et des programmes éducatifs qui le positionnent aujourd'hui comme un leader mondial dans le domaine de l'art et de la préservation culturelle. En ce qui concerne l'aile de l'art égyptien, le Met a commencé à acquérir ses premières pièces dès 1874, peu après la création du musée, marquant ainsi le début d'une collection égyptienne d'une richesse inestimable.",
                style={
                    "color": "#262626"
                }
            ),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Impact des œuvres égyptiennes sur le musée", 
                id="part2",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "L'Égypte ancienne a joué un rôle crucial dans la formation des collections du Met. À la fin du 19e siècle, le musée a financé et mené des expéditions archéologiques en Égypte, conduisant à l'acquisition d'une vaste gamme d'objets et d'œuvres d'art égyptiens. Les collections égyptiennes du Met comprennent des artefacts variés, des sculptures monumentales aux artefacts du quotidien, reflétant la richesse et la profondeur de la civilisation égyptienne, notamment le fameux temple de Dendur, grand temple égyptien exposé dans une vaste salle dédiée au Met, pour ne citer que lui. Ces acquisitions ont élargi la renommée du musée et ont joué un rôle crucial dans la recherche et la compréhension de cette ancienne civilisation par les historiens de l'art et les archéologues, offrant au public une immersion captivante dans l'histoire de l'Égypte ancienne.",
                style={
                    "color": "#262626"
                }
            ),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "API du musée", 
                id="part3",
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.P(
                "L'API du Met est une interface numérique mise en place en 2018 par le musée pour permettre un accès facilité à sa collection, toujours dans un but éducatif. Cette API fournit aux développeurs des données structurées sur les œuvres d'art du musée, y compris des images haute résolution, des informations sur les artistes, des descriptions détaillées et des informations historiques. Elle permet également des fonctionnalités de recherche avancée, permettant aux utilisateurs d'explorer la collection du Met de manière interactive. L'API du Met a ouvert de nouvelles possibilités pour les développeurs et les amateurs d'art, encourageant la création d'applications et d'outils novateurs exploitant les richesses de la collection du musée, à l'instar de ce travail que nous produisons, offrant ainsi une immersion technologique dans le patrimoine culturel du Metropolitan Museum of Art.",
                style={
                    "color": "#262626"
                }
            ),
        ])
    ], style={"width": "65%", "margin": "auto", "backgroundColor": "#F2F2F2", "padding": "20px"})
], style={
    "padding": "20px",
    "width": "100%",
    "position": "relative"
})

# Tab 2
tab2_layout = html.Div(children=[
    html.Div([
        html.H3("Cnockaert Jules", style={"textAlign": "left", "color": "#262626"}),
        html.H1(
            "Explication des programmes",
            style={
                "color": "#0D0D0D",
                "textAlign": "center",
                "marginBottom": "80px"
            }),
        html.Br(),
        html.Div([
            html.H2(
                "Table des matières", 
                style={
                    "color": "#0D0D0D"
                }
            ),
            html.Ul([
                html.Li(html.A("Récupération des données via l'API", href="#recup")),
                html.Li(html.A("Nettoyage des données", href="#clean")),
                html.Li(html.A("Application pour la visualisation avec Dash", href="#app"))
            ]),
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Récupération des données via l'API",
                id="recup",
                style={
                    "color": "#0D0D0D"
                }),
            html.Pre(
                html.Code(
                    ''''''
######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

import time
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

start = time.time()

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=10"
req = requests.get(url)
wb = req.json()

object_ids = wb["objectIDs"] # total 27970 données

def get_object_id(id):
    id_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
    id_req = requests.get(id_url)
    return id_req.json()

# Utilisation du ThreadPoolExecutor pour exécuter les requêtes en parallèle (réduit le temps d'execution du programme par 10x)
with ThreadPoolExecutor(max_workers=10) as executor: # limite de 80 requetes par seconde
    list_objet = list(executor.map(get_object_id, object_ids))

df = pd.DataFrame(list_objet)
selected_columns = ['objectID', 'GalleryNumber', 'title', 'accessionYear', 'objectBeginDate', 'objectEndDate', 'medium', 'period', 'dynasty', 'reign', 'country', 'region', 'subregion', 'locale']
df_selected = df[selected_columns]

# Supprimer les doublons (au cas où) 
df_selected = df_selected.drop_duplicates()

df_selected.to_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Projet/Data.csv", index=True)

end = time.time()
print("Temps d'exécution : ", end - start)

# Pour 1000 données avec 11 colonnes :  22.447643041610718 s
# Pour 10000 données avec 11 colonnes :  190.076833486557 s = 3,16794722477595 min
# Pour toutes les données (27970) avec 15 colonnes : 619.6592223644257 s = 10,3276537060737616 min
                    '''''',
                    style={ 
                        "margin": 0, 
                        "padding": "10px", 
                    }
                ),
            style={
                "border": "1px solid #ccc",
                "borderRadius": "4px",
                "overflowX": "auto",
                "margin": "10px",
                "position": "relative",
                "padding": "10px"
            }),
            html.P(
                "Pour collecter des données via l'API du Met, nous avons suivi principalement les procédures enseignées en cours. Tout d'abord, nous avons créé une URL en utilisant les explications fournies dans la documentation de l'API du Met. Ensuite, nous avons effectué une requête à cette URL en utilisant la bibliothèque requests. Nous avons interprété les résultats de cette requête au format JSON. En suivant cela, nous avons créé une liste contenant les identifiants (ID) des différents objets. Ces ID ont été utilisés pour récupérer les données de chaque objet en utilisant notre fonction get_object_id(), qui nous permet de récupérer toutes les informations au format JSON pour chaque objet en fonction de son ID. Pour exécuter cette fonction plus efficacement, nous avons utilisé la bibliothèque concurrent.futures avec ThreadPoolExecutor. Cette approche nous a permis d'exécuter notre fonction plusieurs fois simultanément, réduisant ainsi considérablement le temps nécessaire pour collecter les données. Ensuite, nous avons transformé notre liste d'objets en un DataFrame à l'aide de la bibliothèque Pandas. Nous avons sélectionné les colonnes pertinentes nécessaires à la visualisation des données, en nous assurant de supprimer les doublons éventuels. Enfin, pour une utilisation ultérieure, nous avons sauvegardé notre DataFrame dans un fichier CSV, permettant ainsi de réutiliser facilement ces données dans d'autres programmes.",
                style={
                    "color": "#262626"
                })
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Nettoyage des données",
                id="clean",
                style={
                    "color": "#0D0D0D"
                }),
            html.Pre(
                html.Code(
                    ''''''
######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

import pandas as pd
import numpy as np

data = pd.read_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Projet/Data.csv")

for i in data.columns:
    if data[i].dtype == "object":
        data[i] = data[i].str.replace(" \(\?\)", "", regex=False)
        data[i] = data[i].fillna("Unknown")
    if data[i].dtype == "float64":
        data[i] = data[i].replace([np.inf, -np.inf], np.nan) 
        data[i] = data[i].fillna(np.nan) 
        data[i] = data[i].astype("Int64") 
    if data[i].dtype == "int64":
        data[i] = data[i].fillna(np.nan)

data.to_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Projet/Data_final.csv", index=False)
                    '''''',
                    style={
                        "margin": 0, 
                        "padding": "10px",
                    }
                ),
            style={
                "border": "1px solid #ccc",
                "borderRadius": "4px",
                "overflowX": "auto",
                "margin": "10px",
                "position": "relative",
                "padding": "10px"
            }),
            html.P(
                "Pendant le processus de nettoyage des données, nous avons adopté une approche qui considère toute donnée manquante comme délibérée de la part du Metropolitan Museum of Art. En d'autres termes, nous supposons que si des données sont absentes dans une ligne (par exemple, des cellules vides), c'est parce que le musée ne possède pas cette information, et non pas en raison d'une erreur de sa part. Pour les colonnes de type 'object' (équivalent du type 'string'), nous avons principalement remplacé les valeurs manquantes par 'Unknown'. Pour les colonnes de type 'float64', nous les avons converties en 'int64'. En ce qui concerne les données de type 'int64', nous avons laissé les valeurs manquantes comme NaN (Not a Number) en utilisant la bibliothèque NumPy. Enfin, après ce processus de nettoyage, nous avons enregistré notre jeu de données dans un nouveau fichier CSV, prêt à être utilisé pour d'autres applications.",
                style={
                    "color": "#262626"
                })
        ]),
        html.Br(),
        html.Div([
            html.H2(
                "Application pour la visualisation avec Dash",
                id="app",
                style={
                    "color": "#0D0D0D"
                }),
            html.Pre(
                html.Code(
                    '''
                    ''',
                    style={
                        "margin": 0, 
                        "padding": "10px",
                    }
                ),
            style={
                "border": "1px solid #ccc",
                "borderRadius": "4px",
                "overflowX": "auto",
                "margin": "10px",
                "position": "relative",
                "padding": "10px"
            }),
            html.P(
                "Dans un premier temps, nous pouvons observer le rendu de l'application grâce à l'inspecteur d'éléments de notre navigateur web. Pour créer cette application web, nous avons utilisé la bibliothèque Dash avec ses extensions html, dcc, callback, Output, Input, ainsi que la bibliothèque dash_table. De plus, nous avons utilisé la bibliothèque plotly.express pour concevoir un site internet à partir de Python, incluant un tableau de bord sur la page suivante. Pour la structure de notre site, nous avons créé trois pages distinctes afin de présenter les informations de manière précise et complète : Une page d'introduction présentant le préambule de notre sujet et les informations nécessaires pour la visualisation. Une page détaillant la création du code, les cheminements de réflexion utilisés et les méthodes employées pour sa réalisation. Une page dédiée à la visualisation interactive, qui constitue la partie principale de ce site.",
                style={
                    "color": "#262626"
                })
        ])
    ], style={"width": "65%", "margin": "auto", "backgroundColor": "#F2F2F2", "padding": "20px"})
], style={
    "padding": "20px",
    "width": "100%",
    "position": "relative"
})

# Tab 3
tab3_layout = html.Div(children=[
    html.H3("Cnockaert Jules", style={"textAlign": "left", "color": "#262626"}),
    html.H1("Visualisations interactives", style={"marginBottom": "80px", "textAlign": "center", "color": "#262626"}),
    html.Br(),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig1)
        ], style={'display': 'inline-block', 'width': '100%'}),
        html.Div([
            dcc.Graph(figure=fig2)
        ], style={'display': 'inline-block', 'width': '100%'})
    ], style={
        'display': 'grid', 
        'grid-template-columns': 'repeat(2, 1fr)', 
        'grid-gap': '20px'
        }
    ),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig3)
        ], style={'display': 'inline-block', 'width': '100%'}),
        html.Div([
            dcc.Graph(figure=fig4)
        ], style={'display': 'inline-block', 'width': '100%'})
    ], style={
        'display': 'grid', 
        'grid-template-columns': 'repeat(2, 1fr)', 
        'grid-gap': '20px'
        }
    ),
], className="container")


# Callback 
@app.callback(
        Output('page-content', 'children'), 
        [Input('tabs', 'value')]
)


#Fonction
def display_page(tab):
    if tab == 'tab1':
        return tab1_layout
    elif tab == 'tab2':
        return tab2_layout
    elif tab == 'tab3':
        return tab3_layout


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
                    ''',
                    style={
                        "margin": 0, 
                        "padding": "10px",
                    }
                ),
            style={
                "border": "1px solid #ccc",
                "borderRadius": "4px",
                "overflowX": "auto",
                "margin": "10px",
                "position": "relative",
                "padding": "10px"
            }),
            html.P(
                "Dans un premier temps, nous pouvons observer le rendu de l'application grâce à l'inspecteur d'éléments de notre navigateur web. Pour créer cette application web, nous avons utilisé la bibliothèque Dash avec ses extensions html, dcc, callback, Output, Input, ainsi que la bibliothèque dash_table. De plus, nous avons utilisé la bibliothèque plotly.express pour concevoir un site internet à partir de Python, incluant un tableau de bord sur la page suivante. Pour la structure de notre site, nous avons créé trois pages distinctes afin de présenter les informations de manière précise et complète : Une page d'introduction présentant le préambule de notre sujet et les informations nécessaires pour la visualisation. Une page détaillant la création du code, les cheminements de réflexion utilisés et les méthodes employées pour sa réalisation. Une page dédiée à la visualisation interactive, qui constitue la partie principale de ce site.",
                style={
                    "color": "#262626"
                })
        ])
    ], style={"width": "65%", "margin": "auto", "backgroundColor": "#F2F2F2", "padding": "20px"})
], style={
    "padding": "20px",
    "width": "100%",
    "position": "relative"
})

# Tab 3
tab3_layout = html.Div(children=[
    html.H3("Cnockaert Jules", style={"textAlign": "left", "color": "#262626"}),
    html.H1("Visualisations interactives", style={"marginBottom": "80px", "textAlign": "center", "color": "#262626"}),
    html.Br(),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig1)
        ], style={'display': 'inline-block', 'width': '100%'}),
        html.Div([
            dcc.Graph(figure=fig2)
        ], style={'display': 'inline-block', 'width': '100%'})
    ], style={
        'display': 'grid', 
        'grid-template-columns': 'repeat(2, 1fr)', 
        'grid-gap': '20px'
        }
    ),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig3)
        ], style={'display': 'inline-block', 'width': '100%'}),
        html.Div([
            dcc.Graph(figure=fig4)
        ], style={'display': 'inline-block', 'width': '100%'})
    ], style={
        'display': 'grid', 
        'grid-template-columns': 'repeat(2, 1fr)', 
        'grid-gap': '20px'
        }
    ),
], className="container")


# Callback 
@app.callback(
        Output('page-content', 'children'), 
        [Input('tabs', 'value')]
)


#Fonction
def display_page(tab):
    if tab == 'tab1':
        return tab1_layout
    elif tab == 'tab2':
        return tab2_layout
    elif tab == 'tab3':
        return tab3_layout


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

