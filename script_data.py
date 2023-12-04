######## SAE 3-01 VCOD Collecte de données Web
###### Cnockaert Jules

# Fais avec Vscode, Python 3.11.1

# En utilisant l’API du Metropolitan Museum of New https://metmuseum.github.io/ et d’éventuelles
# données supplémentaires, vous produirez un tableau de bord offrant un état des lieux des collections du
# musée suivant un axe d’étude de votre choix. Vous devrez rendre tous les codes et les fichiers de données
# intermédiaires.


# ---------- [ Programme ] ----------

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

df_selected.to_csv("F:/IUT/Année 2 -- 2023 - 2024/VCOD/SAE 3-01 VCOD Collecte de données Web/TD 1/Cnockaert Jules SAE 3-01-VCOD Collecte automatisée de données Web/Data.csv", index=True)

end = time.time()
print("Temps d'exécution : ", end - start)

# Pour 1000 données avec 11 colonnes :  22.447643041610718 s
# Pour 10000 données avec 11 colonnes :  190.076833486557 s = 3,16794722477595 min
# Pour toutes les données (27970) avec 15 colonnes : 619.6592223644257 s = 10,3276537060737616 min
