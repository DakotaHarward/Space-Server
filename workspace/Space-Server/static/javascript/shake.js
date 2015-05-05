var shake;
var magnitude = 0;
var willstop = true;
function offline(){
        hideSomething('EVERYTHING')
        showSomething('computermalfunction')
        willstop = false;
    if(willstop){magnitude += 3;}
    else{magnitude = 3;}
    clearInterval(shake);
    shake = setInterval(function(){doshake()},100);
      }
      function doshake(){
    document.getElementById("computermalfunction").style["-webkit-filter"] = "blur("+magnitude+"px)";
    document.getElementById("computermalfunction").style["filter"] = "blur("+magnitude+"px)";
    document.getElementById("computermalfunction").style.top = randomIntFromInterval(magnitude * -1, magnitude)+'px';
    document.getElementById("computermalfunction").style.left = randomIntFromInterval(magnitude * -1, magnitude)+'px';
    document.getElementById("computermalfunction").style['-webkit-transform'] = "rotate("+randomIntFromInterval(magnitude * -1, magnitude)/10+'deg)';
    document.getElementById("computermalfunction").style['-moz-transform'] = "rotate("+randomIntFromInterval(magnitude * -1, magnitude)/10+'deg)';
    if(willstop){magnitude -= (magnitude+1)/10;}
      }
    function online(){
    magnitude = 0;
    clearInterval(shake);
    document.getElementById("computermalfunction").style.top = '0px';
    document.getElementById("computermalfunction").style.left = '0px';
    document.getElementById("computermalfunction").style["-webkit-filter"] = "blur(0px)";
    document.getElementById("computermalfunction").style["filter"] = "blur(0px)";
    document.getElementById("computermalfunction").style['-webkit-transform'] = "rotate(0deg)";
    document.getElementById("computermalfunction").style['-moz-transform'] = "rotate(0deg)";
      hideSomething('computermalfunction')
      showSomething('EVERYTHING')
    }
function randomIntFromInterval(min,max)
{
    return Math.floor(Math.random()*((max-min)+1)+min);
}