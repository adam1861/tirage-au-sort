import random
import pandas as pd
import plotly.figure_factory as ff


les_equipes_participantes = [
    "les gars de khemisset", "Oxymax", "Prime performers", "Σi²", 
    "The Math3Magicians", "Al-Khwârizmî", "Berrada's elites", 
    "Chercheurs en herbe", "Les matheuses", "PythaMaths", "The Pi-oneers", 
    "أباطرة الرياضيات", "Maτhemaτlca Prodlgla", "Les Chercheurs de l'infini", 
    "Les jeunes mathématiciens", "Les Maestros des Maths", "Les Maîtres des Variables", 
    "Lakersine", "Math Power", "MTYM", "SMI", "Checkmaters", "INSTITUT JAWAD", 
    "Prime Pioneers", "Problem Solvers", "Team EUCLID", "The Quintuple Effort", 
    "Bessie's team", "Briwat Dirichlet", "GROATS", "Hélène de Troie", "KERNELS", 
    "mathemaniacs", "Mathrix", "Trop mathisme", "Weierstrass", "ALGEBRA LENGENDS", 
    "Cicaida 4112", "Hidden gems", "Infinity And Beyond", "Ribbithmetic", 
    "Spider-math", "The π-rates", "Fantasti-X?", "Les nombres invincibles", "Mathupia"
]

nombre_pool_4=1
nombre_pool_3=14


pool_3_ = [[None for _ in range(3)] for _ in range(nombre_pool_3)] 

pool_4_ = [[None for _ in range(4)] for _ in range(nombre_pool_4)]  
  

for h in range(nombre_pool_3):
    for f in range(3):
        k = random.randint(0, len(les_equipes_participantes) - 1)
        equipe = les_equipes_participantes[k]
        pool_3_[h][f] = equipe
        les_equipes_participantes.pop(k)
        
for i in range(nombre_pool_4):
    for j in range(4):
        k = random.randint(0, len(les_equipes_participantes) - 1)
        equipe = les_equipes_participantes[k]
        pool_4_[i][j] = equipe
        les_equipes_participantes.pop(k)





df_pool_4 = pd.DataFrame(pool_4_, columns=["Equipe 1", "Equipe 2", "Equipe 3", "Equipe 4"])
df_pool_3 = pd.DataFrame(pool_3_, columns=["Equipe 1", "Equipe 2", "Equipe 3"])




fig_pool_4 = ff.create_table(df_pool_4)
fig_pool_3 = ff.create_table(df_pool_3)

fig_pool_4.show()
fig_pool_3.show()