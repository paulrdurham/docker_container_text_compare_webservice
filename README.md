# docker_container_text_compare_webservice
A docker container that can be started and ran that hosts a webservice with an end points to compare the similarities of two text strings.

<h1>How to run</h1>
  <h2>step 1.</h2> Docker will need to be installed on your device. <br/>
  <h2>step 2.</h2> clone this repo. (This repo only has the .py file for reference)<br/>
  <h2>step 3.</h2> Open a terminal. <br/>
  <h2>step 4.</h2> Run (this will pull the image down)<br/>
      docker pull paulrdurham/durham_python <br/>
        ## Yeah, I know. Its not a creative name. <br/>
  <h2>step 5.<h2/> Run (this will start the webservice while running the image)<br/>
      docker run -it -p 5000:5000 durham_python python /mnt/main.py<br/>
  <h2>step 6.<h2/><br/>
      You may now use curl commands to access the end point<br/>
 <br/>
  Example<br/>
      curl -g -X POST http://127.0.0.1:5000/compare -H "Content-Type: application/json" -d "{\"one\":\"This was the first test.\",\"two\":\"This is only a test.\"}" <br/>
    <br/>
  Please note. I am using a windows PC and that is why i'm escaping the ". You may not need to do this on your PC.<br/>
  <br/>
Thanks and let me know if you have any questions! <br/>
  
