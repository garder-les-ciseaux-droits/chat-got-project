<template>
        <div class="dark flex w-full shrink-0 overflow-x-hidden bg-[#0d0d0d]" :style="classWidth" @click="hideDeleteMenu">
            <div class="h-full w-[260px]">
                <div class="flex h-full flex-col">
                    <div class="relative h-full w-full flex-1 tems-start border-white/20">
                        <nav class="flex h-full w-full flex-col px-3 pb-3.5 place-items-center">
                            <div class="text-white">
                                <button id="topButton" class="rounded-[8px] hover:bg-white hover:bg-opacity-10 flex space-x-2  place-items-center" @click="createNewChat">
                                    <div class="bg-white border-1 rounded-[50%] w-8 h-8 flex justify-center place-items-center">
                                        <img class="flex w-5 h-5" src="https://freelogopng.com/images/all_img/1681038325chatgpt-logo-transparent.png">
                                    </div>
                                    <div class="text-sm flex">New Chat</div>          
                                </button>
                            </div>
                            <div class="text-white w-full place-items-start flex justify-center h-[96rem] mb-36 overflow-y-scroll  space-y-4" id="allButtons">
                                <div class="flex-col">
                                    <div v-show="dataHistory.data.find(c => c.date === getDate.today)" class="mb-4">
                                        <div>
                                            <p class="text-xs text-white/[.65] ml-2">Today</p>
                                        </div>
                                        <div class="flex flex-col-reverse relative mt-4">
                                            <button id="allButtons" class="relative button buttonsToday rounded-[8px] hover:bg-white hover:bg-opacity-10" v-show="userChat.date === getDate.today"  v-for="(userChat,index) in dataHistory.data" :key="index" @click="show(userChat.chatName, $event, index)" @mouseover="showDeleteButton(index)" @mouseleave="hideDeleteButton(index)">
                                                {{ userChat.chatName }}
                                                <button class="absolute top-0 right-0 mr-3 text-xl" v-if="deleteButtons[index]"  @click.stop="showDeleteMenu(index)">...</button>
                                                <div>
                                                    <div class="fixed z-50 bsolute border flex place-items-center  border-white/[.15] rounded-lg bg-[#171717] ml-[150px] w-[150px] h-[116px]" v-if="deleteMenuButtons[index]">
                                                        <div class="flex flex-col items-start">
                                                            <button class="text-white mb-2 ml-5">Share</button>
                                                            <button class="text-white mb-2 ml-5">Rename</button>
                                                            <button class="text-red-500 ml-5" @click="deleteChat(index)">Delete</button>
                                                        </div>
                                                    </div>    
                                                </div> 
                                            </button>
                                        </div>
                                    </div>
                                    <div v-show="dataHistory.data.find(c => c.date === getDate.yesterday)">
                                        <div>
                                            <p class="text-xs text-white/[.65] ml-2">Yesterday</p>
                                        </div>
                                        <div class="flex flex-col-reverse relative mt-4">
                                        <button id="allButtons" class="relative button buttonsToday rounded-[8px] hover:bg-white hover:bg-opacity-10" v-show="userChat.date === getDate.yesterday"  v-for="(userChat,index) in dataHistory.data" :key="index" @click="show(userChat.chatName, $event, index)" @mouseenter="showDeleteButton(index)" @mouseleave="hideDeleteButton(index)">
                                            {{ userChat.chatName }}
                                            <button class="absolute top-0 right-0 mr-3 text-xl" v-if="deleteButtons[index]"  @click.stop="showDeleteMenu(index)">...</button>
                                            <div>
                                                <div class="fixed z-50 border flex place-items-center  border-white/[.15] rounded-lg bg-[#171717] ml-[150px] w-[150px] h-[116px]" v-if="deleteMenuButtons[index]">
                                                    <div class="flex flex-col items-start">
                                                        <button class="text-white mb-2 ml-5">Share</button>
                                                        <button class="text-white mb-2 ml-5">Rename</button>
                                                        <button class="text-red-500 ml-5" @click="deleteChat(index)">Delete</button>
                                                    </div>
                                                </div>    
                                            </div> 
                                        </button>
                                        </div>
                                    </div>
                                
                                </div>
                            </div>                
                        </nav>                    
                    </div>
                </div>      
            </div>
        </div>
        <div v-show="chatListShown" class="text-white dark flex flex-col justify-center bg-[#0d0d0d] absolute bottom-0 items-center mb-3" :style="anotherClassWidth">
            <button class="buttonProfile rounded-[8px] hover:bg-white hover:bg-opacity-20 flex justify-items-start">
                <span class="font-bold text-xs">Upgrade plan</span>
                <span class="text-xs">Get GPT-4, DALL·E, and more</span>
            </button>
            <button class="relative buttonProfile rounded-[8px] hover:bg-white hover:bg-opacity-20 flex-justify-items-start">
                <img class="avatar-small" :src="userById(1).avatar">
                <span class="text-xs mt-2 font-bold flex"> {{ userById(1).profileName}}</span>
            </button>
        </div>
        <div class="text-white flex justify-center items-center ml-1.5">
            <button @click="showChatList" @mouseover="sidebarOver" @mouseleave="sidebarLeave">
                    <div id="sidebarContainer" class="flex h-6 w-6 flex-col items-center opacity-25 hover:opacity-100">
                        <div id="sidebarUp" class="h-3 w-1 bg-white rounded-full bg-token-text-primary" style="transform: translateY(0.15rem) rotate(0deg) translateZ(0px);">
                        </div>
                        <div id="sidebarDown" class="h-3 w-1 bg-white rounded-full bg-token-text-primary" style="transform: translateY(-0.15rem) rotate(0deg) translateZ(0px);">
                        </div>
                    </div>  
                    <span style="position: absolute; border: 0px; width: 1px; height: 1px; padding: 0px; margin: -1px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; word-wrap: normal;">
                        Close sidebar   
                    </span>
            </button>
        </div>
        
</template>

<script>

import json from '/src/assets/dataHistory.json'
import UserInteraction from '/src/components/UserInteraction.vue'
export default {
    components: {
        UserInteraction : UserInteraction
    },
    data() {
        return{
            visibleChatName: 'Welcome',
            dataHistory: json,
            classWidth: {width: '260px'},
            anotherClassWidth: {width:'260px', height: '100px'},
            chatListShown:  true,
            deleteButtons: Array(json.data.length).fill(false),
            deleteMenuButtons: Array(json.data.length).fill(false),
            shownDeleteButton: false,
            
        }
    },
    computed: {
        getDate(){
            const currentDate = new Date();
            const day = currentDate.getDate();
            const month = currentDate.getMonth() + 1;
            const year = currentDate.getFullYear();
            const todayDate = `${day}.${month}.${year}`;

            const yesterday = new Date(currentDate); 
            yesterday.setDate(yesterday.getDate() - 1);


            const yday = yesterday.getDate()
            const ymonth = yesterday.getMonth() + 1;
            const yyear = yesterday.getFullYear();
            const yesterdayDate = `${yday}.${ymonth}.${yyear}`;

            let dates = {
                today: "",
                yesterday: "",
                
            }

            dates.today = todayDate
            dates.yesterday = yesterdayDate

            return dates
        }
    },
    methods: {

        userById(userId) {
          return this.dataHistory.users.find(u => u.id === userId );
        },
        afterButtonAdded(){
            const buttons = document.querySelectorAll('.buttonsToday');

            buttons[buttons.length - 1].classList.toggle('active')
            
        },
        createNewChat() {
            let buttons = document.querySelectorAll('#allButtons');
            buttons.forEach((button) => {
                button.classList.remove('active')
            })
            this.visibleChatName = 'Welcome'
            
        },
        show(name, event, i) {
            this.visibleChatName = name
            const buttons = document.querySelectorAll('#allButtons');
           
            buttons.forEach((button) => {
                button.classList.remove('active')
            })
            event.target.classList.toggle('active')
            
            console.log(buttons[buttons.length - 1])
        },
        deleteChat(index) {
            this.dataHistory.data.splice(index, 1)
            this.deleteButtons.fill(false)
            this.visibleChatName = 'Welcome'
        },
        showChatList(){
            const sideBarCon = document.getElementById('sidebarContainer')
            if (this.chatListShown){
                this.classWidth = {width: '0'}
                this.anotherClassWidth = {width: '0', height: '0'}
                sideBarCon.style.transform = "rotate(180deg)"
                this.chatListShown = !this.chatListShown
                
            }
            else{
                
                sideBarCon.style.transform = "rotate(0)"
                this.classWidth = {width: '260px'}
                this.anotherClassWidth = {width: '260px', height: '100px'}
                this.chatListShown = !this.chatListShown
            }
        },
        sidebarOver(){
            const sidebarUp = document.getElementById('sidebarUp')
            sidebarUp.style.transform = "translateY(0.15rem) rotate(15deg) translateZ(0px)"
            const sidebarDown = document.getElementById('sidebarDown')
            sidebarDown.style.transform = "translateY(-0.15rem) rotate(-15deg) translateZ(0px)"
        },
        sidebarLeave(){
            const sidebarUp = document.getElementById('sidebarUp')
            sidebarUp.style.transform = "translateY(0.15rem) rotate(0deg) translateZ(0px)"
            const sidebarDown = document.getElementById('sidebarDown')
            sidebarDown.style.transform = "translateY(-0.15rem) rotate(0deg) translateZ(0px)" 
        },
        showDeleteButton(index) {
                this.deleteButtons[index] = true

        },
        hideDeleteButton(index) {
                this.deleteButtons[index] = false
        },
        showDeleteMenu(index) {
            this.deleteMenuButtons.fill(false)
            this.deleteMenuButtons[index] = true;
        },
        hideDeleteMenu(){
            this.deleteMenuButtons.fill(false)
        },
    },
    watch: {
        'dataHistory.data.length': function(newVal, oldVal){
            if(newVal > oldVal){
                setTimeout(this.afterButtonAdded, 0);
                this.visibleChatName = this.dataHistory.data.at(-1).chatName
               
                
            }   
            
           
        }
       
    },


}
</script>

<style>
.button {
    width: 220px;
    height: 40px;
    text-align: left;
    padding: 10px;
    margin-bottom: 5px;
}
.buttonProfile {
    width: 240px;
    height: 70px;
    text-align: left;
    padding: 10px;
    margin-bottom: 5px;
}

.button:active,
.active {
    background-color:#474750;
}

#topButton {
    width: 220px;
    margin-top: 15px;
    height: 45px;
    margin-bottom:30px; 
    text-align: left;
    padding: 10px;
}

#blackRectangle {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    height: 100vh;
    width: 260px;
    background-color: black;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.innerContainer{
    max-height: 100vh;
    margin: 0 20px;
    overflow-y: auto;

}

.dark {
    height: 100vh;
}

.avatar-small {
    float: left;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    margin-right: 10px;
}
</style>