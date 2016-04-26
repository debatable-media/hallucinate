function getCookie(cookieName){
  var cookieArray = document.cookie.split(';');
  for(var i=0; i<cookieArray.length; i++){
    var cookie = cookieArray[i];
    while (cookie.charAt(0)==' '){
      cookie = cookie.substring(1);
    }
    cookieHalves = cookie.split('=');
    if(cookieHalves[0] == cookieName){
      return cookieHalves[1];
    }
  }
  return "";
}

function show_login_overlay(){
        grecaptcha.reset();
	$('#login-overlay').css('display', 'block');
	$('#login-prompt').css('display', 'block');
        return false;
}

function hide_login_overlay(){
	$('#login-overlay').css('display', 'none');
	$('#login-prompt').css('display', 'none');
        return false;
}

function set_logged_in(){
        hide_login_overlay();
	$("#signup-form input:eq(0)").val('');
	$("#signup-form input:eq(1)").val('');
	$("#signup-form input:eq(2)").val('');
	$('#nav-login').css('display', 'none');
	$('#nav-logout').css('display', 'inline-block');
	$('#nav-account').css('display', 'inline-block');
	$('#nav-account').text(getCookie('user'));
	$('#post-form').css('display', 'block');
        return false;
}

function set_logged_out(){
	hide_login_overlay();
        $("#signup-form input:eq(0)").val('');
	$("#signup-form input:eq(1)").val('');
	$("#signup-form input:eq(2)").val('');
	$("#login-form input:eq(0)").val('');
	$("#login-form input:eq(1)").val('');
	$('#nav-login').css('display', 'inline-block');
	$('#nav-logout').css('display', 'none');
	$('#nav-account').css('display', 'none');
	$('#post-form').css('display', 'none');
        return false;
}

if (getCookie('user') != "")
	set_logged_in();
else
	set_logged_out();

$('#nav-login').click(show_login_overlay);
$('#login-overlay').click(hide_login_overlay);

$('#nav-logout').click(function(){
	$.ajax({
		type: 'POST', 
		url: 'logout.py',
		success: function(data) {
			var response = JSON.parse(data);
			if (response.success)
				set_logged_out();
			else
				$("#signup-error").text(response.error);
		}
		});
	return false;
});

var signup_form = $("#signup-form");
signup_form.submit(function(event){
	var username = $("#signup-form input:eq(0)").val();
	var password = $("#signup-form input:eq(1)").val();
	var confirm_password = $("#signup-form input:eq(2)").val();

	if (username == '' || password == '' || confirm_password == '')
		$("#signup-error").text("all fields are required");
	else if (password != confirm_password)
		$("#signup-error").text("passwords must match");
	else
	{
		$.ajax({
		type: signup_form.attr('method'), 
		url: signup_form.attr('action'),
		data: signup_form.serialize(),
		success: function(data) {
			var response = JSON.parse(data);
			if (response.success)
				set_logged_in();
			else
				$("#signup-error").text(response.error);
		}
		});	
	}

	event.preventDefault();
});

var login_form = $("#login-form");
login_form.submit(function(event){
	var username = $("#login-form input:eq(0)").val();
	var password = $("#login-form input:eq(1)").val();

	if (username == '' || password == '')
		$("#login-error").text("all fields are required");
	else
	{
		$.ajax({
		type: login_form.attr('method'), 
		url: login_form.attr('action'),
		data: login_form.serialize(),
		success: function(data) {
			var response = JSON.parse(data);
			if (response.success)
				set_logged_in();
			else
				$("#login-error").text(response.error);
		}
		});
	}

	event.preventDefault();
});

