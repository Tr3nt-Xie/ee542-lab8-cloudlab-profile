"""EE 542 Lab 8 Part 7: two bare-metal d7525 nodes (A30 GPU + ConnectX-6) on one LAN.

node0 = 10.10.1.1, node1 = 10.10.1.2 (netmask 255.255.255.0), Ubuntu 24.04.
Each node mounts a local blockstore at /mydata for Docker's data-root (the DOCA image
is about 22 GB and the root disk is 64 GB).
"""
import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
request = pc.makeRequestRSpec()

lan = request.LAN("lan")
for i in range(2):
    node = request.RawPC("node%d" % i)
    node.hardware_type = "d7525"
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"
    iface = node.addInterface("if%d" % i)
    iface.addAddress(pg.IPv4Address("10.10.1.%d" % (i + 1), "255.255.255.0"))
    lan.addInterface(iface)
    bs = node.Blockstore("bs%d" % i, "/mydata")
    bs.size = "200GB"

pc.printRequestRSpec(request)
