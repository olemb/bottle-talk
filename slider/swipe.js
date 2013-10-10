// http://padilicious.com/code/touchevents/

// TOUCH-EVENTS SINGLE-FINGER SWIPE-SENSING JAVASCRIPT
// Courtesy of PADILICIOUS.COM and MACOSXAUTOMATION.COM

// this script can be used with one or more page elements to perform actions based on them being swiped with a single finger

swipe = function(element, callback) {

    var triggerElementId = null; // this variable is used to identity the triggering element
    var fingerCount = 0;
    var startX = 0;
    var startY = 0;
    var curX = 0;
    var curY = 0;
    var deltaX = 0;
    var deltaY = 0;
    var horzDiff = 0;
    var vertDiff = 0;
    var minLength = 72; // the shortest distance the user may swipe
    var swipeLength = 0;
    var swipeAngle = null;
    var swipeDirection = null;
    
    // The 4 Touch Event Handlers
    
    // NOTE: the touchStart handler should also receive the ID of the triggering element
    // make sure its ID is passed in the event call placed in the element declaration, like:
    // <div id="picture-frame" ontouchstart="touchStart(event,'picture-frame');"  ontouchend="touchEnd(event);" ontouchmove="touchMove(event);" ontouchcancel="touchCancel(event);">
    
    var touchStart = function(event,passedName) {
        // disable the standard ability to select the touched object
        event.preventDefault();
        // get the total number of fingers touching the screen
        fingerCount = event.touches.length;
        // since we're looking for a swipe (single finger) and not a gesture (multiple fingers),
        // check that only one finger was used
        if ( fingerCount == 1 ) {
            // get the coordinates of the touch
            startX = event.touches[0].pageX;
            startY = event.touches[0].pageY;
            // store the triggering element ID
            triggerElementId = passedName;
        } else {
            // more than one finger touched so cancel
            touchCancel(event);
        }
    }
    
    var touchMove = function(event) {
        event.preventDefault();
        if ( event.touches.length == 1 ) {
            curX = event.touches[0].pageX;
            curY = event.touches[0].pageY;
        } else {
            touchCancel(event);
        }
    }
    
    var touchEnd = function(event) {
        event.preventDefault();
        // check to see if more than one finger was used and that there is an ending coordinate
        if ( fingerCount == 1 && curX != 0 ) {
            // use the Distance Formula to determine the length of the swipe
            swipeLength = Math.round(Math.sqrt(Math.pow(curX - startX,2) + Math.pow(curY - startY,2)));
            // if the user swiped more than the minimum length, perform the appropriate action
            if ( swipeLength >= minLength ) {
                caluculateAngle();
                determineSwipeDirection();
                processingRoutine();
                touchCancel(event); // reset the variables
            } else {
                touchCancel(event);
            }
        } else {
            touchCancel(event);
        }
    }
    
    var touchCancel = function(event) {
        // reset the variables back to default values
        fingerCount = 0;
        startX = 0;
        startY = 0;
        curX = 0;
        curY = 0;
        deltaX = 0;
        deltaY = 0;
        horzDiff = 0;
        vertDiff = 0;
        swipeLength = 0;
        swipeAngle = null;
        swipeDirection = null;
        triggerElementId = null;
    }
    
    var caluculateAngle = function() {
        var X = startX-curX;
        var Y = curY-startY;
        var Z = Math.round(Math.sqrt(Math.pow(X,2)+Math.pow(Y,2))); //the distance - rounded - in pixels
        var r = Math.atan2(Y,X); //angle in radians (Cartesian system)
        swipeAngle = Math.round(r*180/Math.PI); //angle in degrees
        if ( swipeAngle < 0 ) { swipeAngle =  360 - Math.abs(swipeAngle); }
    }
    
    var determineSwipeDirection = function() {
        if ( (swipeAngle <= 45) && (swipeAngle >= 0) ) {
            swipeDirection = 'left';
        } else if ( (swipeAngle <= 360) && (swipeAngle >= 315) ) {
            swipeDirection = 'left';
        } else if ( (swipeAngle >= 135) && (swipeAngle <= 225) ) {
            swipeDirection = 'right';
        } else if ( (swipeAngle > 45) && (swipeAngle < 135) ) {
            swipeDirection = 'down';
        } else {
            swipeDirection = 'up';
        }
    }
    
    var processingRoutine = function() {
        callback(swipeDirection);
    }

    var add = function(name, handler) {
        document.addEventListener(name, handler, false);
    }

    // Todo: this ID must be selectable by the user.
    element.id = 'swipe_element';
    add('touchstart', function(event) { touchStart(event, element.id); });
    add('touchend', function(event) { touchEnd(event); });
    add('touchmove', function(event) { touchMove(event); });
    add('touchcancel', function(event) { touchCancel(event); });
}
