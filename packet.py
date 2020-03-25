import sys
import time
import json
import math
import queue
import socket
import datetime
import threading

class packet(object):

  def send(sequence_number):              # send function that runs in a separate thread, receives a global sequence number, the first time a router runs
    while True:
      sequence_number = sequence_number.split(" ")[0] + " " + str((int(sequence_number.split(" ")[1]) + 1))      # incrementing sequence number
      packet_contents = []                                                                                       # packet to be sent

      alive_routers = []                                               # a list to check for alive routers
      while routers_queue.empty() != True:                             # while the queue that contains alive routers is not empty
        alive_routers.append(routers_queue.get())                # get router names and append it to alive routers

      for router, state in routers_state.items():                      # run a for loop on router_state list
        if router in alive_routers:                              # if a router in the list is also in the alive router list
          lock.acquire()
          routers_state[router] = 1                        # initialize that router as 1 (it is alive)
          lock.release()
          lock.acquire()
          router_packets[router] = 3                       # and initialize router_packets to 3 as it is not dead
          lock.release()
        else:                                                    # if a router is not alive router list
          lock.acquire()
          router_packets[router] = router_packets[router] - 1      # decrement its counter making it closer to be delared as dead
          lock.release()

      lock.acquire()
      routers_state[router_id] = 1                                     # a router declaring itself as alive
      lock.release()
      lock.acquire()
      router_packets[router_id] = 3                                    # and initializing its own router_packets id to 3
      lock.release()

      for router, packets in router_packets.items():          # run a loop on router_packets list to check which has the value less than or equal to 0
        if packets <= 0:                                         # if a router's value is less than or equal to 0, it means that it is dead
          lock.acquire()
          routers_state[router] = 0                        # initialize the router_state to 0 (dead) 
          lock.release()
          received_packets.pop(router, None)      # and pop that router from the received packets list so we reset the sequence numbers of that router

      packet_contents.append(router_id)
      packet_contents.append(port)
      packet_contents.append(sequence_number)
      packet_contents.append(number_of_neighbors)
      packet_contents.append(neighbors)                                # making the packet
      packet_contents.append(routers_state)
      packet_contents.append(weights)
      packet_contents.append(port_numbers)
      packet = json.dumps(packet_contents)
      for neighbor_port in port_numbers:                               # iterating over all the neighbors and sending the packet to them
        clientSocket.sendto(packet.encode(), ("localhost", neighbor_port))
      time.sleep(1)                                                    # sleep for 1 second

   def receive():                          # receive function used to receive packets from all neighboring routers
    while True:
      encoded_packet, clientAddress = serverSocket.recvfrom(2048)                   # receive a packet from a neighbor
      packet = encoded_packet.decode()                                              # decode it
      packet_contents = json.loads(packet)                                          # convert it to a list from a stream

      node = packet_contents[0]                                                     # save the senders name in a variable
      sequence_number = packet_contents[2]                                          # save the sequence number in a variable
      neighbor_nodes = packet_contents[4]                                           # save the neighbors in a new list
      neighbor_ports = packet_contents[7]                                           # save the neighbor ports in a new list
      distances = packet_contents[6]                                                # save the distances of the neighbors in a new list

      routers_state.update({node : 1})                                              # update the sender's state as 1 (alive)
      router_packets.update({node : 3})                                             # update it's counter to 3

      routers_queue.put(node)                                                       # put the senders name in the queue so it can be declared as alive

      if node not in received_packets:                                              # if the router has sent the packet first time
        received_packets.setdefault(node, [])                                 # create its place in the received packets list
        received_packets[node].append(sequence_number)                        # and append its sequence number in it

      if sequence_number not in received_packets[node]:                             # if the packet received is a new sequence number
        received_packets[node].append(sequence_number)                        # append this sequence number to received packets list
        #print(packet_contents)
        lock.acquire()
        graph.add_node(node)                                                  # add the arrived router in the graph
        lock.release()
        for index, neighbor_node in enumerate(neighbor_nodes):                # iterate over neighbor names of the sender
          if neighbor_node not in routers_state or routers_state[neighbor_node] != 0:      # if a neighbor is not dead or it is not in the router_state list altogether
            lock.acquire()
            graph.add_edge(node, neighbor_node, distances[index])                    # make an edge from the sender and its neighbors with their distances
            # print("node: ", node, ", neighbor_node: ", neighbor_node, ", distance: ", distances[index])
            lock.release()
        # print()

        # print("Received:")
        # print(packet_contents)
        # print()

        for neighbor_port in port_numbers:                                     # iterate over the neighboring router's port numbers
          if neighbor_port != packet_contents[1] and neighbor_port not in neighbor_ports:     # don't send the packet to the one it received from
            clientSocket.sendto(packet.encode(), ("localhost", neighbor_port))          # else send the packet to all other neighbors
            # time.sleep(1)
