
import sys
import os
sys.path.append(os.path.abspath(__file__))
from aip import AipImageClassify

'''
This script is to test baidu API
'''

# APP_ID ='17896377'
# API_KEY ='Fi71Yp0B0ivGB8SNj9BFdi0b'
# SECRET_KEY ='lwgXKw5suGRK3dYFnlSaRvVTWOoAIGES'

class animalAPI:
    def __init__(self,id,key,secret):
        self.id=id
        self.key=key
        self.secret=secret
    
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def query_api(self,filePath,options=None):
        image=self.get_file_content(filePath)
        client = AipImageClassify(self.id, self.key, self.secret)
        res=client.advancedGeneral(image)['result']
        res=sorted(res,key=lambda x:x['score'],reverse=True)
        if len(res)>=3:
            res=res[:3]
            for r in res:
                r['score']=float('%.2f' % (r['score']*100))
        print(res)
        return res

# path="D:/GitHub/animaltest/animaltest/static/uploads/188.jpg"
# animalAPI=animalAPI(APP_ID,API_KEY,SECRET_KEY)
# animalAPI.query_api(path)

# image = get_file_content('D:/GitHub/animaltest/animaltest/static/uploads/188.jpg')

# """ 调用通用物体识别 """
# client.advancedGeneral(image)

# """ 如果有可选参数 """
# options = {}
# options["baike_num"] = 3

# """ 带参数调用通用物体识别 """
# print(client.advancedGeneral(image))