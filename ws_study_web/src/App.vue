<template>
  <div id="app">
<!--    <router-view></router-view>-->
    <!-- 刷新事件 -->
    <router-view v-if="isShow"></router-view>
    <!-- 刷新事件 END -->
  </div>
</template>

<script>
import Login from "./components/Login";
export default {
  name: 'app',
  components: {Login},
  /* 刷新事件 */
  data(){
    return{
      isShow:true
    }
  },
  provide(){
    return{
      reload:this.reload
    }
  },
  methods:{
    reload(){
      this.isShow = false;
      this.$nextTick(function () {
        this.isShow = true
      })
    }
  }
  /* 刷新事件 END */
}
</script>

<style>
  html,body{
    margin: 0;
    padding: 0;
    border: none;
    width: 100%;
    /*min-height: ;*/
  }
</style>
