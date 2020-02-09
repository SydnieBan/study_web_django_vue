<template>
    <div id="video" class="video">
      <div class="video_inner">
<!--      <div class="video_inner" :style="{'background-color':color}">-->
<!--        <el-color-picker v-model="color"></el-color-picker>-->

        <larkplayer :course_id="course_id" :video_id="video_id"></larkplayer>
        <tab-box></tab-box>

        <el-row>
          <el-col :span="18">
            <question-list :video_id="video_id" :type="'video'"></question-list>
          </el-col>
          <el-col :span="6">
            <recommend-course :course_id="course_id"></recommend-course>
          </el-col>
        </el-row>



      </div>
    </div>
</template>

<script>
    import RecommendCourse from "./coursedetailbox/RecommendCourse";
    import Larkplayer from "./videobox/Larkplayer";
    import TabBox from "./videobox/TabBox";
    import QuestionList from "./videobox/QuestionList";
    export default {
        name: "Video",
      data(){
          return{
            course_id:this.$route.query.course_id,
            video_id:this.$route.query.video_id
          }
      },
      components: {QuestionList, TabBox, Larkplayer, RecommendCourse}
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
  .video{
    width: 100%;
    min-width: 1251px;
    background-color: #f3f5f7;
  }
  .video .video_inner{
    width: 1251px;
    margin: 0 auto;
  }
</style>
