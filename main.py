import csv

import matplotlib.pyplot as plt
import networkx as nx

CSVPATH = "./data/medley_data.csv"
NOTE_TO_INDEX = {
    "C": 0,
    "Cs": 1,
    "Db": 1,
    "D": 2,
    "Ds": 3,
    "Eb": 3,
    "E": 4,
    "F": 5,
    "Fs": 6,
    "Gb": 6,
    "G": 7,
    "Gs": 8,
    "Ab": 8,
    "A": 9,
    "As": 10,
    "Bb": 10,
    "B": 11,
}


def read_csv():
    with open(CSVPATH, "r") as f:
        reader = csv.reader(f, skipinitialspace=True)
        data = list(reader)

    songdict = {}
    for t, se, key, scale in data:
        if t not in songdict:
            songdict[t] = {"S": {}, "E": {}}

        songdict[t][se] = {
            f"{key}{scale}": {
                "key": key,
                "scale": scale,
                "note_index": NOTE_TO_INDEX[key],
            }
        }

    scaledict = {"S": {}, "E": {}}
    for t, se, key, scale in data:
        if f"{key}{scale}" in scaledict[se]:
            scaledict[se][f"{key}{scale}"].append(t)
        else:
            scaledict[se][f"{key}{scale}"] = [t]

    return songdict, scaledict


def make_network(songdict, scaledict):
    G = nx.DiGraph()

    for start_chordname in scaledict["S"].keys():
        for end_chordname in scaledict["E"].keys():
            if start_chordname != end_chordname:
                continue

            for start_title in scaledict["S"][start_chordname]:
                for end_title in scaledict["E"][end_chordname]:
                    if start_title == end_title:
                        continue

                    for end_start_chordname in songdict[end_title]["S"].keys():
                        G.add_edge(end_start_chordname, start_chordname)

    return G


songdict, scaledict = read_csv()
G = make_network(songdict, scaledict)

# Draw the graph
pos = nx.circular_layout(G)
nx.draw(G, with_labels=True, font_size=8, node_size=30, pos=pos)
# nx.draw_kamada_kawai(G, with_labels=True, font_size=8, node_size=30)

plt.show()
