<template>
  <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="10px" class="login-css"  size="medium ">
    <p>用户登录</p>
    <el-form-item  prop="telephone">
      <el-input type="text" v-model="ruleForm.telephone" placeholder="手机号"></el-input>
    </el-form-item>
    <el-form-item prop="password">
      <el-input type="password" v-model="ruleForm.password" autocomplete="off" placeholder="密码"></el-input>
    </el-form-item>
    <el-form-item prop="checked" text-color="white" class="check-css">
      <el-checkbox v-model="ruleForm.checked">记住密码</el-checkbox>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import { validateTelRules,validatePasRules } from '../utils/validate';//导入验证规则
  import Bus from '../../Bus'
  export default {
    name:"Login",
    data() {
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
      };

      return {
        name: "login",
        ruleForm: {
          telephone:'',
          password: '',
          checked: false
        },
        rules: {
          telephone: [
            {validator: validateTel, trigger: 'blur'}
          ],
          password: [
            {validator: validatePass, trigger: 'blur'}
          ],
        },
      };
    },
    methods: {
      //表单提交
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let data_s = JSON.stringify(this.ruleForm);
            let data_json=JSON.parse(data_s);
            this.check_login(data_json)
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      check_login:function (data) {
        let url = this.Global.server_url + '/user/get_user/';

        this.axios.post(url, {
          user_tel: data.telephone,
          user_psw: data.password
        })
          .then(this.show_data)
          .catch(function (error) {
            console.log(error);
          });
      },
      show_data(res){
        let data = res.data;
        if (data.id) {
          window.localStorage.setItem('islogin',true);
          window.localStorage.setItem('token',data.token);
          window.localStorage.setItem('user_id',data.id);
          window.localStorage.setItem('telephone',this.ruleForm.telephone);

          Bus.$emit('login_state_change',true);
          // this.$router.push('/');
          this.$router.go(-1);
          //判断是否记住密码
          if (this.ruleForm.checked){
            window.localStorage.setItem('is_remember',true);
            window.localStorage.setItem('password',this.ruleForm.password);
          } else {
            window.localStorage.removeItem('is_remember');
            window.localStorage.removeItem('password');
          }
        }else {
          alert('登录失败');
        }
      }
    },
    created: function () {
      //验证是否记住密码，获取localStorage到界面
      if (window.localStorage.getItem('is_remember')) {
        this.ruleForm.telephone=window.localStorage.getItem('telephone');
        this.ruleForm.password=window.localStorage.getItem('password');
        this.ruleForm.checked=true;
      }else{
          this.ruleForm.telephone=window.localStorage.getItem('telephone');
      }
    }
  }
</script >

<style scoped>
  .login-css {
    padding: 60px 50px 10px 50px;
    /*background: #E9E9F2;*/
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }

  .login-css p {
    display: block;
    width: 100%;
    height: 30px;
    font-size: 23px;
    padding: 0 0 0 100px;
    margin-bottom: 10px;
  }
  .login-css .el-form-item{
    width: 300px;
    height: 60px;
    margin-bottom: 0px;
  }
  .login-css .el-input__inner{
    height: 30px;
  }
  .login-css .el-button {
    width:290px;
    background: #ffffff;
    color: black;
  }
  .login-css .el-button--primary{
    border:none;
  }
  .login-css .el-form-item.is-error .el-input__inner, .el-form-item.is-error .el-input__inner:focus, .el-form-item.is-error .el-textarea__inner, .el-form-item.is-error .el-textarea__inner:focus, .el-message-box__input input.invalid, .el-message-box__input input.invalid:focus{
    border-color:red;
  }
  .login-css .el-form-item__error{
    color: red;
  }
  .login-css .el-button{
    height: 30px;
    padding: 6px 20px;
  }
  .check-css{
    height: 40px !important;
  }
</style>
