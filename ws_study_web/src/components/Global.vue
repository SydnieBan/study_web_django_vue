<!-- 不会改变时：【因为改变的话，某个组件变化其值，但其他组件不会重新渲染】-->
<script>
    export default {
        name: "Global",

      // server_url:"http://127.0.0.1:8080",
      server_url:"http://49.234.234.123:8080",
      // img_url:"http://pxebavmp1.bkt.clouddn.com",
      img_url:"http://pykpufs15.bkt.clouddn.com",
      //测试使用的url
      // img_url_icon:"http://pz0exm10r.bkt.clouddn.com",
      default_img:"http://pykpufs15.bkt.clouddn.com/images/default_user_icon.png"

    }
</script>

<!--
// main.js
import Global from 'components/Global'
Vue.prototype.Global = Global;

// index.vue
{{Global.server_url}}
-->
