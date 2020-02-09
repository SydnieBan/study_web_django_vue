<template>
    <div class="dialog-upload">
      <div class="content">
        <div class="vip-close">
          <h3 class="title">上传头像</h3>
          <i class="icon" @click="exit">×</i>
        </div>
        <div class="upload-area">
          <input type="file" class="image" @change="getFile">
        </div>
        <p class="note">图片宽度*高度至少为150*150像素，大小不超过2MB</p>
        <div class="btn-group">
          <el-button @click="exit">取 消</el-button>
          <el-button type="primary" @click="exit">确 定</el-button>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    name:'Diologheader',
    // props:['centerDialogVisible'],
    // created(){

    // },
    inject:['reload'],
    data() {
      return {
        centerDialog: true,
        photo_name:''
      };
    },
    methods:{
        exit:function () {
          this.centerDialog=false;
          console.log(this.photo_name);
          this.$emit("back",false);
          this.reload();
        },
      //输入框改变获取文件
      getFile(event){
        //获取文件属性
        var local_file=event.target.files[0];
        //获取文件名
        var local_file_name=local_file.name;
        let url = this.Global.server_url + '/user/upload_token/';
        this.GlobalFunc.func_axios(url,'GET',{"local_file_name":local_file_name},
        res=>{this.show_data(res,local_file)})  /* {"upload_token": token, "new_file_name": key} */
      },
      show_data:function(res,local_file){
        var qiniu = require('qiniu-js');
        let upload_token=res.upload_token;
        let new_file_name=res.new_file_name;
        let new_file=new File([local_file],new_file_name);
        var config={
          useCdnDomain: false, // 是否使用 cdn 加速域名，为布尔值，true 表示使用，默认为 false
          disableStatisticsReport:true, // 是否禁用日志报告，为布尔值，默认为false
          retryCount:6, // 上传自动重试次数（整体重试次数，而不是某个分片的重试次数）
          region: qiniu.region.z2 // 选择上传域名区域；当为 null 或 undefined 时，自动分析上传域名区域
        };
        var putExtra = {
          fname: "", // 文件原文件名
          params: {}, // 用来放置自定义变量
          mimeType: ["image/png", "image/jpeg", "image/gif"] // 限制上传文件类型
        };
        putExtra.params["x:name"]=new_file_name.split('.')[0];
        // qiniu.upload 返回一个 observable 对象用来控制上传行为，同时返回一个 subscription 对象
        var observable = qiniu.upload(local_file, new_file_name, upload_token, putExtra, config); // 上传的文件 + 文件资源名 + token + putExtra + config
        // observable 对象通过 subscribe 方法可以被 observer 所订阅，订阅同时会开始触发上传
        var subscription=observable.subscribe({
          next:res=>{},
          error:res=>{console.log(res)},
          complete:res=>{
            // console.log(res);
            //显示七牛云的前缀地址
            let qiniu_url=this.Global.img_url;
            //完整的图片地址
            let img_url=qiniu_url+'/'+res.key;
            //把返回的图片地址发送给父组件
            // this.$emit("change_img_url",img_url); # 直接点击确定刷新
            this.add_img_url(res.key);
          },
        });  // 上传开始
      },
      //拿到图片地址作为条件传给后台，添加到数据库
      add_img_url(res){
        let data={
          user_id:localStorage.getItem('user_id'),
          user_icon:res
        };
        let url = this.Global.server_url + '/user/update_user_icon/';
        this.GlobalFunc.func_axios(url,'GET',data,
          res=>{this.check_result(res)})
      },
      check_result:function (res) {
        this.reload()
      }

    }
  };
</script>

<style scoped>
    .dialog-upload{
      position: fixed;
      display: block;
      box-sizing: border-box;
      background: rgba(0,0,0,.6);
      z-index: 10000;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
    }
    .dialog-upload .content{
      margin: 50px auto 0 auto;
      width: 685px;
      height: 314px;
      padding: 25px;
      background-color: #fff;
      border-radius: 2px;
    }
    .image{
      width: 610px;
      height: 200px;
      margin: auto;
      opacity: 0;
      text-decoration: none;
      cursor: pointer;
      outline: none;
    }
    /**********模态框内容  ********************/
    .vip-close .title{
      font-size: 16px;
      float: left;
    }

    .vip-close .icon{
      width: 16px;
      height: 16px;
      margin-top: 18px;
      float: right;
      text-align: center;
      line-height: 8px;
      cursor: pointer;
    }
    .upload-area{
      position: relative;
      margin-top: 50px;
      width: 685px;
      height: 170px;
      background-color: rgba(0,0,0,.03);
      text-align: center;
      border: 1px dashed rgba(0,0,0,.08);
      overflow: hidden;
    }
    .content .note{
      font-size: 14px;
      color: #999;
      margin-bottom: 4px;
      margin-top: 4px;
    }
    .btn-group{
      float: right;
    }
</style>
