
async function setWelcome() {
	let channel = document.getElementById("joinChannels").value
	let message = document.getElementById("joinMessage").value
	if(message.length < 1) {
 document.getElementById("error").style.display = "block";
setTimeout(function(){document.getElementById("error").style.display = "none"; }, 2000);
return
	}
	
	fetch(`/server?server={server}&user={user}&code={code}&key=joinChannel&value=${channel}`)
	fetch(`/server?server={server}&user={user}&code={code}&key=joinMessage&value=${message}`)
 document.getElementById("success").style.display = "block";
setTimeout(function(){document.getElementById("success").style.display = "none"; , 2000);
	}