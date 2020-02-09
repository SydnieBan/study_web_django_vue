<template>
    <div id="header_box_right_login_yes" class="header_box_right_login_yes">
      <el-dropdown @command="handleCommand">
        <span>
          <router-link class="router_link" :to="{path:'/my/profile'}">
            <img :src="user_icon" alt="" style="width: 34px;height: 34px;border-radius: 50%;">
          </router-link>
        </span>
        <el-dropdown-menu class="el-dropdown-menu" slot="dropdown">
          <el-dropdown-item class="el-dropdown-menu__item" command="my_setting">个人设置</el-dropdown-item>
          <el-dropdown-item class="el-dropdown-menu__item" command="sign_out">退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
</template>

<script>
    export default {
        name: "HeaderBoxRightLoginYes",
      /* 刷新事件 */
      inject:['reload'],
      /* 刷新事件 END */
      data(){
          return{
            user_id:null,
            user_icon:this.Global.default_img
          }
      },
      created:function () {
        this.user_id = window.localStorage.getItem('user_id');
        this.get_user_info()
      },
      methods:{
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
          // this.user_icon = this.Global.img_url + '/images/' + res[0].user_icon__icon_img
          this.user_icon = this.Global.img_url + '/' + res[0].user_icon__icon_img // 七牛云
        },
        /* 显示用户信息 END */

        /* 下拉菜单事件 */
        handleCommand:function (command) {
          if (command==='my_setting') {
            this.$router.push({path:'/my/account',query:{i:5}})
          }
          else if (command==='sign_out') {
            if (window.localStorage.getItem('is_remember')) {
              window.localStorage.removeItem('islogin');
              window.localStorage.removeItem('token');
              window.localStorage.removeItem('user_id');
            }
            else{
              window.localStorage.clear();
            }
            /* 刷新事件 */
            this.reflesh();
            /* 刷新事件 END */
          }
        },
        /* 下拉菜单事件 END */

        /* 刷新事件 */
        reflesh:function(){
          this.reload();
          this.$emit('reflesh')
        }
        /* 刷新事件 END */

      }
    }
</script>

<style scoped>
  div,img{
    margin: 0;
    padding: 0;
    border: none;
  }
  .router_link{
    margin: 0;
    padding: 0;
    text-decoration: none;
    color: white;
    line-height: 40px
  }
  .header_box_right_login_yes {
    /*width: 100px;*/
    height: 40px;
    padding: 3px 0;
    box-sizing: border-box;
    text-align: center;
  }
  .el-dropdown-menu{
    margin: 0;
  }
  .el-dropdown-menu .el-dropdown-menu__item{
    transition: background-color 0.5s,color 0.5s
  }
</style>
