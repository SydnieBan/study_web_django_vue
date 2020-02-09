<template>
  <div id="header_box_left2" class="header_box_left2" style="display: flex;justify-content: flex-start">

    <el-page-header class="el-page-header" @back="goBack"></el-page-header>
    <span class="span_css">{{ title }}</span>

  </div>
</template>

<script>
    export default {
        name: "HeaderBoxLeft2",
      props:['course_id','title'],
      methods:{
          goBack:function () {
            this.$router.push({path:'/course_detail',query:{course_id:this.course_id}})
          }
      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
  .header_box_left2{
    width: 625px;
    height: 40px;
  }
  .header_box_left2 .el-page-header{
    color: white;
    height: 40px;
    line-height: 40px;
    transition: opacity 0.5s;
  }
  .span_css{
    line-height: 40px;
    color: white;
  }
</style>
