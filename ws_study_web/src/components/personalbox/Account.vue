<template>
  <div class="contain">
    <div class="personal_top">
      <h3 class="title">账号设置</h3>
    </div>
    <div class="split"></div>
    <div class="change">
          <div class="change_left">
            <span>当前账号:{{information[1]}}</span>
          </div>
          <div class="change_right" @click="skip">
            <span>修改账号 | 修改密码</span>
          </div>
    </div>
    <div class="split"></div>
    <div class="change_email">
      <div class="change_left">
        <span>当前邮箱:{{information[2]}}</span>
      </div>
      <div class="change_right">
        <span>修改邮箱</span>
      </div>
    </div>
    <div class="split"></div>
    <div class="connection">
      <div class="word">绑定登录账号</div>
      <div class="icon_content">
        <div class="icon">
          <div class="qq">
            <icon name="qq" style="width: 50px;height: 50px"></icon>
          </div>
          <div class="we_chat">
            <icon name="微信" style="width: 50px;height: 50px"></icon>
          </div>
          <div class="wei_bo">
            <icon name="weibo" style="width: 50px;height: 50px"></icon>
          </div>
          <div class="github">
            <icon name="github" style="width: 50px;height: 50px"></icon>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: "account",
    data() {
      return {
        information: [], /* content user_name  user_icon__icon_img   user_sex__name  identity  address introduce */
        user_id: window.localStorage.getItem('user_id'),
      };
    },
    created() {
      this.get_user();
    },
    methods: {
      /* 获取用户信息 */
      get_user:function(){
        let url=this.Global.server_url+'/user/get_user/';
        this.GlobalFunc.func_axios(url, 'POST', {"user_id":this.user_id},
          res=>{ this.show_information(this.information, res)}
        )
      },
      /* 获取用户的所有信息 END */
      /* 显示用户的所有信息 */
      show_information:function (to_data, res) {
        for (let i in res){
          to_data.push(res[i])
        }
      },
      /* 显示用户的所有信息 END */
      skip:function () {
        this.$router.push('/login')
      }
    },
  }
</script>

<style scoped>
  .split{
    width: 96%;
    height: 1px;
    margin: auto;
    background: gray;
  }
  .contain{
    width: 1020px;
    height: 520px;
    overflow: hidden;

  }
  .contain .personal_top{
    height: 100px;
    line-height: 50px;
    overflow: hidden;
  }
  /**********修改密码账号*******************/
  .contain .change{
    width: 100%;
    height: 120px;
    display: flex;
    justify-content: space-between;
  }
  .change_left{
    width: 500px;
    height: 120px;
    line-height: 120px;
    padding-left: 20px;
  }
  .change_right{
    width: 500px;
    height: 120px;
    padding-right: 20px;
    text-align: right;
    line-height: 120px;
  }
  .change_right span{
    cursor: pointer;
    color: #3399ea;;
  }
  /**********修改邮箱*******************/
  .contain .change_email{
    width: 100%;
    height: 120px;
    display: flex;
    justify-content: space-between;
  }
  .change_email .change_right{
    padding-right: 60px;
  }
  /**********第三方链接*******************/
  .contain .connection{
    width: 100%;
    height: 120px;
  }
  .contain .connection .word{
    padding-left: 20px;
  }
  .contain .connection .icon_content{
    margin-top: 20px;
    display: flex;
    justify-content: center;
  }
  .icon_content .icon{
    width: 400px;
    display: flex;
    justify-content: space-between;
  }
  .icon_content .icon>div{
    cursor: pointer;
  }
  .contain .personal_top .title{
    padding-left: 20px;
  }
</style>
