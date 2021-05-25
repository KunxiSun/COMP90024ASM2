<template>
  <div style="max-height:1000px; weight:250px; min-width:250px; text-align:center;">
    <h2 style="color: #30B08F">{{cityName}}</h2>
    <br/>
    <br/>
    <chart :options=tweet_chart style="width: 300px; height: 200px" v-show=this.chart_show></chart>
    <chart :options=aurin_chart style="width: 300px; height: 200px" v-show=this.chart_show></chart>
    <div v-show=!this.chart_show><br/><br/><h3>Its unemployment rate is not found on Aruin</h3></div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        'chart_show': (this.tweet_chart != null && this.aurin_chart != null)
      }
    },
    name: 'infowindow',
    props: [
      'cityName',
      'tweet_chart',
      'aurin_chart'
    ]
  }
</script>

<style lang="scss" scoped>
  .melbourne {
    padding: 20px;

    .student-icon {
      font-size: 28px;
    }
  }
</style>
