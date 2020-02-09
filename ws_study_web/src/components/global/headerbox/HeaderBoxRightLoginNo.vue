<template>
    <div id="header_box_right_login_no" class="header_box_right_login_no">
      <span><router-link class="router_link" to="/login">登录 | 注册</router-link></span>
    </div>
</template>

<script>
    export default {
        name: "HeaderBoxRightLoginNo"
    }
</script>

<style scoped>
  .router_link{
    margin: 0;
    padding: 0;
    text-decoration: none;
    color: white;
    line-height: 30px
  }
  .header_box_right_login_no {
    width: 100px;
    height: 40px;
    padding: 5px 0;
    box-sizing: border-box;
    text-align: center;
  }
</style>
