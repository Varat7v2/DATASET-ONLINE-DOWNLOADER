import glob
import os, sys
import cv2
import numpy as np

from PIL import Image
from tqdm import tqdm

from myFROZEN_GRAPH_FACE import FROZEN_GRAPH_FACE
from myFROZEN_GRAPH_HEAD import FROZEN_GRAPH_HEAD

src_path = 'data/training'
dst_path = 'data/only_head'

PATH_TO_CKPT_FACE = 'models/FACE_DETECTION_512x512_ssd_mobilenetv2.pb'
PATH_TO_CKPT_HEAD = 'models/HEAD_DETECTION_300x300_ssd_mobilenetv2.pb'
face_detector = FROZEN_GRAPH_FACE(PATH_TO_CKPT_FACE)
head_detector = FROZEN_GRAPH_FACE(PATH_TO_CKPT_HEAD)

for mydir in os.listdir(src_path):
	for subdir in os.listdir(os.path.join(src_path, mydir)):
		for img in tqdm(glob.glob(os.path.join(src_path,mydir,subdir)+'/*')):
			filename = img.split('/')[-1]
			frame = cv2.imread(img)
			im_height, im_width, im_channel = frame.shape

			full_dst_path = os.path.join(dst_path, mydir, subdir)

			if not os.path.exists(full_dst_path):
			    os.makedirs(full_dst_path)

			# # RUNNING FACE DETECTION
			# image, faces = face_detector.run(frame, im_width, im_height)
			# for face in faces:
			# 	cv2.imwrite(full_dst_path+'/{}'.format(filename), face['cropped'])

			# RUNNING HEAD DETECTION
			image, heads = head_detector.run(frame, im_width, im_height)
			for head in heads:
				cv2.imwrite(full_dst_path+'/{}'.format(filename), head['cropped'])