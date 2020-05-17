var ectest_showtime = echarts.init(document.getElementById("showtime"),'macarons')
var ectest_length = echarts.init(document.getElementById("length"),'macarons')
var ectest_average = echarts.init(document.getElementById("average"),'macarons')
var option_showtime = {
        title: {
            text: '上映时间－评分关系',
            x: "center"
        },
        tooltip: {
            trigger: 'axis',
            showDelay: 0,
            formatter: function(params) {
                return params[0].seriesName + '<br/>' + params[0].value[0] + '年 ' + params[0].value[1] + '分';
            },
            axisPointer: {
                show: true,
                type: 'cross',
                lineStyle: {
                    type: 'dashed',
                    width: 1
                }
            }
        },
        xAxis: [{
            type: 'value',
            min: 1930,
            max: 2020
        }],
        yAxis: [{
            type: 'value',
            min: 8.5,
            max: 10
        }],
        series: [{
            name: '上映时间－评分',
            type: 'scatter',
            data: null
        }]
    }
var option_length = {
        title: {
            text: '片长－评分关系',
            x: "center"
        },
        tooltip: {
            trigger: 'axis',
            showDelay: 0,
            formatter: function(params) {
                return params[0].seriesName + '<br/>' + params[0].value[0] + '分钟 ' + params[0].value[1] + '分';
            },
            axisPointer: {
                show: true,
                type: 'cross',
                lineStyle: {
                    type: 'dashed',
                    width: 1
                }
            }
        },
        xAxis: [{
            type: 'value',
            min: 20,
            max: 250
        }],
        yAxis: [{
            type: 'value',
            min: 8.5,
            max: 10
        }],
        series: [{
            name: '片长－评分',
            type: 'scatter',
            data: null,
        }]
    }
var option_average = {
        title: {
            text: '各国家各类别平均评分',
            x: 'left',
            padding: [10, 10, 10, 56]
        },
        tooltip: {
            trigger: 'item'
        },
        calculable: true,
        xAxis: [{
            type: 'category',
            data:null
        }],
        yAxis: [{
            type: 'value',
            min: 8.5,
            max: 10
        }],
        series: [{
            name: '各国家各类别平均评分',
            type: 'bar',
            data:null,
            markPoint: {
                data: [{
                    type: 'max',
                    name: '最大值'
                }, {
                    type: 'min',
                    name: '最小值'
                }]
            },
            markLine: {
                data: [{
                    type: 'average',
                    name: '平均值'
                }]
            }
        }]
    }
ectest_showtime.setOption(option_showtime)
ectest_length.setOption(option_length)
ectest_average.setOption(option_average)


//类型-按钮
$('#categories span').click(function () {
    $('#categories span').removeClass('active')
    $('#districts span').removeClass('active')
    $('#districts span[name="all"]').addClass('active')
    $(this).addClass('active')
    dataload($(this).text(),'全部')
})

//国家-按钮
$('#districts span').click(function () {
    $('#categories span').removeClass('active')
    $('#districts span').removeClass('active')
    $('#categories span[name="all"]').addClass('active')
    $(this).addClass('active')
    dataload('全部',$(this).text())
})

//国家-下拉框
$('#select').change(function () {
    country = $(this).val()
    $.ajax({
        type:"get",
        url:'/averageWithCategory',
        contentType:'application/x-www-form-urlencoded',
        data:{"country":country},
        datatype:"json",
        success:function (data) {
            ectest_average.setOption({
                xAxis: [{
                    data:data[0]
                }],
                series: [{
                    data:data[1]
                }]
            })
        },
        error:function () {
            console.log('上映时间或片长与评分的关系数据请求失败...')
        }
    })
})

function dataload(selectedCategory,selectedCountry) {
    u = null
    d = null
    if (selectedCountry=='全部'){
        u = '/scoreWithCategory'
        d = {"category":selectedCategory}
    }else{
        u = '/scoreWithCountry'
        d = {"country":selectedCountry}
    }
    $.ajax({
    type:"get",
    url:u,
    contentType:'application/x-www-form-urlencoded',
    data:d,
    datatype:"json",
    success:function (data) {
        ectest_showtime.setOption({
            series:[{
                data:data[0]
            }]
        }),
        ectest_length.setOption({
            series:[{
                data:data[1]
            }]
        })
    },
    error:function () {
        console.log('上映时间或片长与评分的关系数据请求失败...')
    }
})
}