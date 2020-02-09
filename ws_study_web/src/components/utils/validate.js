//手机号验证
export function validateTelRules(tel) {
  const reg_tel=/^1[35678]\d{9}$/;
  return reg_tel.test(tel)
}

//密码验证
export function validatePasRules(pwd) {
  const reg_pwd=/^\w{6,}$/;
  return reg_pwd.test(pwd)
}
