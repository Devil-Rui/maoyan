// 电影制作国家
var ectest_area = echarts.init(document.getElementById("language"),'macarons')
var option_area
$.ajax({
    type:"get",
    url:"/area",
    datatype:"json",
    success:function (data) {
    option_area = {
                title: {
                    text: '电影票房统计',
                    subtext: '单位：百万',
                    x: 'center',
                    padding: [10, 10, 10, 10]
                },
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c}部 ({d}%)"
                },
                calculable: true,
                series: [{
                    name: '电影票房统计',
                    type: 'pie',
                    radius: '50%',
                    center: ['50%', '55%'],
                    data: data
                }]
            }
    ectest_area.setOption(option_area)
    },
    error:function () {
        console.log('电影制作国家数据请求失败...')
    }
})
