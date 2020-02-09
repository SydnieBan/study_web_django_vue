<template>
    <div class="panel">
        <div class="top">
          <el-row type="flex" justify="start">
            <el-col :span="1" class="left-nav">
            <!--    左侧导航          -->
              <div class="left-center">
                <button type="button" class="btn-select" @click="show_title =!show_title" ><i class="el-icon-s-unfold" style="font-size: 18px"><br><span style="font-size: 14px">章节</span></i></button>
                <button type="button" class="btn-select" @click="show_sub =!show_sub"><i class="el-icon-chat-dot-square" style="font-size: 18px"><br><span style="font-size: 14px">问答</span></i></button>
                <button type="button" class="btn-select"><i class="el-icon-edit" style="font-size: 18px"><br><span style="font-size: 14px">评论</span></i></button>
              </div>
            </el-col>
            <el-col :span="6" class="show-content">
              <happy-scroll color="rgba(0,0,0,0.5)" size="5" resize>
                 <show-content :list_data="list_data"></show-content>
              </happy-scroll>
            </el-col>
            <!--     章节进入       -->
            <transition name="el-zoom-in-top">
              <el-col :span="6" :push="1" class="show-title" v-show="show_title">
                <el-input placeholder="输入关键字进行过滤" v-model="filterText"  prefix-icon="el-icon-search"></el-input>
                    <el-tree
                      class="filter-tree"
                      :data="data"
                      :props="defaultProps"
                      node-key="id"
                      accordion
                      check-on-click-node
                      :default-expanded-keys="[expand]"
                      :default-checked-keys="[checked]"
                      :filter-node-method="filterNode"
                      @node-click="get_data()"
                      ref="tree"
                      style="background: ghostwhite;min-height: 585px">
                    </el-tree>
              </el-col>
            </transition>
            <!--    编辑器        -->
            <el-col :span="11" class="editor-panel">
              <editor-python @editor_result="editor_result"></editor-python>
            </el-col>
            <!--    编辑器输出屏幕       -->
            <el-col :span="6" class="show-editor-result">
              <div style="height: 625px;overflow-y: scroll">{{result}}</div>
            </el-col>
            <!--    发布问题        -->
            <transition name="el-zoom-in-top">
            <el-col :span="6" class="sub-question" v-if="show_sub">
              <sub-question :param="param" @close_question="close_question"></sub-question>
            </el-col>
            </transition>
          </el-row>
        </div>
        <div class="main">
          <el-row type="flex" justify="start" class="select-title">
            <el-col :span="2" :push="4" class="s-col">课程提问</el-col>
            <el-col :span="2" :push="5" class="s-col">课程评价</el-col>
            <el-col :span="2" :push="6" class="s-col">课程笔记</el-col>
          </el-row>
          <el-row style="height: 100%">
            <el-col :span="18" class="question-css">
              <question-list :courseware_id="courseware_id.courseware_id" :type="'courseware'" :key="courseware_id.courseware_id"></question-list>
            </el-col>
            <el-col :span="6" class="course-pro-css">
              <recommend-course :course_id="course_id.course_id"></recommend-course>
            </el-col>
          </el-row>
        </div>
    </div>
</template>

<script>
  import ShowCourseContent from './coursewarebox/ShowCourseContent'
  import Editor from './coursewarebox/Editor'
  import ReleaseCoursewareQuestion from './coursewarebox/ReleaseCoursewareQuestion'
  import RecommendCourse from "./coursedetailbox/RecommendCourse";
  import QuestionList from "./videobox/QuestionList";
    export default {
      name: "Courseware",
      inject:['reload'],
      data() {
        return {
          show_title:false,
          show_sub:false,
          //右侧内容
          list_data:{
            id:'',
            content:''
          },
          //课程id
          course_id:{course_id: this.$route.query.course_id},
          //课件id
          courseware_id:{courseware_id:this.$route.query.courseware_id},
          //默认展开,选中
          expand_first:this.$route.query.courseware_id,
          expand:[this.expand_first],
          checked_first:this.$route.query.courseware_id,
          checked:[this.checked_first],
          //右侧标题
          courseware_title:'',
          //关键词过滤
          filterText: '',
          //左侧列表
          data:[],
          //data数据默认值
          defaultProps: {
            children: 'children',
            label: 'label'
          },
          //默认显示输出
          result:'',
          //传给发布问题的条件
          param:{
            p_user_id:17,
            p_courseware_id:'',
          }
        }
      },
      components: {
        QuestionList,
        RecommendCourse,
        "show-content": ShowCourseContent,
        'editor-python':Editor,
        "sub-question":ReleaseCoursewareQuestion
      },
      methods: {
        //过滤关键词方法
        filterNode(value, data) {
          if (!value) return true;
          return data.label.indexOf(value) !== -1;
        },
        /* 获取课件列表 根据id */
        onGetListCourseware:function () {
          let url = this.Global.server_url + '/course/get_courseware_chapter/';

          this.GlobalFunc.func_axios(url,'GET', this.course_id,
            res=>{ this.show_course(this.data,res) }
          )
        },
        /* 获取课程 根据条件 END */
        show_course:function(to_data, res){
          for(let i=0;i<res.length;i++){
            to_data.push({id: res[i].id, label: res[i].name, children:[]});
            let list=res[i].sections;
            if (list !== null) {
              for (let j=0;j<list.length;j++){
                to_data[i].children.push({id:list[j].section_id ,label:list[j].section_name})
              }
            }
          }
        },
        //通过key获取
        get_data:function () {
          //获取选择的id
          let chose=this.$refs.tree.getCheckedKeys();
          if (chose.length > 1) {
            if (chose.length == 2) {
              this.courseware_id.courseware_id=chose[1];
              this.$router.push({path:'/section/courseware',query:{course_id:this.course_id.course_id,courseware_id:this.courseware_id.courseware_id}});
              this.reload();
              //给发布评论的id赋值
              this.param.p_courseware_id = chose[1];
              this.onGetCoursewareInfo();

            }
          }else {
            //课件id
            this.courseware_id.courseware_id=chose[0];
            //给发布评论的id赋值
            this.param.p_courseware_id = chose[0];
            this.$router.push({path:'/section/courseware',query:{course_id:this.course_id.course_id,courseware_id:this.courseware_id.courseware_id}});
            this.reload();
            this.onGetCoursewareInfo();
          }
          //清空选择数组
          this.$refs.tree.setCheckedKeys([]);
        },
        //获取课件axios
        onGetCoursewareInfo:function () {
          let url = this.Global.server_url + '/course/get_courseware_info/';

          this.GlobalFunc.func_axios(url,'GET', this.courseware_id,
            res=>{ this.show_courseware(this.list_data,res) }
          )
        },
        show_courseware:function(to_data, res){
          to_data.id=res[0].id;
          to_data.content= res[0].content;
          // 关闭章节页
          this.show_title=false;
        },
        //获取编辑的结果
        editor_result:function (data) {
          this.result = data;
        },
        //发布问题关闭条件传值
        close_question:function (data) {
          this.show_sub = data
        }
      },
      watch:{
        filterText(val) {
          this.$refs.tree.filter(val);
        }
      },
      created() {
        //获取课程列表
        this.onGetListCourseware();
        this.onGetCoursewareInfo()
      }

    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }

  .main{
    width: 1215px;
    margin: 0 auto;
    height: 600px;
    /*background: red;*/
  }

  /*************** top-begin******************/
  .top{
    /*background: #766ee1;*/
  }
  .left-nav{
    background: #FFFFFF;
    height: 625px;
  }
  .left-center{
    margin-top: 195px;
  }
  .btn-select{
    width: 100%;
    height: 50px;
    border: none;
    outline: none;
    background:  #FFFFFF;
    color: #606266;
    margin-bottom: 5px;
  }
  .btn-select:hover{
    background: #ECF5FF;
    color: #409EFF;
    cursor: pointer;
  }
  .show-content{
    background: ghostwhite;
    height: 625px;
    padding: 15px 10px 0 10px;
    box-sizing: border-box;

  }
  .show-title{
    position: absolute;
    /*background: #8c19f5;*/
    height: 625px;
  }
  .editor-panel{
    background: white;
    height: 625px;
  }
  .show-editor-result{
    background: ghostwhite;
    height: 625px;
  }
  .sub-question{
    position: absolute;
    right: 0;
    /*background: #c49aff;*/
    height: 625px;
  }
  /*************** top-end ******************/
  /*************** main-start ******************/
  .select-title{
    font-size: 20px;
    padding: 10px 0;
    background: white
  }
  .s-col:hover{
    color:gray;
    cursor: pointer;
  }
  /*.question-css{*/
  /*  background: #c49aff;*/
  /*  height: 100%;*/
  /*}*/
  /*.course-pro-css{*/
  /*  background: #00d6ff;*/
  /*  height: 100%;*/
  /*}*/
  /*************** main-end ******************/
</style>
