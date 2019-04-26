$(function(){
	var name = $(".name").eq(0);
	var telAry = /^1(3|5|4|7|8)\d{9}$/;
	var mailAry = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
	var stop = $(".stop").eq(0);
	var picCode = $(".picCode").eq(0);
	var code = $(".code").eq(0);
	var change = $(".change").eq(0);
	var loginBtn = $(".loginBtn").eq(0);
	var p = $("<p></p>");
	var exist = true;
	
	//用户名验证




	code.click(function () {
		console.log('点击成功')
		request_data={
			'msg':'success'
		}
		$.get('/getcode/',request_data,function (response) {
			console.log(response)
			if (response.status==1){
				code.html(response.code)

			}

		})


	})

	// var strs = "";
	// for(var i=0;i<4;i++){
	// 	var num=parseInt(Math.random()*100%10+48);
	// 	var stra=String.fromCharCode(num);
	// 	strs=strs.concat(stra);
	// }
	// code.html(strs);
	//
	// code.click(function(){
	// 	var strSum = "";
	// 	for(var i=0;i<4;i++) {
	// 		var num = parseInt(Math.random() * 100 % 10 + 48);
	// 		var str = String.fromCharCode(num);
	// 		strSum = strSum.concat(str);
	// 	}
		//
		// console.log('点击成功')
		// request_data={
		// 	'code':$('.code').html()
		//
		// }
		// $.get('/register/',request_data,function (response) {
		// 	// console.log(response)
		//
		// })



	// })
	// 	code.html(strSum);
	// })
	//
	// change.click(function(){
	// 	var strSum = "";
	// 	for(var i=0;i<4;i++){
	// 		var num=parseInt(Math.random()*100%10+48);
	// 		var str=String.fromCharCode(num);
	// 			strSum=strSum.concat(str);
	// 	}
	// 	code.html(strSum);
	// })
	//
	// picCode.find("input").blur(function(){
	// 	if(picCode.find("input").val() != code.html()){
	// 		$(this).attr("placeholder","请重新输入验证码");
	// 		 exist = false;
	// 	}
	//
	// })


	//登录


})
