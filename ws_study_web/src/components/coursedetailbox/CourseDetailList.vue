<template>
  <div id="course_detail_list" class="course_detail_list">

    <div class="div_chapters" v-if="!(list_tag_index === 2)">
      <div class="top_introduce">
        <p>{{introduce}}</p>
      </div>

      <div class="chapters">

        <ul v-for="chapter in section_chapter">
          <h3>{{chapter.name}}</h3>
          <p>{{chapter.introduce}}</p>
          <li v-for="section in chapter.sections" @click="onClickToSection(section.section_id)">{{section.section_name}}</li>
        </ul>

      </div>
    </div>

    <div class="div_evaluations" v-else>

      <el-row class="top_evaluation">
        <el-col :span="20">
          <el-input type="textarea" :rows="4"  placeholder="请输入内容" v-model="user_eva"></el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="onClickPubEva">我要发布</el-button>
        </el-col>
      </el-row>

      <el-row class="evaluation" v-for="(eva,index) in evaluation" :key="index">

        <el-col :span="24">


          <el-row>
            <el-col :span="2">
              <img :src="Global.img_url + '/'+ eva.user__userinfo__user_icon__icon_img" alt="">
            </el-col>
            <el-col :span="22" style="font-weight: bolder">
              {{eva.user__userinfo__user_name}}
            </el-col>
          </el-row>

          <el-row style="">
            {{eva.content}}
          </el-row>

          <el-row style="text-align: right">
            {{eva.eva_date}}
          </el-row>

        </el-col>
      </el-row>

      <el-row style="display: flex;justify-content: flex-end">
        <div>
          <button-page-box :current_page="course_eva_index" :page_size="course_eva_items" :total="course_eva_total" @click_page="on_click_page($event)"></button-page-box>
        </div>
      </el-row>

    </div>

  </div>
</template>

<script>
    import ButtonPageBox from "../coursebox/ButtonPageBox";
    export default {
        name: "CourseDetailList",
      components: {ButtonPageBox},
      props:['course_id','user_id','is_sc','introduce','list_tag_index'],
      inject:['reload'],
      data(){
          return{
            flag:0,
            section_chapter:[], /* [{"id":, "name":"", "introduce":"", "sections":[ {"section_name":"", "section_id": },{}] },{}] */
            evaluation:[],
            user_eva:'',
            course_eva_index:1,
            course_eva_items:5,
            course_eva_total:0,
          }
      },
      created:function(){
        this.get_chapters_section();
      },
      watch:{
        list_tag_index:function (newVal) {
            if ((newVal === 0) ||  (newVal === 1)){
              this.get_chapters_section();
            }else{
              this.get_evaluation_number();
              this.get_evaluation();
            }
          }
      },
      methods:{
          /* 获取章节 */
          get_chapters_section:function () {
            this.section_chapter.splice(0);
            let url = this.Global.server_url + '/course/get_video_chapter/';
            if (this.list_tag_index === 0){
              url = this.Global.server_url + '/course/get_video_chapter/';
            }else {
              url = this.Global.server_url + '/course/get_courseware_chapter/';
            }
            this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
              res=>{ this.show_chapters_section(this.section_chapter, res) }
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

        /* 获取课程评论 */
        get_evaluation:function () {
          this.section_chapter.splice(0);
          this.evaluation.splice(0);
          let url = this.Global.server_url + '/user_course/get_course_eva/';
          this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id,"course_eva_index":this.course_eva_index,"course_eva_items":this.course_eva_items},
            res=>{ this.show_evaluation(this.evaluation, res) }
          );
        },
        get_evaluation_number:function () {
          let url = this.Global.server_url + '/user_course/get_course_eva_number/';
          this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
            res=>{ this.course_eva_total=res.course_eva_number; }
          );
        },
        /* 获取课程评论 END */
        /* 显示课程评论 */
        show_evaluation:function (to_data, res) {
          for (let i in res){
            to_data.push(res[i])
          }
        },
        /* 显示课程评论 END */

        /* 点击进入Video或Courseware */
        onClickToSection:function (id) {
          if (this.user_id){
            // 已选该课
            if (this.is_sc){
              this.insert_user_section(id);
            }
            else{
              let url = this.Global.server_url+'/user_course/insert_sc/';
              this.GlobalFunc.func_axios(url,'GET',{user_id:this.user_id,course_id:this.course_id},
                res=>{
                  // alert(res.result);
                  if (res.result==="can't select course"){
                    this.open_sc_error();
                  } else{
                    this.insert_user_section(id);
                  }
                }
              )
            }
          }
          else{
            this.GlobalFunc.open_login(this);
          }
        },
        /* 点击进入Video或Courseware END */
        /* 积分不够提示框 */
        open_sc_error() {
          this.$alert('您的积分不够，不可以选择该课程', '提示', {
            confirmButtonText: '确定',
          });
        },
        /* 积分不够提示框 END */
        /* 添加用户视频/用户课件 */
        insert_user_section:function(id){
          if (this.list_tag_index===0){ // 视频
            /* 添加用户视频 */
            let url = this.Global.server_url+'/user_course/insert_user_video/';
            this.GlobalFunc.func_axios(url,'GET',{user_id:this.user_id,video_id:id},
              res=>{ this.$router.push({path:'/section/video',query:{course_id:this.course_id,video_id:id}}); }
            )
          }
          else if (this.list_tag_index===1){ // 课件
            /* 添加用户课件 */
            let url = this.Global.server_url+'/user_course/insert_user_courseware/';
            this.GlobalFunc.func_axios(url,'GET',{user_id:this.user_id,courseware_id:id},
              res=>{ this.$router.push({path:'/section/courseware',query:{course_id:this.course_id,courseware_id:id}}); }
            )
          }
        },
        /* 添加用户视频/用户课件 END */



        /* 发布课程评论 */
        onClickPubEva:function () {
          if (this.user_id){
            let url=this.Global.server_url+'/user_course/insert_course_eva/';
            this.GlobalFunc.func_axios(url,'GET',{content:this.user_eva,user_id:this.user_id,course_id:this.course_id},
                res=>{this.reload(); this.list_tag_index=2;}
            )
          }else{
            this.GlobalFunc.open_login(this)
          }
        },
        /* 发布课程评论 END */

        /* 分页组件触发的方法 */
        on_click_page:function (ev) {
          this.course_eva_index = ev.children_cur_page;
          this.get_evaluation();
        }
        /* 分页组件触发的方法 END */

      }
    }
</script>

<style scoped>
  div,p,img,ul,li,h3{
    margin: 0;
    padding: 0;
    border: none;
  }
  .course_detail_list{
  }
  .course_detail_list .top_introduce{
    width: 780px;
    font-size: 14px;
    background: white;
    border-radius: 10px;
    padding: 20px 20px;
  }
  .course_detail_list .div_chapters .chapters ul{
    width: 780px;
    background: white;
    border-radius: 10px;
    padding: 20px 20px;
    margin-top: 10px;
    list-style: none;
  }
  .course_detail_list .div_chapters .chapters ul h3{
    margin-bottom: 20px;
  }
  .course_detail_list .div_chapters .chapters ul p{
    margin: 10px;
    font-size: 14px;
    font-weight: normal;
    color: gray;
  }
  .course_detail_list .div_chapters .chapters ul li{
    margin: 0 10px;
    font-size: 14px;
    padding: 10px 10px;
    border-radius: 10px;
    transition: background-color  0.3s,color 0.3s;
  }
  .course_detail_list .div_chapters .chapters ul li:hover{
    background: rgba(255, 192, 203, 0.36);
    color: #e9afb9;
    cursor: pointer;
  }

  .div_evaluations{
    padding-right: 50px;
  }
  .course_detail_list .top_evaluation{
    /*width: 780px;*/
    font-size: 14px;
    background: white;
    border-radius: 10px;
    padding: 20px 20px;
  }
  .course_detail_list .div_evaluations .top_evaluation .el-col:nth-child(2){
    text-align: center;
  }
  .course_detail_list .div_evaluations .evaluation{
    /*width: 780px;*/
    font-size: 14px;
    background: white;
    border-radius: 10px;
    padding: 20px 20px;
    margin-top: 10px;
  }
  .course_detail_list .div_evaluations .evaluation>.el-col>.el-row:nth-child(1)>.el-col{
    height: 32px;
    line-height: 32px;
    margin-bottom: 5px;
  }
  .course_detail_list .div_evaluations .evaluation>.el-col>.el-row:nth-child(2){
    line-height: 40px;
    margin:10px 0 0 20px;
  }
  .course_detail_list .div_evaluations .evaluation img{
    width: 32px;
    height: 32px;
    border-radius: 50px;
    object-fit: cover;
  }

</style>
