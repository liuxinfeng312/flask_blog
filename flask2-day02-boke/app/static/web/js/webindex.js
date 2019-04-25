$(function () {
    $(' #title_id').click(function () {
        console.log('点击成功')

        request_data={
            'title_id':$(this).attr('data-titleid')
        }
        console.log($(this).attr('data-titleid'))
         var $that = $(this)
        $.get('/index/',request_data,function (response) {
            // console.log(response)

        })


    })


})