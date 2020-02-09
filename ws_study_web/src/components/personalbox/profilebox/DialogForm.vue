<template>
  <div class="dialog">
    <div class="dia_content">
      <div class="box">
        <h3 class="title">修改资料</h3>
        <span class="close" @click="abandon">×</span>
      </div>
      <form action="">
        <p class="word">
          <span class="nc">昵称:</span>
          <input type="text" class="input_inner" :value="informations.user_name" ref="input1" @change="assigned1">
        </p>
        <p class="word">
          <span class="nc">性别:</span>
          <el-select v-model="value" clearable placeholder="请选择" ref="input2" @change="assigned2">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </p>
        <p class="word">
          <span class="nc">身份:</span>
          <input type="text" class="input_inner" ref="input3" @change="assigned3" :value="informations.identity">
        </p>
        <p class="word">
          <span class="nc">地址:</span>
          <input type="text" class="input_inner" ref="input4" @change="assigned4" :value="informations.address">
        </p>
        <div class="word">
          <span class="nc">简介:</span>
          <div class="bao">
                <textarea name="" id="area" maxlength="300" placeholder="300字以内" ref="input5" @change="assigned5" :value="informations.introduce">
                </textarea>
          </div>
        </div>
      </form>
      <div class="btn_group">
        <el-button class="cancel" @click="abandon">取消</el-button>
        <el-button type="primary" class="confirm" @click="send">确定</el-button>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: "Dialogform",
    props:['information','user_id'],
    data() {
      return {
        options: [{
          value: 1,
          label: '男'
        }, {
          value: 3,
          label: '女'
        }],
        value: (this.information.user_sex__name==='女')?3:1,
        news:{u_name:"",u_sex:"",u_identity:"",u_address:"",u_introduce:"",user_id:this.user_id},
        depiction:[],
        informations:{user_img:this.information.user_img, user_name:this.information.user_name,user_sex__name:this.information.user_sex__name,
          identity:this.information.identity,address:this.information.address,introduce:this.information.introduce},
      }
    },
    methods:{
      abandon:function(){
        this.$emit("gain",false)
      },
      send:function () {
        this.get_information();
      },
      assigned1:function(){
        this.news.u_name=this.$refs.input1.value;
        this.informations.user_name=this.news.u_name;
      },
      assigned2:function(val){
        if((val===1)||(val===3))
          this.news.u_sex=val;
      },
      assigned3:function(){
        this.news.u_identity=this.$refs.input3.value;
        this.informations.identity=this.news.u_identity;
      },
      assigned4:function(){
        this.news.u_address=this.$refs.input4.value;
        this.informations.address=this.news.u_address;
      },
      assigned5:function(){
        this.news.u_introduce=this.$refs.input5.value;
        this.informations.introduce=this.news.u_introduce;
      },
      /* 获取用户信息 */
      get_information:function(){
        let url=this.Global.server_url+'/user/update_user_info/';
        this.GlobalFunc.func_axios(url, 'POST', this.news,
          res=>{ this.$emit("reflesh"); }
        )
      },
      /* 获取用户的所有信息 END */
    },

  }
</script>

<style scoped>
  .dialog{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,.6);
    z-index: 999;
  }
  .dialog .dia_content{
    width: 502px;
    height: 450px;
    margin: 100px auto;
    background: #fff;
    padding: 16px;
    box-sizing: border-box;
  }
  .dia_content .box{
    overflow: hidden;
  }
  .dia_content  h3.title{
    font-size: 16px;
    color: #3d3d3d;
    float: left;
    height: 24px;
    line-height: 24px;
  }
  .dia_content .close{
    color: #999;
    font-size: 16px;
    margin-top: 16px;
    float: right;
    cursor: pointer;
    width: 24px;
    height: 24px;
    text-align: center;
    line-height:24px ;
  }
  .dia_content .word{
    margin-top: 10px;
    height: 40px;
    line-height: 40px;
    font-size: 14px;
    /*background: #82ff60;*/
  }
  .word .nc{
    overflow: hidden;
    margin-right: 8px;
    height: 40px;
    line-height: 40px;
    float: left;
    font-size: 14px;
    color: #4d4d4d;
  }
  .word .input_inner{
    width: 190px;
    height: 40px;
    padding: 0 15px;
    line-height: 100%;
    background-image: none;
    border-radius: 4px;
    text-shadow: none;
    text-align: start;
    outline: none;
    cursor: text;
    border: 1px solid #dcdfe6;
  }
  .word .bao #area{
    width: 396px;
    height: 54px;
    outline: none;
    border-radius: 4px;
    border: 1px solid #ccc;
    padding-top: 4px;
    padding-left: 14px;
    font-size: 14px;
    color: #4d4d4d;
  }
  /* ***************按钮********************* */
  .btn_group{
    margin-top: 50px;
    margin-left: 290px;
    overflow: hidden;
    display: flex;
  }
  .btn_group .cancel{
    width: 72px;
    height: 36px;
    outline: none;
    background: #e0e0e0;
    border-radius: 4px;
    font-size: 14px;
    color: #3d3d3d;
    border: none;
    margin-right: 16px;
    cursor: pointer;
  }
  .btn_group .confirm{
    width: 72px;
    height: 36px;
    background: rgba(51, 142, 222, 0.87);
    border-radius: 4px;
    outline: none;
    font-size: 14px;
    color: #3d3d3d;
    border: none;
    margin-right: 16px;
    cursor: pointer;
  }
  .btn_group>button:hover{
    opacity: 0.8;
  }
</style>
