from llama_cpp import Llama

m_path = '/Users/evanvosh/Downloads/model-q4_K.gguf'
llm = Llama(model_path=m_path)


while True: 
    print('ask')
    user_query = input()

    with open("/Users/evanvosh/Documents/chat-gpt-project/backend/model/BabyFile.txt", "r") as f:
        memory = f.read()
    output = llm(
                prompt =  memory + '\n' + 'User: ' + user_query + '\n',   
                echo=False,
                stop = ['User:'],
                max_tokens=64)

    text = str(output['choices'][0]['text'])

    print(text)