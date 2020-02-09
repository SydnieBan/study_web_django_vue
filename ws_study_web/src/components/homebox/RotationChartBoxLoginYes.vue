<template>
  <el-container>
    <el-header class="el-header" style="height: 100px">
      <router-link class="rcb_router_link" to="/course_free" style="">免费精品课程</router-link>
    </el-header>
    <el-main style="height: 180px" class="el-main">
      <router-link to="/my">
        <img :src="user_icon" alt="你好啊" class="my_img">
      </router-link>
    </el-main>
    <el-footer style="height: 120px;border-radius: 0 0 10px 0">
      <el-button type="primary" @click="onToMy" style="background-color: #87cefa;width: 150px">我的课程</el-button>
    </el-footer>

  </el-container>
</template>

<script>
    export default {
        name: "RotationChartBoxLoginYes",
      data(){
          return{
            user_id:null,
            user_icon:this.Global.default_img,
          }
      },
      created:function () {
        this.user_id = window.localStorage.getItem('user_id');
        this.get_user_info()
      },
      methods:{
        onToMy:function(){
          this.$router.push({path:'/my/total',query:{i:1}})
        },
        /* 获取用户信息 */
        get_user_info:function () {
          let url = this.Global.server_url + '/user/get_user_info/';
          this.GlobalFunc.func_axios(url, 'GET', {user_id:this.user_id},
            res=>{ this.show_user_info(this.user_icon, res) }
          )
        },
        /* 获取用户信息 END */
        /* 显示用户信息 */
        show_user_info:function (to_data, res) {
          if (res[0].user_icon__icon_img){
            // this.user_icon = this.Global.img_url + '/images/' + res[0].user_icon__icon_img
            this.user_icon = this.Global.img_url + '/' + res[0].user_icon__icon_img // 七牛云
          }
        }
        /* 显示用户信息 END */
      }
    }
</script>

<style scoped>
  .el-header,.el-main,.el-footer{
    margin: 0;
    padding: 0;
    text-align: center;
  }
  .el-header{
    border-radius: 0 10px 0 0;
    padding-top: 65px;
  }
  .el-main{
    padding-top: 40px;
  }
  .my_img{
    width: 84px;
    height: 84px;
    border-radius: 50%;
  }
  .rcb_router_link{
    font-size: 18px;
    color: white;
    text-decoration: none;
    transition: color 0.5s;
  }
  .rcb_router_link:hover{
    color: gray;
  }
</style>
