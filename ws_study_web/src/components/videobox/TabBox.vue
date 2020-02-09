<template>
    <div id="tab_box" class="tab_box">

      <el-tabs v-model="activeName">
        <el-tab-pane label="问答" name="first"></el-tab-pane>
        <el-tab-pane label="评论" name="second"></el-tab-pane>
      </el-tabs>

    </div>
</template>

<script>
    export default {
        name: "TabBox",
      data(){
          return{
            activeName:'first'
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
  .tab_box{
    width: 1251px;
    margin: 0 auto;
    /*background-color: #ffffff;*/
    height: 50px;
    padding: 20px 20px;
  }
</style>
