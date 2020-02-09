<template>
    <el-container class="home_course_list_box" style="background-color: #E1E1E1 ">
      <el-aside style="overflow-y: hidden;width:277px">
        <img :src="flag.left_img" alt="" class="img-css">
      </el-aside>
      <el-main class="el-main" style="overflow-y: hidden;overflow-x:hidden;">
        <div class="course" v-for="item in flag.data_info" :key="item.course_id" @click="onShowCourseDetails(item.course_id)">
          <div><img :src="item.course_img" alt="" style="width: 100%;height:160px "></div>
          <div class="text-css">
            <div class="fi">{{item.course_name}}</div>
            <div class="fir">{{item.course_price}}</div>
          </div>
        </div>
      </el-main>
    </el-container>
</template>
<script>
    export default {
      name: "HomeCourseListBox",
      props:['flag'],
      data() {
        return {
        }
      },
      methods:{
        onShowCourseDetails:function (id) {
          this.$router.push({ path: 'course_detail', query: { course_id: id} })
        }
      },
    }

</script>

<style scoped>
  div,h1{
    margin: 0;
    padding: 0;
    border: none;
  }
  .home_course_list_box{
    width: 1215px;
    margin: 0 auto;
    height: 450px;
    background-color: white;
  }
  .el-main{
    padding: 0 0 0 5px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .img-css{
    height: 450px;
    width: 267.38px
  }
  .img-css:hover{
    transform: translate(0px,-2px);
    box-shadow: 0px 0px 5px;
    cursor: pointer;
  }
  .course{
    height: 215px;
    width:200px;
    margin-bottom: 20px;
    background: white;
  }
  .course:hover{
    transform: translate(0px,-2px);
    box-shadow: 0px 0px 5px;
    cursor: pointer;
  }
  .text-css{
    text-align: left;
    margin-left: 5px;
  }
  .fi{
    width: 195px;
    height: 20px;
    display: -webkit-box;
    -webkit-box-orient: vertical ;
    overflow: hidden;
    -webkit-line-clamp:1;
  }
  .fir{
    margin-top: 5px;
    font-size: 12px;
    color: gray;
  }

/********************element****************************/
  .bg-purple {
    background: white;
  }
  .grid-content {
    min-height: 215px;
  }
  .grid-content:hover{
    transform: translate(0px,-2px);
    box-shadow: 0px 0px 5px;
  }

/********************element****************************/
</style>
