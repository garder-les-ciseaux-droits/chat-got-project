<template>
    <div class="h-screen w-full">
        <div class="text-white top-0 border border-white/[.15] w-36 h-11 mt-2 text-xl flex justify-center bg-white bg-opacity-15">
            <button @click="showGptMenu"> ChatGPT{{ picked }} </button>
            <div v-show="gptModulesView" class="text-white fixed w-80 h-48 mt-12 ml-44 border border-white/[.15] bg-[#2d2d2d] rounded-lg flex">
                <div class="flex flex-col grow mx-2 my-2 w-screen space-y-0.5 text-sm">
                    <button class="flex hover:bg-white hover:bg-opacity-10 rounded pl-2 space-y-0.5 items-center w-full h-24" @click="picked = 3.5">
                        <div class="flex items-center">
                            <div class="flex flex-col text-left">
                                <h1>GPT-3.5</h1>
                                <p class="text-white/[.65]">Great for everyday tasks</p>
                            </div>
                            <div class="absolute right-0 mr-5">
                                <div class="border border-white/[.15] rounded-xl w-4 h-4">
                                    <div v-show="picked === 3.5" class="bg-white w-4 h-4 rounded-xl"></div>
                                </div>
                            </div>
                        </div>
                    </button>
                    <button class="flex items-center hover:bg-white hover:bg-opacity-10 rounded pl-2 space-y-0.5 h-full" @click="picked = 4">
                        <div class="flex flex-col text-left">
                            <h1>GPT-4</h1>
                            <p class="text-white/[.65]">Our smartest and most capable model.</p>
                            <p class="text-white/[.65]">Includes DALL-E, browsing and more.</p>
                        </div>
                        <div class="absolute right-0 mr-5">
                            <div class="border border-white/[.15] rounded-xl w-4 h-4">
                                <div v-show="picked === 4" class="bg-white w-4 h-4 rounded-xl"></div>
                            </div>
                        </div>
                    </button>
                   
                </div>
                  
            </div>
        </div>
        <div class="flex h-screen place-items-center justify-center flex-col">
            <div v-if="shownChatName === 'Welcome' || (dataHistory.data.find(c => c.chatName === shownChatName).messages.length === 0)" class="flex place-items-center justify-center w-full h-screen flex-col">
                <div class="mb-1 bg-white border-1 rounded-[50%] w-12 h-12 flex justify-center place-items-center">
                    <img class="flex w-8 h-8" src="https://freelogopng.com/images/all_img/1681038325chatgpt-logo-transparent.png">
                </div>
                <div>
                    <p id="topText" class="flex text-white">How can I help you today?</p>
                </div>
            </div>
            <div v-else class="flex place-items-center w-full h-[630px] mb-15 mt-10 flex-col overflow-y-auto overflow-x-hidden">
                <div class="w-[47rem] justify-center text-left">
                    <div class="mb-5 text-white"  v-for="mess in ourArray(shownChatName).messages" :key="mess.id">
                        <img class="float-left w-6 h-6 rounded-xl mr-4 flex" :src="userById(mess.userId).avatar">
                        <div class="flex flex-col">
                            <p class="flex">
                                {{ userById(mess.userId).userName }}
                            </p>
                            <p class="flex" v-html="replaceCodeWithHTML(mess.textMessage)"></p>
                        </div>
                            
                    </div>
                </div>
            </div>
            <div v-show="shownChatName === 'Welcome'" class="flex w-full justify-center mb-5">
                <div class="grid grid-cols-2 gap-4 w-[46rem] text-white">
                    <button class="col-span-1 p-4 border border-white/[.15] h-16 bg-[#171717] space-y-0.5  rounded-xl text-left text-xs hover:bg-white hover:bg-opacity-20" v-for="prompt in recommendedPropmts" :key="prompt.id" @click="sendRecPrompt(prompt)">
                        <h1 class="font-bold">{{prompt.title}}</h1>
                        <p class="text-white/[.45]">{{ prompt.text }}</p>
                    </button>
                </div>
            </div>
            <div v-if="picked === 3.5" class="flex grow w-full justify-center mb-16 flex-col place-items-center bottom-0">
                <div class="flex justify-center place-items-center w-[48rem] h-[55px] text-white border border-white/[.15] rounded-2xl bottom-0">
                    <input id="mainInput" type="text" placeHolder="Message your GPT" v-model="userMessage" @keyup.enter="send(shownChatName)">
                    <button :class="lightTheButton" class="flex place-items-center justify-center  w-9 h-9 rounded-xl mr-3" id="myButtonS" type="button" @click="send(shownChatName)">
                        <img class="w-4 h-4 flex" :src="'https://uxwing.com/wp-content/themes/uxwing/download/arrow-direction/up-arrow-icon.png'">
                    </button>
                </div>
                <div class="flex bottom-0 mt-5 text-xs text-gray-300">
                    <span>ChatGPT can make mistakes. Consider checking important information.</span>
                </div>
            </div>
            <div v-else class="flex w-full justify-center mb-16 flex-col place-items-center bottom-0">
                <div class="flex justify-center w-[48rem] text-white border border-white/[.15] rounded-2xl bottom-0 flex-col" :style="containerHeight">
                    <div class="flex ml-4 mt-4" v-show="fileReady">
                       
                        <div class="flex w-56 h-14 border border-white/[.25] rounded-xl bg-[#34344200] text-white place-items-center" @mouseenter="deleteButton = true" @mouseleave="deleteButton = false">
                            <div  v-show="deleteButton" class="absolute mb-12 ml-52 border bg-[#414141] border-white/[.25] rounded-xl w-5 h-5 flex justify-center">
                                <button @click="deleteChosenFile">
                                    <span class="flex place-items-center text-xs">X</span>
                                </button>
                               
                            </div>
                            <img class="ml-3 w-10 h-10 flex bg-white" id="chosen-file">
                            <div id="info" class="text-xs flex truncate  px-2 flex-col space-y-1"> 
                                <figcaption id="file-name"></figcaption>
                                <p class="text-white/50">PDF</p>
                            </div>
                        </div>
                    </div>
                    <div class="flex justify-center place-items-center w-full h-full" :style="margingWithFiles">
                        <input type="file" id="fileInput" accept=".pdf" style="display: none;">
                        <button class="ml-3" @click="chooseFile">
                            <img class="flex w-9 h-6" :src="'src/assets/paperlclip.png'">
                        </button>
                        <input class="w-full border-box h-[44px] bg-[#34344200] p-[10px]" type="text" placeHolder="Message your GPT" v-model="userMessage" @keyup.enter="sendNewGpt(shownChatName)" style="outline: none">
                        <button :class="lightTheButton" class="flex place-items-center justify-center  w-9 h-9 rounded-xl mr-3" id="myButtonS" type="button" @click="sendNewGpt(shownChatName)">
                            <img class="w-4 h-4 flex" :src="'https://uxwing.com/wp-content/themes/uxwing/download/arrow-direction/up-arrow-icon.png'">
                        </button>
                    </div>
                </div>
                <div class="flex bottom-0 mt-5 text-xs text-gray-300">
                    <span>ChatGPT can make mistakes. Consider checking important information.</span>
                </div>
            </div>
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
            text: "Hello, this is your script: ```print(123)```. Do you like it?",
            gptModulesView: false,
            picked: 3.5,
            fileReady: false,
            containerHeight: 'height: 55px',
            margingWithFiles: 'margin-top: 0rem',
            deleteButton: false,
            recommendedPropmts: [{title: 'Compare design principles', text: 'for mobile apps and desktop software'}, {title:'Brainstorm content ideas', text: 'for my new podcast on urban design'}, {title: 'Explain airplane turbulance', text: 'to someone who has never flown before'}, {title: 'Write an email', text: 'requesting a deadline extension for my project'}],
            
        }
    },
    methods: {
        userById(userId) {
          return this.dataHistory.users.find(u => u.id === userId );
        },
       
        sendNewGpt(currentChat) {
            const currentDate = new Date();
            if(currentChat != 'Welcome'){
                if(this.userMessage != '') {
                    const curChat = this.dataHistory.data.find(n => n.chatName === currentChat)
                    let fileName = document.getElementById('file-name');
                    if (fileName.textContent){
                        curChat.messages.push({userId: 1, textMessage: fileName.textContent + this.userMessage})
                        this.deleteChosenFile();
                    }
                    else{
                        curChat.messages.push({userId: 1, textMessage: this.userMessage})
                    }

                   

                    let ask = this.userMessage;

                    let preparedAsk = ask.replace(/\s+/g, '+');

                    axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                    .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                    .catch(error => console.log('Sending error:', error))


                    this.userMessage = ''
                }
            }
            else {
                if(this.userMessage != ''){
                    const name = this.userMessage
                    let fileName = document.getElementById('file-name');

                    if (fileName.textContent){
                        this.dataHistory.data.push({chatName: name, date: `${currentDate.getDate()}.${currentDate.getMonth() + 1}.${currentDate.getFullYear()}`, messages: [{userId: 1, textMessage: fileName.textContent +  this.userMessage  }]})
                        
                        this.deleteChosenFile();
                    }
                    else{
                        this.dataHistory.data.push({chatName: name, date: `${currentDate.getDate()}.${currentDate.getMonth() + 1}.${currentDate.getFullYear()}`, messages: [{userId: 1, textMessage: this.userMessage}]})
                    }
                    
                    const curChat = this.dataHistory.data.find(c => c.chatName === name)

                    
                    
                    let ask = this.userMessage;

                    let preparedAsk = ask.replace(/\s+/g, '+');

                    axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                    .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                    .catch(error => console.log('Sending error:', error))
                    this.userMessage = ''

                }
            }


        },
        send(currentChat) {
            const currentDate = new Date();
            if(currentChat != 'Welcome'){
                if(this.userMessage != '') {
                const curChat = this.dataHistory.data.find(n => n.chatName === currentChat)
                curChat.messages.push({userId: 1, textMessage: this.userMessage})

                let ask = this.userMessage;

                let preparedAsk = ask.replace(/\s+/g, '+');

                
                axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                .catch(error => console.log('Sending error:', error))
                this.userMessage = ''
                }
            }
            else {
                if(this.userMessage != ''){
                    const name = this.userMessage

                    this.dataHistory.data.push({chatName: name, date: `${currentDate.getDate()}.${currentDate.getMonth() + 1}.${currentDate.getFullYear()}`, messages: [{userId: 1, textMessage: this.userMessage}]})

                    
                    const curChat = this.dataHistory.data.find(c => c.chatName === name)
                    console.log(curChat)
                    
                    
                    let ask = this.userMessage;

                    let preparedAsk = ask.replace(/\s+/g, '+');

                    axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                    .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                    .catch(error => console.log('Sending error:', error))

                    this.userMessage = ''

                }
            }
        },
        deleteChosenFile(){
            let uploadButton = document.getElementById('fileInput');
            let chosenFile = document.getElementById('chosen-file');
            let fileName = document.getElementById('file-name'); 
            this.containerHeight = 'height: 55px';
            chosenFile.removeAttribute("src");
            fileName.textContent = null;
            uploadButton.value = null;
            this.fileReady = false;
            
        },
        chooseFile(){
            let uploadButton = document.getElementById('fileInput');
            let chosenFile = document.getElementById('chosen-file');
            let fileName = document.getElementById('file-name');
            uploadButton.click();
            uploadButton.onchange = () => {
                let reader = new FileReader();
                this.fileReady = true;
                this.containerHeight = 'height: 125px';
                reader.readAsDataURL(uploadButton.files[0]);
                reader.onload = () => {
                    chosenFile.setAttribute("src", reader.result);

                }
                fileName.textContent = uploadButton.files[0].name;
                
            }

        },
        sendRecPrompt(prompt){
            const currentDate = new Date();
            const name = prompt.title
            this.userMessage = `${prompt.title}: ${prompt.text}`
            this.dataHistory.data.push({chatName: name, date: `${currentDate.getDate()}.${currentDate.getMonth() + 1}.${currentDate.getFullYear()}`, messages: [{userId: 1, textMessage: this.userMessage}]})
            const curChat = this.dataHistory.data.find(c => c.chatName === name)
            console.log(curChat)
            let ask = this.userMessage;

            let preparedAsk = ask.replace(/\s+/g, '+');

            axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
            this.userMessage = ''
        },
        replaceCodeWithHTML(text){
          
            let parts = text.split(/```(.*?)\```/);

            
            let result = "";

            
            for (let i = 0; i < parts.length; i++) {    
                
                if (i % 2 !== 0) {
                    result += "<code class='w-[44rem] h-auto py-5 pl-4 mt-3 mb-3 bg-black'>" + parts[i].trim(   ) + "</code>";
                } else {
                   
                    result += "<p class='break-all'>" + parts[i].trim() + "</p>\n";
                }
            }

            result = "<div class='text-left flex flex-col'>" + result + "</div>";

            return result;
        },
        replaceCodeWithHtmlS(text){
            let parts = text.split(/```(.*?)\```/);

            
            let result = "";


            for (let i = 0; i < parts.length; i++) {
                
                if (i % 2 !== 0) {
                    result += `\n ${parts[i].trim()}\n`;
                } else {
                
                    result += parts[i].trim();
                }
            } 
            return result
            
        }
        ,
        
        ourArray(name){
           
            return this.dataHistory.data.find(c => c.chatName === name)
        },
        lastArray() {
            return this.dataHistory.data
        },
        showGptMenu(){
            this.gptModulesView = !this.gptModulesView
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




.icon-small {
    width: 45px;
    height: 45px;
    background-color: white;
    border-radius: 50%;
    border-width: 7px;
    margin-bottom: 10px;
}

.pre-formatted {
  white-space: pre;
}



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
</style>