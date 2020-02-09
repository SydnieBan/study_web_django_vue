<template>
    <div id="home_teacher_list_box" class="home_teacher_list_box">
      <div class="title">精品讲师</div>
      <div class="container">
        <div class="per_teacher" v-for="(item,index) in teacher_data" @mouseover="onMouseOverTea(index)" @mouseleave="onMouseLeaveTea" >

          <img :src="Global.img_url + '/images/'+ item.teacher_icon__icon_img" alt="" :class="{'img_style_01':!(index===teacher_index),'img_style':(index===teacher_index)}">
          <div :class="{'teacher_info':!(index===teacher_index),'teacher_info_change':(index===teacher_index)}">
            <h3>{{item.name}}</h3>
            <p>{{item.teacher_identity__identity}}</p>
          </div>
          <p class="text_info" style="float: right" v-if="index===teacher_index">&nbsp;&nbsp;&nbsp;&nbsp;{{item.introduce}}</p>
        </div>
      </div>
    </div>
</template>

<script>
    import Global from "../Global";

    export default {
        name: "HomeTeacherListBox",
      data(){
          return{
            teacher_data:[],
            teacher_index:11
          }
      },
      created:function () {
        this.get_teacher();
      },
      mounted:function(){
        // console.log(this.teacher_data)
      },
      methods:{
        onMouseOverTea:function (itt) {
          this.teacher_index = itt
        }  ,
        onMouseLeaveTea:function () {
          this.teacher_index = 11
        },
        /* 获取教师 */
        get_teacher:function(){
          let url = this.Global.server_url + '/user/get_teacher/';
          this.GlobalFunc.func_axios(url,'GET', null,
            res=>{ this.show_teacher(this.teacher_data, res) }
          );
        },
        /* 获取教师 END */
        /* 显示教师动画 */
        show_teacher:function(to_data, res){
          for (let item in res) {
            to_data.push(res[item])
          }
        },
        /* 显示教师动画 END */
      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
  .home_teacher_list_box{
    width: 1215px;
    margin: 0 auto;
    height: 550px;
    background-color: #eaeaea;
    margin-top: 30px;
  }
  .title{
    width: 1215px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    font-size: 20px;
  }
  .container{
    width: 1215px;
    height: 500px;
    text-align: center;
    display: flex;
    justify-content: start;
    flex-wrap: wrap;
  }
  .per_teacher{
    width:16.5%;
    height: 240px;
    background-color: white;
    position: relative;
    z-index: 1000;
    overflow: hidden;
    border-radius: 6px;
    margin-bottom: 20px;
    margin-right: 53.1px;
  }
  .per_teacher:nth-child(5n){
    margin-right: 0;
  }
  .per_teacher:hover{
    cursor: pointer;
  }
  .per_teacher .img_style_01{
    width: 100%;
    height: 240px;
    object-fit: cover;
    transition:  width 0.5s,height 0.5s;
  }
  .per_teacher .teacher_info{
    position: absolute;
    top: 280px;
    right: 10px;
    font-size: 15px;
    text-align: center;
    transition:  width 0.5s,height 0.5s,font-size 0.5s,top 0.5s,right 0.5s;
  }
  .per_teacher .img_style{
    width: 70px;
    height: 70px;
    border-radius: 50%;
    float: left;
    transition:  width 0.5s,height 0.5s;
    padding: 10px;
  }
  .per_teacher .teacher_info_change{
    position: absolute;
    top: 5px;
    right: 0;
    width: 114px;
    height: 56px;
    font-size: 12px;
    text-align: center;
    transition:  width 0.5s,height 0.5s,font-size 0.5s,top 0.5s,right 0.5s;
  }
  .per_teacher .text_info{
    display: block;
    font-size: 14px;
  }


</style>
