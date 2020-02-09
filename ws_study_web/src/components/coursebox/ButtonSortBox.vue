<template>
    <div id="button_sort_box" class="button_sort_box">
      <input type="button" v-for="(tag,index) in sort_tags" :class="{sort_btn:!(sort_btn_index===index),sort_btn_on:sort_btn_index===index}" :value="tag" @click="onChangeSort(index)">
    </div>
</template>

<script>
    export default {
        name: "ButtonSortBox",
      data(){
          return{
            sort_btn_index:0,
            sort_tags:['最新','按选课量','按收藏量']
          }
      },
      methods:{
          onChangeSort:function (index) {
            this.sort_btn_index=index;
            this.$emit('change_sort',{sort:this.sort_btn_index});
          }
      }
    }
</script>

<style scoped>
  div,input{
    margin: 0;
    padding: 0;
    border: none;
  }
  .button_sort_box{
    width: 1215px;
    margin: 0 auto;
    height: 60px;
    line-height: 60px;
  }
  .sort_btn{
    font-size: 14px;
    height: 30px;
    width: 80px;
    border-radius: 20%;
    line-height: 30px;
    margin-right: 10px;
    background: none;
    transition: background-color 0.5s;
    outline: none;
  }
  .sort_btn_on{
    background-color: gray;
    font-size: 14px;
    height: 30px;
    width: 80px;
    border-radius: 20%;
    line-height: 30px;
    margin-right: 10px;
    transition: background-color 0.5s;
    outline: none;
  }
  .sort_btn:hover{
    cursor: pointer;
    background-color: #bebebe;
  }
</style>
