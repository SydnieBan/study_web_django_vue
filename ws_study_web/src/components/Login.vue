<template>
    <div class="panel">
      <div class="to_home">
        <span class="to_home_t" @click="onToHome">Study Web</span>
      </div>
      <div class="center">
        <user-login v-if="1==i"></user-login>
        <user-register v-if="2==i"></user-register>
        <user-retrieve-password v-if="3==i"></user-retrieve-password>
        <!--         选项 -->
        <div class="show_select">
          <span><a href="javascript:void 0" class="btn_style" @click="i=1" >登录</a></span>
          <span style="color: gainsboro">|</span>
          <span><a href="javascript:void 0" class="btn_style" @click="i=2">去注册</a></span>
          <span style="color: gainsboro">|</span>
          <span><a href="javascript:void 0" class="btn_style" @click="i=3" >忘记密码</a></span>
        </div>
      </div>
    </div>
</template>

<script>
  import UserLogin from './loginbox/UserLogin'
  import UserRegister from './loginbox/UserRegister'
  import UserRetrievePassword from './loginbox/UserRetrievePassword'
    export default {
        name: "Login",
      data(){
          return{
            i:1,
          }
      },
      created:function(){
        // this.bg();
      },
      methods:{
        onToHome:function () {
          this.$router.push({path:'/'})
        },

        /* =============================================================== */
        bg:function () {
          document.body.style="background-image: url(\"http://img.zcool.cn/community/01a3f4589ea315a801219c77c63f72.jpg@1280w_1l_2o_100sh.jpg\");background-repeat: no-repeat;width:100%;height:100%;background-size: cover;top:0;left:0;";
          function n(n, e, t) {
            return n.getAttribute(e) || t
          }

          function e(n) {
            return document.getElementsByTagName(n)
          }

          function t() {
            var t = e("script"), o = t.length, i = t[o - 1];
            return {l: o, z: n(i, "zIndex", -1), o: n(i, "opacity", .5), c: n(i, "background-color", "white"), n: n(i, "count", 50)}
          }

          function o() {
            a = m.width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth, c = m.height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
          }

          function i() {
            r.clearRect(0, 0, a, c);
            var n, e, t, o, m, l;
            s.forEach(function (i, x) {
              for (i.x += i.xa, i.y += i.ya, i.xa *= i.x > a || i.x < 0 ? -1 : 1, i.ya *= i.y > c || i.y < 0 ? -1 : 1, r.fillRect(i.x - .5, i.y - .5, 1, 1), e = x + 1; e < u.length; e++) n = u[e], null !== n.x && null !== n.y && (o = i.x - n.x, m = i.y - n.y, l = o * o + m * m, l < n.max && (n === y && l >= n.max / 2 && (i.x -= .03 * o, i.y -= .03 * m), t = (n.max - l) / n.max, r.beginPath(), r.lineWidth = t, r.strokeStyle = "rgba(" + d.c + "," + (t + .2) + ")", r.moveTo(i.x, i.y), r.lineTo(n.x, n.y), r.stroke()))
            }), x(i)
          }

          var a, c, u, m = document.createElement("canvas"), d = t(), l = "c_n" + d.l, r = m.getContext("2d"),
            x = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function (n) {
              window.setTimeout(n, 1e3 / 15)
            }, w = Math.random, y = {x: null, y: null, max: 2e4};
          m.id = l, m.style.cssText = "position:fixed;top:0;left:0;z-index:" + d.z + ";opacity:" + d.o, e("body")[0].appendChild(m), o(), window.onresize = o, window.onmousemove = function (n) {
            n = n || window.event, y.x = n.clientX, y.y = n.clientY
          }, window.onmouseout = function () {
            y.x = null, y.y = null
          };
          for (var s = [], f = 0; d.n > f; f++) {
            var h = w() * a, g = w() * c, v = 2 * w() - 1, p = 2 * w() - 1;
            s.push({x: h, y: g, xa: v, ya: p, max: 6e3})
          }
          u = s.concat([y]), setTimeout(function () {
            i()
          }, 500)
        }
        /* =============================================================== END */

      },
      components:{
          "user-login":UserLogin,
          "user-register":UserRegister,
          "user-retrieve-password":UserRetrievePassword }
    }

</script>

<style scoped>
  div,h1{
    margin: 0;
    padding: 0;
    border: none;
  }
  .panel{
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    background-image: url("http://pykpufs15.bkt.clouddn.com/images/login.jpg");
    /*background-image: url("http://pykpufs15.bkt.clouddn.com/images/login_background.jpg");*/
    /*background-image: url("http://pykpufs15.bkt.clouddn.com/images/login_background2.jpg");*/
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
  }
  .panel .to_home{
    height: 40px;
    width: 400px;
    position: fixed;
    top: 50%;
    left: 50%;
    margin-top: -305px;
    margin-left: -200px;
    text-align: center;
    line-height: 40px;
    padding: 20px 0;
    z-index: 5000;
  }
  .panel .to_home .to_home_t{
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
  .panel .to_home .to_home_t:hover{
    cursor: pointer;
    color: #bee8fa;
  }
  .panel .center{
    width: 400px;
    height: 400px;
    position: fixed;
    top: 50%;
    left: 50%;
    margin-top: -250px;
    margin-left: -200px;
    background: rgba(78, 78, 80, 0.29);
  }
  .show_select{
    padding: 0 0 0 220px;
    width: 400px;
    height: 20px;
    box-sizing: border-box;
  }
  .btn_style{
    font-size: 14px;
    color: whitesmoke;
  }
  .btn_style:hover{
    color: #ff4730;
  }
  /***************************/
  /***************************/
</style>

