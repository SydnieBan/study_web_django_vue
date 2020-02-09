<template>
  <div class="panel" v-if="is_question">
    <div class="center">
      <div class="close_all" @click="onClose">
        <icon name="modal_error" class="close_icon"></icon>
      </div>
      <h3>我要问答：</h3>
      <div class="content">
        <textarea name="content_eva" v-model="question_content"></textarea>
      </div>
      <div class="btn_submit">
        <input type="button" value="发布内容"  class="btn_sub" @click="onSubmit">
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "ModalPanel",
      props:['is_question'],
      data(){
        return{
          question_content:'',
        }
      },
      methods:{
        onClose:function () {
          this.$emit('close_modal',{is_question:false})
        },
        onSubmit:function () {
          this.$emit('submit_modal',{question_content:this.question_content})
        }
      }
    }
</script>

<style scoped>
  div,p,h3,input{
    margin: 0;
    padding: 0;
    border: none;
  }
  .panel{
    width: 100%;
    height: 100%;
    position: fixed;
    background: rgba(0,0,0,.5);
    top: 0;
    left: 0;
    z-index: 1000;
  }
  .panel .center{
    width: 600px;
    height: 280px;
    background-color: whitesmoke;
    position: fixed;
    top:50%;
    left:50%;
    margin:-200px 0 0 -310px;
    z-index: 1000;
    border-radius: 10px;
  }
  .panel .center .content{
    width: 530px;
    height: 150px;
    margin: 50px 30px 20px 30px;
    background: #cfcfcf;
    box-sizing: border-box;
  }
  .panel .center .content textarea{
    height: 150px;
    width: 530px;
    outline: none;
    border: 1px solid #e1e1e1;
  }
  .panel .center .btn_submit{
    width: 530px;
    height: 40px;
    margin: auto;
  }
  .panel .center .btn_submit .btn_sub{
    width:100px;
    height: 40px;
    padding: 10px;
    box-sizing: border-box;
    /*background: #7ef2ff;*/
    background: #95c0ff;
    outline: black;

    /*border: none;*/
    border-radius: 5px;
    color: white;
    float: right;
    cursor: pointer;
  }
  .panel .center .close_all{
    position: absolute;
    top:20px;
    right:30px;
    width:15px;
    height:15px;
    font-size:15px;
    cursor: pointer;
  }
  .panel .center .close_all .close_icon{
    width: 20px;
    height: 20px;
  }
  .panel .center h3{
    position: absolute;
    top: 20px;
    left: 30px;
  }
</style>
