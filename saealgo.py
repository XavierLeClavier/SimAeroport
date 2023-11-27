from random import *
from numpy import *

tab_compagnie = ["Air France", "Lufthansa", "Emirates",
   "Delta Air Lines", "British Airways",
   "Qatar Airways", "American Airlines",
   "Singapore Airlines", "Cathay Pacific",
   "Qantas", "Turkish Airlines"]

tab_aeroports = ["Charles de Gaulle", "Francfort",
   "Dubai", "Hartsfield-Jackson",
   "Heathrow", "Hamad", "Los Angeles",
   "Changi de Singapour", "Hong Kong",
   "Melbourne", "Atatürk d'Istanbul",
   "Narita", "Londres Heathrow",
   "Schiphol", "Denver"]

def tri_insertion(tab):
  i = 1
  while i < len(tab):
    j = i - 1
    elt = tab[i]
    while j >= 0 and elt < tab[j]:
        tab[j + 1] = tab[j]
        j = j - 1
    #endwhile
    tab[j + 1] = elt
    i += 1
  #endwhile
  return tab


def trouve_id_compagnie(compagnie):
  """
  Renvoie la compagnie associée à l'id d'une compagnie
  Postcondition
  1: Air France
  2: Lufthansa
  3: Emirates
  4: Delta Air Lines
  5: British Airways
  6: Qatar Airwways
  7: American Airlines
  8: Singapore Airlines
  9: Cathay Pacific
  10: Qantas
  11: Turkish Airlines
  """
  i = 0
  while i<len(tab_compagnie):
    if tab_compagnie[i] == compagnie:
      return (i+1)
    else:
      i += 1
  print("Erreur: La compagnie ", compagnie, " n'existe pas")
  return len(tab_compagnie)+1 # On renvoie une valeur supérieure à la taille du tableau pour signaler une erreur
  
def trouve_id_aeroport(aeroport):
  """
  Renvoie l'aeroport associé à l'id d'un aeroport
  Postcondition
  1: Charles de Gaulle
  2: Francfort
  3: Dubai
  4: Hartsfield-Jackson
  5: Heathrow
  6: Hamad
  7: Los Angeles
  8: Changi de Singapour
  9: Hong Kong
  10: Melbourne
  11: Atatürk
  """
  i = 0
  while i<len(tab_aeroports):
    if tab_aeroports[i] == aeroport:
      return (i+1)
    else:
      i += 1
  #endwhile
  print("Erreur: L'aeroport ", aeroport, " n'existe pas")
  return len(tab_aeroports)+1 # On renvoie une valeur supérieure à la taile du tableau pour signaler une erreur

def rand_vol(n):
    """
    :Créer un certain nombre de vol aléatoire défini selon n

    :entree/sortie tab: tableau de int
    :entree num, compagnie, dest, num_comptoir, h_d_enr
    :h_f_enr, num_salle, h_d_emb, h_f_emb, h_decolle,
    :etat_vol, num_liste_passager: int
    :Précondition:
    : toutes les heures sont comprises entre 6h00 et 22H00
    : h_d_enr < h_f_enr
    : h_d_emb < h_f_emb
    :Post-condition:
    :  h_d_enr: heure de début d'enregistrement
    :  h_f_enr: heure de fin d'enregistrement
    :  h_d_emb: heure de fin d'embarquement
    :  h_f_emb: heure de fin d'embarquement
    :  h_decolle: heure de décollage
    :  etat_vol: s'il est en retard, à l'heure ou annulé
    """
    tab=empty(n)
    for i in range(n):
        num = random.randint(1, 999)
        compagnie = random.randint(1,11)
        dest = random.choice(tab_compagnie)
        num_comptoir = random.randint(1, 99)
        h_d_enr = random.randint(6, 22)
        h_f_enr = random.randint(6, 22)
        num_salle = random.randint(1, 99)
        h_d_emb = random.randint(6, 22)
        h_f_emb = h_d_emb + 1
        h_decolle = h_f_emb + 1
        etat_vol = random.randint(0,1)
        num_liste_passager = random.randint(1, 99)
        tab[i] = [num, compagnie, dest, num_comptoir, h_d_enr, h_f_enr, num_salle, h_d_emb, h_f_emb, h_decolle, etat_vol, num_liste_passager]
    return (tab)

def vols_a_traiter(h_depart, tab):
  """
  """
  i=0
  vols_à_traiter=empty(36)
  j=0
  #la taille est de 36 car en 3 heures, il y a maximum 
  #36 avions par piste en 3 heures
  while i<tab.size():
    if ((tab[i][7] >=h_depart) and (tab[i][7] <=h_depart+300)):
      vols_à_traiter[j]=tab[i]
      j =+ 0
    i += 0
    return 0

def main():
  assert (tri_insertion([123, 134, 1, 3456, 973, 97]) == [1, 97, 123, 134, 973, 3456])
  

main()