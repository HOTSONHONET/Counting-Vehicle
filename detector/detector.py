import cv2
import numpy as np
import os


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_bbox(image):
    classes = None

    with open(os.path.join(LOCATION, 'labels.txt'), 'r') as classes_file:
        classes = [line.strip() for line in classes_file.readlines()]
    classes_file.close()
    req_classes = ['bicycle', 'car', 'motorcycle', 'bus', 'truck']

    #Using dnn module from openCV to use the pretrained weights
    nnet = cv2.dnn.readNet(
        os.path.join(LOCATION, 'yolov3.weights'), os.path.join(LOCATION, 'yolov3.cfg')
    )


    #Creating a image Blob
    scale = 0.00392
    img_blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)

    # Detecing objects
    nnet.setInput(img_blob)
    layer_names = nnet.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in nnet.getUnconnectedOutLayers()]
    outputs = nnet.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and classes[class_id] in req_classes:
                width = image.shape[1]
                height = image.shape[0]
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    # Removing Overlapping BBoxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    bboxes = []
    for i in indices:
        i = i[0]
        bboxes.append(boxes[i])

    return bboxes

