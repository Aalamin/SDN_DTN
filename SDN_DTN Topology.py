#!/usr/bin/python
from mininet.node import RemoteController, OVSKernelSwitch, Host
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
import sys
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.wmediumdConnector import interference
from mn_wifi.cli import CLI_wifi
from mininet.link import TCLink
from subprocess import call

def topology(coord):

    "Create a network."
    net = Mininet_wifi(topo=None, build=False, link=wmediumd, accessPoint=OVSKernelAP, wmediumd_mode=interference,ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c1 = net.addController(name='c1',
                           controller=RemoteController,
                           ip='10.0.0.1',
                           protocol='tcp',
                           port= 6633)

    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='8', mode='n', ip='', position='790.0,330.0,0',range=150)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='7', mode='n', ip='', position='450.0,332.0,0',range=150)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='6', mode='n', ip='', position='60.0,209.0,0',range=150)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)


    print "*** Add hosts/stations"

    sta1 = net.addStation('sta1', ip='10.0.0.26/8')
    sta2 = net.addStation('sta2', ip='10.0.0.2/8')
    sta3 = net.addStation('sta3', ip='10.0.0.3/8')
    sta4 = net.addStation('sta4', ip='10.0.0.4/8')
    sta5 = net.addStation('sta5', ip='10.0.0.5/8')
    sta6 = net.addStation('sta6', ip='10.0.0.6/8')
    sta7 = net.addStation('sta7', ip='10.0.0.7/8')
    sta8 = net.addStation('sta8', ip='10.0.0.8/8')
    sta9 = net.addStation('sta9', ip='10.0.0.9/8')
    sta10 = net.addStation('sta10', ip='10.0.0.10/8')
    sta11 = net.addStation('sta11', ip='10.0.0.11/8')
    sta12 = net.addStation('sta12', ip='10.0.0.12/8')
    sta13 = net.addStation('sta13', ip='10.0.0.13/8')
    sta14 = net.addStation('sta14', ip='10.0.0.14/8')
    sta15= net.addStation('sta15', ip='10.0.0.15/8')
    sta16 = net.addStation('sta16', ip='10.0.0.16/8')
    sta17 = net.addStation('sta17', ip='10.0.0.17/8')
    sta18 = net.addStation('sta18', ip='10.0.0.18/8')
    sta19 = net.addStation('sta19', ip='10.0.0.19/8')
    sta20= net.addStation('sta20', ip='10.0.0.20/8')

    

    h5 = net.addHost('h5', cls=Host, ip='10.0.0.21/8')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.22/8')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.23/8')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.24/8')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.25/8')
  

 
    print "*** Configuring Propagation Model"
    net.setPropagationModel(model="logDistance", exp=3)

    print "*** Configuring wifi nodes"
    net.configureWifiNodes()

    net.plotGraph(max_x=1000, max_y=750)
    if coord:
        sta5.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta6.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta1.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta2.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta3.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta4.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta7.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta8.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta9.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta10.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta11.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta12.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta13.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta14.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta15.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta16.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']
        sta17.coord = ['40.0,30.0,0.0', '31.0,10.0,0.0', '31.0,30.0,0.0']
        sta18.coord = ['40.0,40.0,0.0', '55.0,31.0,0.0', '55.0,81.0,0.0']

    else:
        net.startMobility(time=0, repetitions=1)
        net.addLink(sta1, cls=adhoc, ssid='adhocNet', mode='g',range=100)
        net.addLink(sta2, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta3, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta4, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta5, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta6, cls=adhoc, ssid='adhocNet', mode='g',range=100)
 	net.addLink(sta7, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta8, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta9, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta10, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta11, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta12, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta13, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta14, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta15, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta16, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta17, cls=adhoc, ssid='adhocNet', mode='g',range=100)
    	net.addLink(sta18, cls=adhoc, ssid='adhocNet', mode='g',range=100)
 
    net.mobility(sta1, 'start', time=2, position='50.0,400.0,0.0')
    net.mobility(sta1, 'stop', time=25, position='250.0,50.0,0.0')

    net.mobility(sta2, 'start', time=2, position='10.0,400.0,0.0')
    net.mobility(sta2, 'stop', time=26, position='100.0,35.0,0.0')

    net.mobility(sta3, 'start', time=2, position='300.0,480.0,0.0')
    net.mobility(sta3, 'stop', time=28, position='390.0,60.0,0.0')

    net.mobility(sta4, 'start', time=2, position='240.0,600.0,0.0')
    net.mobility(sta4, 'stop', time=28, position='610.0,60.0,0.0')

    net.mobility(sta5, 'start', time=2, position='590.0,600.0,0.0')
    net.mobility(sta5, 'stop', time=26, position='120.0,150.0,0.0')

    net.mobility(sta6, 'start', time=2, position='500.0,580.0,0.0')
    net.mobility(sta6, 'stop', time=26, position='500.0,30.0,0.0')

    net.mobility(sta7, 'start', time=2, position='750.0,590.0,0.0')
    net.mobility(sta7, 'stop', time=29, position='790.0,70.0,0.0')

    net.mobility(sta8, 'start', time=2, position='890.0,600.0,0.0')
    net.mobility(sta8, 'stop', time=23, position='900.0,70.0,0.0')

    net.mobility(sta9, 'start', time=2, position='900.0,150.0,0.0')
    net.mobility(sta9, 'stop', time=27, position='500.0,480.0,0.0')

    net.mobility(sta10, 'start', time=2, position='800.0,90.0,0.0')
    net.mobility(sta10, 'stop', time=23, position='600.0,500.0,0.0')

    net.mobility(sta11, 'start', time=2, position='500.0,20.0,0.0')
    net.mobility(sta11, 'stop', time=28, position='900.0,450.0,0.0')

    net.mobility(sta12, 'start', time=2, position='400.0,150.0,0.0')
    net.mobility(sta12, 'stop', time=26, position='900.0,390.0,0.0')

    net.mobility(sta13, 'start', time=2, position='700.0,110.0,0.0')
    net.mobility(sta13, 'stop', time=26, position='280.0,350.0,0.0')

    net.mobility(sta14, 'start', time=2, position='900.0,50.0,0.0')
    net.mobility(sta14, 'stop', time=27, position='400.0,310.0,0.0')

    net.mobility(sta15, 'start', time=2, position='300.0,20.0,0.0')
    net.mobility(sta15, 'stop', time=23, position='480.0,320.0,0.0')

    net.mobility(sta16, 'start', time=2, position='240.0,20.0,0.0')
    net.mobility(sta16, 'stop', time=26, position='10.0,380.0,0.0')

    net.mobility(sta17, 'start', time=2, position='650.0,200.0,0.0')
    net.mobility(sta17, 'stop', time=28, position='80.0,400.0,0.0')

    net.mobility(sta18, 'start', time=2, position='300.0,20.0,0.0')
    net.mobility(sta18, 'stop', time=23, position='500.0,200.0,0.0')

    net.mobility(sta19, 'start', time=2, position='900.0,20.0,0.0')
    net.mobility(sta19, 'stop', time=28, position='480.0,230.0,0.0')

    net.mobility(sta20, 'start', time=2, position='400.0,50.0,0.0')
    net.mobility(sta20, 'stop', time=28, position='200.0,150.0,0.0')





    net.stopMobility(time=30)

    print "*** Associating and Creating links"
    net.addLink(ap1, s4)
    net.addLink(s4, s3)
    net.addLink(s4, ap2)
    net.addLink(s3, ap3)
    net.addLink(s3, s2)
    net.addLink(s2, s1)
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s1, h3)
    net.addLink(s1, h4)
    net.addLink(s1, h5)
    


    print "*** Starting switches/APs"
    net.get('ap3').start([c1])
    net.get('s2').start([c1])
    net.get('ap2').start([c1])
    net.get('s3').start([c1])
    net.get('s4').start([c1])
    net.get('ap1').start([c1])
    net.get('s1').start([c1])
    

    print "*** Starting network"
    net.build()
    c1.start()
    for controller in net.controllers:
        controller.start()

    """plotting graph"""

    "*** Available models: RandomWalk, TruncatedLevyWalk, RandomDirection, RandomWayPoint, GaussMarkov, ReferencePoint, TimeVariantCommunity ***"
    net.startMobility(time=0, model='RandomWayPoint', max_x=100, max_y=100, min_v=0.5, max_v=0.8)

    print "*** Running CLI"
    CLI_wifi(net)

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    coord = True if '-c' in sys.argv else False
    topology(coord)

