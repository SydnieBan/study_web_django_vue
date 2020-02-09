<template>

  <div id="nav_fixed" class="nav_fixed">
    <!-- 签到 -->
    <div class="div_sign_in" @click="onSignIn" v-if="!is_sign_in">
      <span>签<br/>到</span>
    </div>
    <div class="div_sign_in2" v-if="is_sign_in">
      <span>已<br/>签<br/>到</span>
    </div>
    <!-- 签到 END -->
    <!-- 返回顶部 -->
    <div class="div_top" @mouseover="isOver=true" @mouseleave="isOver=false">
      <el-backtop :bottom="10" :right="5" class="el-backtop">
        <div class="el_backtop_inner el-icon-arrow-up" v-show="!isOver"></div>
        <div class="el_backtop_inner2" v-show="isOver"><span>返回<br/>顶部</span></div>
      </el-backtop>
    </div>
    <!-- 返回顶部 END -->
  </div>

</template>
<script>
    export default {
        name: "NavFixed",
      inject:['reload'],
      data(){
          return{
            is_sign_in:false,
            isOver:false,
          }
      },
      created:function(){
          this.judge_SignIn();
      },
      methods:{

          /* 判断用户是否已经签到 */
        judge_SignIn:function(){
          let user_id = window.localStorage.getItem('user_id');
          if(user_id){
            let url = this.Global.server_url+'/user/is_checkin/';
            this.GlobalFunc.func_axios(url, 'GET', {user_id:user_id},
              res=>{
                if (res.result){
                  this.is_sign_in = true
                } else{
                  this.is_sign_in = false
                }
              }
            )
            // this.is_sign_in=true;
          } else{
            this.is_sign_in=false;
          }
        },
        /* 判断用户是否已经签到 END */
          /* 签到 */
        onSignIn:function () {
          let user_id = window.localStorage.getItem('user_id');
          /* 判断是否登录 */
          if (user_id){
            // alert('登录') 此时说明已登录但未签到
            let url = this.Global.server_url +'/user/insert_checkin/';
            this.GlobalFunc.func_axios(url,'GET',{user_id:user_id},
              res=>{
                if (res.result==='insert success'){
                  this.open_sign_in();
                  this.reload();
                } else{
                  this.open_sign_in_error();
                }
              }
            )
          } else{
            // alert('未登录')
            this.GlobalFunc.open_login(this);
          }
        },
        /* 签到 END */
        /* 签到成功提示框 */
        open_sign_in() {
          this.$alert('签到成功', '提示', {
            confirmButtonText: '确定',
          });
        },
        /* 签到成功提示框 END */
        /* 签到失败提示框 */
        open_sign_in_error() {
          this.$alert('签到失败', '提示', {
            confirmButtonText: '确定',
          });
        },
        /* 签到失败提示框 END */

      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
  }
  .nav_fixed{
    position: fixed;
    right: 5px;
    bottom: 10px;
    height: 160px;
    width: 40px;
  }
  /* 签到 */
  .nav_fixed .div_sign_in{
    width: 40px;
    height: 85px;
    background-color: rgba(135, 183, 237, 0.65);
    font-size: 17px;
    text-align: center;
    color: white;
    padding: 20px 10px;
    box-sizing: border-box;
  }
  .nav_fixed .div_sign_in:hover{
    cursor: pointer;
  }
  .nav_fixed .div_sign_in2{
    width: 40px;
    height: 85px;
    background-color: rgba(135, 183, 237, 0.65);
    font-size: 17px;
    text-align: center;
    color: white;
    padding: 10px;
    box-sizing: border-box;
  }
  /* 签到 END */
  /* 返回顶部 */
  .nav_fixed .div_top{
    width: 40px;
    height: 75px;
  }
  .nav_fixed .div_top .el-backtop{
    width: 40px;
    height: 75px;
    border-radius: 0;
    background-color: rgba(135, 183, 237, 0.65);
    color: white;
    text-align: center;
  }
  .nav_fixed .div_top .el-backtop .el_backtop_inner{
    width: 25px;
    height: 25px;
    border-radius: 50%;
    border: 2px solid white;
    line-height: 22px;
  }
  .nav_fixed .div_top .el-backtop .el_backtop_inner2{
    font-size: 17px;
    padding:15px 0;
    box-sizing: border-box;
  }
  /* 返回顶部 END */
</style>
