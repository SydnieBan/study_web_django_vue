<template>
  <div id="section" class="section">
    <header-box2 :course_id="course_id" :title="title" @reflesh="onReflesh"></header-box2>
    <router-view></router-view>
  </div>
</template>

<script>

    import HeaderBox2 from "./global/HeaderBox2";
    export default {
        name: "Section",
      components: {HeaderBox2},
      data(){
          return{
            course_id:this.$route.query.course_id,
            video_id:this.$route.query.video_id,
            courseware_id: this.$route.query.courseware_id,
            title:'标题'
          }
      },
      created:function(){
          if (this.video_id){
            this.get_video_title()
          } else{
            this.get_courseware_title()
          }
      },
      methods:{
          /* 获取视频小节标题 */
         get_video_title:function () {
           let url=this.Global.server_url+'/course/get_video_info/';
           this.GlobalFunc.func_axios(url, 'GET',{video_id: this.video_id},
            res=>{ this.title=res[0].name }
           )
         },
        /* 获取视频小节标题 END */

        /* 获取课件小节标题 */
        get_courseware_title:function () {
          let url=this.Global.server_url+'/course/get_courseware_info/';
          this.GlobalFunc.func_axios(url, 'GET',{courseware_id: this.courseware_id},
            res=>{ this.title=res[0].name }
          )
        },
        /* 获取课件小节标题 END */

        /* 页面退出刷新 */
        onReflesh:function () {
          this.$router.push({path:'/'})
        }
        /* 页面退出刷新 END */
      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
</style>
