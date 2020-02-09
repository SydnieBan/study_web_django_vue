<template>
  <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="10px"  class="register-css" size="medium ">
    <p>找回密码</p>
    <el-form-item  prop="telephone">
      <el-input type="text" v-model="ruleForm.telephone" placeholder="手机号"></el-input>
    </el-form-item>
    <el-form-item prop="password">
      <el-input type="password" v-model="ruleForm.password" autocomplete="off" placeholder="新密码"></el-input>
    </el-form-item>
    <el-form-item prop="check_code">
      <el-input type="text" v-model="ruleForm.check_code" placeholder="验证码" style="width: 175px"></el-input>
      <el-button @click="onSendCode" style="width: 110px;" :disabled="state">发送验证码</el-button>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">重置密码</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import { validateTelRules,validatePasRules } from '../utils/validate';//导入验证规则
  export default {
    name: "UserRetrievePassword",
    data(){
      //手机号验证
      const validateTel = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入手机号'));
        } else {
          if (validateTelRules(value)){
            callback();
          }else {
            return callback(new Error('手机号格式错误'));
          }
        }
      };1
      //密码验证
      const validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('*请输入密码'));
        } else {
          if (validatePasRules(value)){
            callback();
          }else {
            return callback(new Error('密码格式错误'));
          }
        }
      };
      //验证码验证
      const validateCode = (rule, value, callback) =>{
        if (value === ""){
          callback(new Error('请输入验证码'));
        }else if (value !== this.get_code) {
          callback(new Error('验证码错误!'));
        }else {
          callback();
        }
      }
      return{
        ruleForm: {
          telephone:'',
          password: '',
          check_code: ''
        },
        get_code:'',//验证码
        state:false,
        rules: {
          telephone: [
            {validator: validateTel, trigger: 'blur'}
          ],
          password: [
            {validator: validatePass, trigger: 'blur'}
          ],
          check_code: [
            {validator: validateCode, trigger: 'blur'}
          ],
        },
      }
    },
    methods:{
      //表单提交
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let data_s = JSON.stringify(this.ruleForm);
            let data_json = JSON.parse(data_s);
            this.FindPassword(data_json)
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      //发送验证码
      onSendCode:function () {
        if (this.ruleForm.telephone) {
          //b把按钮变成不可编辑状态
          this.state=true;
          setTimeout(() => {
            //5秒后按钮回复可编辑状态
            this.state=false;
          },5000);
          this.onGetCode(this.ruleForm.telephone);
        }else {
          alert('请输入手机号')
        }
      },
      onGetCode:function (tel) {
        let url = this.Global.server_url + '/user/get_verification_code/';

        this.axios.post(url, {
          tel: tel,
        })
          .then(this.get_data)
          .catch(function (error) {
            console.log(error);
          });
      },
      //解决异步获取不到数据
      get_data(res){
        let data = JSON.parse(res.data.vc);
        this.get_code = data.verification_code;
        console.log(this.get_code);
      },

      //找回密码
      FindPassword:function (data) {
        let url = this.Global.server_url + '/user/update_user_psw/';

        this.axios.post(url, {
          user_tel: data.telephone,
          user_psw: data.password
        })
          .then(this.show_data)
          .catch(function (error) {
            console.log(error);
          });
      },
      show_data(res) {
        let data = res.data;
        if (data.token) {
          console.log(data.result);
          window.localStorage.setItem('islogin',true);
          window.localStorage.setItem('token',data.token);
          window.localStorage.setItem('user_id',data.id);
          window.localStorage.setItem('telephone',this.ruleForm.telephone);
          // this.$router.push('/');
          this.$router.go(-1);
        }else {
          console.log(data.result);
        }
      },
    },
  }
</script>

<style scoped>
  .register-css {
    padding: 60px 50px 10px 50px;
    /*background: #E9E9F2;*/
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .register-css p {
    display: block;
    width: 100%;
    height: 30px;
    font-size: 23px;
    padding: 0 0 0 100px;
    margin: 0 0 10px 0;
  }
  .register-css .el-form-item{
    width: 300px;
    height: 60px;
    margin-bottom: 0px;
  }
  .register-css .el-input__inner{
    height: 30px;
  }
  .register-css .el-button--primary{
    border:none;
    width:290px;
    background: #ffffff;
    color: black;
  }
</style>
