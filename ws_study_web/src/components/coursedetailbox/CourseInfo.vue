<template>
    <div id="course_info" class="course_info">
      <!--　课程信息　-->
      <div class="top">
        <div class="top_inner">
          <el-row class="ti_top">
            <el-col :span="18" class="pre_course">
              <el-breadcrumb class="el-breadcrumb" separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{path:'/course_all'}">{{course_info.pro}}</el-breadcrumb-item>
                <el-breadcrumb-item :to="{name:'course_all',params:{direction_name:course_info.classify__direction__name}}">{{course_info.classify__direction__name}}</el-breadcrumb-item>
                <el-breadcrumb-item :to="{name:'course_all',params:{direction_name:course_info.classify__direction__name,classify_name:course_info.classify__name}}">{{course_info.classify__name}}</el-breadcrumb-item>
                <el-breadcrumb-item>{{course_info.name}}</el-breadcrumb-item>
              </el-breadcrumb>
            </el-col>
            <el-col :span="6" class="collection">
              <el-row @click.native="onClickCollection">
                <el-col :span="12">
                  <icon name="collection" style="width: 24px;height: 24px;margin-top: 5px" v-if="!is_collection"></icon>
                  <icon name="collection_yes" style="width: 24px;height: 24px;margin-top: 5px" v-if="is_collection"></icon>
                </el-col>
                <el-col :span="12"><span>收藏</span></el-col>
              </el-row>
            </el-col>
          </el-row>
          <el-row class="ti_main">
            <!-- 课程ICON -->
            <el-col class="ti_main_col" :span="6">
              <img :src="this.Global.img_url+'/images/course'+course_info.course_icon" alt="">
            </el-col>
            <!-- 课程ICON END -->
            <!-- 中部 -->
            <el-col class="ti_main_col" :span="13">
              <el-row class="tim_mid_top">
                <el-col :span="24"><h1>{{course_info.name}}</h1></el-col>
              </el-row>
              <el-row class="tim_mid_main">
                <el-col :span="12">
                  <el-row><el-col :span="24">难度：{{course_info.difficulty__name}}</el-col></el-row>
                  <el-row><el-col :span="24">学习人数：{{course_sc_num}}</el-col></el-row>
                </el-col>
                <el-col :span="12">
                  <el-row><el-col :span="24">时长：{{course_time}}</el-col></el-row>
                  <el-row><el-col :span="24">收藏量：{{course_collection_num}}</el-col></el-row>
                </el-col>
              </el-row>
            </el-col>
            <!-- 中部 END -->
            <!-- 选课按钮 -->
            <el-col class="ti_main_col" :span="5">
              <el-button type="primary" style="height: 40px;padding: 3px 0" round v-if="!is_sc" @click="onClickSc">{{(course_info.integral===0)?('进入学习'):(course_info.integral+'积分兑换')}}</el-button>
              <el-button type="primary" style="height: 40px;line-height: 40px;cursor: default;padding: 3px 0" round v-if="is_sc">已参与，进入学习</el-button>
            </el-col>
            <!-- 选课按钮 END -->
          </el-row>
        </div>
      </div>
      <!--　课程信息　END　-->
      <!--　标签　-->
      <div class="bottom">
        <div class="bottom_inner">
          <ul>
            <li v-for="(tag,index) in tags"><a href="javascript:void 0" @click="onClickTag(index)" :class="{a_style:index===info_tag_index}">{{tag}}</a></li>
          </ul>
        </div>
      </div>
      <!--　标签　END　-->
      <!-- 分割线 -->
      <el-divider class="el-divider"></el-divider>
      <!-- 分割线 END　-->

    </div>
</template>

<script>
    export default {
      name: "CourseInfo",
      props:['course_id','is_sc'],
      inject:['reload'],
      data(){
        return{
          is_collection:false,
          user_id:window.localStorage.getItem('user_id'),
          course_info:{pro:"测试"},
          course_time:0,
          course_sc_num:0,
          course_collection_num:0,
          tags:['视频章节','课件章节','用户评价'],
          info_tag_index:0
        }
      },
      created:function () {
        this.get_course_info();
        this.get_course_time();
        this.get_course_sc_num();
        this.get_course_collection_num();
        this.judge_is_collection();
      },
      methods:{
        /* 获取课程信息 */
        get_course_info:function () {
            let url = this.Global.server_url + '/course/get_course_info/';
          this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
              res => {this.show_course_info(this.course_info, res[0]);}
              )
        },
        /* 获取课程信息 END */
        /* 显示课程信息 */
        show_course_info:function (to_data, res) {
          to_data.pro = "课程";
          to_data.name = res.name;
          to_data.introduce = res.introduce;
          to_data.course_icon = res.course_icon;
          to_data.notice = res.notice;
          to_data.integral = res.integral;
          to_data.difficulty__name = res.difficulty__name;
          to_data.classify__name = res.classify__name;
          to_data.classify__direction__name = res.classify__direction__name;

          /* 子给父传值 */
          this.$emit('bus_info',{"introduce":this.course_info.introduce,"notice":this.course_info.notice})
          /* 子给父传值 END　*/

        },
        /* 显示课程信息 END */

        /* 获取课程学习时长 */
        get_course_time:function () {
          let url = this.Global.server_url + '/course/get_course_time/';
          this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
            res => {this.course_time = res.course_time.split(':')[0]+'小时'+res.course_time.split(':')[1]+'分钟'})
        },
        /* 获取课程学习时长 END */

        /* 获取课程学习人数 */
        get_course_sc_num:function () {
          let url = this.Global.server_url + '/user_course/get_sc_number/';
          this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
            res => {this.course_sc_num = res.user_num})
        },
        /* 获取课程学习人数 END */

        /* 获取课程收藏量 */
        get_course_collection_num:function () {
          let url = this.Global.server_url + '/user_course/get_collection_number/';
          this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
            res => {this.course_collection_num = res.collection_num})
        },
        /* 获取课程收藏量 END */

        /* 单击课程/课件/评论标签 */
        onClickTag:function (index) {
          this.info_tag_index=index;
          this.$emit('select_tag',{"info_tag_index":index})
        },
        /* 单击课程/课件/评论标签 END */


        /* 判断是否收藏 */
        judge_is_collection:function () {
          if (this.user_id){
            let url = this.Global.server_url + '/user_course/is_collection/';
            this.GlobalFunc.func_axios(url, 'GET', {user_id:this.user_id,course_id:this.course_id},
              res=>{
                if (res.result){
                  this.is_collection = true
                } else{
                  this.is_collection = false
                }
              }
            )
          }
        },
        /* 判断是否收藏 END */
        /* 收藏课程 / 取消收藏 */
        onClickCollection:function () {
          if (this.user_id){
            if (this.is_collection){
              // alert('是否取消收藏')
              let url=this.Global.server_url+'/user_course/delete_collection_course/';
              this.GlobalFunc.func_axios(url, 'GET', {user_id:this.user_id,course_id:this.course_id},
                res=>{ this.reload(); }
              )
            }
            else{
              // alert('是否收藏')
              let url=this.Global.server_url+'/user_course/collection_course/';
              this.GlobalFunc.func_axios(url, 'GET', {user_id:this.user_id,course_id:this.course_id},
                res=>{ this.reload(); }
              )
            }
          }
          else{
            this.GlobalFunc.open_login(this);
          }
        },
        /* 收藏课程 / 取消收藏 END */

        /* 选课 */
        onClickSc:function () {
          if (this.user_id){
            let url = this.Global.server_url+'/user_course/insert_sc/';
            this.GlobalFunc.func_axios(url,'GET',{user_id:this.user_id,course_id:this.course_id},
              res=>{
                // alert(res.result);
                if (res.result==="can't select course"){
                  this.open_sc_error();
                } else{
                  this.reload();
                }
              }
            )
          } else{
            this.GlobalFunc.open_login(this);
          }
        },
        /* 选课 END */
        /* 积分不够提示框 */
        open_sc_error() {
          this.$alert('您的积分不够，不可以选择该课程', '提示', {
            confirmButtonText: '确定',
          });
        },
        /* 积分不够提示框 END */


      }
    }
</script>

<style scoped>
  div,.el-row,.el-col,.el-breadcrumb,img,h1,.el-button,ul,li{
    margin: 0;
    padding: 0;
    border: none;
  }
  .course_info{
    background-color: #889fc7;
    width: 100%;
    height: 310px;
  }

  /* 课程信息头部 */
  .course_info .top{
    background-color: #889fc7;
    width: 100%;
    height: 250px;
  }
  .course_info .top .top_inner{
    background-color: #889fc7;
    width: 1215px;
    margin: 0 auto;
    height: 250px;
  }
  .course_info .top .top_inner .ti_top{
    height: 60px;
    padding: 12px 0;
  }
  .course_info .top .top_inner .ti_top .pre_course .el-breadcrumb{
    height: 36px;
    line-height: 36px;
    font-size: 16px;
  }
  .course_info .top .top_inner .ti_top .collection{
    width: 72px;
    height: 36px;
    line-height: 36px;
    text-align: center;
    color: gray;
    font-size: 16px;
    transition: opacity 0.5s;
  }
  .course_info .top .top_inner .ti_top .collection:hover{
    cursor: pointer;
    opacity: 0.5;
  }

  .course_info .top .top_inner .ti_main{
    height: 190px;
    line-height: 190px;
  }
  .course_info .top .top_inner .ti_main .ti_main_col{
    height: 190px;
  }
  .course_info .top .top_inner .ti_main .ti_main_col img{
    width: 303px;
    height: 190px;
    object-fit: cover;
  }
  .course_info .top .top_inner .ti_main .ti_main_col .tim_mid_top{
    height: 80px;
    line-height: 80px;
    padding-left: 10px;
    overflow: hidden;
  }
  .course_info .top .top_inner .ti_main .ti_main_col .tim_mid_top h1{
    color: white;
    font-size: 35px;
  }
  .course_info .top .top_inner .ti_main .ti_main_col .tim_mid_main{
    height: 110px;
  }
  .course_info .top .top_inner .ti_main .ti_main_col .tim_mid_main>.el-col{
    height: 110px;
  }
  .course_info .top .top_inner .ti_main .ti_main_col .tim_mid_main>.el-col>.el-row{
    height: 55px;
    line-height: 55px;
    font-size: 18px;
    color: white;
    padding-left: 10px;
  }
  .course_info .top .top_inner .ti_main .ti_main_col .el-button{
    width: 240px;
    height: 40px;
    line-height: 40px;
    background-color: #7ff0ff;
    font-size: 20px;
    color: white;
    transition: background-color 0.5s;
  }
  .course_info .top .top_inner .ti_main .ti_main_col .el-button:hover{
    background-color: #6ccbd8;
  }
  /* 课程信息头部 END*/

  /* 课程信息 */
  .course_info .bottom{
    background-color: #ffffff;
    width: 100%;
    height: 50px;
  }
  .course_info .bottom_inner{
    background-color: #ffffff;
    width: 1215px;
    margin: 0 auto;
    height: 50px;
    line-height: 50px;
  }
  .course_info .bottom_inner ul{
    list-style: none;
    display: flex;
    justify-content: flex-start;
  }
  .course_info .bottom_inner ul li{
    width: 200px;
  }
  .course_info .bottom_inner ul li a{
    color: black;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    transition: color 0.5s;
    cursor: default;
  }
  .course_info .bottom_inner ul li .a_style{
    background: gainsboro;
    padding: 5px;
  }
  .course_info .bottom_inner ul li a:hover:not([class='a_style']){
    color: lightskyblue;
    cursor: pointer;
  }
  /* 课程信息 END */

  /* 分割线 */
  .el-divider{
    width: 100%;
    min-width: 1215px;
    height: 10px;
    background: white;
    box-shadow: 0 5px 5px #c4c4c4;
  }
  /* 分割线 END */
</style>
