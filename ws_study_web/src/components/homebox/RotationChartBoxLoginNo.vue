<template>
    <el-container>
      <el-header class="el-header1" style="height: 100px">
        <router-link class="rcb_router_link" to="/course_free" style="font-size: 18px">免费精品课程</router-link>
      </el-header>
      <el-main style="height: 190px">
        <el-header class="el-header2" style="height: 130px;">
          <router-link to="/login">
            <img :src="default_user_img"  alt="你好呀">
          </router-link>
        </el-header>
        <el-main style="height: 60px;">
          <el-button type="primary" @click="onToLogin" class="rcb_btn">登录</el-button>
        </el-main>
      </el-main>
      <el-footer style="height: 110px;border-radius: 0 0 10px 0">
        <router-link class="rcb_router_link" to="/login">没有账号，去注册</router-link>
      </el-footer>
    </el-container>
</template>

<script>
    export default {
        name: "RotationChartBoxLoginNo",
      data(){
        return{
          default_user_img:this.Global.default_img
        }
      },
      methods:{
        onToLogin:function () {
          this.$router.push({path:'/login'})
        }
      }
    }
</script>

<style scoped>

  .el-header,.el-main,.el-footer{
    margin: 0;
    padding: 0;
    text-align: center;
  }
  .el-header1{
    border-radius: 0 10px 0 0;
    padding-top: 65px;
  }
  .el-header2{
    padding-top: 20px;
  }
  .el-header2 img{
    width: 84px;
    height: 84px;
    border-radius: 50%;
  }
  .rcb_btn{
    font-size: 18px;
    color: white;
    transition: color 0.5s;
    background-color: #87cefa;
    width: 150px
  }
  .rcb_btn:hover{
    color: gray;
  }
  .rcb_router_link{
    font-size: 16px;
    color: white;
    text-decoration: none;
    transition: color 0.5s;
  }
  .rcb_router_link:hover{
    color: gray;
  }
</style>
