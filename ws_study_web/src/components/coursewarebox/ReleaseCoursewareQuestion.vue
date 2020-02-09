<template>
  <el-card class="box-card" shadow="hover" :key="param.p_courseware_id">
    <div slot="header" class="clearfix">
      <span>发布问题</span>
      <el-button class="btn-close" icon="el-icon-close" @click="close_que"></el-button>
    </div>
    <textarea name="" id="" class="textarea-css" v-model="content"></textarea>
    <el-button type="primary" round class="btn-submit" @click="sub_question">发布</el-button>
  </el-card>
</template>

<script>
    export default {
        name: "ReleaseCoursewareQuestion",
        props:["param"],
      data(){
          return{
            content:''
          }
      },
      methods:{
        sub_question:function () {
          console.log(this.content);
          let data={
            content:this.content,
            user_id:this.param.p_user_id,
            courseware_id:this.param.p_courseware_id,
          }
          this.onSendCourseQuestion(data)
        },
        onSendCourseQuestion:function (data) {
          let url = this.Global.server_url + '/user_course/insert_question_courseware/';

          this.GlobalFunc.func_axios(url,'GET',data ,
            res=>{ this.show_data(res) }
          )
        },
        show_data:function (res) {
          if (res.result == 'insert success') {
            let data = false;
            this.$emit('close_question',data)
          }else {
            console.log('Error');
          }
        },
        //关闭发布组件
        close_que:function () {
          let data = false;
          this.$emit('close_question',data)
        }
      }
    }
</script>

<style scoped>
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
  .btn-close{
    float: right;
    padding: 3px 0;
    outline: none;
    border: none
  }
  .textarea-css{
    width:100%;
    height: 300px;
    font-size: 18px;
  }
  .btn-submit{
    float: right;
    margin: 5px 0;
  }
</style>
