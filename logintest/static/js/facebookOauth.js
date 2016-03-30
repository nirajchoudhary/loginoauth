// Facebook login 

// This is called with the results from from FB.getLoginStatus().
function statusChangeCallback(response) {
	console.log('statusChangeCallback');
	console.log(response);
	// The response object is returned with a status field that lets the
	// app know the current login status of the person.
    
	if (response.status === 'connected') {
		testAPI();							// Logged into your app and Facebook.
	} 
	else if (response.status === 'not_authorized') {
      	// The person is logged into Facebook, but not your app.
      	//document.getElementById('userid').value = 'Please log ' + 'into this app.';
    }
	else {
     	// The person is not logged into Facebook, so we're not sure if
      	// they are logged into this app or not.
      	//document.getElementById('userid').value = response.status;
	}
}


// This function is called when someone finishes with the Login Button.  
function checkLoginState() {
    FB.getLoginStatus(function(response) {
      	statusChangeCallback(response);
    });
}

window.fbAsyncInit = function() {
    FB.init({
      	appId      : '411808378989743',
		cookie     : true,
      	xfbml      : true,
      	version    : 'v2.5'
    });
};

(function(d, s, id){
 	var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    	js = d.createElement(s); js.id = id;
    	js.src = "//connect.facebook.net/en_US/sdk.js";
    	fjs.parentNode.insertBefore(js, fjs);
   	}(document, 'script', 'facebook-jssdk'));


// Here we run a very simple test of the Graph API after login is successful.  
function testAPI() {
	FB.api('/me?fields=name,email', function(response) {
      	console.log('Successful login for: ' + response.name);
		console.log('Id: ' + response.id);
		//document.getElementById('oauthid').value = response.email;
		document.getElementById('oauthid').value = response.id;
		document.getElementById('userid').value = response.name;
		document.getElementById('passwd').value = "fbLogin";
		document.getElementById("LoginForm").submit();
		//document.getElementById('status').innerHTML = "working " + response.name;
	});
}
