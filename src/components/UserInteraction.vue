<template>
        <div class="flex h-screen place-items-center justify-center" style="width: 100%;">
            <div v-if="shownChatName === 'Welcome' || (dataHistory.data.find(c => c.chatName === shownChatName).messages.length === 0)" class="flex justify-center place-items-center h-screen w-full h-[630px] pt-10 pb-10 flex-col">
                <div class="mb-1 bg-white border-1 rounded-[50%] w-12 h-12 flex justify-center items-center">
                    <img class="w-8 h-8" src="https://freelogopng.com/images/all_img/1681038325chatgpt-logo-transparent.png">
                </div>
                <div>
                    <p id="topText" class="text-white">How can I help you today?</p>
                </div>
            </div>
            <div v-else class="flex relative place-items-center w-full h-[600px] pt-5 pb-5 flex-col overflow-y-auto mb-[20px]">
                <div class="w-[800px] mb-5 text-white"  v-for="mess in ourArray(shownChatName).messages" :key="mess.id">
                    <img class="avatar-small" :src="userById(mess.userId).avatar">
                            <div class="text-container ml-2">
                                <p class="user-name">
                                {{ userById(mess.userId).userName }}
                                </p>
                            <div v-html="replaceCodeWithHTML(mess.textMessage)"></div>
                    </div>
                </div>
            </div>
            <div class="absolute flex justify-center bottom-0">
                    <div class="flex justify-center w-[850px] h-[55px] text-white border border-gray-500 rounded-2xl mb-10">
                        <input id="mainInput" type="text" placeHolder="Message your GPT" v-model="userMessage" @keyup.enter="send(shownChatName)">
                        <button :class="lightTheButton" id="myButtonS" type="button" @click="send(shownChatName)">
                            <img class="icon" :src="'https://uxwing.com/wp-content/themes/uxwing/download/arrow-direction/up-arrow-icon.png'">
                        </button>
                    </div>
                </div>
                <div class="flex fixed bottom-0 mb-2.5 text-xs text-gray-300">
                    <span>ChatGPT can make mistakes. Consider checking important information.</span>
            </div>
        </div>

</template>

<script>
import axios from "axios"
import json from '/src/assets/dataHistory.json'
export default {
    props: {
        shownChatName: String,
    },
    data() {
        return {
            userMessage: '',
            dataHistory: json,
            text: "Hello, this is your script: ```print(123)```. Do you like it?"
        }
    },
    methods: {
        userById(userId) {
          return this.dataHistory.users.find(u => u.id === userId );
        },
       
        send(currentChat) {
            if(currentChat != 'Welcome'){
                if(this.userMessage != '') {
                const curChat = this.dataHistory.data.find(n => n.chatName === currentChat)
                curChat.messages.push({userId: 1, textMessage: this.userMessage})

                let ask = this.userMessage;

                let preparedAsk = ask.replace(/\s+/g, '+');

                
                axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                this.userMessage = ''
                }
            }
            else {
                if(this.userMessage != ''){
                    const name = this.userMessage
                    this.dataHistory.data.push({chatName: name, messages: [{userId: 1, textMessage: this.userMessage}]})
                    const curChat = this.dataHistory.data.find(c => c.chatName === name)
                    console.log(curChat)
                    let ask = this.userMessage;

                    let preparedAsk = ask.replace(/\s+/g, '+');

                    axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                    .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                    this.userMessage = ''

                }
            }

        },
        replaceCodeWithHTML(text){
            return text.replace(/```([^`]+)```/g, '<code class="text-red-300">$1</code>');
        },
        
        ourArray(name){
            console.log(name)
            return this.dataHistory.data.find(c => c.chatName === name)
        },
        lastArray() {
            return this.dataHistory.data
        }
    },
    computed: {
        lightTheButton() {
            if (this.userMessage.trim() !== '') {
                return "bg-white"
            }
            else {
                return false
            }
        }

    }
}    
</script>

<style>

#workspace {
    flex: 1;
    padding: 20px; 
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;


}
#workspaceChat {
    flex: 1;
    padding: 20px; 
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow-y: auto;
}

#innerZone {
    width: calc(100% - 150px);
    height: 100vh;
    max-width: 800px;
    text-align: left;

}

.avatar-small {
    float: left;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-right: 10px;
}
/* .text-container {
    text-align: left;
    margin-left: 40px; /* Выравнивание текста по левой стороне */
/* } */ */

.icon-small {
    width: 45px;
    height: 45px;
    background-color: white;
    border-radius: 50%;
    border-width: 7px;
    margin-bottom: 10px;
}

.icon{
    width: 18px;
    height: 18px;
    margin-left: 9px;
}

/* .message {

    display: block;
} */

.user-name {
    font-weight: bold; 
}



#myContainer {
    width: calc(100% - 150px);
    padding: 20px;
    text-align: left;
    padding: 50px;
    position: fixed;
    margin-top: 20px;
    bottom: 0px;
}

#myInput {
    background-color:#34344200;
    width: 100%;
    position: relative;
    border-radius: 18px;
    border: 1px solid rgb(143, 143, 143);
    height: 60px;
}    

#mainInput{
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
    background-color: #34344200;
    height: 55px;
    outline: none; 
}

#myButtonS {
    margin-right: 13px;
    position: absolute;
    right: 0;
    top: 0;
    margin-top: 10px;
    height: 35px;
    width: 35px;
    border-radius: 10px;
    cursor: pointer;
}

#grayNew {
    background-color: #ff0b0b;
}

#topText {
      font-size: 24px;
}

#welcomeText{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
</style>