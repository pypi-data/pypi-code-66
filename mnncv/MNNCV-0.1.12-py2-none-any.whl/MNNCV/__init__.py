#!/usr/bin/python
# -*- coding: UTF-8 -*-

import streamlit as st
from PIL import Image, ImageDraw
import os
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

class Kit():
    def __init__(self):
        self.selectedImage = None
        pass

    def open(self, openType):
        pass

    def setLabel(self, index, text, config=None):
        st.text(text)

    def getEnvVars(self):
        envs = os.environ
        if os.environ.get('workPath') == None:
            envs['workPath'] = './'
        return envs

    def setCamera(self, cameraCallback, defaultVideo=None):
        # data, format, imgw, imgh, inangle, outangle
        # 播放时，一帧一帧输入
        if defaultVideo:
            pass
        else:
            pass
        pass

    # <type 'numpy.ndarray'>
    def drawImage(self, data):

        # ndata = np.array(data)
        # print type(ndata)

        img = Image.fromarray(np.uint8(data))
        st.image(img, caption='', use_column_width=True)


    def selectPhoto(self, photoCallback, defaultImg=None):
        if defaultImg:
            # 同步执行
            self.selectedImage = defaultImg
            if photoCallback:
                imageData, format, width, height = self._processSelectPhoto(defaultImg)
                photoCallback(imageData, format, width, height)
        else:
            # 异步回调
            uploaded_file = st.file_uploader("Select a photo", type=['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'])
            if uploaded_file is not None:
                self.selectedImage = uploaded_file
                if photoCallback:
                    imageData, format, width, height = self._processSelectPhoto(uploaded_file)
                    photoCallback(imageData, format, width, height)
            else:
                print("do not choose photo")

    def drawPoints(self, points, color='red', width=4):
        if self.selectedImage == None:
            raise Exception("select image first")
        image = Image.open(self.selectedImage)
        idraw = ImageDraw.Draw(image)

        if width <= 1:
            idraw.point(points, fill=color)
        else:
            for x in range(0, len(points)):
                point = points[x]
                idraw.rectangle(
                    [
                        (point[0] - width/2, point[1] - width/2),
                        (point[0] + width/2, point[1] + width/2)
                     ],
                fill=color)
        st.image(image)

    def drawRects(self, coordList, texts, lineColor='red', lineWidth=2):
        if coordList is None or texts is None:
            raise Exception("drawRects input error, coordList or texts is None")
        if len(coordList) != len(texts):
            raise Exception("drawRects input error, coordList length is " + str(len(coordList)) + " but texts length is " + str(len(texts)))

        if self.selectedImage == None:
            raise Exception("select image first")

        image = Image.open(self.selectedImage)
        idraw = ImageDraw.Draw(image)

        if lineColor == None:
            lineColor = 'red'

        if lineWidth == None:
            lineWidth = 2

        for x in range(0, len(coordList)):
            coord = coordList[x]
            text = texts[x]

            x = coord[0]
            y = coord[1]
            w = coord[2]
            h = coord[3]

            idraw.polygon([
                (x, y),
                (x+w, y),
                (x + w, y + h),
                (x, y+h)
            ], outline=lineColor)

            idraw.text((coord[0]+2, coord[1]+2), text, fill=lineColor)
        st.image(image)

    def _processSelectVideo(self, videoPath):
        videoFile = open(videoPath, 'rb')
        videoBytes = videoFile.read()
        st.video(videoBytes)

    def _processSelectPhoto(self, imagePath):
        image = Image.open(imagePath)
        st.image(image, caption='', use_column_width=True)
        width, height = image.size
        format = self._toMNNImageFormat(image)
        imageData = self._toMNNData(image)
        return imageData, format, width, height

    def _toMNNData(self, image):
        return np.array(image)

    def _toMNNImageFormat(self, image):
        format = image.mode
        if format == 'RGBA':
            return 0
        elif format == 'RGB':
            return 1
        elif format == 'GRAY':
            return 3
        return 0

    def setCloseCallback(self, closeCallback):
        pass