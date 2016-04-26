var post_form = $("#post-form");
function clear_post_form()
{
	$('#post-content').val('');
}

post_form.submit(function(event){
	$.ajax({
		type: post_form.attr('method'), 
		url: post_form.attr('action'),
		data: post_form.serialize(),
		success: function(data) {
			var response = JSON.parse(data);
			if (response.success)
				clear_post_form();
			else
				$("#post-error").text(response.error);
		}
	});	

	event.preventDefault();
});
