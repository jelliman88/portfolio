function slideMenuIn() {
    $('#slide-in-menu').animate({
        marginLeft: "60%"
    }, 300);

}

function slideMenuOut() {
    $('#slide-in-menu').animate({
        marginLeft: "100%"
    }, 300);

}



function showMenu() {


    const menu = document.getElementById('slide-in-menu').style.display = 'block'
    const hideButton = document.getElementById('hide-button').style.display = 'block'
    slideMenuIn()




}

function hideMenu() {
    slideMenuOut()
}