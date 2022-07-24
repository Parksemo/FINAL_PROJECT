import schedule
import time
import import_ipynb


#스케쥴 모듈이 동작시킬 코드 : 현재 시간 출력
def test_function():
    print("최신 데이터 받고 내일 업종별 주가 방향 예측 ")
    import UTDdata2
    import 전처리2
    import TomorrowPredict
    
    
#매일 특정시간에 동작
#07:00+ 9시간 = 16시
schedule.every().day.at('07:00').do(test_function)


#무한 루프를 돌면서 스케쥴을 유지한다.
while True:
    schedule.run_pending()
    time.sleep(1)


