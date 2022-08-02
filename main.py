import csv
import networkx as nx
import matplotlib.pyplot as plt

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

    slist = []
    elist = []
    for t, se, chord, scale in data:
        if se == "S":
            slist.append((t, se, NOTE_TO_INDEX[chord], scale))
        elif se == "E":
            elist.append((t, se, NOTE_TO_INDEX[chord], scale))

    return slist, elist


def make_network(slist, elist):
    G = nx.DiGraph()

    for st, _, schord, sscale in slist:
        for et, _, echord, escale in elist:
            if st == et:
                continue

            if (schord, sscale) == (echord, escale):
                G.add_edge(et, st)

    return G


slist, elist = read_csv()
G = make_network(slist, elist)

nx.draw_networkx(G, with_labels=True, font_size=8)
plt.show()
