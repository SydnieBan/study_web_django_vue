<template>
    <div id="recommend_course" class="recommend_course">

      <h3 style="font-size: 18px">推荐课程</h3>

      <el-row class="recommend_per" v-for="(rec,index) in recommend_courses" :key="index" @click.native="onClickToPerCourse(rec.id)">

        <el-col :span="6">
            <el-image fit="cover" style="width: 80px;height: 60px;border-radius: 10px" :src="'http://pykpufs15.bkt.clouddn.com/images/course'+rec.course_icon"></el-image>
<!--            <el-image fit="cover" style="width: 88px;height: 80px" :src="this.Global.img_url+'/images/course'+rec.course_icon"></el-image>-->
        </el-col>

        <el-col :span="18" style="padding-left: 10px">

          <el-row>
            <el-col class="rec_name" :span="24">{{rec.name}}</el-col>
          </el-row>

          <el-row class="rec_info">
            <el-col :span="5">{{rec.difficulty__name}}</el-col>
            <el-col :span="2">
              <el-divider direction="vertical"></el-divider>
            </el-col>
            <el-col :span="12">{{rec.integral}}积分兑换</el-col>
          </el-row>

        </el-col>


      </el-row>

    </div>
</template>

<script>
    export default {
        name: "RecommendCourse",
      props:['course_id'],
      inject:['reload'],
      data(){
          return{
            recommend_courses:[]  /* id name integral difficulty__name course_icon*/
          }
      },
      created:function(){
          this.get_recommend_course();
      },
      methods:{
          /* 获取推荐课程 */
        get_recommend_course:function () {
          let url = this.Global.server_url + '/course/get_course_precourse/';
          this.GlobalFunc.func_axios(url, 'GET', {"course_id":this.course_id},
            res=>{ this.show_recommend_course(this.recommend_courses, res) }
          )
        },
          /* 获取推荐课程 END */
        show_recommend_course:function (to_data, res) {
          for (let i in res){
            to_data.push(res[i])
          }
        },

        /* 点击进入推荐课程详情 */
        onClickToPerCourse:function (course_id) {
          this.$router.push({path:'/course_detail',query:{course_id:course_id}});
          this.reload();
        },
        /* 点击进入推荐课程详情 END */
      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
  .recommend_course{
    /*width: 350px;*/
  }
  .recommend_course .recommend_per{
    height: 60px;
    margin: 40px 0;
    color: gray;
    transition:color 0.5s;
  }
  .recommend_course .recommend_per:hover{
    cursor: pointer;
    color: black;
  }
  .recommend_course .recommend_per>.el-col{
    height: 60px;
  }
  .recommend_course .recommend_per .rec_name{
    height: 30px;
    line-height: 30px;
    padding-left: 1px;
    font-size: 14px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space: nowrap;
  }
  .recommend_course .recommend_per .rec_info{
    height: 30px;
    line-height: 30px;
    padding-left: 1px;
    font-size: 14px;
  }
</style>
