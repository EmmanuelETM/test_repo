from colorama import Fore as F, init
from tabulate import tabulate

init(autoreset= True)

ls = [1,2,3,4,5,6,7,8,9]

tabla = [
[ls[0], ls[1], ls[2]],
[ls[3], ls[4], ls[5]],
[ls[6], ls[7], ls[8]]
]

print(F.CYAN + tabulate(tabla))
