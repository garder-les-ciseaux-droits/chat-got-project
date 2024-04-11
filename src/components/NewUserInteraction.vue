<template>
        <div class="relative w-full h-[50px] flex items-center justify-center md:mt-2 border-b border-white/15 md:border-0">
            <div class="flex w-full h-full justify-center">
                <div class="inline-block md:hidden w-10 flex items-center justify-start ml-4">
                    <button>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" />
                        </svg>
                    </button>
                </div>
                <div class="w-full h-full flex justify-center md:justify-start">
                    <button class="text-white text-xl bg-[#212121] w-36 h-11 rounded-xl hover:bg-white hover:bg-opacity-5" @click="showGptMenu">
                        <div class="w-full h-full flex items-center justify-center space-x-1">
                            <p class="text-base">ChatGPT  </p>
                            <p class="text-base text-white/75">{{ picked }}</p>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-3 h-3">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
                            </svg>

                        </div>
                       
                    </button>
                    <div v-show="gptModulesView" class="text-white w-80 h-48 mt-12 fixed border border-white/[.15] bg-[#2d2d2d] rounded-lg flex">
                <div class="flex flex-col mx-2 my-2 w-full justify-center space-y-0.5 text-sm">
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
                <div class="w-10 h-full flex justify-end items-center mr-4 inline-block md:hidden">
                    <button>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10" />
                        </svg>
                    </button>
                </div>
            </div>

            
        </div>
        <div class="w-full h-[630px] flex justify-center min-h-0 min-w-0" @click="hideGptMenu">
            <div class="flex w-full h-full min-h-0 min-w-0 items-center justify-center">
                <div v-if="shownChatName === 'Welcome' || (dataHistory.data.find(c => c.chatName === shownChatName).messages.length === 0)" class="flex flex-col items-center justify-center w-full h-full space-y-2" :style="welcomeContainerMargin">
                    <div class="flex flex-col items-center h-[500px] justify-center space-y-2 md:mt-24">
                        <div class="bg-white border-1 rounded-[50%] w-12 h-12 flex justify-center items-center">
                            <img class="flex w-8 h-8 min-w-0 min-h-0" src="https://freelogopng.com/images/all_img/1681038325chatgpt-logo-transparent.png">
                        </div>
                        <div>
                            <p class="flex text-white text-2xl">How can I help you today?</p>
                        </div>
                    </div>
                    <div class="flex w-full justify-center pb-4">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 w-[46rem] text-white h-full min-h-0 min-w-0 justify-center items-center mx-4">
                            <button class="min-w-0 flex flex-col justify-center p-4 border border-white/[.15] bg-[#212121] rounded-xl text-left text-xs hover:bg-white hover:bg-opacity-20" v-for="prompt in recommendedPropmts" :key="prompt.id" @click="sendRecPrompt(prompt)">
                                <h1 class="font-bold">{{prompt.title}}</h1>
                                <p class="text-white/[.45] text-xs truncate w-full">{{ prompt.text }}</p>
                            </button>
                        </div>
                    </div>
                </div>
                <div v-else class="w-full h-[32rem] flex flex-col overflow-x-hidden overflow-y-scroll min-w-0 items-center space-y-10">
                    <div class="w-full h-auto flex items-center justify-start mt-4 min-w-0 px-10 md:px-0 md:max-w-[44.5rem]"  v-for="mess in ourArray(shownChatName).messages" :key="mess.id">
                        <div class="flex ">
                            <div class="w-6 h-6 shrink-0">
                                <img class="rounded-xl" :src="userById(mess.userId).avatar"> 
                            </div> 
                            <div class="flex flex-col ml-4 text-white justify-start">
                                <p>
                                    {{ userById(mess.userId).userName }}
                                </p>
                                <p v-html="replaceCodeWithHTML(mess.textMessage)"></p>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
            
        </div>
        <div class="w-full flex justify-center items-center min-w-0" @click="hideGptMenu" :style="parentContainerHeight">
            <div v-if="picked === 3.5" class="flex flex-col w-[48rem] h-[80px] justify-center items-center min-w-0 min-h-0 space-y-4 mb-4 mx-4 md:mx-0">
                <div class="flex items-center w-full h-[55px] bg-[#34344200] text-white border border-white/[.15] rounded-2xl min-h-0 min-w-0">
                    <input class="w-full h-full bg-[#34344200] outline-none pl-[15px] min-w-0 min-h-0" type="text" placeHolder="Message your GPT" v-model="userMessage" @keyup.enter="send(shownChatName)">
                    <button :class="lightTheButton" class="flex items-center justify-center min-w-0 w-9 h-9 rounded-xl mr-3 min-w-0 min-h-0" id="myButtonS" type="button" @click="send(shownChatName)">
                        <img class="w-4 h-4 flex min-w-0 min-h-0" :src="'https://uxwing.com/wp-content/themes/uxwing/download/arrow-direction/up-arrow-icon.png'">
                    </button>
                </div>
                <div class="flex w-full h-[10px] items-center justify-center min-w-0 min-h-0">
                    <p class="text-xs text-gray-300 min-w-0 min-h-0">ChatGPT can make mistakes. Consider checking important information.</p>
                </div>
            </div>
            <div v-else class="flex w-[48rem] justify-center flex-col items-center min-h-0 space-y-4 mb-4 min-w-0 mx-4 md:mx-0">
                <div class="flex bg-[#34344200]  w-full text-white border border-white/[.15] rounded-2xl flex-col" :style="containerHeight">
                    <div class="flex ml-4 mt-2" v-show="fileReady">
                        <div class="flex w-56 items-center h-14 border border-white/[.25] rounded-xl bg-[#34344200] text-white" @mouseenter="deleteButton = true" @mouseleave="deleteButton = false">
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
                            <img class="flex w-9 h-6" src='/src/assets/paperlclip.png'>
                        </button>
                        <input class="w-full border-box h-[44px] bg-[#34344200] p-[10px]" type="text" placeHolder="Message your GPT" v-model="userMessage" @keyup.enter="sendNewGpt(shownChatName)" style="outline: none">
                        <button :class="lightTheButton" class="flex place-items-center justify-center  w-9 h-9 rounded-xl mr-3" id="myButtonS" type="button" @click="sendNewGpt(shownChatName)">
                            <img class="w-4 h-4 flex" :src="'https://uxwing.com/wp-content/themes/uxwing/download/arrow-direction/up-arrow-icon.png'">
                        </button>
                    </div>
                </div>
                <div class="flex w-full  h-[10px] items-center justify-center min-w-0 min-h-0">
                    <p class="text-xs text-gray-300 min-w-0 min-h-0">ChatGPT can make mistakes. Consider checking important information.</p>
                </div>
            </div>
        </div>

</template>


<script>
import axios from "axios"
import json from '/src/assets/dataHistory.json'
import openai from '/newBackend/useOpenAi.js'
export default {
    props: {
        shownChatName: String,
    },
    data() {
        return {
            userMessage: '',
            dataHistory: json,
            apiKey: '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',
            endpoint: 'https://api.openai.com/v1/chat/completions',
            text: "Hello, this is your script: ```print(123)```. Do you like it?",
            gptModulesView: false,
            picked: 3.5,
            fileReady: false,
            containerHeight: 'height: 55px',
            parentContainerHeight: 'height: 90px',
            welcomeContainerMargin: 'margin-bottom: 0rem',
            margingWithFiles: 'margin-top: 0rem',
            deleteButton: false,
            recommendedPropmts: [{title: 'Compare design principles', text: 'for mobile apps and desktop software'}, {title:'Brainstorm content ideas', text: 'for my new podcast on urban design'}, {title: 'Explain airplane turbulance', text: 'to someone who has never flown before'}, {title: 'Write an email', text: 'requesting a deadline extension for my project'}],
            
        }
    },
    methods: {
        hideGptMenu(){
            if (this.gptModulesView) this.gptModulesView = !this.gptModulesView;
        },
        userById(userId) {
          return this.dataHistory.users.find(u => u.id === userId );
        },
       
        async sendNewGpt(currentChat) {
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

                   

                    
                    this.userMessage = ''
                    
                    let ask = this.userMessage;
                    const chatCompletion = await openai.chat.completions.create({
                        messages: [{role: 'user', content: ask }],
                        model: 'gpt-3.5-turbo'
                    })
                    
                    curChat.messages.push({userId: 2, textMessage: chatCompletion.choices[0].message.content})
                    // let preparedAsk = ask.replace(/\s+/g, '+');

                    // axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                    // .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                    // .catch(error => console.log('Sending error:', error))


                    // this.userMessage = ''
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

                    this.userMessage = ''
                    
                    let ask = this.userMessage;
                    const chatCompletion = await openai.chat.completions.create({
                        messages: [{role: 'user', content: ask }],
                        model: 'gpt-3.5-turbo'
                    })
                    
                    curChat.messages.push({userId: 2, textMessage: chatCompletion.choices[0].message.content})
                    // let preparedAsk = ask.replace(/\s+/g, '+');

                    // axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                    // .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                    // .catch(error => console.log('Sending error:', error))
                    

                }
            }


        },
        async send(currentChat) {
            const currentDate = new Date();
            if(currentChat != 'Welcome'){
                if(this.userMessage != '') {
                const curChat = this.dataHistory.data.find(n => n.chatName === currentChat)
                curChat.messages.push({userId: 1, textMessage: this.userMessage})

                let ask = this.userMessage;

                // let preparedAsk = ask.replace(/\s+/g, '+');

                this.userMessage = '';
                const chatCompletion = await openai.chat.completions.create({
                        messages: [{role: 'user', content: ask }],
                        model: 'gpt-3.5-turbo'
                    })
                    
                curChat.messages.push({userId: 2, textMessage: chatCompletion.choices[0].message.content})
                

                // axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                // .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                // .catch(error => console.log('Sending error:', error))
               
                }
            }
            else {
                if(this.userMessage != ''){
                    const name = this.userMessage

                    this.dataHistory.data.push({chatName: name, date: `${currentDate.getDate()}.${currentDate.getMonth() + 1}.${currentDate.getFullYear()}`, messages: [{userId: 1, textMessage: this.userMessage}]})

                    
                    const curChat = this.dataHistory.data.find(c => c.chatName === name)
                    console.log(curChat)
                    
                    
                    let ask = this.userMessage;
                    this.userMessage = '';
                    // let preparedAsk = ask.replace(/\s+/g, '+');
                    const chatCompletion = await openai.chat.completions.create({
                        messages: [{role: 'user', content: ask }],
                        model: 'gpt-3.5-turbo'
                    })
                    
                    curChat.messages.push({userId: 2, textMessage: chatCompletion.choices[0].message.content})

                    // axios.get(`http://127.0.0.1:7770/user/?user=${preparedAsk}`)
                    // .then(response => curChat.messages.push({userId: 2, textMessage: response.data.Message}))
                    // .catch(error => console.log('Sending error:', error))

                    

                }
            }
        },
        deleteChosenFile(){
            let uploadButton = document.getElementById('fileInput');
            let chosenFile = document.getElementById('chosen-file');
            let fileName = document.getElementById('file-name'); 
            this.parentContainerHeight = 'height: 90px';
            this.welcomeContainerMargin = 'margin-bottom: 0rem';
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
                this.parentContainerHeight = 'height: 160px';
                this.welcomeContainerMargin = 'margin-bottom: 3.7rem';
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
          
            text = String(text);
            let parts = text.split(/```(.*?)\```/s);

            
            let result = "";

            
            for (let i = 0; i < parts.length; i++) {    
                
                if (i % 2 !== 0) {
                    result += "<code class='w-full md:w-[42rem] h-full py-5 pl-4 mt-3 mb-3 bg-black'>" + parts[i].trim(   ) + "</code>";
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
::-webkit-scrollbar {
  width: 12px;
}

::-webkit-scrollbar-track {
  background: rgba(241, 241, 241, 0);
}
</style>