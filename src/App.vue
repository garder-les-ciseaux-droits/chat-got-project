<template>
  <div class="relative z-0 flex h-full w-full overflow-hidden">
    <ChatList />
  </div>
</template>
<script>
import ChatList from '/src/components/ChatList.vue'

export default {
  components: {
    ChatList: ChatList
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
body {
    background-color: #171717;
    margin: 0;
}
</style>
