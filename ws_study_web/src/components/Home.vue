<template>
    <div id="home" class="home">
      <rotation-chart-box></rotation-chart-box>
      <ul>
        <li v-for="(flag,index) in tags">
          <div class="sect-four-top">
            <div >{{flag.title_name}}</div>
            <div class="four-top-bottom" @click="onToCourseClassify(index)" :key="index">{{flag.title_right}}</div>
          </div>
          <home-course-list-box :flag="flag"></home-course-list-box>
        </li>
      </ul>
      <home-teacher-list-box></home-teacher-list-box>
      <nav-fixed></nav-fixed>
    </div>
</template>

<script>
    import RotationChartBox from "./homebox/RotationChartBox";
    import HomeCourseListBox from "./homebox/HomeCourseListBox";
    import HomeTeacherListBox from "./homebox/HomeTeacherListBox";
    import NavFixed from "./global/NavFixed";
    export default {
        name: "Home",
      data(){
          return{
            tags:[
              {"title_name":"新手入门","title_right":"查看全部>>","left_img":this.Global.img_url+"/images/left_first.jpg", "data_info":[]},
              {"title_name":"新上好课","title_right":"查看全部>>","left_img":this.Global.img_url+"/images/left_second.jpg", "data_info":[]},
              {"title_name":"精品课程","title_right":"查看全部>>","left_img":this.Global.img_url+"/images/left_third.jpg", "data_info":[]},
              {"title_name":"技术提升","title_right":"查看全部>>","left_img":this.Global.img_url+"/images/left_four.jpg", "data_info":[]},
              {"title_name":"实战课程","title_right":"查看全部>>","left_img":this.Global.img_url+"/images/left_five.jpg", "data_info":[]},
            ],
          }
      },
      components: {NavFixed, HomeTeacherListBox, HomeCourseListBox, RotationChartBox},
      methods:{
        get_new_course:function (data_one,difficulty_name,sort_flag) {
            let url = this.Global.server_url + '/course/get_course/';
            // get
            this.axios.get(url,{
              params:{
                difficulty_name:difficulty_name,
                direction_name:"",
                classify_name:"",
                page_index:1,
                page_items:8,
                sort_flag:sort_flag,
                integral_flag:0,
              }
            })
              .then(function (response) {
                // console.log(response.data);
                  for(let i=0;i<8;i++){
                    if (response.data[i].integral == 0){
                      response.data[i].integral='免费'
                    }
                    else {
                      response.data[i].integral=response.data[i].integral+'积分'
                    }
                    data_one.push(
                      {"course_img":"http://pykpufs15.bkt.clouddn.com/images/course"+response.data[i].course_icon,"course_name":response.data[i].name,
                        "course_price":response.data[i].integral,"course_id":response.data[i].id}
                    )
                  }
              })
              .catch(function (error) {
                console.log(error);
              });
          },
        onToCourseClassify:function (index) {
          if (index === 0 || index === 1) {
            this.$router.push('/course_free');
          }
          else if (index === 2) {
            this.$router.push('/course_unique');
          }
          else if (index === 3 || index === 4) {
            this.$router.push('/course_all');
          }

        }
      },
      created: function () {
        this.get_new_course(this.tags[0].data_info,'入门',0)//新手入门课程
        this.get_new_course(this.tags[1].data_info,'',0)//新上好课课程
        this.get_new_course(this.tags[2].data_info,'',3)//精品课程
        this.get_new_course(this.tags[3].data_info,'中级',0)//技术提升课程
        this.get_new_course(this.tags[4].data_info,'高级',0)//实战课程

      },
    }
</script>

<style scoped>
  div,ul,li{
    margin: 0;
    padding: 0;
    border: none;
  }
  ul{
    list-style: none;
    margin-bottom: 30px;
  }
  .home{
    width: 100%;
    background-color: #eaeaea;
    min-width: 1215px;
    padding: 30px 0;
  }
  .home li{
    margin-top: 30px;
  }
/********************************************/
  .sect-four-top{
    width: 1215px;
    height: 50px;
    text-align: center;
    margin: auto;
    display: flex;
    justify-content: space-between;
  }
 .sect-four-top>div{
    font-size: 18px;
    line-height: 50px;

  }
   .sect-four-top .four-top-bottom:hover{
    color: #766ee1;
    cursor: pointer;
  }
/********************************************/
</style>
