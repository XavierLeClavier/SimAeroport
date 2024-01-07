from random import *


def rand_vol(n):
    """
    :Créer un certain nombre de vol aléatoire défini selon n

    :entree/sortie tab: tableau de int
    :entree num, compagnie, dest, num_comptoir, h_d_enr
    :h_f_enr, num_salle, h_d_emb, h_f_emb, h_decolle,
    :etat_vol, num_liste_passager: int
    :
    :Précondition:
    :   toutes les heures sont comprises entre 6h00 et 22H00
    :   h_d_enr < h_f_enr
    :   h_d_emb < h_f_emb
    :Post-condition:
    :   h_d_enr: heure de début d'enregistrement
    :   h_f_enr: heure de fin d'enregistrement
    :   h_d_emb: heure de fin d'embarquement
    :   h_f_emb: heure de fin d'embarquement
    :   h_decolle: heure de décollage
    :   etat_vol: s'il est en retard, à l'heure ou annulé
    """
    tab=empty(n)
    for i in range(n):
        num = i
        compagnie = random.randint(1,11)
        dest = randint(1.15)
        num_comptoir = random.randint(1, 99)
        h_d_enr = random.randint(0, 156)
        h_f_enr = h_d_enr + 12
        num_salle = random.randint(1, 99)
        h_d_emb = h_d_enr + 12
        h_f_emb = h_d_emb + 12
        h_decolle = h_f_emb + 12
        etat_vol = random.randint(0,1)
        num_liste_passager = random.randint(1, 99)
        tab[i] = [num, compagnie, dest, num_comptoir, h_d_enr, h_f_enr, num_salle, h_d_emb, h_f_emb, h_decolle, etat_vol, num_liste_passager]
    return (tab)