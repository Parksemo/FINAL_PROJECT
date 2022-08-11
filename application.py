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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Clothing-Food.png?raw=true"
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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Medicine-Chemical.png?raw=true"
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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Metal-NonMetal.png?raw=true"
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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Electronic-Machine.png?raw=true"
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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Transport-Construction.png?raw=true"
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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Power-Distribution.png?raw=true"
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
                "imageUrl": 'https://github.com/97danielj/stock_api/blob/master/CarouselImages/Finance-Tele.png?raw=true'
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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Insure-Brokerage.png?raw=true"
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
                "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Manufacturer-Service.png?raw=true"
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
                        "text": set_d + '일자 ' + pred_dic[answer]
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)