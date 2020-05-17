// 电影评分
var ectest_basic = echarts.init(document.getElementById("basic"),'macarons')
var option_basic
$.ajax({
    type:"get",
    url:"/score",
    datatype:"json",
    success:function (data) {
    option_basic = {
                title: {
                    text: '电影评分统计',
                    x: 'center',
                    padding: [15, 10, 10, 10]
                },
                tooltip: {
                    trigger: 'item',
                    formatter: function(params) {
                        return params.seriesName + '<br>' + params.value[0] + '分：' + params.value[1] + '部';
                    }
                },
                calculable: true,
                xAxis: [{
                    type: 'value',
                    min: 8.5,
                    max: 10,
                }],
                yAxis: [{
                    type: 'value',
                }],
                series: [{
                    name: '电影评分统计',
                    type: 'line',
                    data: data
                }]
            }
    ectest_basic.setOption(option_basic)
    },
    error:function () {
        console.log('电影评分数据请求失败...')
    }
})

