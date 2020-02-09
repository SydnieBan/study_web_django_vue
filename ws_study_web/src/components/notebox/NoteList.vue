<template>
    <div class="note_list">
      <!-- 头部 -->
      <el-row class="el_div">
        <el-col :span="12">
          <input type="checkbox">只看原创
        </el-col>
        <el-col :span="12">
          <el-row>
            <el-col :span="6">排序 ：</el-col>
            <el-col :span="6">默认</el-col>
            <el-col :span="6">按更新时间</el-col>
            <el-col :span="6">按访问量</el-col>
          </el-row>
        </el-col>
      </el-row>
      <!-- 头部 END -->
      <!-- 展示笔记 -->
      <div class="div_list">
        <!-- 笔记列表 -->
        <div class="div_list_dis">
          <div v-for="(item,index) in note_lists" @mouseenter="onMouseEnter(index)" @mouseleave="onMouseLeave">
            <el-row class="note_item">
              <el-col :span="24">

                <el-row style="height: 40px;">
                  <el-col :span="2" style="padding-left:10px;height: 40px;">
                    <div class="title_pre"></div>
                  </el-col>
                  <el-col :span="22" style="height:40px;line-height: 40px;">
                    <h4><span @click="toNoteDetail(item.id)" class="title">{{item.title}}</span></h4>
                  </el-col>
                </el-row>

                <el-row>
                  <p>{{item.content_editor}}</p>
                </el-row>

                <el-row>
                  <el-col :span="12">
                    <span>{{item.publish_date}}</span>
                    <span>|</span>
                    <span>阅读数 18928</span>
                    <span>|</span>
                    <span>评论数 18928</span>
                  </el-col>
                  <el-col :span="12" v-show="i===index">
                    <span style="color: #0099FF"> 置顶 </span>
                    <span> | </span>
                    <span style="color: #0099FF" @click="edit_note(item.id)"> 编辑 </span>
                    <span> | </span>
                    <span style="color: red" @click="delete_note(item.id)"> 删除  </span>
                  </el-col>
                </el-row>

              </el-col>
            </el-row>
          </div>
        </div>
        <!-- 笔记列表 END -->
        <!-- 分页 -->
        <div class="div_list_page">
          <div>
            <button-page-box style="height: 85px" :current_page="note_page_index" :page_size="note_page_items" :total="note_total" @click_page="on_click_page($event)"></button-page-box>
          </div>
        </div>
        <!-- 分页 END -->
      </div>
      <!-- 展示笔记 END -->
    </div>
</template>

<script>
    import ButtonPageBox from "../coursebox/ButtonPageBox";
    export default {
        name: "NoteList",
      components: {ButtonPageBox},
      data(){
          return{
            user_id:window.localStorage.getItem('user_id'),
            note_lists:[],
            note_page_index:1,
            note_page_items:5,
            note_total:0,
            i:null,
          }
      },
      inject:['reload'],
      created:function(){
        this.get_note();
        this.get_notes_number();
      },
      methods:{
        /* 获取笔记 */
        get_note:function () {
          let url =this.Global.server_url+'/note/get_note/';
          this.GlobalFunc.func_axios(url,'GET', {user_id:this.user_id,note_page_index:this.note_page_index,note_page_items: this.note_page_items},
            res=>{
              this.note_lists.splice(0);
              for (let ii in res){
                this.note_lists.push(res[ii]);
              }
            }
          );
        },
        /* 获取笔记 END */
        /* 获取笔记数量 */
        get_notes_number:function () {
          let url = this.Global.server_url + '/note/get_note_number/';
          this.GlobalFunc.func_axios(url, 'GET', {user_id: this.user_id},
            res=>{ this.note_total = res.note_num;}
          )
        },
        /* 获取笔记数量 END */

        /* 分页组件触发的方法 */
        on_click_page:function (ev) {
          this.note_page_index = ev.children_cur_page;
          this.get_note();
        },
        /* 分页组件触发的方法 END */

        /* 指向某个笔记 */
        onMouseEnter:function (index) {
          this.i = index;
        },
        onMouseLeave:function () {
          this.i = null;
        },
        /* 指向某个笔记 END */

        /* 跳转到笔记详情页 */
        toNoteDetail:function (note_id) {
          this.$router.push({path:'/note/note_detail',query:{note_id: note_id}})
        },
        /* 跳转到笔记详情页 END */

        /* 点击编辑 */
        edit_note:function (note_id) {
          // this.$router.push({path:'/changenote',query:{note_id: note_id}})
          this.$router.push({path:'/note/note_edit',query:{note_id: note_id}})
        },
        /* 点击编辑 END */

        /* 点击删除 */
        delete_note:function (note_id) {
          this.$confirm('确定要删除当前笔记?', '提示', {
            confirmButtonText: '确认',
            cancelButtonText: '取消',
          }).then(() => {
            let url =this.Global.server_url+'/note/delete_note/';
            this.GlobalFunc.func_axios(url, 'GET', {"note_id":note_id},
              res=>{ this.reload(); }
            )
          }).catch(() => {
          });
        },
        /* 点击删除 END */

      }
    }
</script>

<style scoped>
  div,span,h4{
    margin: 0;
    padding: 0;
    border: none;
  }
  .note_list{
    background-color: white;
  }
  .note_list .el_div{
    height: 50px;
    line-height: 50px;
    background-color: #cff1ff;
  }
  .note_list .el_div .el-col{
    height: 50px;
    padding: 0 10px;
  }

  .note_list .div_list .div_list_dis .note_item{
    width: 900px;
    height: 125px;
    background-color: white;
    border-bottom: 1px solid gray;
  }
  .note_list .div_list .div_list_dis .note_item .title_pre{
    width: 40px;
    height: 20px;
    border-radius: 2px;
    border: 1px solid rgba(255, 0, 0, 0.46);
    background-color: white;
    color: #bd0000;
    text-align: center;
    line-height: 20px;
    font-size: medium;
    margin-top: 10px;
  }
  .note_list .div_list .div_list_dis .note_item .title_pre:after{
    content: '原创';
    font-weight: bold;
    font-size: 14px;
  }

  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(1) .title{
    transition: color 0.5s;
  }
  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(1) .title:hover{
    cursor: pointer;
    color: red;
  }
  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(2){
    padding: 0 20px;
    height: 55px;
    margin: auto;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    -webkit-line-clamp: 2;
    font-size: 15px;
  }

  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(3){
    height: 30px;
    padding: 0 10px;
    line-height: 30px;
  }
  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(3) .el-col:nth-child(1){
    height: 30px;
    color: gray;
    font-size: 14px;
  }
  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(3) .el-col:nth-child(2){
    font-size: 16px;
    display: flex;
    justify-content: flex-end;
  }
  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(3) .el-col:nth-child(2) span{
    margin-right: 5px;
  }
  .note_list .div_list .div_list_dis .note_item .el-col .el-row:nth-child(3) .el-col:nth-child(2) span:nth-child(2n+1):hover{
    cursor: pointer;
  }
  .note_list .div_list .div_list_page{
    display: flex;
    justify-content: flex-end;
  }
</style>
