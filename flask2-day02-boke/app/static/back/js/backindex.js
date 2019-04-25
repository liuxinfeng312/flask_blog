$(function () {
    $('.delete_id>#deleteid').click(function () {
        console.log('点击成功')
        request_data={
            'deleteid':$(this).attr('data-del')

        }
        console.log($(this).attr('data-del'))

        var $that = $(this)
        $.get('/delete/',request_data,function (response) {
            console.log(response)
            if (response.status==1){
                $that.parent().parent().remove()

            }


        })
    })
    $('.delete_id>#updata_id').click(function () {
        console.log('点击成功')
        request_data={
            'updateid':$(this).attr('data-id')

        }
        console.log($(this).attr('data-id'))

        var $that = $(this)
         $.get('/backupdate/',request_data,function (response) {
            console.log(response)
             if (response.status==1){
                 window.open(/backupdate01/,'_bank')
                 console.log(response.article_title)

             }


        })

    })

})