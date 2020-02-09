<template>
    <div id="index" class="index">
      <header-box @reflesh="onReflesh"></header-box>
      <router-view></router-view>
      <footer-box></footer-box>
    </div>
</template>

<script>

    import HeaderBox from "./global/HeaderBox";
    import FooterBox from "./global/FooterBox";
    export default {
        name: "Index",
      components: {FooterBox, HeaderBox},
      watch:{
        '$route'(to,from){
          if(to.name==='my'){
            this.$router.push({path:'/my/profile'})
          }
        }
      },
      methods:{
        /* 页面退出刷新 */
        onReflesh:function () {
          this.$router.push({path:'/'})
        }
        /* 页面退出刷新 END */
      }
    }
</script>

<style scoped>
 .index{
    margin: 0;
    padding: 0;
    border: none;
  }
</style>
