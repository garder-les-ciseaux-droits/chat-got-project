from flask import *
from flask_cors import CORS, cross_origin
import json, time
from llama_cpp import Llama
m_path = '/Users/evanvosh/Documents/chat-gpt-project/backend/model/llama-2-7b-chat.Q4_0.gguf'
llm = Llama(model_path=m_path)

with open("/Users/evanvosh/Documents/chat-gpt-project/backend/model/BabyFile.txt", "r") as f:
    memory = f.read()


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def home_page():
    data_set = {'Page': 'Home', 'Message': 'Loaded', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/user/', methods=['GET'])
@cross_origin()
def request_page():
    user_query = str(request.args.get('user'))

    output = llm(
            prompt = memory + '\n' + 'User: ' + user_query + '\n',   
            echo=False,
            stop = ['User:'],
            max_tokens=64)
    text = str(output['choices'][0]['text'])
    answer = text.partition("GPT: ")[2]

    data_set = {'Page': 'Request', 'Message': f'{answer}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=7770)
