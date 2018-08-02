$(document).ready(function(){
	$.ajax({
		url: "http://localhost/mychart/js/data.php",
		method: "GET",
		success: function(data) {
			console.log(data);
			var updatedate = [];
			var total = [];

			for(var i in data) {
				date.push("updatedate " + data[i].updatedate);
				total.push(data[i].total);
			}

			var chartdata = {
				labels: updatedate,
				datasets : [
					{
						label: 'updatedate',
						backgroundColor: 'rgba(200, 200, 200, 0.75)',
						borderColor: 'rgba(200, 200, 200, 0.75)',
						hoverBackgroundColor: 'rgba(200, 200, 200, 1)',
						hoverBorderColor: 'rgba(200, 200, 200, 1)',
						data: total
					}
				]
			};

			var ctx = $("#mycanvas");

			var barGraph = new Chart(ctx, {
				type: 'bar',
				data: chartdata
			});
		},
		error: function(data) {
			console.log(data);
		}
	});
});