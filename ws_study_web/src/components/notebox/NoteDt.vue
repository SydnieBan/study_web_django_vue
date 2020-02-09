<template>
    <div class="note_dt">

      <div class="top">
        <div class="item-one"></div>
        <h3><span>{{this.note_info.title}}</span></h3>
      </div>

      <div class="tips">
        <ul>
          <li>{{this.note_info.publish_date}}</li>
          <li style="color: #bfbfbf">|</li>
          <li>阅读数 2w+</li>
          <li style="color: #bfbfbf">|</li>
          <li>文章标签：{{this.note_info.classify}}</li>
        </ul>
      </div>

      <div class="divide"></div>

      <div class="article">
        <span style="font-size: 14px;color: gray">版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。</span><br/>
        <span style="font-size: 14px;color: gray">本文链接：</span>
        <a :href="cur_url" style="font-size: 14px;text-decoration: none">{{cur_url}}</a>
        <div v-html="this.note_info.content_html"></div>
      </div>

    </div>
</template>

<script>
    export default {
        name: "NoteDt",
      data(){
          return{
            note_id:this.$route.query.note_id,
            note_info:{
              title:null,
              content_html:null,
              content_editor:null,
              publish_date:null,
              classify:null,
              mold:null
            }
            ,
            cur_url:window.location.href
          }
      },
      created:function(){
          this.get_note_info();
      },
      methods:{
          /* 获取笔记详情 */
        get_note_info:function () {
          let url =this.Global.server_url+'/note/get_note_info/';
          this.GlobalFunc.func_axios(url, 'GET', {"note_id":this.note_id},
            res=>{
              this.note_info.title = res[0].title;
              this.note_info.content_html = res[0].content_html;
              this.note_info.content_editor = res[0].content_editor;
              this.note_info.publish_date = res[0].publish_date;
              this.note_info.classify = res[0].classify;
              this.note_info.mold = res[0].mold;
            }
          )
        }
          /* 获取笔记详情 END */
      }
    }
</script>

<style scoped>
  div,ul,li{
    margin: 0;
    padding: 0;
    border: none;
  }
  .note_dt{
    background-color: white;
    padding: 10px 20px;
  }
  .note_dt .top{
    display: flex;
  }
  .note_dt .top .item-one{
    width: 40px;
    height: 20px;
    border-radius: 2px;
    border: 1px solid rgba(255, 0, 0, 0.46);
    background-color: white;
    color: #bd0000;
    text-align: center;
    line-height: 20px;
    font-size: medium;
    margin-top: 20px;
    margin-right: 20px;
  }
  .note_dt .top .item-one:after {
    content: '原创';
    font-weight: bold;
    font-size: 14px;
  }

  .note_dt .tips{
    height: 40px;
    line-height: 40px;
    display: flex;
  }
  .note_dt .tips ul{
    list-style: none;
    display: flex;
  }
  .note_dt .tips ul li{
    margin-left: 10px;
    color: gray;
    font-size: 14px
  }

  .note_dt .divide{
    height: 1px;
    background-color: gray;
    margin: auto;
  }

  .note_dt .article{
    margin-top: 20px;
  }
  .note_dt .article div{
    min-height: 525px;
    margin-top: 10px;
    background-color: white;
    word-break: break-word;
    padding: 20px;
  }

</style>
