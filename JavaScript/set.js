//setting/fetching api file for dashboard - frontend plain vanilla



function disable()
{
 document.onkeydown = function (evt) 
{
var keyCode = evt ? (evt.which ? evt.which : evt.keyCode) : event.keyCode;
  if (keyCode !== 13) return;
  return false;
 }
}

function noenter() {
  return !(window.event && window.event.keyCode == 13);
}


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
    fetch(`/server?server={server}&user={user}&code={code}&key=prefix&value=${p}`)
 document.getElementById("success").style.display = "block";
setTimeout(function(){document.getElementById("success").style.display = "none"; }, 2000);
}




async function setColor() {
    let color = document.getElementById("color").value
    color = color.replace('#', '0x')
        console.log(color)
    fetch(`/server?server={server}&user={user}&code={code}&key=color&value=${color}`)
 document.getElementById("success").style.display = "block";
setTimeout(function(){document.location.reload(true); }, 500);

}



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
setTimeout(function(){document.getElementById("success").style.display = "none"; }, 2000);
}

async function setLeave() {
    let channel = document.getElementById("leaveChannels").value
    let message = document.getElementById("leaveMessage").value
    if(message.length < 1) {
 document.getElementById("error").style.display = "block";
setTimeout(function(){document.getElementById("error").style.display = "none"; }, 2000);
return
    }

    fetch(`/server?server={server}&user={user}&code={code}&key=leaveChannel&value=${channel}`)
    fetch(`/server?server={server}&user={user}&code={code}&key=leaveMessage&value=${message}`)
 document.getElementById("success").style.display = "block";
setTimeout(function(){document.getElementById("success").style.display = "none"; }, 2000);
}


async function setDeletedEdited() {
    let deleted = document.getElementById("deletedChannels").value
    let edited = document.getElementById("editedChannels").value

    fetch(`/server?server={server}&user={user}&code={code}&key=deleteChannel&value=${deleted}`)
    fetch(`/server?server={server}&user={user}&code={code}&key=editChannel&value=${edited}`)
 document.getElementById("success").style.display = "block";
setTimeout(function(){document.getElementById("success").style.display = "none"; }, 2000);
}
