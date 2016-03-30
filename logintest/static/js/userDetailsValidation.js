//jQuery for password matching
$(document).ready(function () {
   $("#Confpasswd1").keyup(function(){
      var psw1 = $("#passwd1").val();
      var psw2 = $("#Confpasswd1").val();
      if(psw1 == psw2)
      {
         $("#matching_status").text("Password matched...");
         $("#matching_status").css("color", "green");
      }
      else
      {
         $("#matching_status").text("Password did not match...");  
      }
   });
   /*jQuery.validator.setDefaults({
      debug: true,
      success: "valid"
   });
   $( "#myForm2" ).validate({
      rules: {
         passwd1: "required",
         Confpasswd1: {
            equalTo: "#passwd1"
         }
      }
   });*/
});

function validateForm() {
	var msg = "Validation Error...";
	var flag = 0;
    if( document.LoggedinForm.contactno.value == "" ||
         isNaN( document.LoggedinForm.contactno.value ) ||
         document.LoggedinForm.contactno.value.length != 10 )
         {
            //alert( "Please provide a valid contact no of 10 digits." );
			msg += "\n\t-> Please provide a valid contact no of 10 digits.";
            document.LoggedinForm.contactno.focus() ;
			flag = 1;
            //return false;
         }
	if( document.LoggedinForm.pin.value == "" ||
         isNaN( document.LoggedinForm.pin.value ) ||
         document.LoggedinForm.pin.value.length != 6 )
         {
            //alert( "Please provide a valid pin no of 6 digits." );
			msg += "\n\t-> Please provide a valid pin no of 6 digits.";
            document.LoggedinForm.pin.focus() ;
			flag = 1;
            //return false;
         }
	if (flag == 1)
	{
		alert(msg);
		return false;
	}
	return true;
}
