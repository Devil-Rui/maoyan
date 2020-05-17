// 电影时长
var ectest_length = echarts.init(document.getElementById("length"),'macarons')
var option_length
$.ajax({
    type:"get",
    url:"/length",
    datatype:"json",
    success:function (data) {
    option_length = {
                title: {
                    text: '电影时长统计',
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
                    min: 20,
                    max: 250,
                }],
                yAxis: [{
                    type: 'value',
                }],
                series: [{
                    name: '电影时长统计',
                    type: 'line',
                    // symbol: 'none',
                    data: data
                }]
            }
    ectest_length.setOption(option_length)
    },
    error:function () {
        console.log('电影时长数据请求失败...')
    }
})

