import axios from 'axios'
// 使用方式：直接在 vue ： this.GlobalFunc.func_axios(url, param, func(){})

export default {

  /* func_axios */
  func_axios:function(url, type='GET', param=null, callback){

    /* GET 方法 */
    if (type.toUpperCase() === 'GET'){
      /* get方法 有参数 */
      if (param){
        axios.get(url,{params:param})
          .then(function (response) {
            callback(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
      /* get方法 无参数 */
      else{
        axios.get(url)
          .then(function (response) {
            callback(response.data)
          })
          .catch(function (error) {
            console.log(error);
          })
      }
    }
    /* POST 方法 */
    else{
      axios.post(url, param)
        .then(function (response) {
          callback(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  /* func_axios END*/

  /* open_login */
  // ev 为当前 this
  open_login(ev) {
    ev.$confirm('您未登录，是否去登录?', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
    }).then(() => {
      ev.$router.push({path:'/login'})
    }).catch(() => {
    });
  },
  /* open_login END */

}
