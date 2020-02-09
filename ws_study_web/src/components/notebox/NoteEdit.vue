<template>
    <div class="note_edit">
<!--      <vue-simplemde  v-model="note_content_editor"  ref="markdownEditor"/>-->


      <div class="editor">
        <quill-editor
          v-model="note_content_html"
          ref="myQuillEditor"
          :options="editorOption"
          @change="onEditorChange($event)" style="height: 500px">
        </quill-editor>
      </div>


      <div class="btn_note">
        <el-button type="info" @click="return_note">取消编辑</el-button>
        <el-button type="danger" @click="editnote">确定编辑</el-button>
      </div>
    </div>
</template>

<script>
    import VueSimplemde from "vue-simplemde";
    export default {
        name: "NoteEdit",
      components: {VueSimplemde},
      data(){
          return{
            note_id:this.$route.query.note_id,
            note_content_editor:null,
            note_content_html:null,
            editorOption: {
              theme: 'snow',
              placeholder: '请输入笔记内容',
            },
          }
      },
      created:function(){
        this.get_note_content();
      },
      methods:{
        /* 获取笔记内容 */
        get_note_content:function () {
          let url =this.Global.server_url+'/note/get_note_info/';
          this.GlobalFunc.func_axios(url, 'GET', {"note_id":this.note_id},
            res=>{
              this.note_content_html = res[0].content_html;
              this.note_content_editor = res[0].content_editor;
            }
          )
        },
        /* 获取笔记内容 END */

        /* editor */
        onEditorChange({editor, html, text}) {//内容改变事件，可以获取到当前文本内容
          this.note_content_html = html;
          this.note_content_editor = text;
        },
        /* editor END */

          /* 确定编辑笔记 */
        editnote:function () {
          let url =this.Global.server_url+'/note/update_note_info/';
          this.GlobalFunc.func_axios(url, 'POST', {"note_id":this.note_id,"content_editor":this.note_content_editor,"content_html":this.note_content_html},
            res=>{ this.$router.push('/note'); }
          )
        },
        /* 确定编辑笔记 END */
        /* 取消编辑 */
        return_note:function () {
          this.$router.push('/note');
        }
        /* 取消编辑 END */
      }

    }
</script>

<style scoped>
  /*@import '~simplemde/dist/simplemde.min.css';*/
  .note_edit{
    height: 760px;
    box-sizing: border-box;
    background-color: white;
    padding: 50px 20px;
  }
  .note_edit .btn_note{
    margin-top: 80px;
    margin-right: 10px;
    text-align: end;
  }

</style>
