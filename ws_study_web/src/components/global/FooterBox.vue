<template>
    <div id="footer_box" class="footer_box">
      <div class="footer_box_inner">
        <el-row style="height:130px;">
          <el-col :span="10">
            <div class="footer_box_inner_left" >
              <el-row style="height: 20px">
                <el-col :span="12" :offset="6">
                  <div class="logo"><h1>LOGO</h1></div>
                </el-col>
              </el-row>
              <el-row>
                <el-col :offset="6">
                  <div class="word">让每一名用户都能有所学，有所得..............</div>
                </el-col>
              </el-row>
            </div>
          </el-col>
          <el-col :span="14">
            <div class="footer_box_inner_right">
                <el-row>
                  <el-col :span="8">
                    <div class="right-one">关于我们</div>
                    <div class="right-two">
                      <p>关于我们</p>
                      <p>联系我们</p>
                      <p>常见问题</p>
                    </div>
                  </el-col>
                  <el-col :span="8" style="height:130px;">
                    <div class="two">关注我们</div>
                    <div class="final-right-img">
                      <div class="img_content" style="margin-top: 10px;text-align: center">
                        <span> <a href="https://wx.qq.com/">
                          <icon name="微信" style="width: 30px;height: 30px"></icon>
                        </a></span><span> <a href="https://weibo.com/">
                          <icon name="weibo" style="width: 30px;height: 30px"></icon>
                        </a></span>
                      </div>
                    </div>
                  </el-col>
                  <el-col :span="8" style="height:130px;">
                    <div class="three">友情链接</div>
                  </el-col>
                </el-row>
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">
            <div class="bottom">
              <span>粤B2-20090191-26  | 京ICP备12020869号-2 | 京公网安备44010602000207 </span><br/>
              <span>©2014-2019 icourse163.org </span>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
</template>

<script>
    export default {
        name: "FooterBox",
      data() {
        return {
        };
      },
    }
</script>

<style scoped>
  .two,.three{
    color: white;
    margin-top: 20px;
    text-align: center;
  }
  /************最底层所在层样式*************/
  .bottom{
    text-align: center;
    color: gray;
    padding: 15px 0;
    box-sizing: border-box;
    height: 70px;
    font-size: 14px;
  }
  .footer_box{
    margin: 0;
    padding: 0;
    border: none;
    width: 100%;
    min-width: 1215px;
    height: 200px;
    background-color: #333333;
  }
  .footer_box .footer_box_inner{
    width: 1215px;
    margin: 0 auto;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  /************LOGO所在层样式*************/
  .footer_box .footer_box_inner_left{
    height: 130px;
  }
  .footer_box .footer_box_inner_right{
    height: 130px;
    padding-left: 100px ;
    box-sizing: border-box;
  }
  .logo{
    text-align: center;
    color: white;
  }
  .word{
    height: 20px;
    margin-top: -10px;
    color: white;
  }
  /************LOGO右面所在层样式*************/
  .footer_box .footer_box_inner_right .right-one{
    margin-top: 20px;
    font-size: 16px;
    text-align: center;
    color: white;
  }
  .footer_box .footer_box_inner_right .right-two  {
    text-align: center;
  }
  .right-two p{
    color: gray;
    font-size: 12px;
    height: 12px;
    transition: color 0.5s;
  }
  .right-two p:hover{
    cursor: pointer;
    color: lightskyblue;
  }
</style>
