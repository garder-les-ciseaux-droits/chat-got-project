<template>
    <div class="w-full h-full flex">
        <div v-show="chatListVisible === true" class="hidden w-[260px] h-full bg-[#171717] md:flex flex-col items-center justify-center min-h-0" :style="classWidth" @click="hideDeleteMenu">
            <div class="w-[244px] h-full flex flex-col items-center min-h-0 overflow-y-hidden">
                <div class="w-[228px] h-[50px] flex mt-4">
                    <button class="rounded-[8px] text-white hover:bg-white hover:bg-opacity-10 flex space-x-2 items-center w-[220px] pl-2 h-[40px]" @click="createNewChat">
                        <div class="w-full h-full flex items-center justify-start space-x-2">
                            <div class="bg-white border-1 rounded-[50%] w-7 h-7 flex justify-center items-center">
                                <img class="flex w-5 h-5" src="https://freelogopng.com/images/all_img/1681038325chatgpt-logo-transparent.png">
                            </div>
                            <div>
                                <p class="text-sm text-white">ChatGPT</p>
                            </div>
                        </div>   
                        <div class="flex items-center justify-end w-10 h-full pr-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10" />
                            </svg>
                        </div>  
                    </button>
                </div>
                <div class="w-[228px] h-full flex items-start text-white">
                    <div class="w-full h-[30rem] mt-4 flex flex-col items-center justify-start overflow-y-auto overflow-x-hidden">
                        <div v-show="dataHistory.data.find(c => c.date === getDate.today)" class="w-full items-start justify-start flex flex-col mt-4">
                            <div class="w-full h-[15px] flex justify-start">
                                <p class="text-xs text-white/[.65] pl-2">Today</p>
                            </div>
                            <div class="flex flex-col-reverse mt-2" v-show="userChat.date === getDate.today" v-for="(userChat,index) in dataHistory.data" :key="index">
                                
                                <button class="flex w-[220px] h-[38px] rounded-[8px] hover:bg-white hover:bg-opacity-10" @click="show(userChat.chatName, $event)" @mouseover="showDeleteButton(index)" @mouseleave="hideDeleteButton(index)">
                                    <div class="w-full h-full flex items-center">
                                        <p class="text-left pl-2 w-[180px] truncate">{{ userChat.chatName }}</p>
                                    </div>
                                    <div class="w-[50px] h-full flex justify-center items-center">
                                        <button class="mr-1 text-xl" v-if="deleteButtons[index]"  @click.stop="showDeleteMenu(index)">
                                            <img class="w-[15px]" src="/src/assets/images/60969-2.png">
                                        </button>
                                    </div>

                                    <div class="border absolute ml-[170px] mt-[17px] flex items-center border-white/[.15] rounded-lg bg-[#2f2f2f] w-[150px] h-[116px]" v-if="deleteMenuButtons[index]">
                                            <div class="flex flex-col items-start">
                                                <button class="text-white mb-2 ml-5">Share</button>
                                                <button class="text-white mb-2 ml-5">Rename</button>
                                                <button class="text-red-500 ml-5" @click="deleteChat(index)">Delete</button>
                                            </div>
                                    </div>    
                                </button>
                            </div>
                        </div>
                        <div  v-show="dataHistory.data.find(c => c.date === getDate.yesterday)" class="w-full justify-start items-start flex flex-col mt-4">
                            <div class="w-full h-[15px] flex justify-start">
                                <p class="text-xs text-white/[.65] ml-2">Yesterday</p>
                            </div>
                            <div class="flex flex-col-reverse mt-2" v-show="userChat.date === getDate.yesterday"  v-for="(userChat,index) in dataHistory.data" :key="index">
                                <button id="allButtons" class="flex w-[220px] h-[38px] rounded-[8px] hover:bg-white hover:bg-opacity-10" @click="show(userChat.chatName, $event)" @mouseenter="showDeleteButton(index)" @mouseleave="hideDeleteButton(index)">
                                    <div class="w-full h-full flex items-center">
                                        <p class="text-left pl-2">{{ userChat.chatName }}</p>
                                    </div>
                                    <div class="w-[50px] h-full flex justify-center items-center">
                                        <button class="mr-1 text-xl" v-if="deleteButtons[index]"  @click.stop="showDeleteMenu(index)">
                                            <img class="w-[15px]" src="/src/assets/images/60969-2.png">
                                        </button>
                                    </div>
                                    <div class="border absolute ml-[170px] mt-[17px] flex items-center border-white/[.15] rounded-lg bg-[#2f2f2f] w-[150px] h-[116px]" v-if="deleteMenuButtons[index]">
                                        <div class="flex flex-col items-start">
                                            <button class="text-white mb-2 ml-5">Share</button>
                                            <button class="text-white mb-2 ml-5">Rename</button>
                                            <button class="text-red-500 ml-5" @click="deleteChat(index)">Delete</button>
                                        </div>
                                    </div>  
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-[244px] h-[112px] flex flex-col justify-center items-center mb-2 text-white"  v-show="chatListShown" :style="anotherClassWidth">
                    <button class="rounded-[8px] w-[236px] h-[56px] hover:bg-white hover:bg-opacity-20 flex justify-center items-center">
                        <span class="font-bold text-xs">Upgrade plan</span>
                        <span class="text-xs">Get GPT-4, DALL·E, and more</span>
                    </button>
                    <button class="rounded-[8px] w-[236px] h-[56px] hover:bg-white hover:bg-opacity-20 flex items-center pl-3">
                        <img class="avatar-small" :src="userById(1).avatar">
                        <span class="text-xs mt-2 font-bold flex"> {{ userById(1).profileName}}</span>
                    </button>

            </div>
        </div>
        <div class="hidden text-white md:flex justify-center items-center ml-1.5">
            <button @click="hideChatMenu" @mouseover="sidebarOver" @mouseleave="sidebarLeave">
                    <div id="sidebarContainer" class="flex h-6 w-6 flex-col items-center opacity-25 hover:opacity-100">
                        <div id="sidebarUp" class="h-3 w-1 bg-white rounded-full bg-token-text-primary" style="transform: translateY(0.15rem) rotate(0deg) translateZ(0px);">
                        </div>
                        <div id="sidebarDown" class="h-3 w-1 bg-white rounded-full bg-token-text-primary" style="transform: translateY(-0.15rem) rotate(0deg) translateZ(0px);">
                        </div>
                    </div>  
                    <!-- <span style="position: absolute; border: 0px; width: 1px; height: 1px; padding: 0px; margin: -1px; overflow: hidden; clip: rect(0px, 0px, 0px, 0px); white-space: nowrap; word-wrap: normal;">
                        Close sidebar   
                    </span> -->
            </button>
        </div>

        <div class="w-full h-full flex flex-col items-center min-w-0 space-y-2 justify-center" @click="hideDeleteMenu">
            <NewUserInteraction :shownChatName="visibleChatName" @click="hideDeleteMenu"/>
        </div>
    </div>
    
</template>

<script>
import NewUserInteraction from '/src/components/NewUserInteraction.vue';
import json from '/src/assets/dataHistory.json';

export default {
    components: {
        NewUserInteraction
    },
    data() {
        return{
            chatListVisible: true,
            visibleChatName: 'Welcome',
            dataHistory: json,
            classWidth: {width: '266px'},
            anotherClassWidth: {width:'266px'},
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


            const yday = yesterday.getDate();
            const ymonth = yesterday.getMonth() + 1;
            const yyear = yesterday.getFullYear();
            const yesterdayDate = `${yday}.${ymonth}.${yyear}`;

            let dates = {
                today: "",
                yesterday: ""
            };

            dates.today = todayDate;
            dates.yesterday = yesterdayDate;

            return dates;
        }
    },
    methods: {
        hideChatMenu(){
            this.chatListVisible = !this.chatListVisible;
            
        },
        userById(userId) {
          return this.dataHistory.users.find(u => u.id === userId );
        },
        afterButtonAdded(){
            const buttons = document.querySelectorAll('.buttonsToday');

            buttons[buttons.length - 1].classList.toggle('active')
            
        },
        createNewChat() {

            this.visibleChatName = 'Welcome'
            
        },
        show(name, event) {
            this.visibleChatName = name;
            // let buttons = document.querySelectorAll('#allButtons');
           
            // buttons.forEach((button) => {
            //     button.classList.remove('active')
            // })
            // event.target.classList.add('active')
            
            // console.log(buttons[buttons.length - 1])
        },
        deleteChat(index) {
            
            this.dataHistory.data.splice(index, 1);
            this.deleteButtons.fill(false);
            setTimeout(() => {
                this.visibleChatName = 'Welcome';
            }, 0);
            console.log(this.visibleChatName)
            
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
            if (this.chatListVisible){
            const sidebarUp = document.getElementById('sidebarUp')
            sidebarUp.style.transform = "translateY(0.15rem) rotate(15deg) translateZ(0px)"
            const sidebarDown = document.getElementById('sidebarDown')
            sidebarDown.style.transform = "translateY(-0.15rem) rotate(-15deg) translateZ(0px)"
            }
            else{
                const sidebarUp = document.getElementById('sidebarUp')
                sidebarUp.style.transform = "translateY(0.15rem) rotate(-15deg) translateZ(0px)"
                const sidebarDown = document.getElementById('sidebarDown')
                sidebarDown.style.transform = "translateY(-0.15rem) rotate(15deg) translateZ(0px)"
            }
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
                // setTimeout(this.afterButtonAdded, 0);
                this.visibleChatName = this.dataHistory.data.at(-1).chatName
                console.log(this.visibleChatName)
                
            }   
            
           
        }
       
    },


}
</script>


<style>
::-webkit-scrollbar {
  width: 12px; /* Ширина полосы */
}

::-webkit-scrollbar-track {
  background: rgba(241, 241, 241, 0); /* Прозрачный цвет фона трека */
}



/* Подсветка при наведении курсора */
::-webkit-scrollbar-thumb:hover {
  background: #020202;
  border-radius: 6px;
}

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



.avatar-small {
    float: left;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    margin-right: 10px;
}
</style>