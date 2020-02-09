import Vue from 'vue'

export default new Vue()

/*
* 导航条
* import Bus
* mouted:function(){
* if(window.localStorage.islogin){
*   this.loginstate=true
* }
*  Bus.$on('login_state_change',(data)=>{
*   this.loginstate=data
* })
* }
*
* 登录
* import Bus
  mounted:function() {
        if (window.localStorage.getItem('islogin')){
          this.login_state=true;
        }
        Bus.$on('login_state_change',(data)=>{
          this.login_state=data;
        })
    }
* */
