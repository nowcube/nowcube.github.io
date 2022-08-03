//用js设置navbar伸缩
var displayMenu = document.getElementById("show_menu");
var menu_status = 1;
displayMenu.onclick = function () {
    if (menu_status == 1) {
        document.getElementById("item").style.display = "flex";
        document.getElementById("item2").style.display = "flex";
        document.getElementById("item3").style.display = "flex";
        document.getElementById("item4").style.display = "flex";
        document.getElementById("navbar").style.height = "auto";
        menu_status = 2;
    } else if (menu_status == 2) {
        document.getElementById("item").style.display = ""; 
        document.getElementById("item2").style.display = ""; 
        document.getElementById("item3").style.display = ""; 
        document.getElementById("item4").style.display = ""; 
        document.getElementById("navbar").style.height = "";
        menu_status = 1;
    }
}

//设置body背景
var htmlBgs=[];
htmlBgs[0]="./bg.jpg";
htmlBgs[1]="./bg2.jpg";
htmlBgs[2]="./bg3.jpg";
htmlBgs[3]="./bg4.jpg";
htmlBgs[4]="./bg5.jpg";

var randomBgIndex = Math.round(Math.random()*4);
document.body.style.backgroundImage="url('"+htmlBgs[randomBgIndex]+"')";