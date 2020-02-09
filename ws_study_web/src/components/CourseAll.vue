<template>
    <div id="course_all" class="course_all">
      <div class="title">
        <h2>全部课程</h2>
      </div>
      <button-type-box @create_getCourse="on_create_get_course($event)" @click_direction="on_click_direction($event)" @click_classify="on_click_classify($event)" @click_difficulty="on_click_difficulty($event)"></button-type-box>
      <button-divide></button-divide>
      <button-sort-box @change_sort="on_change_sort($event)"></button-sort-box>
      <course-list-box :parameters="parameters" ref="all_course_list" @get_course_number="on_get_course_number($event)"></course-list-box>
      <button-page-box :current_page="parameters.page_index" :key="parameters.page_index" :total="course_number" :page_size="parameters.page_items" @click_page="on_click_page($event)"></button-page-box>
    </div>
</template>

<script>
    import ButtonTypeBox from "./coursebox/ButtonTypeBox";
    import ButtonSortBox from "./coursebox/ButtonSortBox";
    import ButtonPageBox from "./coursebox/ButtonPageBox";
    import CourseListBox from "./coursebox/CourseListBox";
    import ButtonDivide from "./coursebox/ButtonDivide";
    export default {
        name: "CourseAll",
      data(){
        return{
          parameters: {
            difficulty_name:"",
            direction_name:"",
            classify_name:"",
            page_index:1,
            page_items:30,
            sort_flag:0,
            integral_flag:0,
            search_text:''
          },
          course_number:0,
        }
      },
      methods:{
        /* 分类组件触发的方法 */
        on_create_get_course:function(ev){
          this.parameters.direction_name = ev.direction_name;
          this.parameters.classify_name = ev.classify_name;
          this.parameters.difficulty_name = ev.difficulty_name;
        },
        on_click_direction:function (ev) {
          this.parameters.direction_name = ev.direction_name;
          this.parameters.classify_name = "";
          this.parameters.page_index = 1;
        },
        on_click_classify:function (ev) {
          this.parameters.direction_name = ev.direction_name;
          this.parameters.classify_name = ev.classify_name;
          this.parameters.page_index = 1;
        },
        on_click_difficulty:function (ev) {
          this.parameters.difficulty_name = ev.difficulty_name;
          this.parameters.page_index = 1;
        },
        /* 分类组件触发的方法 END */

        /* 排序组件触发方法 */
        on_change_sort:function(ev){
          this.parameters.sort_flag = ev.sort;
        },
        /* 排序组件触发方法 END */

        /* 课程列表触发方法 */
        on_get_course_number:function(ev){
          // alert(`父组件获取课程个数：${ev.course_number}`);
          this.course_number = ev.course_number;
        },
        /* 课程列表触发方法 END */

        /* 分页组件触发的方法 */
        on_click_page:function (ev) {
          this.parameters.page_index = ev.children_cur_page;
        }
        /* 分页组件触发的方法 END */

      },
      components: {ButtonDivide, CourseListBox, ButtonPageBox, ButtonSortBox, ButtonTypeBox},
    }
</script>

<style scoped>
  div,h2{
    margin: 0;
    padding: 0;
    border: none;
  }
  .course_all{
    width: 100%;
    min-width: 1215px;
    /*background-color: #c9ebe4;*/
    background-color: rgba(201, 235, 228, 0.47);
    padding-top: 20px;
  }
  .course_all .title{
    width: 100%;
    height: 95px;
    line-height: 95px;
    background-color: white;
  }
  .course_all .title h2{
    width: 1215px;
    margin: 0 auto;
  }
</style>
