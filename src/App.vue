<template>
  <div class="h-screen w-screen overflow-y-auto flex bg-[#212121]">
    <!-- <ChatList class="w-full h-full" /> -->
    <div class="w-full h-full">
      <NewChatList/>
    </div>

  </div>
</template>
<script>
import ChatList from '/src/components/ChatList.vue'
import NewChatList from '/src/components/NewChatList.vue'


export default {
  components: {
    ChatList,
    NewChatList
  },
  data() {
    return {
    }
  },
  methods: {

  },
  mounted() {
  },
  computed: {

  }
}
</script>


<style>

</style>
