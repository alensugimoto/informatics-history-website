function myFunction() {
    var x1 = document.getElementById('bodyTag');
    console.log("here");
    if (x1.style.overflow === '') {
        console.log("here1");
        x1.style.overflow = 'hidden';
        console.log("here2");
    } else {
        x1.style.overflow = '';
        console.log("here3");
    }
}