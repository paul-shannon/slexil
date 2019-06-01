// ijalUtil.js
//----------------------------------------------------------------------------------------------------
function playSample(audioID)
{
   console.log(audioID);
   document.getElementById(audioID).play();
}
//----------------------------------------------------------------------------------------------------

// Get the audio element with id="audioplayer"
var rec = document.getElementById("audioplayer");
var annotationPlaying = null;
var currentLine = null;
var currentAnnotation = 'none';

// Assign an ontimeupdate event to the audio element, and execute a function if the current playback position has changed
annotationPlaying = document.getElementById('1');
rec.ontimeupdate = function() {trackAnnotations()};
rec.onended = function() {removeFinalHighlight()};

function trackAnnotations() {
	currentAnnotation = findCurrentAnnotation(rec.currentTime);
	if (currentAnnotation != 'none') {
		if (currentAnnotation != null) {
			currentAnnotationID = currentAnnotation.id;
			currentLineID = currentAnnotationID.replace('a','');
			currentLine = document.getElementById(currentLineID);
			setCurrentAnnotation(currentLine);
			}
		} 
// 	document.getElementById("demo").innerHTML = currentAnnotationID;
	
}

//----------------------------------------------------------------------------------------------------

function setCurrentAnnotation(currentLine) {
        if (annotationPlaying != currentLine) {
            annotationPlaying.className ='line-wrapper';
        }
        currentLine.className += ' current-line';      
        annotationPlaying = currentLine;
        annotationPlaying.scrollIntoView(false);
        if (! isScrolledIntoView(annotationPlaying)) {
//        	console.log($(window).scrollTop());
        	elementHeight = $(annotationPlaying).height()+46;
        	newScroll = $(window).scrollTop()+elementHeight;
//        	console.log('newScroll:' + newScroll);
        	$(window).scrollTop = newScroll;
//         	$(window).stop().animate({
//         		scrollTop: newScroll
//         		});
//        	console.log($(window).scrollTop());
        }
        //window.scroll(0,23px);
}

//----------------------------------------------------------------------------------------------------
// Returns the annotation in which this time (in milliseconds) occurs, or
// null if this time is not associated with an annotation.

function findCurrentAnnotation(time_ms) {
        for (var i = 0; i < window.annotations.length; i++) {
            annotation = window.annotations[i];
            if ((time_ms >= annotation.start/1000) && (time_ms <= annotation.end/1000)) {
                return annotation;
            }
        }
        return null;
}

//----------------------------------------------------------------------------------------------------

function removeFinalHighlight() {
	annotationPlaying.className ='line-wrapper';
}
//----------------------------------------------------------------------------------------------------

function isScrolledIntoView(elem)
{
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height()+23;

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}