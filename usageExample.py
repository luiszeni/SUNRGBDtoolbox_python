import cv2
import SUNRGBD

frameData = SUNRGBD.readFrame( "/home/zeni/Pictures/SUNRGBD/kv2/kinect2data/000003_2014-05-26_14-24-42_260595134347_rgbf000040-resize", True );

cv2.imshow("RGB Image",frameData.imgRGB);
cv2.imshow("Detph Image",frameData.imgD);

cv2.waitKey(0);
	


