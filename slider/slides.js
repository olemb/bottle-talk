// Makes slide show out of a file generated by rst2html
//
// Ole Martin Bjorndalen

slides = [];
current = 0;

function show(num) {
    if(!(num >= 0 && num < slides.length)) {
        return;
    }

    for(i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none'
    }

    slides[num].style.display = 'block';
    current = num;

    var slide_title = slides[num].querySelector('h1').innerHTML;
    document.title = slide_title;
}

function first() {
    show(0);
}

function last() {
    show(slides.length - 1);
}

function next() {
    show(current + 1);
}

function prev() {
    show(current - 1);
}

function on_keydown(event)
{
    switch(event.keyCode) {
    case 33:  // PgUp
    case 38:  // Up
    case 37:  // Left
    case 66:  // b
        prev();
        break;
    case 34:  // PgDn
    case 40:  // Down
    case 39:  // Right
    case 32:  // Space
        next();
        break;
    case 36:  // Home
        first();
        break;
    case 35:  // End
        last();
        break;
    }
}

function on_mousedown(event) {
    button = event.button;

    switch(button) {
    case 0:  // Left button
        next();
        break;
    case 2:  // Right button
        // prev();
        break;

    // Down should be next()
    case 5:  // Scroll (up or down?)
        next();
        break;
    case 6:
        prev();
        break;
    }
}

function on_mousewheel(event) {
    if(event.wheelDeltaY < 0) {
        next();
    } else {
        prev();
    }
}

function init() {
    slides = document.querySelectorAll(".section");

    document.addEventListener('keydown', on_keydown, false);
    document.addEventListener('mousedown', on_mousedown, false);
    document.addEventListener('mousewheel', on_mousewheel, false);

    if(typeof swipe !== 'undefined') {
        var body = document.getElementsByTagName('body')[0];
        swipe(body, function(direction) {
            if(direction == 'left') {
                next();
            } else if(direction == 'right') {
                prev();
            } else if(direction == 'up') {
                first();
            } else if(direction == 'down') {
                last();
            }
        });
    }

    first();
}

window.onload = init;
