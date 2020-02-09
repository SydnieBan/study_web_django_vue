<template>
    <div id="question_list" class="question_list">

      <el-row class="top_publish">
        <el-col :span="20">
          <el-input type="textarea" :rows="4"  placeholder="请输入内容" v-model="question_per"></el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="onClickPublish">我要发布</el-button>
        </el-col>
      </el-row>

      <el-row class="evaluation" v-for="(qu,index) in questions" :key="index">

        <el-col :span="24">


          <el-row>
            <el-col :span="2">
              <img :src="Global.img_url + '/'+ qu.user__userinfo__user_icon__icon_img" alt="">
            </el-col>
            <el-col :span="22" style="font-weight: bolder">
              {{qu.user__userinfo__user_name}}
            </el-col>
          </el-row>

          <el-row style="">
            {{qu.content}}
          </el-row>

          <el-row style="text-align: right">
            {{(type==='video')?qu.qv_date:qu.qc_date}}
          </el-row>

        </el-col>
      </el-row>

      <el-row style="display: flex;justify-content: flex-end">
        <div>
          <button-page-box style="width: auto;" :current_page="question_page_index" :page_size="question_page_items" :total="question_total" @click_page="on_click_page($event)"></button-page-box>
        </div>
      </el-row>

    </div>
</template>

<script>
    import ButtonPageBox from "../coursebox/ButtonPageBox";
    export default {
        name: "QuestionList",
      components: {ButtonPageBox},
      props:['video_id','courseware_id','type'],
      inject:['reload'],
      data(){
          return{
            user_id:window.localStorage.getItem('user_id'),
            questions:[], /* content    user__userinfo__user_name     user__userinfo__user_icon__icon_img   question_video__id   qv_date*/
                          /* content    user__userinfo__user_name     user__userinfo__user_icon__icon_img   question_courseware__id   qc_date*/
            // video_id:1003,
            question_per:'',
            question_page_index:1,
            question_page_items:5,
            question_total:0,
          }
      },
      created:function(){
        this.get_questions_number();
        this.get_questions();
      },
      methods:{
          /* 发布评论 */
        onClickPublish:function(){
          if (this.type==='video'){
            let url=this.Global.server_url+'/user_course/insert_question_video/';
            /* question_video_id */
            this.GlobalFunc.func_axios(url,'GET',{content:this.question_per,user_id:this.user_id,video_id:this.video_id,},
              res=>{ this.reload(); this.question_per=''; }
            );
          }
          else {
            let url=this.Global.server_url+'/user_course/insert_question_courseware/';
            /* question_courseware_id */
            this.GlobalFunc.func_axios(url,'GET',{content:this.question_per,user_id:this.user_id,courseware_id:this.courseware_id,},
              res=>{ this.reload(); this.question_per=''; }
            );
          }
        },
          /* 发布评论 END */

          /* 获取某视频的所有评论 */
          get_questions:function () {
            if (this.type==='video'){
              let url = this.Global.server_url + '/user_course/get_question_video/';
              this.GlobalFunc.func_axios(url, 'GET', {"video_id": this.video_id,"question_page_index":this.question_page_index,"question_page_items":this.question_page_items},
                res=>{ this.show_questions(this.questions, res) }
              )
            }
            else{
              let url = this.Global.server_url + '/user_course/get_question_courseware/';
              this.GlobalFunc.func_axios(url, 'GET', {"courseware_id": this.courseware_id,"question_page_index":this.question_page_index,"question_page_items":this.question_page_items},
                res=>{ this.show_questions(this.questions, res) }
              )
            }
          },
          get_questions_number:function () {
            if (this.type==='video'){
              let url = this.Global.server_url + '/user_course/get_question_number_video/';
              this.GlobalFunc.func_axios(url, 'GET', {"video_id": this.video_id},
                res=>{ this.question_total = res.question_number; }
              )
            }
            else{
              let url = this.Global.server_url + '/user_course/get_question_number_courseware/';
              this.GlobalFunc.func_axios(url, 'GET', {"courseware_id": this.courseware_id},
                res=>{ this.question_total = res.question_number; }
              )
            }
          },
        /* 获取某视频的所有评论 END */
        /* 显示某视频的所有评论 */
        show_questions:function (to_data, res) {
          to_data.splice(0);
          for (let i in res){
            to_data.push(res[i])
          }
        },
        /* 显示某视频的所有评论 END */

        /* 分页组件触发的方法 */
        on_click_page:function (ev) {
          this.question_page_index = ev.children_cur_page;
          this.get_questions();
        }
        /* 分页组件触发的方法 END */

      }
    }
</script>

<style scoped>
  div,img{
    margin: 0;
    padding: 0;
    border: none;
  }
  .question_list{
    padding: 15px;
  }
  .question_list .top_publish{
    font-size: 14px;
    border: 1px solid rgba(174, 174, 174, 0.47);
    border-radius: 10px;
    padding: 20px 20px;
  }
  .question_list .top_publish .el-col:nth-child(2){
    text-align: center;
  }

  .question_list .evaluation{
    font-size: 14px;
    border: 1px solid rgba(174, 174, 174, 0.47);
    border-radius: 10px;
    padding: 20px 20px;
    margin-top: 10px;
  }
  .question_list .evaluation>.el-col>.el-row:nth-child(1)>.el-col{
    height: 50px;
    line-height: 50px;
    margin-bottom: 5px;
  }
  .question_list .evaluation>.el-col>.el-row:nth-child(2){
    line-height: 40px;
    margin:10px 0 0 20px;
  }
  .question_list .evaluation img{
    width: 50px;
    height: 50px;
    border-radius: 50px;
    object-fit: cover;
  }

</style>
