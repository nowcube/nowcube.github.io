var displayMenu = document.getElementById("show_menu");
var menu_status = 1;
window.onresize = function(){
    if(document.documentElement.clientWidth > 576){
        document.getElementById("item").style.display = "flex";
        document.getElementById("item2").style.display = "flex";
        document.getElementById("item3").style.display = "flex";
        document.getElementById("item4").style.display = "flex";
        // document.getElementById("navbar").style.height = "50px";
    }else{
        document.getElementById("item").style.display = "none"; 
        document.getElementById("item2").style.display = "none"; 
        document.getElementById("item3").style.display = "none"; 
        document.getElementById("item4").style.display = "none"; 
        // document.getElementById("navbar").style.height = "50px";
    }
}
displayMenu.onclick = function () {
    if (menu_status == 1) {
        document.getElementById("item").style.display = "flex";
        document.getElementById("item2").style.display = "flex";
        document.getElementById("item3").style.display = "flex";
        document.getElementById("item4").style.display = "flex";
        document.getElementById("navbar").style.height = "auto";
        menu_status = 2;
    } else if (menu_status == 2) {
        document.getElementById("item").style.display = "none"; 
        document.getElementById("item2").style.display = "none"; 
        document.getElementById("item3").style.display = "none"; 
        document.getElementById("item4").style.display = "none"; 
        document.getElementById("navbar").style.height = "50px";
        menu_status = 1;
    }
}