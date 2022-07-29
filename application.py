from flask import Flask, request, jsonify
import pickle
import sys
from datetime import date, timedelta,datetime
application = Flask(__name__)

rinuxtimenow = datetime.now() #리눅스 현재 시각
krtimenow = rinuxtimenow+timedelta(hours=9) # kr현재시각
tomorrow = rinuxtimenow+timedelta(days=1,hours=9) #kr 24시간 후
if(16 <= krtimenow.hour and krtimenow.hour<= 23):
    set_d = tomorrow.date()
elif (0 <= krtimenow.hour and krtimenow.hour< 16):
    set_d = krtimenow.date()
set_d = set_d.isoformat()
set_d = set_d.replace('-','')[2:]
set_d

@application.route("/")
def hello():
    return "Hello goorm!"
    
with open(f'{set_d}pred_dic.pickle','rb') as f:
    pred_dic = pickle.load(f)
    

@application.route("/pred_carousel", methods=["POST"])
def redflavor():
    

    # 답변 텍스트 설정
    response = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "basicCard",
          "items": [
            {
              "title": "음식료품, 섬유의복",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%9D%8C%EC%8B%9D%EB%A3%8C%ED%92%88,%EC%84%AC%EC%9C%A0%EC%9D%98%EB%B3%B5.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "음식료품",
                  "messageText": '음식료품'
                },
                {
                  "action":  "message",
                  "label": "섬유의복",
                  "messageText": '섬유의복'
                }
              ]
            },
            {
              "title": "화학, 의약품",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%ED%99%94%ED%95%99,%EC%9D%98%EC%95%BD%ED%92%88.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "화학",
                  "messageText": '화학'
                },
                {
                  "action":  "message",
                  "label": "의약품",
                  "messageText": '의약품'
                }
              ]
            },
              {
              "title": "비금속광물, 철강금속",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EB%B9%84%EA%B8%88%EC%86%8D%EA%B4%91%EB%AC%BC,%EC%B2%A0%EA%B0%95%EA%B8%88%EC%86%8D.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "비금속광물",
                  "messageText": '비금속광물'
                },
                {
                  "action":  "message",
                  "label": "철강금속",
                  "messageText": '철강금속'
                }
              ]
            },
              {
              "title": "기계, 전기전자",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EA%B8%B0%EA%B3%84,%EC%A0%84%EA%B8%B0%EC%A0%84%EC%9E%90.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "기계",
                  "messageText": '기계'
                },
                {
                  "action":  "message",
                  "label": "전기전자",
                  "messageText": '전기전자'
                }
              ]
            },
              {
              "title": "건설업, 운수창고",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EA%B1%B4%EC%84%A4%EC%97%85,%EC%9A%B4%EC%88%98%EC%B0%BD%EA%B3%A0.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "건설업",
                  "messageText": '건설업'
                },
                {
                  "action":  "message",
                  "label": "운수창고",
                  "messageText": '운수창고'
                }
              ]
            },
              {
              "title": "유통업, 전기가스업",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%9C%A0%ED%86%B5%EC%97%85,%EC%A0%84%EA%B8%B0%EA%B0%80%EC%8A%A4%EC%97%85.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "유통업",
                  "messageText": '유통업'
                },
                {
                  "action":  "message",
                  "label": "전기가스업",
                  "messageText": '전기가스업'
                }
              ]
            },
              {
              "title": "통신업, 금융업",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%ED%86%B5%EC%8B%A0%EC%97%85,%EA%B8%88%EC%9C%B5%EC%97%85.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "통신업",
                  "messageText": '통신업'
                },
                {
                  "action":  "message",
                  "label": "금융업",
                  "messageText":'금융업'
                }
              ]
            },
              {
              "title": "증권, 보험",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%A6%9D%EA%B6%8C,%EB%B3%B4%ED%97%98.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "증권",
                  "messageText": '증권'
                },
                {
                  "action":  "message",
                  "label": "보험",
                  "messageText": '보험'
                }
              ]
            },
              {
              "title": "서비스업, 제조업",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
              "thumbnail": {
                "imageUrl": "https://github.com/Parksemo/Parksemo/blob/master/image/%EC%84%9C%EB%B9%84%EC%8A%A4%EC%97%85,%EC%A0%9C%EC%A1%B0%EC%97%85.png?raw=true"
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "서비스업",
                  "messageText": '서비스업'
                },
                {
                  "action":  "message",
                  "label": "제조업",
                  "messageText": '제조업'
                }
              ]
            }
          ]
        }
      }
    ]
  }
}

    # 답변 전송
    return jsonify(response)


@application.route("/block", methods=["POST"])
def sector():
    
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['sector_entity']['value']   # json파일 읽기
    
    
    
    

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": set_d + pred_dic[answer]
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)