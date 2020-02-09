<template>
<div class="note" :style="{backgroundColor:color}">
  <!-- 头部 -->
  <div class="first">
    <div class="first-left">
      <div class="left-text"><strong @click="toMyNote">{{this.information.user_name}}的笔记</strong></div>
      <el-color-picker v-model="color" size="mini" style="margin-top: 70px"></el-color-picker>
    </div>
  </div>
  <!-- 头部 END -->
  <!-- container -->
  <div class="second" style="padding-top: 30px">
      <!-- 左侧 -->
      <div class="second_left">
        <note-left :information="information"></note-left>
      </div>
    <!-- 左侧 END -->
    <!-- 右侧 -->
      <div class="second_right">
        <router-view></router-view>
      </div>
    <!-- 右侧 END -->


  </div>
  <!-- container END　-->
</div>
</template>

<script>
  import NoteLeft from "./notebox/NoteLeft";
  import NoteList from "./notebox/NoteList";

  export default {
        name: "Note2",
      data(){
          return{
            user_id:window.localStorage.getItem('user_id'),
            information:{user_img:this.Global.default_img, user_name:null,user_sex__name:null,identity:null,address:null,introduce:null},
            color:'rgba(158, 165, 199, 0.63)'
          }
      },
      components:{ NoteList, NoteLeft, },
      created:function(){
            this.get_information()
      },
      methods:{
          /* 到笔记列表页 */
        toMyNote:function(){
          this.$router.push({path:'/note'})
        },
          /* 到笔记列表页 END */
        /* 获取用户信息 */
        get_information:function(){
          let url=this.Global.server_url+'/user/get_user_info/';
          this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id},
            res=>{
              this.information.user_img = this.Global.img_url+'/'+res[0].user_icon__icon_img;
              this.information.user_name = res[0].user_name;
              this.information.user_sex__name = res[0].user_sex__name;
              this.information.identity = res[0].identity;
              this.information.address = res[0].address;
              this.information.introduce = res[0].introduce;
            }
          )
        },
        /* 获取用户的所有信息 END */
      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
  .note{
    width: 100%;
    min-width: 1215px;
    padding-bottom: 100px;
  }
  .first{
    width: 100%;
    height: 100px;
    background-image: url("http://pykpufs15.bkt.clouddn.com/images/note1.png");
    background-size: cover;
    margin-top: 0;
  }
  .first .first-left{
    width: 1215px;
    height: 100px;
    margin: auto;
    display: flex;
    justify-content: space-between;
  }
  .first .first-left .left-text{
    height: 100px;
    text-align: start;
    line-height: 80px;
    color: white;
    font-size: 25px;
  }
  .first .first-left .left-text strong{
    transition: color 0.5s;
  }
  .first .first-left .left-text strong:hover{
    cursor: pointer;
    color: lightskyblue;
  }
  /*2222222*/
  .second{
    width: 1215px;
    margin: auto;
    display: flex;
  }
  .second .second_left{
    width: 300px;
    height: 760px;
  }
  .second .second_right{
    width: 900px;
    height: 760px;
    margin-left: 15px;
  }
/*22222222*/
</style>
