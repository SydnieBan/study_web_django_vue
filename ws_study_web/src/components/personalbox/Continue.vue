<template>
    <div class="contain">
      <div class="personal_top">
        <h3 class="title">未完成课程</h3>
      </div>
      <div class="split"></div>
      <div class="dis_article_c" v-for="cou_item in course" :key="cou_item.course_id">
        <div class="dis_article_c_inner">
          <div class="img_box" >
            <img :src="cou_item.course_img" alt="not found">
          </div>
          <div class="info-box">
            <div class="title">
              <span class="integral">{{cou_item.course_price}}</span>
              <div class="hd">{{cou_item.course_name}}</div>
            </div>
            <div class="introduce">
              <p class="p_intro">{{cou_item.introduce}}</p>
            </div>
            <div class="op">
              <button class="cancel" @click="ToCourseDetail(cou_item.course_id)">继续学习</button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    name: "continue",
    data (){
      return {
        course:[],
        user_id: window.localStorage.getItem('user_id'),
        iscomplete:0,
      }
    },
    created(){
      this.get_course();
    },
    methods:{
      /* 获取用户未完成全部课程 */
      get_course:function(){
        let url=this.Global.server_url+'/user_course/get_sc_peruser/';
        this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id,"iscomplete":this.iscomplete},
          res=>{ this.show_course(this.course, res) }
        )
      },
      /* 获取用户未完成全部课程 END */
      /* 显示用户的全部课程 */
      show_course:function (to_data, res) {
        to_data.splice(0);
        if(res && res.length>0){
          for(let i=0;i<5 && i<res.length;i++){
            (res[i].course__integral===0)?(res[i].course__integral='免费'):(res[i].course__integral=res[i].course__integral+'积分');
            to_data.push(
              {"course_img":this.Global.img_url+"/images/course"+res[i].course__course_icon,
                "course_name":res[i].course__name,
                "course_price":res[i].course__integral,"course_id":res[i].course__id,
                "introduce":res[i].course__introduce}
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
  .dis_article_c{
    /*margin-top: 50px;*/
    height: 150px;
    width: 1000px;
    margin-left:10px;
    margin-top: 20px;
    padding: 10px 10px;
  }
  .dis_article_c_inner{
    height: 144px;
    display: flex;
    flex-direction: row;
    width: 1000px;
  }
  .dis_article_c_inner .img_box{
    width: 223px;
    margin-right: 30px;
  }
  .dis_article_c_inner .img_box img{
    height: 135px;
    width: 223px;
    overflow: hidden;
  }
  .dis_article_c_inner .hd{
    font-size: 20px;
    color: #07111b;
    font-weight: 700;
    margin-left: 10px;
    line-height: 36px;
    white-space: nowrap;
  }
  .dis_article_c_inner .info-box{
    display: flex;
    flex-direction: column;
    border-bottom: 1px solid #d9dde1;
    width: 730px;
  }
  .dis_article_c_inner .introduce{
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 12px;
  }
  .dis_article_c_inner p{
    color: gray;
  }
  .info-box .op{
    text-align: right;
  }
  .info-box .op .cancel{
    outline: none;
    width: 104px;
    font-size: 14px;
    border: none;
    color: #fff;
    height: 36px;
    line-height: 36px;
    text-align: center;
    background: lightskyblue;
    cursor: pointer;
    opacity: 0.8;
    border-radius: 18px;
  }
  .info-box .op .cancel:hover{
    opacity: 1;
  }
  .info-box .title{
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .dis_article_c_inner .p_intro{
    height: 50px;
    font-size: 12px;
    color: #4d555d;
    line-height: 24px;
    margin: 0;
    padding: 0;
    width: 727px;
    display: -webkit-box;
    -webkit-box-orient: vertical; /* 子元素显示方式:vertical-垂直 */
    overflow: hidden; /* 多余的隐藏 */
    -webkit-line-clamp:2; /* 有隐藏的则用省略号代替 */
  }
  .dis_article_c_inner .integral{
    color: #000;
    background: #f5f7fa;
    border-radius: 2px;
  }
</style>
