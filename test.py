# import os

# from ultralytics import YOLO
# import cv2


# VIDEOS_DIR = '/content/drive/MyDrive/Colab Notebooks'

# video_path = os.path.join(VIDEOS_DIR, 'fire.mp4')
# video_path_out = '{}_out.mp4'.format(video_path)

# cap = cv2.VideoCapture(video_path)
# ret, frame = cap.read()
# H, W, _ = frame.shape
# out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# model_path = os.path.join('/content/drive/MyDrive/Colab Notebooks', 'runs', 'detect', 'train', 'weights', 'last.pt')

# # Load a model
# model = YOLO(model_path)  # load a custom model

# threshold = 0.1

# while ret:

#     results = model(frame)[0]

#     for result in results.boxes.data.tolist():
#         x1, y1, x2, y2, score, class_id = result

#         if score > threshold:
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
#             cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

#     out.write(frame)
#     ret, frame = cap.read()

# cap.release()
# out.release()
# cv2.destroyAllWindows()



# from ultralytics import YOLO

# # Load a pretrained YOLOv8n model
# model = YOLO('C:/Users/arn18/Documents/GitHub/40.-MIT--Fire-Flame-and-Smoke-Detection/runs/detect/train3/weights/best.pt')

# # Define path to the image file
# source = 'C:/Users/arn18/Documents/GitHub/40.-MIT--Fire-Flame-and-Smoke-Detection/test_image/test1.png'

# # Run inference on the source
# results = model(source)  # list of Results objects
# for r in results:
#     print(r.boxes)


from PIL import Image
from ultralytics import YOLO

model = YOLO('C:/Users/arn18/Documents/GitHub/40.-MIT--Fire-Flame-and-Smoke-Detection/runs/detect/train3/weights/best.pt')
results = model('C:/Users/arn18/Documents/GitHub/40.-MIT--Fire-Flame-and-Smoke-Detection/test_image/test1.png')[0]  # results list
# for r in results:
#     im_array = r.plot()  # plot a BGR numpy array of predictions
#     im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
#     im.show()  # show image
#     im.save('results.jpg')  # save image

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result
    print(score)
