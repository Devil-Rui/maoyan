// 上映年份
var ectest_year = echarts.init(document.getElementById("year"),'macarons')
var option_year
$.ajax({
    type:"get",
    url:"/year",
    datatype:"json",
    success:function (data) {
    option_year = {
                title: {
                    text: '历年电影产量统计',
                    x: 'center',
                    padding: [15, 10, 10, 10]
                },
                tooltip: {
                    trigger: 'item',
                    formatter: function(params) {
                        return params.seriesName + '<br>' + params.value[0] + '年：' + params.value[1] + '部';
                    }
                },
                calculable: true,
                xAxis: [{
                    type: 'value',
                    min: 1930,
                    max: 2020,
                }],
                yAxis: [{
                    type: 'value',
                }],
                series: [{
                    name: '历年电影产量',
                    type: 'line',
                    data: data
                }]
            };
    ectest_year.setOption(option_year)
    },
    error:function () {
        console.log('电影类型数据请求失败...')
    }
})

