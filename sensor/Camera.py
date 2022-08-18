import cv2

class Camera():
  def __init__(self, FPS):
    self.cap = cv2.VideoCapture(0)
    # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920*0.6)
    # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080*0.6)
    self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
    self.cap.set(cv2.CAP_PROP_FPS,FPS)

  def capture(self):
    ret, frame = self.cap.read()
    if ret:
      return frame
    else:
      self.close()
      return None

  def close(self):
    self.cap.release()
    cv2.destroyAllWindows()
    print('camera closed')

if __name__ == "__main__":
  FPS = 10
  camera = Camera(FPS)
