$(document).ready(function() {
    var recordButton = document.getElementById('recordButton');
    var stopButton = document.getElementById('stopButton');
    var preview = document.getElementById('preview');

    var chunks = [];
    var mediaRecorder;
    var audioStream;

    recordButton.addEventListener('click', startRecording);
    stopButton.addEventListener('click', stopRecording);

    function startRecording() {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(function(stream) {
                audioStream = stream;
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.addEventListener('dataavailable', onRecordingReady);
                mediaRecorder.start();

                recordButton.disabled = true;
                stopButton.disabled = false;
            })
            .catch(function(error) {
                console.error('Ошибка при получении доступа к микрофону:', error);
            });
    }

    function stopRecording() {
        mediaRecorder.stop();
        audioStream.getTracks().forEach(function(track) {
            track.stop();
        });

        recordButton.disabled = false;
        stopButton.disabled = true;
        uploadButton.disabled = false;
    }

    function onRecordingReady(event) {
        chunks.push(event.data);
        preview.src = URL.createObjectURL(event.data);
        preview.play();
    }
});