<template>
  <div class="contain">
<!--    <Header  v-if="centerDialogVisible" v-on:back="get" v-model="information" @change_img_url="change_img_url"></Header>-->
    <Header  v-if="centerDialogVisible" v-on:back="get" v-model="information"></Header>
    <Form :information="information" :user_id="user_id" v-if="dialog" v-on:response="request" v-on:gain="achive" @reflesh="onReflesh"></Form>
    <div class="personal_top">
    <h3 class="title">个人资料</h3>
    </div>
    <div class="split"></div>
    <div class="bottom">
        <div class="header"  @click="change">
            <div class="image">
              <img :src="information.user_img" alt="not found " style="width: 100px;height: 100px; border-radius: 50px">
            </div>
            <p class="modify">修改头像</p>
        </div>
        <div class="bottom_right">
            <div class="right_peak">
              <div class="integral">
                <p>积分</p>
                <p class="strong">{{integral}}</p>
              </div>
              <div class="note">
                <p>笔记数量</p>
                <p class="strong">{{note_number}}</p>
              </div>
              <div class="learn">
                <p>学习时长</p>
                <p class="strong">{{study_time}}</p>
              </div>
            </div>
            <div class="split"></div>
            <div class="right_bottom">
              <span class="mod" @click="transform">修改资料</span>
              <ul class="self">
                <li class="common">昵称:{{information.user_name}}</li>
                <li class="common">性别:{{information.user_sex__name}}</li>
                <li class="common">身份:{{information.identity}}</li>
                <li class="common">地址:{{information.address}}</li>
                <li class="common">简介:{{information.introduce}}</li>
              </ul>
            </div>
        </div>
    </div>
  </div>

</template>
<script>
  import Header from './DialogHeader'
  import Form from './DialogForm'

  export default {
    name:'profile',
    inject:['reload'],
    data() {
      return {
        centerDialogVisible:false,
        dialog:false,
        information:{user_img:this.Global.default_img, user_name:null,user_sex__name:null,identity:null,address:null,introduce:null},
        user_id: null,
        integral:null,
        note_number:null,
        study_time:null,
      };
    },
    components:{Header,Form,},
    created:function(){
      this.user_id = window.localStorage.getItem('user_id');
      this.get_information();
      this.get_integral();
      this.get_note_number();
      this.get_study_time();
    },
    methods: {
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
      /* 获取积分数 */
      get_integral:function(){
        let url=this.Global.server_url+'/user/get_user_integral/';
        this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id},
          res=>{ this.integral = res['integral_sum'] }
        )
      },
      /* 获取积分数 END */
      /* 获取用户笔记数量信息 */
      get_note_number:function(){
        let url=this.Global.server_url+'/note/get_note_number/';
        this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id},
          // res=>{ this.show_note_number(this.note_number, res) }
          res=>{ this.note_number = res['note_num'] }
        )
      },
      /* 获取用户的笔记数量信息 END */
      /* 学习时长 */
      get_study_time:function(){
        let url=this.Global.server_url+'/user_course/study_time/';
        this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id},
          res=>{ this.study_time = res['stu_time'] }
        )
      },
      /* 学习时长 END */

      change:function (){
        this.centerDialogVisible=true
      },
      transform:function () {
        this.dialog=true
      },
      achive:function(data){
        this.dialog=data;
      },
      request:function (data) {
        this.dialog=data;
        this.reload();
      },
      get:function (data) {
        this.centerDialogVisible=data;

      },

      //由子组件传给父组件，图片的地址
      // change_img_url:function (res) {
      //   this.information[0].user_img = res;
      // }
      // 由子组件传给父组件，图片的地址 END

      /* 刷新 */
      onReflesh:function () {
        this.reload();
      }
      /* 刷新 EMD */
    }
  }
</script>



<style scoped>
  .split{
    width: 96%;
    height: 1px;
    margin: auto;
    background: gray;
  }
  .strong{
    font-weight:700;
    font-size: 18px;
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
  .contain .personal_top .title{
    padding-left: 20px;
  }
  .contain .bottom{
    width: 980px;
    height:335px ;
    margin: auto;
    display: flex;
  }
  .contain .bottom .header{
    width: 100px;
    height: 144px;
    cursor: pointer;
  }
  .contain .bottom .header .image{
    width: 100px;
    height: 100px;
    margin: 16px auto 0 auto;
    border-radius: 50px;
    background: #0000e7;
  }
  .contain .bottom .header .modify{
    text-align: center;
    margin-top: 8px;
    font-size: 14px;
    color: #3399ea;
  }
  .contain .bottom .bottom_right{
    width: 840px;
    height: 335px;
    margin-left: 40px;
  }
  .contain .bottom .bottom_right .split{
    width: 100%;
    height: 1px;
    margin: auto;
    background: gray;
  }
  .contain .bottom .bottom_right .right_peak{
    width: 840px;
    height: 85px;
    display: flex;
  }
  .contain .bottom .bottom_right .right_bottom{
    width: 840px;
    height:200px;
    margin: 16px auto;
  }
  .right_bottom .mod{
    margin-top: 4px;
    float: right;
    font-size: 14px;
    color: #3399ea;
    cursor: pointer;
  }
  .right_bottom .self{
    width: 500px;
    height: 180px;
  }
  .right_bottom .self .common{
    list-style: none;
    margin-left: -40px;
    padding: 0;
    height: 40px;
    line-height: 40px;
    font-size: 14px;
    color: #4d4d4d;
  }
  .integral{
    width: 100px;
    height: 85px;
    text-align: center;
  }
  .note{
    width: 100px;
    height: 85px;
    text-align: center;
  }
  .learn{
    width: 100px;
    height: 85px;
    text-align: center;
  }
</style>
