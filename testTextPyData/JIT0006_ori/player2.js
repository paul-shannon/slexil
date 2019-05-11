
function setValues() {
    // A reference to the Flowplayer instance.
    window.fp = document.getElementsByTagName("audio")[0];
    
    // Reference to the current annotation being played.
    window.currentAnnotation = null;
    
    // ID of the timer which tracks the end of annotations.
    window.endAnnotationTimer = null;
    
    //set variable to store scroll value for the window
    window.previousScroll = 0;
    
    //get left fixed position of player
    window.playerLeftMax = window.fp.getBoundingClientRect().left - 4;

}

//get the current scroll Position

function getScrollPosition() {
    scrollPosition = 0;
    if (document.body & document.body.scrollTop) {
        scrollPosition = document.body.scrollTop;
    } else if (document.documentElement && document.documentElement.scrollTop) {
        scrollPosition = document.documentElement.scrollTop;
    } else if (window.pageYOffset) {
        scrollPosition = window.pageYOffset;
    }
    return scrollPosition;
}

// get the current window height

function getWindowHeight() {
    windowHeight = 0;
    if (typeof(window.innerHeight) == 'number') {
        windowHeight = window.innerHeight;
    } else if (document.documentElement && document.documentElement.clientHeight) {
        windowHeight = document.documentElement.clientHeight;
    } else if (document.body && document.body.clientHeight) {
        windowHeight = document.body.clientHeight;
    }
    return windowHeight;
}

// Returns the annotation in which this time (in milliseconds) occurs, or
// null if this time is not associated with an annotation.

function findAnnotation(time_ms) {
        for (var i = 0; i < window.annotations.length; i++) {
            annotation = window.annotations[i];
            if ((time_ms >= annotation.start) && (time_ms <= annotation.end)) 	{
                return annotation;
            }
        }

        return null;
}

//set the player at the bottom of the screen, left aligned and fit to text
//corrects for sidebar width and window resize, not pretty if the page has a footer
//some of this function is specific to WordPress Theme 2014

function setPlayer() {
    windowHeight = getWindowHeight();
    playerPosition = windowHeight - 33;
    topPixels = playerPosition.toString() + "px"
    document.getElementById('CuPEDPlayer').style.top = topPixels;
    textWidth = window.innerWidth;
    sidebarWidth = window.innerWidth - textWidth;
    if (sidebarWidth > window.playerLeftMax) {
        sidebarWidth = window.playerLeftMax;
    }
    leftPixels = sidebarWidth.toString() + "px";
    document.getElementById('CuPEDPlayer').style.left = leftPixels;
    playerWidth = textWidth - 8;
    playerPixels = playerWidth.toString() + "px";
    document.getElementById('CuPEDPlayer').style.width = playerPixels;
}

// Scroll to a position where the annotation is in the specified spot
// on the screen ('top', 'middle', 'bottom', 'none' (no tracking)).

function scrollToAnnotation(annotation, position) {
    // If we should not scroll to follow the current annotation, skip this
    // code.
    if (position == 'none') {
        return;
    }
    
    // Get the current scroll position.
    scrollPosition = getScrollPosition();
    
    // Get the height of the current window.
    windowHeight = getWindowHeight();
    
    //get bottom of window
    docViewBottom = scrollPosition + windowHeight;

    // Get the height of the entire document.
    documentHeight = document.body.scrollHeight;

    // Get the height of the media player.
    mediaHeight = 33;

    // Get the y-position of the annotation in the page.
    div = document.getElementById(annotation.id);
    divPosition = div.offsetTop;
    while (div = div.offsetParent) {
        divPosition += div.offsetTop;
    }
    
    //Get bottom of element
    elemBottom = divPosition + document.getElementById(annotation.id).offsetHeight
    
    //check to see if annotation is onscreen before scrolling
    
    if (elemBottom >= docViewBottom) {

        finalPosition = divPosition;
        if (position == 'top') {
            finalPosition = divPosition - mediaHeight - 10;
        } else if (position == 'middle') {
            finalPosition = divPosition - mediaHeight -
                ((windowHeight - mediaHeight) / 2) +
                (document.getElementById(annotation.id).offsetHeight / 2);
        } else if (position == 'bottom') {
            finalPosition = divPosition - windowHeight +
                document.getElementById(annotation.id).offsetHeight + 10;
        } else {
            return;
        }
        window.scrollTo(0, finalPosition);
    }
}

function setCurrentAnnotation(annotation) {
        // Unset the current annotation, if there is one.
        if (window.currentAnnotation != null) {
            var anElement = document.getElementById(window.currentAnnotation.id);
            var m = anElement.className.match(' CuPED-current-annotation'); 
            anElement.className = anElement.className.replace(m, '');
        }

        // Set the current annotation to be the one given, if one was provided.
        if (annotation != null) {
            var anElement = document.getElementById(annotation.id);
            anElement.className += ' CuPED-current-annotation';

            // Scroll to the new element.
            scrollToAnnotation(annotation, 'top');
        }

        // Finally, keep a reference to the current annotation.
        window.currentAnnotation = annotation;
}

// Callback: check the Flowplayer instance to find out what annotation
// we're in and update the display as necessary.

function checkAnnotation() {
        closestAnnotation = findAnnotation(window.fp.currentTime);
        if (closestAnnotation != window.currentAnnotation) {
            setCurrentAnnotation(closestAnnotation);
        }
}

// Once the player has been initialized, begin watching for changes in
// the current annotation.
//
// The idea behind this is that the JavaScript polls the player every
// 'updateInterval' milliseconds to see if we've entered into a new
// annotation.  If we have, then the display is updated.

function onFlowPlayerReady() {
    setValues();
    setPlayer();
	window.fp.addEventListener("loadstart", function(){
        	window.currentAnnotation = null;
       		setInterval(checkAnnotation, 50);
		}
	);
    window.fp.addEventListener("pause", function(){
            if (window.currentAnnotation != null) {
                    var anElement = document.getElementById(window.currentAnnotation.id);
                    var m = anElement.className.match(' CuPED-current-annotation');
                    anElement.className = anElement.className.replace(m, '');
                }
        }
    );
    window.addEventListener("resize", function(){
                            setPlayer();
                            },
			true
    );
//    window.resize(function(){
//                            setPlayer();
//                            }
//    );
}

// Alright, if we can’t rely on cue points to work both for audio and for
// video, then we'll have to tie our own rope.

function onStop(clip) {
        clearInterval(window.endAnnotationTimer);
}

function onSeek(clip) {
        clearInterval(window.endAnnotationTimer);
}

function onPause(clip) {
        clearInterval(window.endAnnotationTimer);
}

// Callback: when an annotation is done, pause the player.

function onEndAnnotation(end_time) {
    if (window.fp.currentTime >= end_time) {
        window.fp.pause();
        clearInterval(window.endAnnotationTimer);
    }
}

// User wishes to play the annotation with the given ID and starting time
// (in seconds).

function playAnnotation(start_time, end_time) {
    // Start the media playing, then seek to the start of the annotation.
    window.fp.currentTime = start_time
    window.fp.play()
    
    window.endAnnotationTimer = setInterval(function(){onEndAnnotation(end_time)}, 50);

}
