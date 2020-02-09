<template>
    <div id="header_box_right" class="header_box_right">
      <div class="search">
        <input placeholder="请输入内容" class="search_text" type="text" v-model="content"  @keydown="onKeySearch($event)">
        <button class="search_btn" @click="onSearch">搜索</button>
      </div>
      <header-box-right-login-yes v-if='login_state' @reflesh="onReflesh"></header-box-right-login-yes>
      <header-box-right-login-no v-else></header-box-right-login-no>
    </div>
</template>

<script>
    import Bus from '../../../Bus'
    import HeaderBoxRightLoginNo from "./HeaderBoxRightLoginNo";
    import HeaderBoxRightLoginYes from "./HeaderBoxRightLoginYes";
    export default {
        name: "HeaderBoxRight",
      data(){
        return{
          login_state:false,
          content:''
        }
      },
      components: {HeaderBoxRightLoginYes, HeaderBoxRightLoginNo},
      mounted:function() {
          if (window.localStorage.getItem('islogin')){
            this.login_state=true;
          }
          Bus.$on('login_state_change',(data)=>{
            this.login_state=data;

          })
      },
      methods:{
        onSearch:function () {
          if (this.content && this.content.trim()!==''){
            this.$router.push({ path: '/search', query: { q: this.content.trim()} }).catch(err => { console.log(err) })
          }else{
            this.content='';
          }
        },
        onKeySearch:function (ev) {
          if (ev.keyCode===13){
            this.onSearch();
          }
        },
        /* 页面退出刷新 */
        onReflesh:function () {
          this.$emit('reflesh')
        }
        /* 页面退出刷新 END */
      },
      watch:{
        '$route'(to,from){
          if (this.content) this.content='';
        }
      }

    }
</script>

<style scoped>
  div,span,input,button{
    margin: 0;
    padding: 0;
    border: none;
  }
  .router_link{
    margin: 0;
    padding: 0;
    text-decoration: none;
    color: white;
    line-height: 30px
  }
  .header_box_right{
    width: 425px;
    height: 40px;
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
  }
  .header_box_right .search{
    width: 300px;
    height: 40px;
    padding: 5px 0;
    box-sizing: border-box;
    display: flex;
    justify-content: flex-start;
  }
  .header_box_right .search .search_text{
    width: 250px;
    height: 30px;
    outline: none;
    box-sizing: border-box;
    padding-left: 5px;
  }
  .header_box_right .search .search_btn{
    width: 50px;
    height: 30px;
    color: white;
    transition: color 0.5s;
    outline: none;
  }
  .header_box_right .search .search_btn:hover{
    cursor: pointer;
    color: gray;
  }


</style>
