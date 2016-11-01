import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")
from ping_network import pingNetwork

pingNetwork()