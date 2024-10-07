# 测试dlib是否安装成功
import dlib
import cv2
print(dlib.__version__)
print(dlib.DLIB_USE_CUDA)
print(dlib.cuda.get_num_devices())


# 加载三个模型文件
hog_face_detector = dlib.get_frontal_face_detector()  # HOG + SVM 模型
cnn_face_detector = dlib.cnn_face_detection_model_v1('./dlib_files/mmod_human_face_detector.dat')  # CNN 模型
predictor = dlib.shape_predictor('./dlib_files/shape_predictor_68_face_landmarks.dat')  # 68个特征点模型

# 1. 使用 HOG + SVM 检测人脸
def detect_face_hog(image, gray_image):
    faces_hog = hog_face_detector(gray_image)
    for face in faces_hog:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

# 2. 使用 CNN 模型检测人脸
def detect_face_cnn(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces_cnn = cnn_face_detector(rgb_image, 1)  # 第二个参数1 表示图像放大1倍
    for face in faces_cnn:
        x, y, w, h = face.rect.left(), face.rect.top(), face.rect.width(), face.rect.height()
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image

# 3. 使用 68 个特征点模型进行检测
def detect_face_landmarks(image, gray_image):
    faces = hog_face_detector(gray_image)
    #faces= cnn_face_detector(image, 1) 
    for face in faces:
        landmarks = predictor(gray_image, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
    return image

# 主函数入口
if __name__ == "__main__":
    # 加载图像
    image = cv2.imread('test.jpg')

    # 检查图像是否成功加载
    if image is None:
        print("Error: Unable to load image.")
        exit()

    # # 缩小图像大小（例如宽度为800像素，高度按比例缩放）
    # width = 600
    # aspect_ratio = width / float(image.shape[1])  # 计算宽高比例
    # height = int(image.shape[0] * aspect_ratio)   # 计算新的高度
    # resized_image = cv2.resize(image, (width, height))  # 调整图像尺寸

    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 读取图像并应用每个模型
    image_hog = detect_face_hog(image.copy(), gray)
    image_cnn = detect_face_cnn(image.copy())
    image_landmarks = detect_face_landmarks(image.copy(), gray)

    # 显示每个模型的结果
    cv2.imshow('HOG Detected Faces', image_hog)
    cv2.imshow('CNN Detected Faces', image_cnn)
    cv2.imshow('68 Landmarks Detected', image_landmarks)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
