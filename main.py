# -*- coding: utf-8 -*-
import collections
from operator import attrgetter
from pilot import Pilot

def read_and_process_data(filename):
    file = open(filename, "r")

    data = collections.defaultdict(dict)

    for line in file:
        if not line.startswith("Hora"):
            line_splitted = line.split()
            code = line_splitted[1]
            name = line_splitted[3]
            lap = line_splitted[4]
            time = line_splitted[5]
            data.setdefault(code, Pilot(name, code)).add_time(lap, time)

    return data

if __name__ == "__main__":
    data = read_and_process_data("log.txt")
    sorted_pilots = data.values()
    sorted_pilots.sort()

    print "\n=======================\n  Classificação final\n=======================\n"
    print ",".join([
        "Posição Chegada",
        "Código Piloto",
        "Nome Piloto",
        "Qtde Voltas Completadas",
        "Tempo Total de Prova"
    ])
    for v in sorted_pilots:
        print "%d,%s" % (sorted_pilots.index(v) + 1, v)
