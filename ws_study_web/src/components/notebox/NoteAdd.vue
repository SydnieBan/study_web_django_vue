<template>
  <div class="note_add">
    <div class="top">
      <el-button type="info" icon="el-icon-arrow-left" @click="return_note">返回</el-button>
      <el-input placeholder="请输入笔记标题" v-model="title" clearable></el-input>
    </div>

    <div class="editor">
      <quill-editor
        v-model="content_html"
        ref="myQuillEditor"
        :options="editorOption"
        @change="onEditorChange($event)" style="height: 500px">
      </quill-editor>
    </div>

    <div class="btn_note">
      <el-input placeholder="请输入笔记分类" v-model="classify" clearable style="width: 300px"></el-input>
      <el-button type="info" @click="cancle_note">取消发布</el-button>
      <el-button type="danger" @click="add_note">发布笔记</el-button>
    </div>

  </div>
</template>

<script>
    export default {
        name: "NoteAdd",
      data(){
          return{
            user_id:window.localStorage.getItem('user_id'),
            title: null,
            /* editor */
            content_html:'', /* html */
            content_editor:'', /* 文本 */
            editorOption: {
              theme: 'snow',
              placeholder: '请输入笔记内容',
            },
            /* editor END */
            classify:null
          }
      },
      created:function(){
      },
      methods:{
          /* 返回笔记列表页面 */
        return_note:function () {
          this.$router.push({path:'/note'})
        },
          /* 返回笔记列表页面 END */

        /* editor */
        onEditorChange({editor, html, text}) {//内容改变事件，可以获取到当前文本内容
          this.content_html = html;
          this.content_editor = text;
        },
        /* editor END */

        /* 取消发布笔记 */
        cancle_note:function(){
          this.$router.push('./note');
        },
        /* 取消发布笔记 END */
        /* 发布笔记 */
        add_note:function () {
          if (this.title){
            if (this.content_html){
              if (this.classify){
                this.$confirm('确定要发布当前笔记?', '提示', {
                  confirmButtonText: '确认',
                  cancelButtonText: '取消',
                }).then(() => {
                  let url =this.Global.server_url+'/note/insert_note_info/';
                  this.GlobalFunc.func_axios(url, 'POST',
                    {
                      "user_id":this.user_id,
                      "title":this.title,
                      "content_html":this.content_html,
                      "content_editor":this.content_editor,
                      "classify":this.classify
                    },
                    res=>{ this.$router.push('/note'); }
                  )
                }).catch(() => {
                });
              } else{
                this.$alert('笔记分类不能为空', '提示', {
                  confirmButtonText: '确定',
                });
              }
            } else{
              this.$alert('笔记内容不能为空', '提示', {
                confirmButtonText: '确定',
              });
            }
          } else{
            this.$alert('笔记标题不能为空', '提示', {
              confirmButtonText: '确定',
            });
          }
        }
        /* 发布笔记 END */

      }
    }
</script>

<style scoped>
  div{
    margin: 0;
    padding: 0;
    border: none;
  }
  .note_add{
    width: 1215px;
    padding-top: 20px;
    margin: 0 auto;
    background-color: white;
  }
  .note_add .top{
    display: flex;
  }

  .note_add .editor{
    background-color: white;
  }

  .note_add .btn_note{
    margin-top: 50px;
    text-align: end;
  }
</style>
