# docker_container_text_compare_webservice
A docker container that can be started and ran that hosts a webservice with an end points to compare the similarities of two text strings.

<h1>How to run</h1>
  <h2>step 1.</h2> Docker will need to be installed on your device. <br/>
  <h2>step 2.</h2> clone this repo. (This repo only has the .py file for reference)<br/>
  <h2>step 3.</h2> Open a terminal. <br/>
  <h2>step 4.</h2> Run (this will pull the image down)<br/>
      <br/>
      docker pull paulrdurham/durham_python <br/>
      <br/>
        Yeah, I know. Its not a creative name. <br/>
  <h2>step 5.<h2/> Run (this will start the webservice while running the image)<br/>
        <br/>
        docker run -it -p 5000:5000 durham_python python /mnt/main.py<br/>
        <br/>
  <h2>step 6.<h2/><br/>
      You may now use curl commands to access the end point<br/>
 <br/>
  Example<br/>
      curl -g -X POST http://127.0.0.1:5000/compare -H "Content-Type: application/json" -d "{\"one\":\"This was the first test.\",\"two\":\"This is only a test.\"}" <br/>
    <br/>
    curl -g -X POST http://127.0.0.1:5000/compare -H "Content-Type: application/json" -d "{\"one\":\"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.\",\"two\":\"The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.\"}"<br/>
    <br/>
    curl -g -X POST http://127.0.0.1:5000/compare -H "Content-Type: application/json" -d "{\"one\":\"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.\",\"two\":\"We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way.\"}"<br/>
    <br/>
    2v3 curl -g -X POST http://127.0.0.1:5000/compare -H "Content-Type: application/json" -d "{\"one\":\"\The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.\",\"two\":\"We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way.\"}"<br/>
    <br/>
    <br/>
  Please note. I am using a windows PC and that is why i'm escaping the ". You may not need to do this on your PC.<br/>
  <br/>
Thanks and let me know if you have any questions! <br/>
  
