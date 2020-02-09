<template>
    <div id="search" class="search">

      <div class="top" style="margin-bottom: 30px">
        <div class="search_div">
          <input placeholder="请输入内容" v-model="search_text" class="search_input" type="text" @keydown="onKeyDownSearch($event)">
          <el-button type="primary" icon="el-icon-search" class="el-button" @click="onSearchCourse">搜索</el-button>
        </div>
      </div>
      <course-list-box :parameters="parameters" :key="search_key"  ref="search_course_list" @get_course_number="on_get_course_number($event)"></course-list-box>
      <button-page-box :current_page="parameters.page_index" :key="parameters.page_index" :total="course_number" :page_size="parameters.page_items" @click_page="on_click_page($event)"></button-page-box>

    </div>
</template>

<script>
    import ButtonSortBox from "./coursebox/ButtonSortBox";
    import CourseListBox from "./coursebox/CourseListBox";
    import ButtonPageBox from "./coursebox/ButtonPageBox";
    export default {
      name: "Search",
      data(){
        return{
          search_text:this.$route.query.q,
          search_key:this.$route.query.q,
          parameters:{
            difficulty_name:'',
            direction_name:"",
            classify_name:"",
            page_index:1,
            page_items:30,
            sort_flag:0,
            integral_flag:0,
            search_text:this.search_text
          },
          course_number:0,
        }
      },
      components: {ButtonPageBox, CourseListBox, ButtonSortBox},
      created:function(){
        this.onSearchCourse();
      },
      methods:{
        onKeyDownSearch:function(ev){
          if(ev.keyCode===13){
            this.onSearchCourse();
          }
        },
        onSearchCourse:function () {
          if (this.search_text && this.search_text.trim()!==''){
            this.search_text=this.search_text.trim();
            this.parameters.page_index = 1;
            this.parameters.search_text = this.search_text;
            this.search_key = this.search_text;
            this.$router.push({ path: '/search', query: { q: this.parameters.search_text} }).catch(err => { console.log(err) })
          }else{
            this.search_text=''
          }
        },

        /* 课程列表触发方法 */
        on_get_course_number:function(ev){
          // alert(`搜索==父组件获取课程个数：${ev.course_number}`);
          this.course_number = ev.course_number;
        },
        /* 课程列表触发方法 END */

        /* 分页组件触发的方法 */
        on_click_page:function (ev) {
          this.parameters.page_index = ev.children_cur_page;
        }
        /* 分页组件触发的方法 END */

      },
      watch:{
        '$route'(to,from){
          if(to.name==='search'){
            this.search_text = this.$route.query.q;
            this.onSearchCourse();
          }
          if (this.content) this.content='';
        }
      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
  .search{
    width: 100%;
    min-width: 1215px;
    background-color: #f3f5f7;
  }
  .search .top{
    width: 100%;
    min-width: 1215px;
    margin: 0 auto;
    height: 130px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background-color: rgba(207,207,207,0.57);
  }
  .search .top .search_div{
    height: 40px;
    width: 850px;
    margin: 0 auto;
    box-sizing: border-box;
    display: flex;
    justify-content: flex-start;
  }
  .search .top .search_div .search_input{
    height: 40px;
    width: 730px;
    outline: none;
    border-radius: 10px 0 0 10px;
    font-size: 20px;
    border: none;
    box-sizing: border-box;
    padding-left: 5px;
  }
  .search .top .search_div .el-button{
    height: 40px;
    width: 120px;
    box-sizing: border-box;
    border-radius: 0 10px 10px 0;
    transition: color 0.5s;
    background-color: #93bbed;
    padding: 0;
    font-size: 16px;
  }
  .search .top .search_div .el-button:hover{
    color: gray;
  }

</style>
