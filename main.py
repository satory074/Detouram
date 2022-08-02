import csv
import networkx as nx
import matplotlib.pyplot as plt

CSVPATH = "./data/medley_data.csv"


def read_csv():
    with open(CSVPATH, "r") as f:
        reader = csv.reader(f, skipinitialspace=True)
        data = list(reader)

    slist = []
    elist = []
    for t, se, chord, scale in data:
        if se == "S":
            slist.append((t, se, chord, scale))
        elif se == "E":
            elist.append((t, se, chord, scale))

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
