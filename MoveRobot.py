import cv2

import rospy
import geometry_msgs.msg

import intera_interface
import numpy as np
from intera_interface import (
    Gripper,
    Head,
)
import uuid
import IK
class MoveRobot():
    def __init__(self):
        rospy.init_node('Tester' + str(uuid.uuid4().hex), anonymous=True)
       
    def Test(self,x,y,z,ox,oy,oz,ow):
        
        try:
       
            pose_target = geometry_msgs.msg.PoseStamped()    

            pose_target.pose.position.x = x
            pose_target.pose.position.y = y
            pose_target.pose.position.z = z

            pose_target.pose.orientation.x =  ox
            pose_target.pose.orientation.y =  oy
            pose_target.pose.orientation.z = oz

            pose_target.pose.orientation.w = ow

            self.headText(pose_target.pose.orientation)
            
            self.go(pose_target)
        except Exception, e:
            print str(e)
#        rospy.signal_shutdown('k')
       
    def go(self,pose_target):
    
        ik = IK.IK()
        success,joints = ik.ik_service_client(pose_target, rospy )
        print(pose_target)
        limb_joints = dict(zip(joints.joints[0].name, joints.joints[0].position))
        limb = intera_interface.Limb("right")
        limb.set_joint_position_speed(.3 )

        limb.move_to_joint_positions(limb_joints, timeout=20.0,threshold=intera_interface.settings.JOINT_ANGLE_TOLERANCE)

    def headText(self, q):
        t = 'x:{x} y:{y} z:{z} w:{w}'
        template = {'x':q.x,'y':q.y,'z':q.z,'w':q.w}
        text = t.format(**template)
        h = 600
        w = 1024
        img = np.zeros((h,w,3), np.uint8)
        img.fill(255)
        #cv2.putText(img,text, (50,200), cv2.FONT_HERSHEY_SIMPLEX, 6, 100,14)
        y0, dy = 150, 120
        for i, line in enumerate(text.split(' ')):
            y = y0 + i*dy
            cv2.putText(img, line, (50, y ), cv2.FONT_HERSHEY_SIMPLEX,  4, 2,10)


        cv2.imwrite("/home/microshak/Pictures/head.png",img)
        head_display = intera_interface.HeadDisplay()
        
        head_display.display_image("/home/microshak/Pictures/head.png", False, 1.0) 




