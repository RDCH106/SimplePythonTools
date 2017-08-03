import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")
from SimplePythonTools.network.ping_network import pingNetwork

pingNetwork()