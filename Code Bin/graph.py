# this dictionary is the agent
import math
import random
import networkx as nx


vertex = {
    "vid": 0,  # vertex id will be rowise
    "vcon": [],  # the neiboring vertices
    "sinkpos": [],  # list of vertices marked as sink
    "source pos": [],  # list of vertices marked as source
    "qpackets": [],  # it is the queus that will be responsible for the transfer of packets
}


def gen_grid(grid_size):
    grid = []

    for i in range(grid_size):
        vertex = {
            "vid": i + 1,  # vertex id will be rowise
            "vcon": [],  # the neiboring vertices
            "sinkpos": 0,  # list of vertices marked as sink
            "source pos": 0,  # list of vertices marked as source
            "qpackets": [],  # it is the queus that will be responsible for the transfer of packets
        }
        grid.append(vertex)
    return grid


# grid_row = 0
# grid_column = 0
grid_size = 16  # int(input("Please enter a perfect square for the grid size : "))
grid_l = grid_size ** 0.5


def vconnected(vid):
    con = []
    mod = vid % grid_l
    if vid == 1:  # top left
        con = [2, grid_l + 1]
    if vid == grid_l:  # top right
        con = [grid_l - 1, grid_l * 2]
    if vid == grid_size - grid_l + 1:  # bottom left
        con = [(grid_l * (grid_l - 2) + 1), grid_size - grid_l + 2]
    if vid == grid_size:  # bottom right
        con = [grid_size - grid_l, grid_size - 1]
    if vid > 1 and vid < grid_l:  # top row excluding first and last node
        con = [vid - 1, vid + 1, vid + grid_l]
    if (
        vid > (grid_size - grid_l + 1) and vid < grid_size
    ):  # bottom row excluding first and last node
        con = [vid - grid_l, vid - 1, vid + 1]
    if vid > grid_l and vid < grid_l * (grid_l - 1) and mod == 1:  # first column
        con = [vid - grid_l, vid + 1, vid + grid_l]
    if vid > grid_l and vid < grid_l * (grid_l - 1) and mod >= 2 and mod <= grid_l - 1:
        con = [vid - grid_l, vid - 1, vid + 1, vid + grid_l]
    if vid > grid_l and vid <= grid_l * (grid_l - 1) and mod == 0:
        con = [vid - grid_l, vid - 1, vid + grid_l]
    return con


def genpacket(pid, source, sink):
    packet = {
        "pid": pid,  # packet id
        "so": source,  # the generation point of the packet
        "si": sink,  # the destination of the packet
        "curvex": source,  # the current position of the packet
    }
    return packet


def passing(packet, movex, movey, grid_l):  # movex and movey are values either 1 0 -1
    curr = packet["curvex"]
    curr += movex
    curr += movey * (grid_l)
    packet["curvex"] = curr
    return curr


def pos(vid, grid_l):
    x0 = (vid - 1) % grid_l
    y0 = (vid - 1) / (grid_l)
    return int(x0), int(y0)


def genetic_path(packet, grid_l):
    l = grid_l
    xo, yo = pos(packet["so"], l)
    xi, yi = pos(packet["si"], l)
    path1 = []
    path2 = []
    x1 = xi - xo
    y1 = yo - yi
    x2 = x1
    y2 = y1
    while x1 != 0 or y1 != 0:
        if x1 < 0:
            path1.append(packet["curvex"] - 1)
            packet["curvex"] = packet["curvex"] - 1
            x1 += 1
        if x1 > 0:
            path1.append(packet["curvex"] + 1)
            packet["curvex"] = packet["curvex"] + 1
            x1 -= 1
        if y1 < 0:
            path1.append(packet["curvex"] + grid_l)
            packet["curvex"] = packet["curvex"] + grid_l
            y1 += 1
        if y1 > 0:
            path1.append(packet["curvex"] - grid_l)
            packet["curvex"] = packet["curvex"] - grid_l
            y1 -= 1
    packet["curvex"] = packet["so"]
    while y2 != 0 or x2 != 0:
        if y2 < 0:
            path2.append(packet["curvex"] + grid_l)
            packet["curvex"] = packet["curvex"] + grid_l
            y2 += 1
        if y2 > 0:
            path2.append(packet["curvex"] - grid_l)
            packet["curvex"] = packet["curvex"] - grid_l
            y2 -= 1
        if x2 < 0:
            path2.append(packet["curvex"] - 1)
            packet["curvex"] = packet["curvex"] - 1
            x2 += 1
        if x2 > 0:
            path2.append(packet["curvex"] + 1)
            packet["curvex"] = packet["curvex"] + 1
            x2 -= 1

    return path1, path2
