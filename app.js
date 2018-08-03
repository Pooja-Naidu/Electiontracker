$(document).ready(function(){
  $.ajax({ 
  url:"http://localhost/chart/data.php",
    method:"GET",
    success: function(data) {
      console.log(data);
      var udate = [] ;
      var ttl = [] ;

      for(var i in data){
        udate.push(data[i].updatedate);
        ttl.push(data[i].total);
      }
      var chartdata = {
        labels: udate,
        datasets : [
         { 
          label: 'update',
          backgroundColor: 'rgba(200,200,200,0.75)',
          borderColor: 'rgba(200,200,200,0.75)',
          hoverBackgroundColor: 'rgba(200,200,200,1)',
          hoverBorderColor: 'rgba(200,200,200,1)',
          data:ttl

        }

      ]
    };
    var ctx = $("#mycanvas");
    var barGraph = new Chart(ctx,{
      type: 'bar',
      data: chartdata
    });
  },
      error: function(data){
        console.log(data);
      }
  
  }); 
      });
    	