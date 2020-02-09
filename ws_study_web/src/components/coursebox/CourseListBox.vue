<template>
  <div class="course_list_box">
    <div class="dis_article_c" v-for="cou_item in course_list" :key="cou_item.course_id" @click="ToCourseDetail(cou_item.course_id)">
      <div class="dis_article_c_inner">
        <img :src="cou_item.course_img" alt="" style="z-index: 1000">

        <h3 v-html="KeyRegExp(cou_item.course_name, parameters.search_text)" v-if="parameters.search_text"></h3>
        <h3 v-else>{{cou_item.course_name}}</h3>

        <p v-if="parameters.search_text" style="font-size: 14px">
          <span v-html="KeyRegExp(cou_item.direction, parameters.search_text)"></span>
          <span style="color:black">/</span>
          <span v-html="KeyRegExp(cou_item.classify, parameters.search_text)"></span>
        </p>
        <p v-else>{{cou_item.difficulty}}</p>

        <p class="p_intro" style="font-size: 14px" v-html="KeyRegExp(cou_item.introduce, parameters.search_text)" v-if="parameters.search_text"></p>
        <p class="p_intro" v-else>{{cou_item.introduce}}</p>

        <p class="integral" v-html="KeyRegExp(cou_item.course_price, parameters.search_text)" v-if="parameters.search_text"></p>
        <p class="integral" v-else>{{cou_item.course_price}}</p>


      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "CourseListBox",
    props:['parameters'],
    data() {
      return {
        course_list: []
      }
    },
    created: function () {
      if (this.parameters.search_text) {
        // this.get_course_number_by_search_text();
        this.get_course_by_search_text();
      }else {
        this.get_course_number_by_condition();
        this.get_course_by_condition();
      }
    },
    watch:{
      parameters:{
        handler(newValue, oldValue){
          if (newValue.search_text){
            // alert('这是搜索')
            this.get_course_by_search_text();
          }
          else{
            // alert('这是分类')
            this.get_course_number_by_condition();
            this.get_course_by_condition();
          }
        },
        deep:true
      }
    },
    methods:{
      /* 获取课程 根据条件 */
      get_course_by_condition:function () {
        // alert(`获取课程时的排序方式：${this.parameters.sort_flag}`);
        let url = this.Global.server_url + '/course/get_course/';
        this.GlobalFunc.func_axios(url,'GET', this.parameters,
          res=>{ this.show_course_by_condition(this.course_list,res) }
        )
      },
      get_course_number_by_condition:function () {
        let url = this.Global.server_url + '/course/get_course_number/';
        this.GlobalFunc.func_axios(url,'GET', this.parameters,
          res=>{
            this.$emit('get_course_number',{"course_number":res.course_num});
          }
        )
      },
      /* 获取课程 根据条件 END */
      /* 显示课程 */
      show_course_by_condition:function(to_data, res){
        to_data.splice(0);
        if(res && res.length>0){
          for(let i=0;i<30 && i<res.length;i++){
            (res[i].integral===0)?(res[i].integral='免费'):(res[i].integral=res[i].integral+'积分');
            to_data.push(
              {"course_img":"http://pykpufs15.bkt.clouddn.com/images/course"+res[i].course_icon,"course_name":res[i].name,
                "course_price":res[i].integral,"course_id":res[i].id,"difficulty":res[i].difficulty__name,
                "introduce":res[i].introduce}
            )
          }
        }
      },
      /* 显示课程 END */



      /* 获取课程 根据搜索条件 */
      get_course_by_search_text:function () {
        // alert(`获取课程时的排序方式：${this.parameters.sort_flag}`);
        // http://localhost:8080/my_search/?q=html&page=3
        let url = this.Global.server_url + '/my_search/';
        this.GlobalFunc.func_axios(url,'GET', {q:this.parameters.search_text,page:this.parameters.page_index},
          res=>{ this.show_course_by_search_text(this.course_list,res.data, this) }
        )
      },
      /* 获取课程 根据搜索条件  END */
      /* 显示课程 */
      show_course_by_search_text:function(to_data, res, ev){
        to_data.splice(0);
        if(res.data && res.data.length>0){
          for(let i=0;i<30 && i<res.data.length;i++){
            (res.data[i].integral===0)?(res.data[i].integral='免费'):(res.data[i].integral=res.data[i].integral+'积分');
            to_data.push(
              {"course_img":"http://pykpufs15.bkt.clouddn.com/images/course"+res.data[i].course_icon,"course_name":res.data[i].name,
                "course_price":res.data[i].integral,"course_id":res.data[i].id,"difficulty":res.data[i].difficulty__name,
                "introduce":res.data[i].introduce, "classify":res.data[i].classify__name,"direction":res.data[i].classify__direction__name,}
            )
          }
          ev.$emit('get_course_number',{"course_number":res.course_num});
        }
      },
      /* 显示课程 END */


      /* 跳转到课程详情 */
      ToCourseDetail:function (id) {
        this.$router.push({ path: 'course_detail', query: { course_id: id} })
      },
      /* 跳转到课程详情 END */

      /* 关键字高亮显示 */
      KeyRegExp:function (str, key) {
          var key = key;
          key = '('+key.replace(/([\+\.\*\|\?\-\(\[\^\$])/g,'\\$1' ).replace(/\s+/g,'|')+')';//把匹配关键字中的正则符转义
          var patt = new RegExp(key ,'igm'); //传  igm  可避免关键词后面的空格造成文字不匹配问题
          var str2 = str.replace(patt,"<span style='color:#f00;'>$1</span>");
          return str2;
      }
      /* 关键字高亮显示 END */

    },
  }
</script>

<style scoped>
  body,html,h3 ,p{
    margin: 0;
    padding: 0;
  }
  .course_list_box{
    width: 1215px;
    /*height: 1920px;*/
    height: 100%;
    margin: 0 auto;
    background: white;
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
  }
  .dis_article_c{
    height: 300px;
    width: 243px;
    margin-bottom: 20px;
    transition: box-shadow 0.3s;
    padding: 10px 10px;
    box-sizing: border-box;
  }
  .dis_article_c:hover{
    cursor: pointer;
    box-shadow: 0 0 10px gray;
  }
  .dis_article_c_inner{
    height: 280px;
    width: 223px;
  }
  .dis_article_c_inner img{
    height: 135px;
    width: 223px;
  }
  .dis_article_c_inner h3{
    margin: 0;
    font-size: 18px;
    height: 56px;
  }
  .dis_article_c_inner p{
    color: gray;
  }
  .dis_article_c_inner .p_intro{
    height: 40px;
    /* 实现p标签多行超界省略号代替 */
    display: -webkit-box;
    -webkit-box-orient: vertical; /* 子元素显示方式:vertical-垂直 */
    overflow: hidden; /* 多余的隐藏 */
    -webkit-line-clamp:2; /* 有隐藏的则用省略号代替 */
  }
  .dis_article_c_inner .integral{
    color: #000;
  }
</style>
