<template>
  <div class="contain">
    <div class="personal_top">
      <h3 class="title">已结束课程</h3>
    </div>
    <div class="split"></div>
    <div class="course_list_box">
      <div class="dis_article_c" v-for="cou_item in course" :key="cou_item.course_id" @click="ToCourseDetail(cou_item.course_id)">
        <div class="dis_article_c_inner" >
          <img :src="cou_item.course_img" alt="not found" style="z-index: 1000">
          <h3 class="hd">{{cou_item.course_name}}</h3>
          <p class="p_intro">{{cou_item.introduce}}</p>
          <p class="integral">{{cou_item.course_price}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "finish",
    data (){
      return {
        course:[],
        user_id:window.localStorage.getItem('user_id'),
        iscomplete:1,
      }
    },
    created(){
      this.get_course();
    },
    methods:{
      /* 获取用户全部课程 */
      get_course:function(){
        let url=this.Global.server_url+'/user_course/get_sc_peruser/';
        this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id,"iscomplete":this.iscomplete},
          res=>{ this.show_course(this.course, res) }
        )
      },
      /* 获取用户全部课程 END */
      /* 显示用户的全部课程 */
      show_course:function (to_data, res) {
        to_data.splice(0);
        if(res && res.length>0){
          for(let i=0;i<12 && i<res.length;i++){
            (res[i].course__integral===0)?(res[i].course__integral='免费'):(res[i].course__integral=res[i].course__integral+'积分');
            to_data.push(
              {"course_img":this.Global.img_url+"/images/course"+res[i].course__course_icon,
                "course_name":res[i].course__name,
                "course_price":res[i].course__integral,"course_id":res[i].course__id,
                "introduce":res[i].course__introduce,
              }
            )
          }
        }
      },
      /* 显示用户的全部课程 END */
      /* 跳转到课程详情 */
      ToCourseDetail:function (id) {
        this.$router.push({ path: '/course_detail', query: { course_id: id} })
      },
      /* 跳转到课程详情 END */
    },
  }
</script>

<style scoped>
  .split{
    width: 96%;
    height: 1px;
    margin: auto;
    background: gray;
  }
  .contain{
    width: 1020px;
    /*height: 520px;*/
    overflow: hidden;
  }
  .contain .personal_top{
    height: 100px;
    line-height: 50px;
    overflow: hidden;

  }
  .contain .personal_top .title{
    padding-left: 20px;
  }
  /****************课程详情页面********************************************/
  body,html,h3 ,p{
    margin: 0;
    padding: 0;
  }
  .course_list_box{
    /*height: 1920px;*/
    /*height: 300px;*/
    margin: 0 auto;
    background: white;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
  .dis_article_c{
    /*margin-top: 50px;*/
    height: 300px;
    width: 243px;
    margin-left: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 10px 10px;
    box-sizing: border-box;
    /*box-shadow: 0 0 1px;*/
  }
  .dis_article_c:hover{
    cursor: pointer;
    box-shadow: 0 0 10px gray;
  }
  .dis_article_c_inner{
    height: 280px;
    width: 243px;
  }
  .dis_article_c_inner img{
    height: 135px;
    width: 223px;
  }
  .dis_article_c_inner .hd{
    margin: 0;
    font-size: 18px;
    height: 56px;
  }
  .dis_article_c_inner p{
    color: gray;
  }
  .dis_article_c_inner .p_intro{
    height: 40px;
    /* 实现p标签多行超界省略号代替 */
    display: -webkit-box;
    -webkit-box-orient: vertical; /* 子元素显示方式:vertical-垂直 */
    overflow: hidden; /* 多余的隐藏 */
    -webkit-line-clamp:2; /* 有隐藏的则用省略号代替 */
  }
  .dis_article_c_inner .integral{
    color: #000;
  }
</style>
