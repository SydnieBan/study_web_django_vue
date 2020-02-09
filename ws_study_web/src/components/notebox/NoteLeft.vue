<template>
  <div class="note_left">
    <!-- 头像 -->
    <div class="second-a">
      <div>
        <img id="note_user_icon" :src="this.information.user_img" alt="图片不存在" style="width: 100%;height:100%;object-fit: cover;    border-radius: 50%;">
      </div>
      <ul>
        <li><span style="font-size: 16px;"><strong id="note_user_name2">{{information.user_name}}</strong></span>
        </li>
        <li><input type="button" id="btn" value="写笔记" @click="add_note"></li>
      </ul>
    </div>
    <!-- 头像 END -->
    <!-- 原创。。。 -->
    <div class="second-b">
      <div class="item-a" v-for="i in links" :key="i.item_text">
        <ul>
          <li class="li2">{{i.item_text}}</li>
          <li class="li1">{{i.item_number}}</li>
        </ul>
      </div>
    </div>
    <!-- 原创。。。 END -->
    <!-- 等级 -->
    <div class="second-c">
      <div class="c-a">
        <ul>
          <li>
            <span>等级：</span>
            <span><img :src="this.Global.img_url+'/images/note3.png'" alt="图片不存在"></span>
          </li>
          <li>
            <span>积分： 31</span>
          </li>
          <li>
            <span>勋章：</span>
            <span><img :src="this.Global.img_url+'/images/note4.svg'" alt="图片不存在" style="width: 20px;height: 22px;"></span>
          </li>

        </ul>
      </div>
      <div class="c-b">
        <ul>
          <li>
            <span>访问： 100w+</span>
          </li>
          <li>
            <span>排名： 2</span>
          </li>
        </ul>
      </div>
    </div>
    <!-- 等级 END -->

    <div class="classhot">
      <div class="second-d">
        <div class="d-a">
          <div class="divide"></div>
          <div><strong>分类专栏</strong></div>
        </div>
        <div class="d-b">
          <ul>
            <li>
              <div><img :src="this.Global.img_url+'/images/note5.jpg'" style="width: 22px;height: 22px" alt="图片不存在"></div>
              <div class="course">Python</div>
              <div><span style="color: gray;font-size: 14px">500篇</span>
              </div>

            </li>
            <li>
              <img :src="this.Global.img_url+'/images/note5.jpg'" style="width: 22px;height: 22px" alt="图片不存在">
              <div class="course">Java</div>
              <span style="color: gray;font-size: 14px">600篇</span>
            </li>
          </ul>
        </div>
      </div>
      <div class="second-e">
        <div class="e-a">
          <div class="divide"></div>
          <div><strong>归档</strong></div>
        </div>
        <div class="e-b">
          <div class="e-1">2019年8月</div>
          <div class="e-2">60篇</div>
        </div>
      </div>
      <div class="second-f">
        <div class="f-a">
          <div class="divide"></div>
          <div><strong>热门文章</strong></div>
        </div>
        <div class="f-b">
          <ul>
            <li>
              <div>python爬虫入门项目</div>
              <div style="font-size: small;color: gray">阅读数 125453</div>
            </li>

            <li>
              <div>IDEA自定义方法注解模板</div>
              <div style="font-size: small;color: gray">阅读数 105453</div>
            </li>

            <li>
              <div>关于Sql和MySQL语句执行顺序</div>
              <div style="font-size: small;color: gray">阅读数 95453</div>
            </li>
          </ul>
        </div>
      </div>
    </div>



  </div>
</template>

<script>
  export default {
    name: "NoteLeft",
    props:['information'],
    data() {
      return {
        links: [
          {"item_text": "原创", "item_number": "1000"},
          {"item_text": "粉丝", "item_number": "10000"},
          {"item_text": "喜欢", "item_number": "50"},
          {"item_text": "评论", "item_number": "10w+"}
        ]
      }
    },
    methods:{
      add_note:function f() {
        this.$router.push({path:'/note_add'}).catch(err => { console.log(err) })
      },
    }
  }
</script>

<style scoped>
  ul{
    margin: 0;
    padding: 0;
  }
  ul li {
    list-style: none;
  }

  .second-a {
    width: 300px;
    height: 89px;
    display: flex;
    border-bottom: 1px solid gray;
    background-color: white;

  }

  .second-a > div {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    padding: 15px;

  }
  .second-a ul li{
    padding: 10px;
  }
  #btn {
    width: 60px;
    height: 30px;
    background-color: rgba(8, 213, 129, 0.9);
    color: white;
    outline: none;
    border: none;
    border-radius: 5px;
  }

  #btn:hover {
    cursor: pointer;
  }

  /*b*/
  .second-b {
    width: 300px;
    height: 79px;
    border-bottom: 1px solid gray;
    text-align: center;
    display: flex;
    justify-content: space-around;
    background-color: white;
  }
  .second-b ul li {
    margin-top: 12px;
  }
  .li1 {
    font-size: 15px;
    color: #4a4a4a;
  }

  .li2 {
    font-size: 14px;
    color: gray;
  }

  /*b*/

  /*c*/

  .second-c {
    width: 300px;
    height: 120px;
    display: flex;
    justify-content: space-between;
    background-color: white;

  }

  .second-c .c-a {
    width: 140px;
    height: 120px;
  }

  .second-c .c-a ul li {
    padding: 5px;
    font-size: 16px;
    height: 18px;
    margin-top: 5px;
    margin-left: 14px;
  }

  .second-c .c-b {
    width: 150px;
    height: 120px;
  }

  .second-c .c-b ul li {
    padding: 5px;
    font-size: 16px;
    height: 18px;
    margin-top: 5px;
    margin-left: 5px;
  }

  /*c*/
  /* d */
  .second-d{
    width: 300px;
    height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    background-color: white;
    margin-top: 10px;
    text-align: center;
  }
  .d-a{
    display: flex;
  }
  .divide{
    width: 4px;
    height: 22px;
    background-color: red;
    margin-left: 10px;
    margin-right: 10px;
  }
  .second-d .d-b{
    width: 300px;
    height: 100px;
  }
  .d-b ul li{
    padding: 5px;
    font-size: 16px;
    height: 25px;
    margin-top: 5px;
    margin-left: 5px;
    display: flex;
    justify-content: space-between;
  }
  .d-b ul li .course{
    margin-left: -140px;
  }

  /*d*/
  /*e*/
  .second-e{
    width: 300px;
    height: 80px;
    background-color: white;
    margin-top: 10px;
    text-align: center;
  }
  .e-a{
    display: flex;
  }
  .second .second-e .e-a>div{
    margin-top: 10px;
  }

  .second .second-e .e-a .divide{
    width: 4px;
    height: 22px;
    background-color: red;
    margin-left: 10px;
    margin-right: 10px;
  }
  .second-e .e-b{
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
  }
  .second-e .e-b .e-1{
    margin-left: 10px;
  }
  .second-e .e-b .e-2{
    margin-right: 10px;
  }

  /*e*/
  /*fff*/
  .second-f{
    width: 300px;
    height: 210px;
    margin-top: 10px;
    background-color: white;
  }
  .f-a{
    display: flex;
  }
  .second .second-f .f-a>div{
    margin-top: 10px;
  }
  .second .second-f .f-a .divide{
    width: 4px;
    height: 22px;
    background-color: red;
    margin-left: 10px;
    margin-right: 10px;
  }
  .f-b{
    margin-top: 15px;
  }
  .second .second-f .f-b ul li{
    margin-left: 10px;
    height: 50px;

  }
  .second .second-f .f-b ul li>div{
    cursor: pointer;
    color: chocolate;
  }
  /*fff*/
</style>
