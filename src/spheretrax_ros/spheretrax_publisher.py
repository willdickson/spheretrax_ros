import roslib
roslib.load_manifest('spheretrax_ros')
import rospy

from spheretrax_ros.msg import SphereTraxData

class SphereTrax_Publisher(object):

    def __init__(self):

        self.pub = rospy.Publisher('/spheretrax/data',SphereTraxData)
        self.spheretrax_data = SphereTraxData()

    def publish_data(self,data):
        self.spheretrax_data.framenumber = data['framenumber']
        self.spheretrax_data.timestamp = data['timestamp']
        self.spheretrax_data.omega_x = data['omega_x']
        self.spheretrax_data.omega_y = data['omega_y']
        self.spheretrax_data.omega_z = data['omega_z']
        self.spheretrax_data.head_rate = data['head_rate']
        self.spheretrax_data.forw_rate = data['forw_rate']
        self.spheretrax_data.side_rate = data['side_rate']
        self.pub.publish(self.spheretrax_data)

    def run(self):
        self.spin()

        
