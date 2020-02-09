<template>
    <div id="larkplayer" class="larkplayer">

      <div class="larkplayer_inner">

        <!-- 视频左侧 -->
        <div class="video_left">

          <div class="vdl_item" id="vdl_chapter" @click="is_chapters_display=!is_chapters_display">
            <icon name="chapter" style="" class="vdl_item_img"></icon>
          </div>
          <!--*************** 章节框 *******************************-->
          <transition name="fade">
            <div v-if="is_chapters_display" :class="{chapter_panel:is_chapters_display}">
              <div v-if="is_chapters_display" :class="{chapter_panel_inner:is_chapters_display}">
                <ul v-for="chapter in chapter_section">
                  <h3>{{chapter.name}}</h3>
                  <p v-for="section in chapter.sections" @click="onClickToSec(section.section_id)">{{section.section_name}}&nbsp;({{section.section_time}})</p>
                </ul>
              </div>
            </div>
          </transition>
          <!--*************** 章节框 END *******************************-->

          <div :class="{vdl_item:1, vdl_item_clicked:is_click}" id="vdl_click" @click="is_click=!is_click">
            <icon name="click_good" style="" class="vdl_item_img" v-if="!is_click"></icon>
            <icon name="click_good_clicked" style="" class="vdl_item_img" v-if="is_click"></icon>
          </div>

          <div class="vdl_item" id="vdl_question" @click="is_question=!is_question">
            <icon name="question" style="" class="vdl_item_img"></icon>
          </div>
          <modal-panel :is_question="is_question" @close_modal="onChangeQuestion($event)" @submit_modal="onSubmitQuestion($event)"></modal-panel>

        </div>
        <!-- 视频左侧 END -->

        <!-- 视频 -->
        <div :class="{player:is_teacher,player_big:!is_teacher}"  @click="is_chapters_display=false">

          <video-player  class="video-player vjs-custom-skin "
                         ref="videoPlayer"
                         :playsinline="true"
                         :options="playerOptions"
                         @play="onPlayerPlay($event)"
                         @pause="onPlayerPause($event)"
                         @ready="playReadied($event)"
          >
          </video-player>


        </div>
        <!-- 视频 END　-->

        <!--　视频右侧　-->
        <div class="video_right" v-if="is_teacher"  @click="is_chapters_display=false">
          <div class="vdr_close" @click="is_teacher=!is_teacher">
            <icon name="error" class="vdr_close_icon"></icon>
          </div>
          <div class="vdr_top">
            <div class="vdr_top_img">
              <img :src="this.Global.img_url+'/images/'+teacher_info.teacher_icon__icon_img" alt="">
            </div>
            <div class="vdr_top_name">
              <h3>{{teacher_info.name}}</h3>
              <p>{{teacher_info.teacher_identity__identity}}</p>
            </div>
          </div>
          <div class="vdr_bottom">
            <p>{{teacher_info.introduce}}</p>
          </div>
        </div>

        <div class="video_div_right_hid" v-if="!is_teacher"  @click="is_chapters_display=false">
          <div class="hid_icon_div" @click="is_teacher=!is_teacher">
            <icon name="arrow" class="hid_icon"></icon>
          </div>
        </div>
        <!--　视频右侧　END　-->

      </div>

    </div>
</template>

<script>

  import {videoPlayer} from 'vue-video-player'
  import ModalPanel from "../global/ModalPanel";
  export default {
    props:['course_id','video_id'],
    name: "myPlayer",
    inject:['reload'],
    data () {
      return {
        user_id:window.localStorage.getItem('user_id'),
        /* 视频左侧 */
        is_chapters_display:false,
        chapter_section:[],
        is_click:false,
        is_question:false,
        question_content:'',
        /* 视频左侧 END */


        user_video_progress:0,
        progress_res:null,
        /* 视频 */
        playerOptions: {
          playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
          autoplay: false, //如果true,浏览器准备好时开始回放。
          muted: false, // 默认情况下将会消除任何音频。
          loop: false, // 导致视频一结束就重新开始。
          preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
          language: 'zh-CN',
          aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
          fluid: false, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
          sources: [{
            // type: "application/x-mpegURL",
            type:"video/mp4",
            // src: "https://baikebcs.bdimg.com/baike-other/big-buck-bunny.mp4" //你的m3u8地址（必填）
            src:""
          }],
          // poster: "poster.jpg", //你的封面地址
          width: document.documentElement.clientWidth,
          notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                 // controlBar: {
                 //   timeDivider: true,
                 //   durationDisplay: true,
                 //   remainingTimeDisplay: false,
                 //   fullscreenToggle: true  //全屏按钮
                 // }
        },
        /* 视频 END */

        /* 视频右侧 */
        teacher_info:{ id: null, name:null, introduce:null,teacher_icon__icon_img: null,teacher_sex__name:null,teacher_identity__identity:null},
        is_teacher:true,
        /* 视频右侧 END */
      }
    },
    created:function(){
      this.get_video_src(); // 获取视频src
      this.get_user_video_progress(); // 获取用户视频进度
      this.get_chapters_section(); // 获取章节信息
      this.get_teacher_per(); // 获取老师
    },
    components:{
      ModalPanel,
      videoPlayer
    },
    methods: {
      // 视频左侧
      /* 获取章节 */
      get_chapters_section:function () {
        this.chapter_section.splice(0);
        let url = this.Global.server_url + '/course/get_video_chapter/';
        this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
          res=>{ this.show_chapters_section(this.chapter_section, res) }
        )
      },
      /* 获取章节 END */
      /* 显示章节 END */
      show_chapters_section:function (to_data, res) {
        for (let i in res){
          to_data.push(res[i])
        }
      },
      /* 显示章节 END */
      /* 点击章节框里的章节跳转 */
      onClickToSec:function(sec_id){
        this.$router.push({path:'/section/video',query:{course_id:this.course_id,video_id:sec_id}}).catch(err => { console.log(err) });
        this.reload();
      },
      /* 点击章节框里的章节跳转 END */
      /* 问答模态框 */
      onChangeQuestion:function(ev){
        this.is_question = ev.is_question;
      },
      onSubmitQuestion:function(ev){
        this.question_content = ev.question_content;

        let url=this.Global.server_url+'/user_course/insert_question_video/';
        /* question_video_id */
        this.GlobalFunc.func_axios(url,'GET',{content:this.question_content,user_id:this.user_id,video_id:this.video_id,},
          res=>{ this.reload();  }
        );
        this.is_question = false;
      },
      /* 问答模态框 END */
      // 视频左侧 END


      // 视频
      /* 获取视频src */
      get_video_src:function(){
        let url = this.Global.server_url+'/course/get_video_info/';
        this.GlobalFunc.func_axios(url,'GET',{video_id:this.video_id},
          res=>{ this.playerOptions.sources[0].src=res[0].video_src; }
        )
      },
      /* 获取视频src END */
      /* 获取用户视频进度 */
      get_user_video_progress:function(){
        let url = this.Global.server_url+'/user_course/get_user_video/';
        this.GlobalFunc.func_axios(url,'GET',{user_id:this.user_id,video_id:this.video_id},
          res=>{ this.user_video_progress=res.progress }
        )
      },
      /* 获取用户视频进度 END */
      onPlayerPlay(player) {
        // alert("play");
      },
      onPlayerPause(player){
        // alert("pause");
        // let url=this.Global.server_url+'/user_course/update_user_video/';
        // this.GlobalFunc.func_axios(url,'GET',null,
        //   res=>{alert('(((((((((((((((((((((')}
        // )
      },
      /* 设置用户所看视频进度 */
      playReadied(player){
        player.currentTime(this.user_video_progress);
      },
      /* 设置用户所看视频进度 END */
      /* 关闭页面 / 跳转路由 时读取用户所看视频进度 */
      beforeunloadHandler:function (e) {

        let url=this.Global.server_url+'/user_course/update_user_video/';
        this.GlobalFunc.func_axios(url,'GET',{user_id:this.user_id,video_id:this.video_id,progress:this.player.currentTime()},
          res=>{ this.progress_res=res.result; }
        )
      },
      /* 关闭页面 / 跳转路由 时读取用户所看视频进度 END */
      // 视频 END


      // 视频右侧
      /* 获取老师信息 */
      get_teacher_per:function () {
        let url = this.Global.server_url + '/user/get_teacher/';
        this.GlobalFunc.func_axios(url, 'GET', {course_id:this.course_id},
          res => {
            this.teacher_info.id = res[0].id;
            this.teacher_info.name = res[0].name;
            this.teacher_info.introduce = res[0].introduce;
            this.teacher_info.teacher_icon__icon_img = res[0].teacher_icon__icon_img;
            this.teacher_info.teacher_sex__name = res[0].teacher_sex__name;
            this.teacher_info.teacher_identity__identity = res[0].teacher_identity__identity;
          }
        )
      },
      /* 获取老师信息 */
      // 视频右侧 END


    },
    mounted:function(){
      /* 关闭页面时 */
      window.addEventListener('beforeunload', e => this.beforeunloadHandler(e));
      /* 关闭页面时 END */
    },
    beforeDestroy:function(){
      /* 跳转路由时 */
      this.beforeunloadHandler('beforeDestroy');
      /* 跳转路由时 END */
    },
    computed: {
      player() {
        return this.$refs.videoPlayer.player
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style type="text/css" scoped>
  div,h3,p,ul,li{
    margin: 0;
    padding: 0;
    border: none;
  }
  .larkplayer{
    width: 1251px;
    margin: 0 auto;
    height: 506px;
    padding-top: 30px;
  }
  .larkplayer_inner{
    width: 1251px;
    margin: 0 auto;
    height: 506px;
    background-color: black;
    display: flex;
    justify-content: space-between;
  }

  /* 视频左侧 */
  .larkplayer .video_left{
    width: 51px;
    height: 506px;
    background: #535353;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
  }
  .larkplayer .video_left .vdl_item{
    width: 51px;
    height: 60px;
    padding: 15px 13px;
    box-sizing: border-box;
    transition: background-color 0.3s;
    opacity: 0.3;
  }
  .vdl_item_clicked{
    opacity: 1 !important;
  }
  .larkplayer .video_left .vdl_item:hover{
    opacity: 1;
    cursor: pointer;
    background-color: #737373;
  }
  .larkplayer .video_left .vdl_item .vdl_item_img{
    width: 25px;
    height: 25px;
  }
  /*******************章节框*********************/
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s, width 0.5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
  .chapter_panel{
    width: 300px;
    height: 506px;
    background-color: rgba(47, 47, 47, 0.89);
    position: absolute;
    left:50px;
    z-index: 1000;
    display: block;
  }
   .chapter_panel_inner{
    width: 300px;
    height: 506px;
    padding:10px 10px;
    box-sizing: border-box;
    overflow-y: scroll;
  }
  .larkplayer .video_left h3{
    color: white;
    margin: 10px 0;
    font-size: 16px;
  }
  .larkplayer .video_left p{
    width: 250px;
    color: lightgray;
    margin: 5px 0 5px 20px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    font-size: 14px;
  }
  .larkplayer .video_left p:hover{
    cursor: pointer;
    color: #93bbed;
  }
  /******************* 章节框 END *********************/

  /* 视频左侧 END */

  /* 视频 */
  .larkplayer .player{
    /*width: 1251px;*/
    width: 900px;
    height: auto;
    margin: 0 auto;
    background-color: lightskyblue;
  }
  .larkplayer .player_big{
    /*width: 1149px;*/
    width: 900px;
    height: 400px !important;
    margin: 0 auto;
    background-color: lightskyblue;
  }
  .demo{
    height: 400px !important;
  }
  /* 视频 END */

  /* 视频右侧 */
  .larkplayer .video_right{
    width: 300px;
    height: 506px;
    background: #535353;
    padding: 10px 10px;
    box-sizing: border-box;
  }
  .larkplayer .video_right .vdr_close{
    padding: 5px 0;
    display: flex;
    justify-content: flex-end;
  }
  .larkplayer .video_right .vdr_close .vdr_close_icon{
    width: 15px;
    height: 15px;
  }
  .larkplayer .video_right .vdr_close .vdr_close_icon:hover{
    cursor: pointer;
  }
  .larkplayer .video_right .vdr_top{
    padding: 5px 5px;
    display: flex;
    justify-content: flex-start;
    color: white;
  }
  .larkplayer .video_right .vdr_top .vdr_top_img img{
    width: 60px;
    height: 60px;
    border-radius: 50%;
  }
  .larkplayer .video_right .vdr_top .vdr_top_name{
    padding: 0 10px;
  }
  .larkplayer .video_right .vdr_top .vdr_top_name h3{
    font-size: 16px;
  }
  .larkplayer .video_right .vdr_top .vdr_top_name p{
    font-size: 14px;
  }
  .larkplayer .video_right .vdr_bottom{
    padding: 10px 10px;
    color: #e2e2e2;
    font-size: 14px;
  }

  .larkplayer .video_div_right_hid{
    width: 51px;
    background: #535353;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 13px;
    box-sizing: border-box;
  }
  .larkplayer .video_div_right_hid .hid_icon_div{
    width: 25px;
    height: 25px;
  }
  .larkplayer .video_div_right_hid .hid_icon{
    width: 25px;
    height: 25px;
  }
  .larkplayer .video_div_right_hid .hid_icon:hover{
    cursor: pointer;
  }
  /* 视频右侧 END */
</style>
