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
            speed = line_splitted[6]
            data.setdefault(code, Pilot(name, code)).add_lap(lap, time, speed)

    return data

def render_the_best_lap_per_pilot(sorted_pilots):
    print "\n===========================\nMelhor volta de cada piloto\n===========================\n"
    print ",".join([
        "Nome Piloto",
        "Nº Volta",
        "Tempo Volta"
    ])
    for pilot in sorted_pilots:
        print "%s,%s,%s" % (pilot.name, pilot.better_lap, pilot.better_time)

def render_the_best_time(sorted_pilots):
    print "\n========================\nMelhor volta da corrida\n========================\n"
    pilot_with_better_time = min(sorted_pilots,key=attrgetter('better_time'))
    print "Nome Piloto: %s\nNº Volta: %s\nTempo Volta: %s" % (pilot_with_better_time.name, pilot_with_better_time.better_lap, pilot_with_better_time.better_time)

def render_time_after_the_first(sorted_pilots):
    print "\n================================\nTempo que chegou após o vencedor\n================================\n"
    for v in sorted_pilots:
        if(sorted_pilots.index(v) != 0):
            print "%s: %s" % (v.name, v.get_time_after(sorted_pilots[0].total_time))

def render_average_speed_per_pilot(sorted_pilots):
    print "\n================================\nVelocidade média de cada piloto\n================================\n"
    for v in sorted_pilots:
        if(sorted_pilots.index(v) != 0):
            print "%s: %s" % (v.name, v.get_average_speed())

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

    render_the_best_lap_per_pilot(sorted_pilots)
    render_the_best_time(sorted_pilots)
    render_average_speed_per_pilot(sorted_pilots)
    render_time_after_the_first(sorted_pilots)
