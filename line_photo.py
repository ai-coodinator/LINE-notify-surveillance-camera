import requests,os

print(os.getcwd())

os.chdir("./photo") #画像保存先に移動
line_notify_token = '発行したトークン'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = 'テスト通知'


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}
files = {'imageFile': open("LESSON04.png", "rb")} #バイナリファイルを開く

line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)
