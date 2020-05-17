$(document).ready(function() {
    $('#search #submit').click(function() {
        var keyword = $('#search input[name="keyword"]').val();
        if (keyword == '') {
            $('#demo').show()
            $('#demo').pagination(1)
        } else {
            $.ajax({
                url: '/keyword',
                type: 'POST',
                contentType:'application/x-www-form-urlencoded',
                data: {"keyword": keyword},
                dataType: 'json',
                error: function() {console.log(('电影数据请求失败...'))},
                success: function(data) {
                   $('#demo').hide()
                   $('#search #searchResult').hide()
                    $('#search #searchResult').empty()
                    var temp = '<p style="margin-bottom:20px;">共<span style="color:#2A9662;margin-left:5px;margin-right:5px;">' + data.length + '</span>条名称含<span style="color:#FF4949;margin-left:5px;margin-right:5px;">' + keyword + '</span>的电影</p>';
                    $('#search #searchResult').append(temp)

                     $('#search #hot').empty()
                    for (var i = 0; i < data.length; i++) {
                        var item = '<br/><div class="movie"><a href="' + data[i]["链接"] + '" target="_blank"><div class="movie_cover" style="background-image:url(' + data[i]["图片"] + ')"></div></a><div class="movie_info"><h4><a href="' + data[i]["链接"] + '" target="_blank">' + data[i]["电影名称"] + '</a><span style="color:#44A031;font-size:14px;margin-left:5px;">';
                        if (data[i]["上映时间"] != 0) {
                            item = item + data[i]["上映时间"] + '年'
                        }
                        item = item + '</span><span style="color:#FB5151;font-size:14px;margin-left:5px;">' + data[i]["评分"] + '分</span></h4><p>排名&nbsp;&nbsp;第' + data[i]["排名"] +'名'+'</p><p>导演&nbsp;&nbsp;' + data[i]["导演"] + '</p><p>主演&nbsp;&nbsp;' + data[i]["主演"] + '</p><p>类型&nbsp;&nbsp;' + data[i]["类型"] + '</p><p>产地&nbsp;&nbsp;' + data[i]["制方国家"] + '</p><p>片长&nbsp;&nbsp;' + data[i]["片长"] + '</p><h5 style="color:#555;">剧情简介</h5><p style="text-indent:2em;color:#777;">';
                            item = item + data[i]['介绍']
                        item = item + '</p></div></div>'
                        $('#search #hot').append(item)
                    }
                    $('#search #searchResult').show()
                    if (data.length==0){
                        $('#main').append('<br><br><br><br><br><br><br><br><br><br><br><br><br>')
                    }
                }
            })
        }
    })

    $('#demo').pagination({
        dataSource: [1,2,3,4,5,6,7,8,9,10],
        pageSize: 1,
        autoHidePrevious: true,
        autoHideNext: true,
        mode: 'fixed',
        className: 'paginationjs-theme-blue paginationjs-big',
        callback: function(d, pagination) {
               $.ajax({
                url: '/page',
                type: 'get',
                contentType:'application/x-www-form-urlencoded',
                data: {"page": d[0]},
                dataType: 'json',
                error: function() {console.log(('电影分页数据请求失败...'))},
                success: function(data) {
                    $('#search #searchResult').hide();
                    $('#search #searchResult').empty();
                    var temp = '<p style="margin-bottom:20px;">共<span style="color:#2A9662;margin-left:5px;margin-right:5px;">' + 10 + '</span>页，当前在第<span style="color:#FF4949;margin-left:5px;margin-right:5px;">' + d[0] + '</span>页</p>';
                    $('#search #searchResult').append(temp)

                    $('#hot').empty();
                    for (var i = 0; i < data.length; i++) {
                        var item = '<br/><div class="movie"><a href="' + data[i]["链接"] + '" target="_blank"><div class="movie_cover" style="background-image:url(' + data[i]["图片"] + ')"></div></a><div class="movie_info"><h4><a href="' + data[i]["链接"] + '" target="_blank">' + data[i]["电影名称"] + '</a><span style="color:#44A031;font-size:14px;margin-left:5px;">';
                        if (data[i]["上映时间"] != 0) {
                            item = item + data[i]["上映时间"] + '年';
                        }
                        item = item + '</span><span style="color:#FB5151;font-size:14px;margin-left:5px;">' + data[i]["评分"] + '分</span></h4><p>排名&nbsp;&nbsp;第' + data[i]["排名"] +'名'+'</p><p>导演&nbsp;&nbsp;' + data[i]["导演"] + '</p><p>主演&nbsp;&nbsp;' + data[i]["主演"] + '</p><p>类型&nbsp;&nbsp;' + data[i]["类型"] + '</p><p>产地&nbsp;&nbsp;' + data[i]["制方国家"] + '</p><p>片长&nbsp;&nbsp;' + data[i]["片长"] + '</p><h5 style="color:#555;">剧情简介</h5><p style="text-indent:2em;color:#777;">';
                            item = item + data[i]['介绍'];
                        item = item + '</p></div></div>';
                        $('#hot').append(item);
                    }
                    $('#search #searchResult').show();
                    //置顶
                    $("html,body").animate({scrollTop:0}, 500);
                }
            })
        }
})
})

