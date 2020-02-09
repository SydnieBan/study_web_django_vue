<template>
  <div class="contain">
    <div class="personal_top">
      <h3 class="title">收藏的课程</h3>
    </div>
    <div class="split"></div>
    <div class="dis_article_c" v-for="(cou_item,index) in course" :key="cou_item.course_id" v-if="show">
      <div class="dis_article_c_inner">
        <div class="img_box" @click="ToCourseDetail(cou_item.course_id)">
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
            <span class="cancel" @click="call_off(index,cou_item.course_id)">取消收藏</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "collection",
    data (){
      return {
        course:[],
        show:true,
        course_id:'',
        user_id: window.localStorage.getItem('user_id'),
      }
    },
    created(){
      this.get_course();
    },
    methods:{
      /* 获取用户全部课程 */
      get_course:function(){
        let url=this.Global.server_url+'/user_course/get_collection_peruser/';
        this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id},
          res=>{ this.show_course(this.course, res) }
        )
      },
      /* 获取用户全部课程 END */
      /* 显示用户的全部课程 */
      show_course:function (to_data, res) {
        to_data.splice(0);
        if(res && res.length>0){
          for(let i=0;i<10 && i<res.length;i++){
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
      /* 后台取消收藏功能 */
      get_res:function(){
        let url=this.Global.server_url+'/user_course/delete_collection_course/';
        this.GlobalFunc.func_axios(url, 'GET', {"user_id":this.user_id,"course_id":this.course_id},
          res=>{  }
        )
      },
    /*取消功能*/
    call_off:function (index,id) {
      this.course.splice(index,1).show=false;
      this.course_id=id
      this.get_res();
    }
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
    cursor: pointer;
  }
  .dis_article_c_inner .img_box img{
    height: 135px;
    width: 223px;
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
  .dis_article_c_inner .introduce .p_intro{
    height: 40px;
    /* 实现p标签多行超界省略号代替 */
    display: -webkit-box;
    -webkit-box-orient: vertical; /* 子元素显示方式:vertical-垂直 */
    overflow: hidden; /* 多余的隐藏 */
    -webkit-line-clamp:2; /* 有隐藏的则用省略号代替 */
  }
  .dis_article_c_inner p{
    color: gray;
  }
  .info-box .op{
    text-align: right;
  }
  .info-box .op .cancel{
    font-size: 16px;
    color: #1c1f21;
    line-height: 20px;
    transition: color 0.5s;
  }
  .info-box .op .cancel:hover{
    cursor: pointer;
    color: lightskyblue;
  }
  .info-box .title{
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .dis_article_c_inner .integral{
    color: #000;
    background: #f5f7fa;
    border-radius: 2px;
  }
</style>
