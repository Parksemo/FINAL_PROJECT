from flask import Flask, request, jsonify

application = Flask(__name__)
import pickle
#업종별 방향 예상 텍스트를 담고있는 딕셔너리
with open('pred_dic.pickle','rb') as f:
    pred_dic = pickle.load(f)

sector_name_list = ['음식료품', '섬유의복', '화학','의약품','비금속광물','철강금속','기계','전기전자','건설업','운수창고','유통업','전기가스업','통신업', '금융업','증권','보험', '서비스업','제조업']

sector_name_mapping = []
count = 0
for sector_name in pred_dic.keys():
    sector_name_mapping.append(zip(sector_name,sector_name_list[count]))
    count+=1





@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/predskill",methods=['POST'])
def sector():
    req = request.get_json()
    
    answer = req["action"]["detailParams"]["sector_entity"]["value"]	# json파일 읽기
    
    for name_zip in sector_name_mapping:
        if answer==name_zip[1]:
            text = pred_dic[name_zip[0]]
    
    
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)