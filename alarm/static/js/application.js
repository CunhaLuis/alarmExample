$(document).ready(function(){

    setInterval(updateTable, 3000);

    

/*
    //connect to the socket server.
    var alarmUrl='http://127.0.0.1:5000/';  
    var socket = io.connect(alarmUrl);

    //var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    //var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number from doctor " + msg.doctor_office);
        
        
        //maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }            
        numbers_received.push(msg);
        
        rows = '';
        for (var i = 0; i < numbers_received.length; i++){
            rows = rows + '<tr>' + 
                            '<td>' + numbers_received[i].timestamp.toString() + '</td>' + 
                            '<td>' + numbers_received[i].doctor_office.toString() + '</td>'+
                            '<td>' + numbers_received[i].level.toString() + '</td>'
                          '</tr>';
            
        }
        
        var newRow = '<tr>' + 
                        '<td>' + numbers_received[i].timestamp.toString() + '</td>' + 
                        '<td>' + numbers_received[i].doctor_office.toString() + '</td>'+
                        '<td>' + numbers_received[i].level.toString() + '</td>'
                     '</tr>';


        $('#table').append(newRow);
    });
*/
});


function updateTable(){

    var alarmUrl='http://127.0.0.1:5000/updateData'

    $.get(alarmUrl, function(data, status){
        //console.log("Data: " + data + "\nStatus: " + status);
        var allData = JSON.parse(data);
        console.log(allData);

        // Empty tables
        $("table tbody").empty();

        var rows = '';
        for(var i=0; i<allData.length; i++){
 
            rows = rows + '<tr>' + 
                            '<td>' + allData[i].time + '</td>' + 
                            '<td>' + allData[i].doctor_office + '</td>'+
                            '<td>' + allData[i].level + '</td>'
                          '</tr>';
            
        }

        $("#table > tbody:last-child").append(rows)

    });    

}


