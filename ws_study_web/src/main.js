import Vue from 'vue'
import App from './App.vue'
import router from './router/route'

import Global from './components/Global'
Vue.prototype.Global = Global;

import axios from 'axios'
Vue.prototype.axios = axios;

/* 公共方法【Axios、登录弹框】 */
// import GlobalFunc from './Axios'
import GlobalFunc from './GlobalFunc'
Vue.prototype.GlobalFunc = GlobalFunc;
/* 公共方法【Axios、登录弹框】 END */

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI);

/* svg */
import Icon from 'vue-svg-icon/Icon'
Vue.component('icon',Icon); // 注册
/* svg END*/


/*富文本编辑*/
import  VueQuillEditor from 'vue-quill-editor'
// require styles 引入样式
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

Vue.use(VueQuillEditor);
/*富文本编辑*/

/* markdown */
import VueSimplrmde from 'vue-simplemde'
// import 'simplemde/dist/simplemde.min.css'

Vue.use(VueSimplrmde);
/* markdown */

/* vue-video */
require('video.js/dist/video-js.css'); // videoJs样式
require('vue-video-player/src/custom-theme.css'); // vue-video-player样式
require('./components/videobox/video.css'); // 自定义 video 样式
import 'videojs-contrib-hls';
// require('videojs-contrib-hls/dist/videojs-contrib-hls');
import VideoPlayer from 'vue-video-player'
Vue.use(VideoPlayer);
/* vue-video END */




//滚动条
import { HappyScroll } from 'vue-happy-scroll'
//自定义组件名
Vue.component('happy-scroll', HappyScroll);
// 引入css
import 'vue-happy-scroll/docs/happy-scroll.css'

//codemirror
import VueCodemirror from 'vue-codemirror'
// require styles
import 'codemirror/lib/codemirror.css'
Vue.use(VueCodemirror)

new Vue({
  el: '#app',
  router,
  render: h => h(App)
});
