import csv
import numpy as np

TAB_COMPAGNIE = [
    "Delta Airlines",
    "Emirates",
    "Lufthansa",
    "British Airways",
    "Air France"]  # 5 éléments

TAB_AEROPORTS = [
    "Paris",
    "New York",
    "Dubai",
    "London",
    "Tokyo"]  # 5 éléments

def lire_fichier_csv(filepath):
    with open(filepath, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def tab_horaire():
    """
    Renvoie un tableau avec les différentes horaires de 6h00 à 22h00, toutes les 5 minutes.
    :Postcondition:
    :   tab: tableau de str contenant les horaires
    """
    tab = np.empty(192, dtype='U5')  # Crée un tableau vide de 192 éléments pour stocker les horaires avec des chaînes de longueur 5
    e = 0  # Indice pour remplir le tableau
    h = 6  # Heure de départ (6h00)
    
    while h < 22:  # Boucle pour chaque heure de 6 à 21
        m = 0 
        while m < 60:  # Boucle pour chaque tranche de 5 minutes dans une heure
            if m < 10:  # Formatage des minutes pour s'assurer que le format est toujours hh:mm
                tab[e] = f"{h}:0{m}"
            else:
                tab[e] = f"{h}:{m}"
            m += 5  # Incrémente de 5 minutes
            e += 1 
        h += 1 
    
    tab[-1] = "22:00" 
    return tab 

def tri_insertion(tab):
    i = 1
    while i < len(tab):
        j = i - 1
        elt = tab[i]
        while j >= 0 and elt < tab[j]:
            tab[j + 1] = tab[j]
            j = j - 1
        # endwhile
        tab[j + 1] = elt
        i += 1
    # endwhile
    return tab

def trouve_id_compagnie(compagnie):
  """
  Renvoie la compagnie associée à l'id d'une compagnie
  Postcondition
  1: "Delta Airlines"
  2: "Emirates"
  3: "Lufthansa"
  4: "British Airways"
  5: "Air France"
  """
  i = 0
  while i<len(TAB_COMPAGNIE):
    if TAB_COMPAGNIE[i] == compagnie:
      return (i+1)
    else:
      i += 1
  print("Erreur: La compagnie ", compagnie, " n'existe pas")
  return len(TAB_COMPAGNIE)+1 # On renvoie une valeur supérieure à la taille du tableau pour signaler une erreur
  
def trouve_id_aeroport(aeroport):
  """
  Renvoie l'aeroport associé à l'id d'un aeroport
  Postcondition
  1: "Paris"
  2: "New York"
  3: "Dubai"
  4: "London"
  5: "Tokyo"
  """
  i = 0
  while i<len(TAB_AEROPORTS):
    if TAB_AEROPORTS[i] == aeroport:
      return (i+1)
    else:
      i += 1
  #endwhile
  print("Erreur: L'aeroport ", aeroport, " n'existe pas")
  return len(TAB_AEROPORTS)+1 # On renvoie une valeur supérieure à la taile du tableau pour signaler une erreur

def recherche(num, tab):
    """
    :Recherche un vol selon son numéro
    :entree/sortie tab: tableau de int
    :entree num: int
    :sortie vol: tableau de int
    :
    :Précondition:
    :   tab est un tableau de vol
    :   num est un numero de vol
    """
    i = 0
    while i < len(tab):
        if tab[i][0] == num:
            return tab[i]
        else:
            i += 1
        #endif
    #endwhile
    #nb pasage: len(tab) - 1
    print("Erreur: Le vol ", num, " n'existe pas")
    return 0

def vols_a_traiter(h_depart, tab):
  
    """
    :Retourne la liste d'avion à traiter selon l'heure donné par h_depart
    :Précondition:
    :   h_depart: int
    :   tab: tableau de vols
    """
    vols_à_traiter = []
    for vol in tab:
        if int(vol['Heure decollage']) >= h_depart and int(vol['Heure decollage']) <= h_depart + 300:
            vols_à_traiter.append(vol)
    return vols_à_traiter

def afficher_informations_vols(tab, h):
  """
  :Affiche les informations sur les vols à venir dans les 3 heures
  :entree
  :   tab: tableau de vols
  :   h: heure qui nous intéresse
  :
  :sortie: 
  :infos: tableau avec les vols, et ses informations
  :
  :Précondition:
  :   tab est un tableau de vols avec des informations détaillées
  """
  # Convertir l'heure 'h' en minutes pour faciliter la comparaison
  # Calculer l'heure 3 heures plus tard en format HHMM
  heure = int(h)
  trois_heures_plus_tard = heure + 300

  # Filtrer les vols à venir dans les 3 heures
  vols_prochains = tab[(tab['Heure decollage'] >= heure) & (tab['Heure decollage'] <= trois_heures_plus_tard)]

  # Trier les vols par heure de décollage
  vols_prochains = vols_prochains.sort_values(by='Heure decollage')

  # Afficher les informations sur les vols
  for index, vol in vols_prochains.iterrows():
    print("Vol:", vol['Numero vol'])
    print("Compagnie:", vol['Compagnie'])
    print("Destination:", vol['Destination'])
    print("Heure de décollage:", vol['Heure decollage'])
    print("----")


def rechercher_vol(compagnie, destination, heure_decollage, tab):
    """
    :Recherche un vol par compagnie, destination, ou heure de décollage.
    :L'utilisateur peut saisir 1, 2, ou les 3 critères pour rechercher
    :Affiche uniquement le numero du vol
    :entree 
    :   compagnie: str
    :   destination: str
    :   heure_decollage: str
    :entree/sortie 
    :   tab: tableau de vols (liste de dictionnaires)
    :sortie
    :   tab_apres_criteres: liste de str (numéros de vol)
    """
    filtres = []
    if compagnie:
        filtres.append(lambda x: x['Compagnie'] == compagnie)
    if destination:
        filtres.append(lambda x: x['Destination'] == destination)
    if heure_decollage:
        filtres.append(lambda x: x['Heure decollage'] == heure_decollage)

    if filtres:
        tab_apres_criteres = [row for row in tab if all(f(row) for f in filtres)]
    else:
        tab_apres_criteres = tab

    return [row['Numero de vol'] for row in tab_apres_criteres]

# Exemple d'utilisation :
# data_vols = lire_fichier_csv('data_vols.csv')
# resultats = rechercher_vol("Air France", "Paris", "1200", data_vols)
# print("Numéros de vol trouvés :", resultats)

def afficher_liste_passagers(num_vol, tab):
    """
    :Affiche la liste des passagers pour un vol donné
    :entree num_vol: int
    :entree/sortie tab: tableau de vols
    :sortie: Aucune (affichage à l'écran)
    
    :Précondition:
    :   tab est un tableau de vols avec des informations détaillées sur les passagers
    :   num_vol est un numéro de vol
    """
    # Trouver le vol correspondant dans le tableau
    vol = tab[tab['Numero de vol'] == num_vol]

    # Vérifier si le vol a été trouvé
    if not vol.empty:
        # Récupérer la liste des passagers pour le vol trouvé
        liste_passagers = vol.iloc[0]['Liste des passagers']
        
        # Séparer les informations des passagers et les afficher
        passagers = liste_passagers.split(';')
        print(f"Liste des passagers pour le vol {num_vol} :")
        for p in passagers:
            details = p.split(',')
            print(f"Nom: {details[0]}, Prénom: {details[1]}, Date de naissance: {details[2]}, Siège: {details[3]}, Prix: {details[4]}")
    else:
        print(f"Aucun vol trouvé avec le numéro {num_vol}")

# Exemple d'utilisation :
# data_vols = pd.read_csv('chemin_vers_data_vols.csv')
# afficher_liste_passagers(29, data_vols)

def gerer_retards_annulations(num_vol, etat, tab):
    """
    :Met à jour l'état d'un vol en cas de retard ou d'annulation
    :entree num_vol: int
    :entree etat: str
    :entree/sortie tab: tableau de vols
    :sortie: Aucune (mise à jour du tableau)
    
    :Précondition:
    :   tab est un tableau de vols
    :   num_vol est un numéro de vol
    :   etat est le nouvel état du vol ('Retarde (XXmin)', 'Annule' ou "A l'heure")
    """
    # Vérifier si le numéro de vol existe dans le tableau
    if num_vol in tab['Numero de vol'].values:
        # Mettre à jour l'état du vol correspondant
        tab.loc[tab['Numero de vol'] == num_vol, 'Etat vol'] = etat
        print(f"L'état du vol numéro {num_vol} a été mis à jour : {etat}")
    else:
        # Afficher un message si le numéro de vol n'est pas trouvé
        print(f"Aucun vol trouvé avec le numéro {num_vol}")

# Exemple d'utilisation :
# data_vols = pd.read_csv('chemin_vers_data_vols.csv')
# gerer_retards_annulations(29, "Retarde (15min)", data_vols)

def valider_donnees(tab):
    """
    :Vérifie et valide les données des vols et des passagers
    :entree/sortie tab: tableau de vols
    :sortie: Aucune (signale les erreurs si présentes)
    
    :Précondition:
    :   tab est un tableau de vols avec des informations détaillées
    """
    erreurs = []
    champs_essentiels = ['Numero de vol', 'Compagnie', 'Destination', 'Heure decollage', 'Etat vol', 'Liste des passagers']
    all_keys = [list(row.keys()) for row in tab]
    if not all([champ in all_keys for champ in champs_essentiels]):
        erreurs.append("Il manque des champs essentiels.")
    
    return erreurs

# Exemple d'utilisation :
# data_vols = pd.read_csv('chemin_vers_data_vols.csv')
# valider_donnees(data_vols)

def main():
    assert (tri_insertion([123, 134, 1, 3456, 973, 97]) == [1, 97, 123, 134, 973, 3456])

    # Charger les données à partir du fichier CSV
    data_vols = lire_fichier_csv('data_vols.csv')
    
    tableau = tab_horaire()
    print(tableau)

main()