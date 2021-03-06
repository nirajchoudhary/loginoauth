//Google+ Oauth script
function onSignIn(googleUser) {
	// Useful data for client-side scripts:
    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Don't send this directly to the server!
    console.log("Name: " + profile.getName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());
    // The ID token need to pass to the backend:
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);
	document.getElementById('oauthid').value = profile.getEmail();
	document.getElementById('userid').value = profile.getName();
	document.getElementById('passwd').value = "googleLogin";
	var auth2 = gapi.auth2.getAuthInstance();
   	auth2.signOut().then(function () {
     		console.log('User signed out.');
   	});
	document.getElementById("LoginForm").submit();
}
