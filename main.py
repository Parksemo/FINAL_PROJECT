'''
import import_ipynb

import UTDdata2
import 전처리2
import TomorrowPredict
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, jsonify
import sys
import random
import pickle
with open('pred_dic.pickle','rb') as f:
    pred_dic = pickle.load(f)
application = Flask(__name__)



@application.route("/random", methods=["POST"])
def random_function():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText" : {
                        "text": pred_dic['Food']
                    }
                }
            ]
        } 
    }
    return jsonify(response)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)


# In[ ]:
