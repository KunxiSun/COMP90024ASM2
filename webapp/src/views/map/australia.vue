<template>
  <div class="melbourne">
    <div id="map" style="height: 100vh; width: 80%; display: inline-block">
    </div>
    <div style="height: 100vh; width: 20%; display: inline-block" >
      <el-table
        empty-text="Empty"
        ref="multipleTable"
        :data="tableData"
        style="height: 100vh; width: 100%"
        :border=true>
        <el-table-column label="rank" prop="index" width="55" align="center"></el-table-column>
        <el-table-column label="keyword" prop="word" align="center"></el-table-column>
        <el-table-column label="zone" prop="zone" align="center"></el-table-column>
        <el-table-column label="rate" prop="rate" align="center"></el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
  import popWindowComponent from '../../components/popWindow'
  import { employ_allcity, wordfrequency_allcity_allyear } from 'api/apis'
  import Vue from 'vue'
  export default {
    mounted () {
      this.initMap()
      this.getPageData()
    },
    data () {
      return {
        showDialog: false,
        s4Data: null,
        tableData: [],
        map: null,
        infowindow: null,
        clickSection: false,
        rank: null,
        cityNameMessage: null
      }
    },
    methods: {
      async colorMap () {
        let colors = this.gradient('#ffffff', '#ff9900', 7)
        this.rank.forEach(each => {
          if (each['negative'] > 100) {
            each['color'] = colors[6]
          } else if (each['negative'] > 60) {
            each['color'] = colors[5]
          } else if (each['negative'] > 30) {
            each['color'] = colors[4]
          } else if (each['negative'] > 20) {
            each['color'] = colors[3]
          } else if (each['negative'] > 10) {
            each['color'] = colors[2]
          } else if (each['negative'] > 0) {
            each['color'] = colors[1]
          } else if (each['negative'] === 0) {
            each['color'] = colors[0]
          }
        })
        this.map.data.setStyle((feature) => {
          let cityId = feature.getProperty('SA2_MAIN16')
          let color = '#000000'
          this.rank.forEach(each => {
            if (each['cityId'] === cityId) {
              color = each['color']
            }
          })
          return {
            fillColor: color,
            fillOpacity: 0.5,
            strokeWeight: 2
          }
        })
      },
      gradient (startColor, endColor, step) {
        let sColor = this.hexToRgb(startColor)
        let eColor = this.hexToRgb(endColor)

        let rStep = (eColor[0] - sColor[0]) / step
        let gStep = (eColor[1] - sColor[1]) / step
        let bStep = (eColor[2] - sColor[2]) / step

        let gradientColorArr = []
        for (var i = 0; i < step; i++) {
          gradientColorArr.push(this.rgbToHex(parseInt(rStep * i + sColor[0]), parseInt(gStep * i + sColor[1]), parseInt(bStep * i + sColor[2])))
        }
        return gradientColorArr
      },
      getRandomColor () {
        const letters = '0123456789ABCDEF'
        let color = '#'
        for (let i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)]
        }
        return color
      },
      rgbToHex (r, g, b) {
        var hex = ((r << 16) | (g << 8) | b).toString(16)
        return '#' + new Array(Math.abs(hex.length - 7)).join('0') + hex
      },

      hexToRgb (hex) {
        var rgb = []
        for (var i = 1; i < 7; i += 2) {
          rgb.push(parseInt('0x' + hex.slice(i, i + 2)))
        }
        return rgb
      },
      async getPageData () {
        const res = await wordfrequency_allcity_allyear()
        // const res = {
        //   isSuccess: true,
        //   data: {
        //     "arch_syd":
        //       {
        //         "2021":
        //           {
        //             "employ_cnt": 90,
        //             "employ_ratio": 0.1361,
        //             "unemploy_cnt": 20,
        //             "unemploy_ratio": 0.0302,
        //             "marrital_cnt": 42,
        //             "marrital_ratio": 0.0635,
        //             "pets_cnt": 3079,
        //             "pets_ratio": 4.6564
        //           }
        //       },
        //     "arch_melb":
        //       {
        //         "2021":
        //           {
        //             "employ_cnt": 89,
        //             "employ_ratio": 0.1439,
        //             "unemploy_cnt": 19,
        //             "unemploy_ratio": 0.0307,
        //             "marrital_cnt": 38,
        //             "marrital_ratio": 0.0614,
        //             "pets_cnt": 3035,
        //             "pets_ratio": 4.9077
        //           }
        //       },
        //     "arch_ade":
        //       {
        //         "2021":
        //           {
        //             "employ_cnt": 139,
        //             "employ_ratio": 0.2426,
        //             "unemploy_cnt": 50,
        //             "unemploy_ratio": 0.0873,
        //             "marrital_cnt": 40,
        //             "marrital_ratio": 0.0698,
        //             "pets_cnt": 2797,
        //             "pets_ratio": 4.8815
        //           }
        //       },
        //     "arch_pth":
        //       {
        //             "2021":
        //               {
        //                 "employ_cnt": 26,
        //                 "employ_ratio": 0.1304,
        //                 "unemploy_cnt": 5,
        //                 "unemploy_ratio": 0.0251,
        //                 "marrital_cnt": 11,
        //                 "marrital_ratio": 0.0552,
        //                 "pets_cnt": 974,
        //                 "pets_ratio": 4.8851
        //               }
        //           },
        //     "arch_bris":
        //       {
        //             "2021":
        //               {
        //                 "employ_cnt": 54,
        //                 "employ_ratio": 0.1667,
        //                 "unemploy_cnt": 13,
        //                 "unemploy_ratio": 0.0401,
        //                 "marrital_cnt": 19,
        //                 "marrital_ratio": 0.0587,
        //                 "pets_cnt": 1381,
        //                 "pets_ratio": 4.2645
        //               }
        //           }
        //       }
        //   }
        if (res.isSuccess) {
          // eslint-disable-next-line no-undef
          let data_of_keyword = {
            employ_ratio: [],
            unemploy_ratio: [],
            marrital_ratio: [],
            pets_ratio: []
          }
          for (let item in res.data) {
            // eslint-disable-next-line no-undef,no-unused-vars
            let zone = null
            if (item === 'arch_syd') {
              zone = 'Sydney'
            }else if (item === 'arch_melb') {
              zone = 'Meblourne'
            }else if (item === 'arch_ade') {
              zone = 'Adelaide'
            }else if (item === 'arch_pth') {
              zone = 'Perth'
            }else if (item === 'arch_bris') {
              zone = 'Brisbane'
            }
            let temp_data = {}
            temp_data['zone'] = zone
            temp_data['word'] = 'employ'
            temp_data['rate'] = res.data[item]['2021']['employ_ratio']
            data_of_keyword['employ_ratio'].push(temp_data)

            temp_data = {}
            temp_data['zone'] = zone
            temp_data['word'] = 'unemploy'
            temp_data['rate'] = res.data[item]['2021']['unemploy_ratio']
            data_of_keyword['unemploy_ratio'].push(temp_data)

            temp_data = {}
            temp_data['zone'] = zone
            temp_data['word'] = 'marrital'
            temp_data['rate'] = res.data[item]['2021']['marrital_ratio']
            data_of_keyword['marrital_ratio'].push(temp_data)

            temp_data = {}
            temp_data['zone'] = zone
            temp_data['word'] = 'pets'
            temp_data['rate'] = res.data[item]['2021']['pets_ratio']
            data_of_keyword['pets_ratio'].push(temp_data)
          }

          // eslint-disable-next-line no-unused-vars,camelcase
          for (var key in data_of_keyword) {
            let rates = data_of_keyword[key]
            var len = rates.length
            for (var i = 0; i < len - 1; i++) {
              for (var j = 0; j < len - 1 - i; j++) {
                if (rates[j]['rate'] < rates[j + 1]['rate']) {
                  var temp = rates[j + 1]
                  rates[j + 1] = rates[j]
                  rates[j] = temp
                }
              }
            }
            for (i = 0; i < rates.length; i++) {
              rates[i]['index'] = i + 1
            }
            data_of_keyword[key] = rates
          }

          this.tableData = this.tableData.concat(data_of_keyword['employ_ratio']).concat(data_of_keyword['unemploy_ratio']).concat(data_of_keyword['marrital_ratio']).concat(data_of_keyword['pets_ratio'])
          this.colorMap()
        } else {
          this.getPageData()
        }
      },
      initMap () {
        // The location of Melbourne
        let au = { lat: -24.707434219905416, lng: 133.45853918431933 }
        // eslint-disable-next-line no-undef
        this.map = new google.maps.Map(
          document.getElementById('map'), {
            zoom: 5,
            center: au,
            styles: [
              {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
              {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
              {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
              {
                featureType: 'administrative.locality',
                elementType: 'labels.text.fill',
                stylers: [{color: '#d59563'}]
              },
              {
                featureType: 'poi',
                elementType: 'labels.text.fill',
                stylers: [{color: '#d59563'}]
              },
              {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{color: '#263c3f'}]
              },
              {
                featureType: 'poi.park',
                elementType: 'labels.text.fill',
                stylers: [{color: '#6b9a76'}]
              },
              {
                featureType: 'road',
                elementType: 'geometry',
                stylers: [{color: '#38414e'}]
              },
              {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{color: '#212a37'}]
              },
              {
                featureType: 'road',
                elementType: 'labels.text.fill',
                stylers: [{color: '#9ca5b3'}]
              },
              {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{color: '#746855'}]
              },
              {
                featureType: 'road.highway',
                elementType: 'geometry.stroke',
                stylers: [{color: '#1f2835'}]
              },
              {
                featureType: 'road.highway',
                elementType: 'labels.text.fill',
                stylers: [{color: '#f3d19c'}]
              },
              {
                featureType: 'transit',
                elementType: 'geometry',
                stylers: [{color: '#2f3948'}]
              },
              {
                featureType: 'transit.station',
                elementType: 'labels.text.fill',
                stylers: [{color: '#d59563'}]
              },
              {
                featureType: 'water',
                elementType: 'geometry',
                stylers: [{color: '#17263c'}]
              },
              {
                featureType: 'water',
                elementType: 'labels.text.fill',
                stylers: [{color: '#515c6d'}]
              },
              {
                featureType: 'water',
                elementType: 'labels.text.stroke',
                stylers: [{color: '#17263c'}]
              }
            ]})
        this.map.data.loadGeoJson('australia_province.json')

        // mouse click event: show grid info
        // eslint-disable-next-line no-undef
        this.infowindow = new google.maps.InfoWindow()
        this.map.data.addListener('click', async (event) => {
          let cityName = event.feature.getProperty('name')
          let database = null
          if (cityName === 'Victoria') {
            database = 'arch_melb'
          } else if (cityName === 'New South Wales') {
            database = 'arch_syd'
          } else if (cityName === 'South Australia') {
            database = 'arch_ade'
          } else if (cityName === 'Queensland') {
            database = 'arch_bris'
          } else if (cityName === 'Western Australia') {
            database = 'arch_pth'
          }
          this.clickSection = true
          let PopWindow = Vue.extend(popWindowComponent)
          const res = await employ_allcity()
          // eslint-disable-next-line camelcase
          let tweet_chart = null
          // eslint-disable-next-line camelcase
          let aurin_chart = null
          // let res = {
          //   isSuccess: true,
          //   data: {
          //     "arch_syd":
          //       {
          //         "2016": {"twitter_data": 0.0355, "AURIN_data": 24285},
          //         "2017": {"twitter_data": 0.0454, "AURIN_data": 25192},
          //         "2018": {"twitter_data": 0.055, "AURIN_data": 23174},
          //         "2019": {"twitter_data": 0.1784, "AURIN_data": 17427},
          //         "2020": {"twitter_data": 0.1606, "AURIN_data": 23736}
          //       },
          //     "arch_melb":
          //       {	"2016": {"twitter_data": 0.0209, "AURIN_data": 13157},
          //         "2017": {"twitter_data": 0.0793, "AURIN_data": 15152},
          //         "2018": {"twitter_data": 0.0509, "AURIN_data": 15557},
          //         "2019": {"twitter_data": 0.1934, "AURIN_data": 15796},
          //         "2020": {"twitter_data": 0.2215, "AURIN_data": 17178}
          //       },
          //     "arch_ade":
          //       {	"2016": {"twitter_data": 0.0247, "AURIN_data": 5069},
          //         "2017": {"twitter_data": 0.0445, "AURIN_data": 4320},
          //         "2018": {"twitter_data": 0.022, "AURIN_data": 3471},
          //         "2019": {"twitter_data": 0.2272, "AURIN_data": 4081},
          //         "2020": {"twitter_data": 0.238, "AURIN_data": 4618}
          //       },
          //     "arch_pth":
          //       {	"2016": {"twitter_data": 0.0, "AURIN_data": 0},
          //         "2017": {"twitter_data": 0.0, "AURIN_data": 0},
          //         "2018": {"twitter_data": 0.1018, "AURIN_data": 0},
          //         "2019": {"twitter_data": 0.1572, "AURIN_data": 0},
          //         "2020": {"twitter_data": 0.203, "AURIN_data": 3954}
          //       },
          //     "arch_bris":
          //       {	"2016": {"twitter_data": 0.0, "AURIN_data": 138200},
          //         "2017": {"twitter_data": 0.0185, "AURIN_data": 150270},
          //         "2018": {"twitter_data": 0.0503, "AURIN_data": 148289},
          //         "2019": {"twitter_data": 0.2148, "AURIN_data": 156136},
          //         "2020": {"twitter_data": 0.1831, "AURIN_data": 158858}
          //       }
          //   }
          // }
          let x = []
          let y_tweet = []
          let y_aurin = []
          if (res.isSuccess === true && res.data != null && database != null) {
            let data = res.data[database]
            for (var key in data) {
              x.push(key)
              y_aurin.push(data[key]['AURIN_data'])
              y_tweet.push(data[key]['twitter_data'])
            }
            // eslint-disable-next-line camelcase
            tweet_chart = {
              title: {
                text: 'Unemployment Rate on Tweet',
                x: 'center',
                y: 'top',
                textAlign: 'left'
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
                data: x
              },
              yAxis: {
                name: 'rate',
                type: 'value'
              },
              series: [{
                data: y_tweet,
                type: 'line',
                areaStyle: {}
              }]
            }
            // eslint-disable-next-line camelcase
            aurin_chart = {
              title: {
                text: 'Unemployment Count on AURIN',
                x: 'center',
                y: 'top',
                textAlign: 'left'
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
                data: x
              },
              yAxis: {
                name: 'count',
                type: 'value'
              },
              series: [{
                data: y_aurin,
                type: 'line',
                areaStyle: {}
              }]
            }
          } else {
            this.$message('failed')
          }
          // send data to the view
          let object = new PopWindow({
            propsData: {
              cityName,
              tweet_chart,
              aurin_chart
            }
          })

          object.$mount()
          this.infowindow.setContent(object.$el)
          this.infowindow.setPosition(event.latLng)
          this.infowindow.open(this.map)
        })

        // mouse over event: highlight color
         this.map.data.addListener('mouseover', (event) => {
           this.map.data.overrideStyle(event.feature, { fillColor: 'red' })
           let cityName = event.feature.getProperty('name')
           this.cityNameMessage = this.$message({
             message: cityName,
             type: 'a',
             center: true
           })
        })

        // mouse our event: reset color/info-window
        this.map.data.addListener('mouseout', (event) => {
          this.cityNameMessage.close()
          this.map.data.revertStyle()
          if (this.clickSection === true) {
            this.clickSection = false
            this.infowindow.close()
          }
        })
      }
    }
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
          
