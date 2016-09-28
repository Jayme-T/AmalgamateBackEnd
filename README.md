# AmalgamateBackEnd

This is a server used to get data from various sensors. For more information about how this is being used see www.amalgamatecompost.com 
To use this API see the DOCS below

 
<div class="Documentation">
    <div class="documentationin">
        <h1> Composters API Documentation </h1>
        <p> This is documentation on how to access the API you create on your composter if you use my code
            <br> on my composter these routes are hit using ngrok so my requests look like
            <code> http://ngrok.io/test </code> Your requests will look different depending on how you run your composter. They may be ngrok or they may include a port if you are choosing to port forward.
        </p>
        <br>
    </div>
    <div class="requestsinner">
        <h1>
     Route <code> /test </code>
     <br>
     <div class="requesttype"> GET </div>
     </h1>
        <div class="resultdata">
            <p> This request will return an object with a key result and a value "test" this is a good route to test initial set up to see if you can access the api </p>
            <br> Example:
            <br>
            <div class="code">
                <code> {"result": "test"} </code>
            </div>
        </div>
    </div>
    <hr>
    <div class="requestsinner">
        <h1>
    Route <code> / </code>
    <br>
    <div class="requesttype"> GET </div>
    </h1>
        <div class="resultdata">
            <p> This request will return an object with a keys of "temp", "humidity" and "dewPoint" and values equivalent to the numeric results produced by the sht1x sensor </p>
            <br> Example:
            <br>
            <div class="code">
                <code> {"temp": 22,
                      "humidity": 21.4,
                      "dewPoint": 81}
                    </code>
            </div>
        </div>


    </div>
    <hr>
    <div class="requestsinner">
        <h1>
    Route <code> /data </code>
    <br>
    <div class="requesttype"> GET </div>
    </h1>
        <div class="resultdata">
            <p> This request will return an object with a keys of "data" and an array that contains another array of each data reading from the database. This includes temperature, humidity, dewPoint, date(), serial_id of the composters computers cpu </p>
            <br> Example:
            <br>
            <div class="code">
                <code> {data:[ [ 22.26, 34.30, 9.222, "2016-09-19:05:04",  "00000002499488"]]}
                    </code>
            </div>
        </div>
    </div>
    <hr>
    <div class="requestsinner">
        <h1>
    Route <code> /water </code>
    <br>
    <div class="requesttype"> POST </div>
    </h1>
        <div class="resultdata">
            <p> This request will water the compost and then return an object with a keys of "result" and a value of "finished water"</p>
                <br> Example:
                <br>
                <div class="code">
                    <code> {"result": "finished water"}
                    </code>
                </div>
        </div>


    </div>
    <hr>
    <div class="requestsinner">
        <h1>
    Route <code> /turn </code>
    <br>
    <div class="requesttype"> POST </div>
    </h1>
        <div class="result data">
            <p> This request will turn the compost and then return an object with a keys of "result" and a value of "finished turn"</p>
              <br>
              Example:
                <br>
                <div class="code">
                    <code>
                {"result": "finished turn"}
                    </code>
                </div>
        </div>


    </div>

</div>
