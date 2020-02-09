<template>
    <div id="course_detail" class="course_detail">

      <course-info :course_id="course_id" :is_sc="is_sc" @bus_info="func_get_course_info($event)" @select_tag="func_select_tag($event)"></course-info>

      <el-row class="el-row">
        <!-- 课程章节列表 -->
        <el-col class="el-col" :span="17">
          <course-detail-list :course_id="course_id" :user_id="user_id" :is_sc="is_sc" :introduce="introduce" :list_tag_index="tag_index" ref="course_detail_list"></course-detail-list>
        </el-col>
        <!-- 课程章节列表 END -->
        <!-- 学习进度 和 推荐课程 -->
        <el-col class="el-col" :span="7">
          <course-progress :course_id="course_id" :notice="notice" :is_sc="is_sc"></course-progress>
          <recommend-course :course_id="course_id"></recommend-course>
        </el-col>
        <!-- 学习进度 和 推荐课程 END -->

      </el-row>

    </div>
</template>

<script>
  import CourseInfo from "./coursedetailbox/CourseInfo";
  import CourseDetailList from "./coursedetailbox/CourseDetailList"
  import CourseProgress from "./coursedetailbox/CourseProgress";
  import RecommendCourse from "./coursedetailbox/RecommendCourse";
    export default {
        name: "CourseDetail",
      data(){
          return{
            course_id:this.$route.query.course_id,
            user_id:window.localStorage.getItem('user_id'),
            is_sc:false, /* 是否选课 */
            introduce:'',
            notice:'',
            tag_index:0,
          }
      },
      components:{CourseDetailList, RecommendCourse, CourseProgress, CourseInfo,},
      created:function(){
          this.judge_is_sc();
      },
      methods:{
        /* 判断是否选课 */
        judge_is_sc:function () {
          if (this.user_id){
            let url = this.Global.server_url + '/user_course/is_sc/';
            this.GlobalFunc.func_axios(url, 'GET', {user_id:this.user_id,course_id:this.course_id},
              res=>{
                if (res.result){
                  this.is_sc = true
                } else{
                  this.is_sc = false
                }
              }
            )
          }
        },
        /* 判断是否选课 END */

        /* 子组件向父组件传课程基本信息 */
        func_get_course_info:function (ev) {
          this.introduce = ev.introduce;
          this.notice = ev.notice;
        },
        /* 子组件向父组件传课程基本信息 END */

        /* 子组件单击课程/课件/评论标签时，触发父组件的该函数 */
        func_select_tag:function (ev) {
          this.tag_index = ev.info_tag_index;
        }
        /* 子组件单击课程/课件/评论标签时，触发父组件的该函数 END */

      }
    }
</script>

<style scoped>
  div,.el-row,.el-col{
    margin: 0;
    padding: 0;
    border: none;
  }
  .course_detail{
    width: 100%;
    min-width: 1215px;
    background-color: #eceef0;
    padding-bottom: 200px;
  }
  .el-row{
    width: 1215px;
    margin: 0 auto;
    margin-top: 30px;
  }
</style>
