<template>
  <div class="header_box2">
    <el-row class="el-row-demo" type="flex" justify="space-between">

      <el-col :span="14">
        <header-box-left2 :course_id="course_id" :title="title"></header-box-left2>
      </el-col>
      <el-col :span="10" style="display: flex;justify-content: flex-end">
        <header-box-right @reflesh="onReflesh"></header-box-right>
      </el-col>

    </el-row>
  </div>
</template>

<script>

    import HeaderBoxRight from "./headerbox/HeaderBoxRight";
    import HeaderBoxLeft2 from "./headerbox/HeaderBoxLeft2";
    export default {
        name: "HeaderBox2",
      props:['course_id','title'],
      components: {HeaderBoxLeft2, HeaderBoxRight, },
      methods:{
        /* 页面退出刷新 */
        onReflesh:function () {
          this.$emit('reflesh')
        }
        /* 页面退出刷新 END */
      }
    }
</script>

<style scoped>
  *{
    margin: 0;
    padding: 0;
    border: none;
  }
  .header_box2{
    width: 100%;
    min-width: 1251px;
    margin: 0 auto;
    /*background-color: lightskyblue;*/
    background-color: black;
  }
  .el-row-demo{
    width: 1251px;
    margin: 0 auto;
  }
</style>
