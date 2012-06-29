#!/usr/bin/env python
from __future__ import print_function
import roslib
roslib.load_manifest('spheretrax_ros')
import rospy

from spheretrax_ros.spheretrax_publisher import SphereTrax_Publisher

rospy.init_node('spheretrax_publisher_test')
pub = SphereTrax_Publisher()

cnt = 0
data = {}
while not rospy.is_shutdown():
    print(cnt)
    data['framenumber'] = cnt
    data['timestamp'] = float(cnt)
    data['omega_x'] = cnt
    data['omega_y'] = cnt+1 
    data['omega_z'] = cnt+2
    data['forw_rate'] = 2*cnt
    data['head_rate'] = 4*cnt
    data['side_rate'] = 6*cnt
    pub.publish_data(data)
    cnt+=1
    rospy.sleep(0.1)



