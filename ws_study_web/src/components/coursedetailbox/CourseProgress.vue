<template>
    <div id="course_progress" class="course_progress">
      <div class="div_progress">
        <h2 style="font-size: 18px" v-if="!is_sc">未选择该门课程</h2>
        <h2 style="font-size: 18px" v-if="is_sc">已学</h2>
        <el-progress :text-inside="true" :stroke-width="26" :percentage="progress" v-if="is_sc"></el-progress>
      </div>
      <div class="div_notice">
        <h3 style="font-size: 18px">课程须知</h3>
        <p style="font-size: 14px;color: gray">{{notice}}</p>
      </div>
    </div>
</template>

<script>
    export default {
        name: "CourseProgress",
      props:['course_id','notice','is_sc'],
      data(){
          return{
            user_id:window.localStorage.getItem('user_id'),
            progress:0,
          }
      },
      created:function () {
        this.get_progress();
      },
      methods:{
          /* 获取学习进度 */
        get_progress:function () {
          let url = this.Global.server_url + '/user_course/study_progress/';
          this.GlobalFunc.func_axios(url,'GET',{"course_id":this.course_id,"user_id":this.user_id},
            res =>{ this.progress = res.stu_pro }
          )
        }
          /* 获取学习进度 END　*/
      }
    }
</script>

<style scoped>
  div,h2,h3,p{
    margin: 0;
    padding: 0;
    border: none;
  }
  .course_progress{
    background-color: #ffffff;
    padding: 20px 20px;
    border-radius: 10px;
  }
  .course_progress h2,h3{
    margin-bottom: 10px;
  }
  .div_notice{
    margin-top: 20px;
  }
</style>
