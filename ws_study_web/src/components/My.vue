<template>
  <div class="container">
    <el-container :class="{'content':isfix,'fix':flag}">
      <el-aside width="180px" class="nav_list">
        <personal-nav :current="current_index" @onChangeCur="ChangeCurI"></personal-nav>
      </el-aside>
    </el-container>
    <div :class="{sort:isactive,'remove':flag}">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import Personal_nav from './personalbox/Personalnavleft'
    export default {
      name: "My",
      data (){
        return {
          isfix:true,
          flag:false,
          isactive:true,
          current_index:this.$route.query.i?this.$route.query.i:0
        }
      },
      mounted(){
        window.addEventListener('scroll',this.handleScroll)
      },
      components:{"personal-nav":Personal_nav},
      methods:{
        ChangeCurI:function(res){
          this.current_index = res;
        },
        handleScroll:function () {
          let scroll=document.documentElement.scrollTop || document.body.scrollTop;
          if(scroll>60){
            this.flag=true
          }else{
            this.flag=false
          }
        },
      },
    }
</script>

<style scoped>
    .fix{
      top: 0;
      position: fixed;
    }
    .remove{
      left: 180px;
    }
    .container{
      width: 1200px;
      position: relative;
      min-height: 520px;
      display: flex;
      margin: 20px auto;
    }
    .container .sort{
      width: 1020px;
      position: relative;
      min-height: 520px;
      box-shadow: 0 0 1px;
    }
    .container .content{
      width: 180px;
      /*position: fixed;*/
      height: 447px;
      box-shadow: 0 0 1px;
    }
  .content .nav_list{
      height: 450px;

  }

</style>
