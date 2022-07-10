from pykiwoom.kiwoom import *

import time
import pandas as pd

# login
kiwoom = Kiwoom() #allocation
print('login..')
kiwoom.CommConnect(block=True) # waiting to login
print('login..complete')

#connect
state = kiwoom.GetConnectState()
if state ==0:
    print('not connected')
elif state ==1:
    print('status : connected')

#login- information
account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명

print(account_num)
#print(accounts)
#print(user_id)
#print(user_name)

# TR요청(연속조회)
dfs = []
df = kiwoom.block_request('opt10081',
                          종목코드='005930',
                          기준일자='20200424',
                          수정주가구분='1',
                          output='주식일봉차트조회',
                          next=0
                          )
print(df.head())
dfs.append(df)







