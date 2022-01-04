import requests

class ApiReportsClient:
  apiLang = 'en'
  jsonApiUrl = 'https://json.apireports.com/v1/'
  pdfApiUrl = 'https://pdf.apireports.com/v1/'

  def __init__(self, uid, key):
    self.userId = uid
    self.apiKey = key

  def setLanguage(self, lang):
    self.apiLang = lang

  def callJsonApi(self,apiEndPoint,data):
    url = self.jsonApiUrl + apiEndPoint
    headers = {
      'Accept-Language': self.apiLang
    }
    resp = requests.request("POST", url, headers=headers, auth=(self.userId, self.apiKey),data=data)
    return resp
  
  def callPdfApi(self,apiEndPoint,data):
    url = self.pdfApiUrl + apiEndPoint
    headers = { 'Accept-Language': self.apiLang }
    resp = requests.request("POST", url, headers=headers, auth=(self.userId, self.apiKey),data=data)
    return resp