// Webcam Capture Functionality
document.addEventListener("DOMContentLoaded", function() {
    const videoElement = document.getElementById('webcam');
    const captureButton = document.getElementById('capture-btn');
    const captureArea = document.getElementById('capture-area');
    let videoStream = null;

    // Start the webcam feed
    function startWebcam() {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(function(stream) {
                    videoElement.srcObject = stream;
                    videoStream = stream;
                })
                .catch(function(err) {
                    alert("Error accessing webcam: " + err.message);
                });
        } else {
            alert("Your browser does not support webcam access.");
        }
    }

    // Stop the webcam feed (for cleanup)
    function stopWebcam() {
        if (videoStream) {
            let tracks = videoStream.getTracks();
            tracks.forEach(track => track.stop());
        }
    }

    // Trigger webcam to start capturing
    captureButton.addEventListener("click", function() {
        startWebcam();
        captureButton.disabled = true; // Disable button after capturing starts
    });

    // Function to capture image from the webcam feed
    function captureImage() {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');
        canvas.width = videoElement.videoWidth;
        canvas.height = videoElement.videoHeight;
        context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

        // Create an image element to display captured image
        const capturedImage = document.createElement('img');
        capturedImage.src = canvas.toDataURL('image/jpeg');
        captureArea.appendChild(capturedImage);

        // Optional: Send image to the server for processing or save
        // You can send capturedImage.src to your server or save it to your local machine
    }

    // Button to stop the webcam and capture image
    document.getElementById("capture-btn").addEventListener("click", captureImage);
});
