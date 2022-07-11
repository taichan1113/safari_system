import requests
import time

class ThetaV():
  def __init__(self):
    self.protocol = 'http://'
    self.IP = '192.168.1.1'
    self.address = self.protocol + self.IP

  def info(self):
    url = self.address + '/osc/info'
    r = requests.get(url)
    return r

  def state(self):
    url = self.address + '/osc/state'
    r = requests.post(url)
    return r

  def execute(self, command_name, parameters=None):
    payload = {'name':command_name, 'parameters':parameters}
    url = self.address + '/osc/commands/execute'
    r = requests.post(url, data=payload)
    return r

def zip_test(zip=None):
  payload = {'zipcode':zip}
  url = 'https://zipcloud.ibsnet.co.jp/api/search'
  r = requests.get(url, payload)
  print(r.text)

def prm_test(prm, a=None):
  dic = {'parameter':prm, 'arg':a}
  return dic

if __name__ == '__main__':
  # zip_test(6340004)
  # prm_test('test')
  camera = ThetaV()
  r = camera.info()
  print(r)
  # camera.execute('camera.tekePicture')
  # time.sleep(1)
  # res = camera.state()
  # print(res.json()['_latestFileUrl'])
  # data = camera.execute('camera.getLivePreview')
  

