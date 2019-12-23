
//----------------------------------------------------------------------------------------------------
//returns a list of all ids of audio elements
function allAudioIds()
{
  var allElements = document.getElementsByTagName("audio");
  var allIds = [];
  for (var i = 0, n = allElements.length; i < n; ++i) {
    var el = allElements[i];
    if (el.id){
      allIds.push(el.id);
      }
    } // for i
  return(allIds)

} // allAudioIds
//----------------------------------------------------------------------------------------------------
// when the sound is complete, resolve is called. resolve is a function provided by the Promise api,
// indicating the successful completion of the promised activity. await pauses until the Promise resolves.
async function playOne(id)
{
   promiseContent = function(resolve, reject){
     var audio = document.getElementById(id);
     audio.addEventListener('ended', resolve);
     audio.play();
     } // promiseContent

   return(new Promise(promiseContent));

} // playOne
//----------------------------------------------------------------------------------------------------
// The await operator pauses for the completion of a Promise. It can only be used inside an async function.
async function playAll(audioElementIds)
{
  for(i=0; i< audioElementIds.length; i++){
    if(!globalVariable_continuePlaying)
       break;
    await playOne(audioElementIds[i])
    } // for i

} // playAll
//----------------------------------------------------------------------------------------------------
globalVariable_continuePlaying = false;
//----------------------------------------------------------------------------------------------------
function startSequentialPlayback()
{
  globalVariable_continuePlaying=true;
  var ids = allAudioIds()
  playAll(ids)

} // startSequentialPlayback
//----------------------------------------------------------------------------------------------------
function stopSequentialPlayback()
{
  globalVariable_continuePlaying=false;

} // stopSequentialPlayback
//----------------------------------------------------------------------------------------------------

// Get the audio element with id="fullplayback"
var rec = document.getElementById("fullplayback");

// Assign an ontimeupdate event to the audi element, and execute a function if the current playback position has changed
rec.ontimeupdate = function() {myFunction()};

function myFunction() {
  // Display the current position of the audio in a p element with id="demo"
  document.getElementById("demo").innerHTML = rec.currentTime;
  if(rec.currentTime == 4)
  	rec.pause();
}