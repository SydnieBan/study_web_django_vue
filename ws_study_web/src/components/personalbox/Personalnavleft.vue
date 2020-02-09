<template>
    <ul class="list">
      <li v-for="(item,index) in list" :class="{bgColor:index==current}" @click="addClass(index,item.link_href)">
        {{item.link_text}}
      </li>
    </ul>
</template>
<script>
  export default {
    props:['current'],
    data() {
      return {
        list:[
          {"link_href":"/my/profile","link_text":'我的资料'},
          {"link_href":"/my/total","link_text":'我的课程'},
          {"link_href":"/my/collection","link_text":'收藏的课程'},
          {"link_href":"/my/continue","link_text":'未完成课程'},
          {"link_href":"/my/finish","link_text":'已结束课程'},
          {"link_href":"/my/account","link_text":'账户设置'},
        ],
        // current:0
      };
    },
    methods: {
      addClass:function (index,link) {
        this.$emit('onChangeCur',index);
        this.$router.push({path:link,query:{i:index}})
      }
    }
  }
</script>



<style scoped>
    .bgColor{
      background: rgba(51, 153, 234, 0.39);
    }
    ul{
      margin: 0;
      padding: 0;
    }
   ul li{
     height: 40px;
     width: 100%;
     line-height: 35px;
     font-size: 16px;
     padding-left: 16px;
     box-sizing: border-box;
     list-style-type:none;
     transition: color 0.5s;
  }
   ul li:hover:not([class="bgColor"]){
     cursor: pointer;
     color: lightskyblue;
   }
</style>
