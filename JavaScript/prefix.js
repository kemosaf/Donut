
async function setPrefix() {
	let p = document.getElementById("prefix").value
	splitPrefix = p.split(" ")
	if(splitPrefix[1]) {

 document.getElementById("error").style.display = "block";
setTimeout(function(){document.getElementById("error").style.display = "none"; }, 2000);
return
}
	if(!splitPrefix[0]) {

 document.getElementById("error").style.display = "block";
setTimeout(function(){document.getElementById("error").style.display = "none"; }, 2000);
return
	}
	fetch(`/server?server={server}&user={user}&code={code}&key=prefix&value=${p`)
 document.getElementById("success").style.display = "block";
setTimeout(function(){document.getElementById("success").style.display = "none"; }, 2000);
{bl}

