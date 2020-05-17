// 电影类型
var ectest_category = echarts.init(document.getElementById("category"),'macarons')
var option_category
$.ajax({
    type:"get",
    url:"/category",
    datatype:"json",
    success:function (data) {
    option_category = {
        title: {
            text: '电影类型统计',
            subtext: '',
            x: 'center',
            padding: [10, 10, 10, 10]
        },
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c}部 ({d}%)"
        },
        calculable: true,
        series: [{
            name: '电影类型统计',
            type: 'pie',
            radius: '50%',
            center: ['50%', '55%'],
            data: data
        }]
    }
    ectest_category.setOption(option_category)
    },
    error:function () {
        console.log('电影类型数据请求失败...')
    }
})

