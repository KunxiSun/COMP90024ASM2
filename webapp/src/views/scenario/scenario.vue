<template>
  <div id="scenario" style="padding: 20px">
    <el-tabs type="border-card">
      <el-tab-pane label="scenario1">
        <el-container>
          <el-header height="150px"><br/><h1 style="font-size: 50px">The attitude towards work and word cloud</h1><br/></el-header>
          <el-container>
            <h1 style="font-size: 20px">Sydney</h1>
            <el-main style="height:50vh;width: 50%;background-color: #ffffff">
              <chart style="float: left"  :options="charts.syd"></chart>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Sydney_before.png" title="Sydney_before.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud before covid</b></p>
              </div>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Sydney_after.png" title="Sydney_after.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud after covid</b></p>
              </div>
            </el-main>
          </el-container>
          <el-container>
            <h1 style="font-size: 20px">Melbourne</h1>
            <el-main style="height:50vh;width: 50%;background-color: #ffffff">
              <chart style="float: left"  :options="charts.melb"></chart>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Melbourne_before.png" title="Melbourne_before.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud before covid</b></p>
              </div>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Melbourne_after.png" title="Melbourne_after.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud after covid</b></p>
              </div>
            </el-main>
          </el-container>
          <el-container>
            <h1 style="font-size: 20px">Adelaide</h1>
            <el-main style="height:50vh;width: 50%;background-color: #ffffff">
              <chart style="float: left"  :options="charts.ade"></chart>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Adelaide_before.png" title="Adelaide_before.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud before covid</b></p>
              </div>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Adelaide_after.png" title="Adelaide_after.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud after covid</b></p>
              </div>
            </el-main>
          </el-container>
          <el-container>
            <h1 style="font-size: 20px">Perth</h1>
            <el-main style="height:50vh;width: 50%;background-color: #ffffff">
              <chart style="float: left"  :options="charts.pth"></chart>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Perth_before.png" title="Perth_before.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud before covid</b></p>
              </div>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Perth_after.png" title="Perth_after.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud after covid</b></p>
              </div>
            </el-main>
          </el-container>
          <el-container>
            <h1 style="font-size: 20px">Brisbane</h1>
            <el-main style="height:50vh;width: 50%;background-color: #ffffff">
              <chart style="float: left"  :options="charts.bris"></chart>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Brisbane_before.png" title="Brisbane_before.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud before covid</b></p>
              </div>
              <div style="padding-left: 10%; float: left; height:30vh">
                <img style="padding-left: 20%; float: left; height:30vh" src="./Brisbane_after.png" title="Brisbane_after.png" />
                <p style="font-size: 18px; padding-top: 365px" align = 'center'><b>Wordcloud after covid</b></p>
              </div>
            </el-main>
          </el-container>
        </el-container>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  // eslint-disable-next-line camelcase
  import { sa_employ_allcity_allyear } from 'api/apis'
  import 'echarts/lib/chart/line'
  import 'echarts/lib/component/polar'
  export default {
    name: 'HelloWorld',
    data () {
      return {
        currentDate: new Date(),
        charts: {}
      }
    },
    methods: {
      async getPageData () {
        // let data = {
        //   "arch_syd":
        //     {
        //       "2019": {"pos": 167, "neg": 68, "avg": 0.11},
        //       "2020": {"pos": 155, "neg": 83, "avg": 0.0547},
        //       "2021": {"pos": 48, "neg": 21, "avg": 0.0698}
        //     },
        //   "arch_melb":
        //     {
        //       "2019": {"pos": 69, "neg": 29, "avg": 0.0871},
        //       "2020": {"pos": 76, "neg": 42, "avg": 0.0853},
        //       "2021": {"pos": 41, "neg": 21, "avg": 0.0928}
        //     },
        //   "arch_ade":
        //     {
        //       "2019": {"pos": 74, "neg": 36, "avg": 0.0718},
        //       "2020": {"pos": 94, "neg": 48, "avg": 0.0591},
        //       "2021": {"pos": 75, "neg": 29, "avg": 0.1271}
        //     },
        //   "arch_pth":
        //     {
        //       "2019": {"pos": 32, "neg": 13, "avg": 0.087},
        //       "2020": {"pos": 48, "neg": 27, "avg": 0.0745},
        //       "2021": {"pos": 14, "neg": 9, "avg": 0.0867}
        //     },
        //   "arch_bris":
        //     {
        //       "2019": {"pos": 86, "neg": 32, "avg": 0.0981},
        //       "2020": {"pos": 71, "neg": 36, "avg": 0.0747},
        //       "2021": {"pos": 26, "neg": 13, "avg": 0.0832}
        //     }
        // }
        this.charts = {
          syd: {},
          melb: {},
          ade: {},
          pth: {},
          bris: {}
        }
        const ret = await sa_employ_allcity_allyear()
        let data = null
        if (ret.isSuccess) {
          data = ret.data
        } else {
          this.getPageData()
        }
        this.charts.syd = this.createPieChart(data.arch_syd)
        this.charts.melb = this.createPieChart(data.arch_melb)
        this.charts.ade = this.createPieChart(data.arch_ade)
        this.charts.pth = this.createPieChart(data.arch_pth)
        this.charts.bris = this.createPieChart(data.arch_bris)
      },
      createPieChart (data) {
        let chart = {
          legend: {
            top: '3.5%'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{b}'
          },
          title: [{
            show: true,
            text: 'The attitude towards work',
            x: 'center',
            y: 'bottom'
          },
            {
              text: 2019,
              left: '25%',
              top: '70%',
              textAlign: 'center',
              textStyle:{
                fontStyle:'normal',
                fontWeight:"lighter",
                fontFamily:"san-serif",
                fontSize:18
              }
            },
            {
              text: 2020,
              left: '50%',
              top: '70%',
              textAlign: 'center',
              textStyle:{
                fontStyle:'normal',
                fontWeight:"lighter",
                fontFamily:"san-serif",
                fontSize:18
              }
            },
            {
              text: 2021,
              left: '75%',
              top: '70%',
              textAlign: 'center',
              textStyle:{
                fontStyle:'normal',
                fontWeight:"lighter",
                fontFamily:"san-serif",
                fontSize:18
              }
            }
          ],
          // title: 'The attitude towards work',
          series: [{
            type: 'pie',
            radius: 60,
            center: ['25%','50%'],
            data:[
              {value: data['2019']['pos'], name:'Postive'},
              {value: data['2019']['neg'], name:'Negative'}
            ],
            itemStyle: {
              emphasis: {
                label: {
                  show: true,
                  formatter: '{d}%',
                  position: 'center'
                },
                labelLine: {
                  show: false
                }
              }
            },
            label: {
              normal: {
                position: 'inner',
                show: false
              }
            },
            encode: {
              itemName: 'Sentiment',
              value: 'Melbourne'
            }
          },
            {
              type: 'pie',
              radius: 60,
              center: ['50%','50%'],
              data:[
                {value: data['2020']['pos'], name:'Postive'},
                {value: data['2020']['neg'], name:'Negative'}
              ],
              itemStyle: {
                emphasis: {
                  label: {
                    show: true,
                    formatter: '{d}%',
                    position: 'center'
                  },
                  labelLine: {
                    show: false
                  }
                }
              },
              label: {
                normal: {
                  position: 'inner',
                  show: false
                }
              },
              encode: {
                itemName: 'Sentiment',
                value: 'Melbourne'
              }
            },
            {
              type: 'pie',
              radius: 60,
              center: ['75%','50%'],
              data:[
                {value: data['2021']['pos'], name:'Postive'},
                {value: data['2021']['neg'], name:'Negative'}
              ],
              itemStyle: {
                emphasis: {
                  label: {
                    show: true,
                    formatter: '{d}%',
                    position: 'center'
                  },
                  labelLine: {
                    show: false
                  }
                }
              },
              label: {
                normal: {
                  position: 'inner',
                  show: false
                }
              },
              encode: {
                itemName: 'Sentiment',
                value: 'Melbourne'
              }
            }]
        }
        return chart
      },
      createS2 () {
        let scenario2 = []
        scenario2[0] = {
          title: {
            text: 'Negative Rate of Job Related Tweets',
            x: 'center',
            y: 'top',
            textAlign: 'left',
            textStyle: {
              fontStyle: 'normal',
              fontWeight: 'bold',
              fontFamily: 'san-serif',
              fontSize: 18
            }
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: this.s2_1Data.x
          },
          yAxis: {
            name: '',
            type: 'value'
          },
          series: [{
            data: this.s2_1Data.y,
            type: 'line',
            areaStyle: {}
          }]
        }
        ///////Chart 2
        scenario2[1] = {
          title: {
            text: 'Education Background (Grade 12+)',
            x: 'center',
            y: 'bottom',
            textAlign: 'left',
            textStyle: {
              fontStyle: 'normal',
              fontWeight: 'bold',
              fontFamily: 'san-serif',
              fontSize: 18
            }
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: this.s2_2Data.x
          },
          yAxis: {
            name: '',
            type: 'value'
          },
          series: [{
            data: this.s2_2Data.y,
            type: 'line',
            areaStyle: {}
          }]
        }
        return scenario2
      },
      createS3 () {
        let scenario3 = []
        scenario3[0] = {
          title: {
            text: 'Negative Rate of Job Related Tweets',
            x: 'center',
            y: 'top',
            textAlign: 'left',
            textStyle: {
              fontStyle: 'normal',
              fontWeight: 'bold',
              fontFamily: 'san-serif',
              fontSize: 18
            }
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: this.s3_1Data.x
          },
          yAxis: {
            name: '',
            type: 'value'
          },
          series: [{
            data: this.s3_1Data.y,
            type: 'line',
            areaStyle: {}
          }]
        }
        ///////Chart 2
        let source = [
          ['Job Type']
        ]
        let series = []

        let title = []

        let index = 0
        let gap = 0
        let row = 1
        let column = 0
        let cityNames = ['Greater Sydney', 'Greater Melbourne', 'Greater Brisbane', 'Greater Adelaide', 'Greater Perth']
        for (let key in this.s3_2Data['Greater Sydney']) {
          source.push([key])
        }
        cityNames.forEach(city => {
          column += 1
          if (column === 3) {
            row += 1
          }
          if (column === 2) {
            index = 1
          } else {
            index = 0
          }
          if (column > 2) {
            column = 1
          }
          if (row > 1 && column === 1) {
            gap += 12
          }
          let total = 0
          for (let key in this.s3_2Data[city]) {
            total += this.s3_2Data[city][key]
          }
          this.s3_2Data[city]['total'] = total
          for (let index = 0; index < source.length; index++) {
            if (index === 0) {
              source[index].push(city)
            } else {
              source[index].push((this.s3_2Data[city][source[index][0]] / this.s3_2Data[city]['total']).toFixed(2))
            }
          }
          series.push({
            type: 'pie',
            radius: 60,
            center: [(20 * (row) + gap).toString() + '%', (25 * (column) + 18* (index)).toString() + '%'],
            itemStyle: {
              emphasis: {
                label: {
                  show: true,
                  formatter: '{d}%',
                  position: 'center'
                },
                labelLine: {
                  show: false
                }
              }
            },
            label: {
              normal: {
                position: 'inner',
                show: false
              }
            },
            encode: {
              itemName: 'Job Type',
              value: city
            }
          })
          title.push({
            text: 'Occupation Distribution',
            x: 'center',
            y: 'bottom',
            textAlign: 'left',
            textStyle: {
              fontStyle: 'normal',
              fontWeight: 'bold',
              fontFamily: 'san-serif',
              fontSize: 18
            }
          })
          title.push({
            text: city.replace('Greater ',''),
            left: (20 * (row) + gap).toString() + '%',
            top: (41* (column) + (1) * (index)).toString() + '%',
            textAlign: 'center',
            textStyle:{
              fontStyle:'normal',
              fontWeight:"lighter",
              fontFamily:"san-serif",
              fontSize:18
            }
          })
        })
        scenario3[1] = {
          legend: {
            type: 'scroll',
            top: 'top'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{b}'
          },
          dataset: {
            source: source
          },
          title: title,
          series: series
        }
        return scenario3
      }
    },
    mounted () {
      this.getPageData()
    }
  }
</script>

<style lang="scss" scoped>
  .scenario {
    padding: 20px;
  }
  @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }
</style>
