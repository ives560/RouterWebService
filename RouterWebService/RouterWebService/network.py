from __future__ import print_function
import subprocess
import platform
import re
import psutil#https://github.com/giampaolo/psutil
import socket
import uptime#https://github.com/Cairnarvon/uptime
from time import sleep
#https://github.com/awkman/pywifi
#import netifaces #https://bitbucket.org/al45tair/netifaces/src/f0e60c1c20c90b97cffaf151fd27f32354d23bca/test.py?at=default&fileviewer=file-view-default
rpivirsion_map = {
    '0002' : 'Model B Revision 1.0',
    '0003' : 'Model B Revision 1.0 + ECN0001',
    '0004' : 'Model B Revision 2.0 (256 MB)',
    '0005' : 'Model B Revision 2.0 (256 MB)',
    '0006' : 'Model B Revision 2.0 (256 MB)',
    '0007' : 'Model A',
    '0008' : 'Model A',
    '0009' : 'Model A',
    '000d' : 'Model B Revision 2.0 (512 MB)',
    '000e' : 'Model B Revision 2.0 (512 MB)',
    '000f' : 'Model B Revision 2.0 (512 MB)',
    '0010' : 'Model B+',
    '0013' : 'Model B+',
    '0011' : 'Compute Module',
    '0012' : 'Model A+',
    'a01041' : 'a01041',
    'a21041' : 'a21041',
    '900092' : 'PiZero 1.2',
    '900093' : 'PiZero 1.3',
    '9000c1' : 'PiZero W',
    'a02082' : 'Pi 3 Model B',
    'a22082' : 'Pi 3 Model B'
    }


af_map = {
    socket.AF_INET: 'IPv4',
    socket.AF_INET6: 'IPv6',
    psutil.AF_LINK: 'MAC',
}

duplex_map = {
    psutil.NIC_DUPLEX_FULL: "full",
    psutil.NIC_DUPLEX_HALF: "half",
    psutil.NIC_DUPLEX_UNKNOWN: "?",
}


def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9.8 K'
    >>> bytes2human(100001221)
    '95.4 M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f%s' % (value, s)
    return '%.2fB' % (n)

class network(object):

    def __init__(self):
        pass

    def GetInterfaces(self):
        io_counters = psutil.net_io_counters(pernic=True)
        interfaces ={}
        for nic, addrs in psutil.net_if_addrs().items():
            interface={}
            if nic in io_counters:
                io = io_counters[nic]
                incoming={}
                incoming["bytes"]=bytes2human(io.bytes_recv)
                incoming["pkts"]=io.packets_recv
                incoming["errs"]=io.errin
                incoming["errs"]=io.dropin
                interface["Rx"]=incoming
                outgoing={}
                outgoing["bytes"]=bytes2human(io.bytes_sent)
                outgoing["pkts"]=io.packets_sent
                outgoing["errs"]=io.errout
                outgoing["errs"]=io.dropout
                interface["Tx"]=outgoing    
            for addr in addrs:
                interface[af_map.get(addr.family, addr.family)]=addr.address
                if addr.netmask:
                    interface["Mask"]=addr.netmask
            interfaces[nic]=interface;
            return interfaces

    

    def getProcess(self,pName):
        process_lst = []
        all_pids  = psutil.pids()
        for pid in all_pids:
            p = psutil.Process(pid)
            if (p.name() == pName):
                process_lst.append(p)
        return process_lst

    def GetRPiVersion(self):
        return rpivirsion_map

    def GetUpTime(self):
        return uptime()


    def GetCPULoad(self):
        process_lst = self.getProcess("Python")
        for p in process_lst:
            print(p)

        sleep(2)

        for p in process_lst:
            print (p) 

    def GetMemUsed(self):
        process_lst = self.getProcess("Python")
        for p in process_lst:
            print(p)
