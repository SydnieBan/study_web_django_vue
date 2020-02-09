<template>
  <div id="header_box_left" class="header_box_left">
    <div class="div-logo" v-on:click="$router.push({path:'/'})">
      <span class="logo_t">Study Web</span>
    </div>
    <div class="nav" style="width: 400px;height: 40px;">
      <ul>
        <li v-for="tag in tags" @click="onClick"><router-link :to="'/'+tag.link" class="router_link">{{tag.name}}</router-link></li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "HeaderBoxLeft",
    data(){
      return{
        tags:[
          {name:'全部课程',link:'course_all'},
          {name:'精品课程',link:'course_unique'},
          {name:'免费课程',link:'course_free'},
          {name:'笔记专栏',link:'note'},
        ]
      }
    },
    methods:{
      onClick:function () {

      }
    }
  }
</script>

<style scoped>
  div,ul,li{
    margin: 0;
    padding: 0;
    border: none;
  }
  .header_box_left{
    width: 608px;
    height: 40px;
    display: flex;
    justify-content: space-between;
  }
  .header_box_left .div-logo{
    width: 200px;
    height: 30px;
    /*background-color:gray;margin: 5px 0;*/
  }
  .header_box_left .div-logo .logo_t{
    color: white;
    font: bolder 30px "Comic Sans MS";
    transition: color 0.5s;
    text-shadow: 0 10px 30px #8ea5fd,
    10px -5px 15px #657aff,
    20px -10px 40px #0e3eec,
    10px -10px 25px #0d0fcd,
    0 -5px 15px #1e2797,
    0 -5px 10px #191c45;
  }
  .header_box_left .div-logo .logo_t:hover{
    cursor: pointer;
    color: #bee8fa;
  }
  .header_box_left .nav ul{
    list-style: none;
    display: flex;
    justify-content: space-between;
  }
  .header_box_left .nav ul li{
    height: 40px;
    box-sizing: border-box;
  }
  .header_box_left .nav ul li .router_link{
    margin: 0;
    text-decoration: none;
    color: white;
    line-height: 40px;
    padding:10px 5px;
    height: 40px;
    font-size: 16px;
    box-sizing: border-box;
    transition: background-color 0.5s, color 0.5s;
  }
  .header_box_left .nav ul li .router_link:hover{
    color: gray;
  }

</style>
