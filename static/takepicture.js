/**
 * Created by nikhil on 11/27/2016.
 */

var imageBlob;
function take_snapshot() {
    Webcam.snap( function(data_uri) {
        imageBlob = dataURItoBlob(data_uri);
    } );
    var file = new File([imageBlob], "image.jpg", {type: "image/jpeg"});
    console.log(file);
    var form = document.getElementById('myForm');
    var formData = new FormData(form);
    formData.append("file", file);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/compute/");

    // xmlhttp.onreadystatechange = function() {
    //
    // if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
    //     }
    // };

    xmlhttp.send(formData);
    console.log(formData.get('file'));
}

