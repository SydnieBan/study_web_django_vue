<template>
    <div id="button_page_box" class="button_page_box">
      <el-pagination class="el-pagination" background layout="prev, pager, next" :total="total" :page-size="page_size" :current-page="cur_page"  @current-change="onCurrentChange">
      </el-pagination>
    </div>
</template>

<script>
    export default {
      name: "ButtonPageBox",
      props:['current_page','total','page_size'],
      data(){
        return{
          cur_page:this.current_page
        }
      },
      methods:{
        onCurrentChange(val) {
          this.cur_page=val;
          this.$emit('click_page',{children_cur_page:this.cur_page})
        },
      },
    }
</script>

<style scoped>
  .button_page_box{
    /*width: 550px;*/
    margin: 0 auto;
    height: 120px;
    display: flex;
    justify-content: center;
    flex-direction: column;
  }
  .el-pagination{
    margin: 0 auto;
  }
</style>
