<template>
  <div :key="list_data.id" class="div-content">
    <el-row type="flex" justify="start">
      <div v-html="list_data.content">
      </div>
    </el-row>
  </div>
</template>

<script>
    export default {
        name: "ShowCourseContent",
        props:['list_data']
    }
</script>

<style scoped>
.div-content{
  /*height: 600px;*/
  margin: 0 auto;
  background: ghostwhite;
}
</style>
