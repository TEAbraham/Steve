import chess
from networks.version2 import Network

net = Network()
print("Training...")
net.train(steps=10)
print("Exporting...")
net.export()