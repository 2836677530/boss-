$(window).load(function(){$(".loading").fadeOut()})  
$(function () {
echarts_2()
echarts_4()
echarts_5()
echarts_6()
echarts_7()
function echarts_2() {
        // 基于准备好的dom，初始化echarts实例
     var myChart = echarts.init(document.getElementById('echart2'));
    // var data = [683, 234, 234, 523, 345, 320, 280, 271, 254, 229, 210, 190, 182]
    // var titlename = ['北京', '上海', '广州', '郑州', '武汉', '南京', '杭州', '东莞', '深圳', '虎门', '青岛', '石家庄', '安阳'];
    $.ajax({
        url:'http://127.0.0.1:5000/data',
        result:{},
        // dataType: 'json',
        // crossDomain: true,
        success:function(result){
            console.log(result.nums)
            data=result.nums
            site=result.site
            option = {
                grid: {
                    left: '0',
                    top:'0',
                    right: '0',
                    bottom: '0%',
                   containLabel: true
                },
                xAxis: {
                    show: false
                },
                yAxis: [{
                    show: true,
                    data: site,
                    inverse: true,
                    axisLine: { show: false},
                    splitLine:{ show: false},
                    axisTick:{ show: false},
                    axisLabel: {
                        textStyle: {
                            color:'#fff'
                        },
                    },
        
                }, {
                    show: false,
                    inverse: true,
                    data: data,
                    axisLabel: {textStyle: {color: '#fff'}},
                    axisLine: { show: false},
                    splitLine:{ show: false},
                    axisTick: { show: false},
                }],
                series: [{
                    name: '条',
                    type: 'bar',
                    yAxisIndex: 0,
                    data: data,
                    barWidth: 15,
                    itemStyle: {
                        normal: {
                           barBorderRadius: 50,
                            color:'#1089E7',
                        }
                    },
                    label: {
                       normal: {
                            show: true,
                            position: 'right',
                            formatter: '{c}',
                           textStyle: {color: 'rgba(255,255,255,.5)'}
                        }
                    },
                }]
            };
            myChart.setOption(option);
        },
        error:function(msg){
            // console.log(msg);
            alert('系统发生错误！')
        }
    })
   
        // 使用刚指定的配置项和数据显示图表。
   
    window.addEventListener("resize",function(){
        myChart.resize();
    });
    }
function echarts_4() {
        // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echart4'));
    $.ajax({
        url:'http://127.0.0.1:5000/expCounts',
        type:'GET',
        result:{},
        success:function(result){
            data=result.data
            labels=result.exp
            var option = {
                color: ["#2f89cf"],
            tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        // 修改图表的大小
        grid: {
          left: "0%",
          top: "10px",
          right: "0%",
          bottom: "4%",
          containLabel: true
        },
        xAxis: [
          {
            type: "category",
            data: labels,
            axisTick: {
              alignWithLabel: true
            },
            // 修改刻度标签 相关样式
            axisLabel: {
              color: "rgba(255,255,255,.6) ",
              fontSize: "8"
            },
            // 不显示x坐标轴的样式
            axisLine: {
              show: false
            }
          }
        ],
        yAxis: [
          {
            type: "value",
            // 修改刻度标签 相关样式
            axisLabel: {
              color: "rgba(255,255,255,.6) ",
              fontSize: 12
            },
            // y轴的线条改为了 2像素
            axisLine: {
              lineStyle: {
                color: "rgba(255,255,255,.1)",
                width: 2
              }
            },
            // y轴分割线的颜色
            splitLine: {
              lineStyle: {
                color: "rgba(255,255,255,.1)"
              }
            }
          }
        ],
        series: [
          {
            name: "薪资",
            type: "bar",
            barWidth: "50%",
            // data: [200, 300, 300, 900, 1500, 1200, 600],
            data: data,
            itemStyle: {
              // 修改柱子圆角
              barBorderRadius: 5
            }
          }
        ]
            //         xAxis: {
            //           type: 'category',
            //           data: labels
            //         },
            //         yAxis: {
            //           type: 'value'
            //         },
            //         series: [
            //           {
            //             data: data,
            //             type: 'bar',
            //             showBackground: true,
            //             backgroundStyle: {
            //               color: 'rgba(180, 180, 180, 0.2)'
            //             }
            //           }
            //         ]
                
             };
         // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);   

        },
        error:function(msg){
            // console.log(msg);
            alert('系统发生错误！')
        }
    })
        
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
	function echarts_5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart5'));
        $.ajax({
            url:'http://127.0.0.1:5000/circle',
            type:'GET',
            result:{},
            success:function(result){
                data=result.key_values
                
                labels=result.edu
                var option = {
                    legend: {
                     orient: 'vertical',
                      itemWidth: 10,
                      itemHeight: 10,
                      textStyle:{
                          color:'rgba(255,255,255,.5)'
                      },
                        top:'20%',
                    right:30,
                      data:labels
                  },
                  color: ['#37a2da','#32c5e9','#9fe6b8','#ffdb5c','#ff9f7f','#fb7293','#e7bcf3','#8378ea'],
                  tooltip : {
                      trigger: 'item',
                      formatter: "{b} : {c} ({d}%)"
                  },
                 
                  calculable : true,
                  series : [
                      {
                        
                          type:'pie',
                          radius : [20, 70],
                          center: ["35%", "50%"],
                          roseType : 'area',
                          data:data,
                           label: {
                           normal: {
                               formatter: function(param) {
                                   return param.name +':\n' + param.value +'\n';
                               }
              
                           }
                       },
                       labelLine: {
                           normal: {
                                length:5,
                                length2:15,
                               lineStyle: { width: 1}
                           }
                       },
              
                       itemStyle: {
                           normal: {
                               shadowBlur: 30,
                               shadowColor: 'rgba(0, 0, 0, 0.4)'
                           }
              
                       },
                      }
                  ]
              };
            myChart.setOption(option);
            },
            error:function(msg){
                alert('系统发生错误！')
            }
        })
        
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
	function echarts_6() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart6'));
        $.ajax({
            url:'http://127.0.0.1:5000//wordclound',
            type:'GET',
            result:{},
            success:function(result){
                data=result.key_words
                var option = {
                    series: [{
                        type: 'wordCloud',
                        width: '100%',
                        height: '100%',
                        sizeRange: [10, 25],
                        textStyle: {
                        fontFamily: 'sans-serif',
                        fontWeight: 'bold',
                        color: function () {
                        return 'rgb(' + [
                        Math.round(Math.random() * 255),
                        Math.round(180 + Math.random() * 75),
                        // Math.round(Math.random() * 160)
                        Math.round(Math.random() * 255)
                        ].join(',') + ')';
                        }
                        },
                        emphasis: {
                        focus: 'self',
                        textStyle: {
                        shadowBlur: 10,
                        shadowColor: '#333'
                        }
                        },
                        data: result.key_words
                        }]
                };
                myChart.setOption(option);
            }
        })
        

        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
    function echarts_7(){
        var myChart = echarts.init(document.getElementById('echart7'));
        $.ajax({
            url:'http://127.0.0.1:5000/count',
            result:{},
            type:'GET',
            success:function(result){
                    option = {
                        grid: {
                            left: '0',
                            top:'0',
                            right: '0',
                            bottom: '15%',
                           containLabel: true
                        },
                        xAxis: {
                            show: false
                        },
                        yAxis: [{
                            show: true,
                            data: result.salary,
                            inverse: true,
                            axisLine: { show: false},
                            splitLine:{ show: false},
                            axisTick:{ show: false},
                            axisLabel: {
                                textStyle: {
                                    color:'#fff'
                                },
                            },
                
                        }, {
                            show: false,
                            inverse: true,
                            data: result.values,
                            axisLabel: {textStyle: {color: '#fff'}},
                            axisLine: { show: false},
                            splitLine:{ show: false},
                            axisTick: { show: false},
                        }],
                        series: [{
                            name: '条',
                            type: 'bar',
                            yAxisIndex: 0,
                            data: result.values,
                            barWidth: 15,
                            itemStyle: {
                                normal: {
                                   barBorderRadius: 50,
                                    color:'#1089E7',
                                }
                            },
                            label: {
                               normal: {
                                    show: true,
                                    position: 'right',
                                    formatter: '{c}',
                                   textStyle: {color: 'rgba(255,255,255,.5)'}
                                }
                            },
                        }]
                    };
                    myChart.setOption(option);
                },
                error:function(msg){
                    // console.log(msg);
                    alert('系统发生错误！')
                }
            })
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
})



		
		
		


		









