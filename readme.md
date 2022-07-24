[toc]

# Final_Project

## 1. 코드 파일

DataCollection2 : 업종별 시가총액 Top5의 항목들의 현재부터 과거까지 최대 3000개의 항목별 주가를 수집한다. 원하는 피쳐를 선택해서 추출한다.
데이터프레임 피쳐) 일자, 거래량, 시가, 고가, 저가, 종가
출력) df_sector.pickle, sector.pickle

Modeling2(Main) : 업종별 각 모델 마다 Datacolletion2에서 모은 업종별 3000개의 일별 데이터를 학습을 시켜서 모델을 만든다.
출력) Models, filename_dic, history_dic 
Model : Conv1D + LSTM + 은닉층 + 출력층



---

UTDdata2 : 웹크롤링으로 현재의 데이터를 업데이트 한다.(이전data+최신data 병합)
출력) df_sector_UTD.pickle

전처리2 : 
1. 업종별로 존재하는 Top5의 항목들을 일자별로 평균을 내서 업종별 일자의 대표값으로 지정한다.
2. 각 칼럼의 데이터 타입을 정수형으로 변환
3. MInMaxScaler로 칼럼 별 정규화


TomorrowPredict : 내일 업종별 주가를 예측한다.
출력) pred_dic.pickle

## 2. 파일명

1. df_sector : 이중 딕셔너리 /  {업종명 : {항목코드: 항목 3000개의 데이터 프레임}} 
2. sector : 딕셔너리 / {업종명 : [항목코드]} 
3. df_sector_UTD : 딕셔너리 / {업종명 : {항목코드: 항목 3000개+α의 데이터 프레임}}  : 기존 3000개에서 오늘날(최신)까지 각 항목별 데이터가 추가
4. df_scaled_UTD : 딕셔너리  / {업종명 :  항목 3000개+α의 데이터 프레임}}  : df_sector_UTD의 업종별 각 항목의 데이터프레임을 일자별로 평균을 낸다음 업종별 하나의 데어터프레임으로 변경. 정규화 적용, 데이터 타입 변환
5. filename_dic : 각 모델의 체크포인트의 이름을 저장하고있는 딕셔너리
6. Models : 모델의 체크포인트 파일이 저장 디렉터리
7. history_dic : 각 업종별로 학습과정의 loss와 val_loss를 히스토그램으로 저장되어있다.
8. pred_dict : 각 업종별로 내일의 주식의 상향/하향을 예측한 문자열을 가진다.
