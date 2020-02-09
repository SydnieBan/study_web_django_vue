<template>
      <div class="div-css">
        <codemirror v-model="code" :options="cmOption" style="height:625px"></codemirror>
        <el-button type="primary" round class="btn-sub" @click="sub_code">提交运行</el-button>
      </div>
</template>

<script>

  // language
  import 'codemirror/mode/python/python.js'
  // theme css
  import 'codemirror/theme/base16-light.css'

  // require active-line.js
  import'codemirror/addon/selection/active-line.js'
  // closebrackets
  import'codemirror/addon/edit/closebrackets.js'
  // keyMap
  import'codemirror/mode/clike/clike.js'
  import'codemirror/addon/edit/matchbrackets.js'
  import'codemirror/addon/comment/comment.js'
  import'codemirror/addon/dialog/dialog.js'
  import'codemirror/addon/dialog/dialog.css'
  import'codemirror/addon/search/searchcursor.js'
  import'codemirror/addon/search/search.js'
  import'codemirror/keymap/emacs.js'
  export default {
    data() {
      const code ='print(123)'
      return {
        code,
        cmOption: {
          autoCloseBrackets: true,
          tabSize: 4,
          height:'625px',
          styleActiveLine: true,
          lineNumbers: true,
          line: true,
          mode: 'text/x-python',
          theme: 'base16-light',
          keyMap: "emacs"
        }
      }
    },
    methods:{
      sub_code:function () {
        this.send_code(this.code);
        // console.log(this.code);
      },
    //  axios
      send_code(code){
        let url = this.Global.server_url + '/course/get_editor_info/';

        this.axios.post(url, {
          code:code
        })
          .then(this.show_data)
          .catch(function (error) {
            console.log(error);
          });
      },
      show_data(res){
        if (res.data.code == "Success") {
          let data = res.data.output
          this.$emit('editor_result',data)
        } else {
          this.$emit('editor_result','Error')
        }
        // console.log(res);
      }
    }
  }
</script>

<style >
.div-css{
  height: 100%;
  position: relative;
  background-color: white;
}
.btn-sub{
  position: absolute;
  bottom: 10px;
  right: 20px;
}
  .vue-codemirror{
    height:100%;
  }
  .CodeMirror{
    height: 100%;
  }
</style>
