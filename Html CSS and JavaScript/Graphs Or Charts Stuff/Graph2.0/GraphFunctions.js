function CreateGraph()
        {
            var from_value = document.getElementById("data_from").value;
            var to_value = document.getElementById("data_to").value;
        
            return new Chart("myChart", {
              type: "line",
              data: {
                labels: xValues.slice(from_value, to_value),                                                            // imported from values.js // also the .slice is basically the python xValues[3:6] here you take all the items from index 3 to 6 and makes a new list of it
                datasets: [{
                  fill: false,
                  lineTension: 0,
                  backgroundColor: document.getElementById('dot_color').value,                                          // dot color
                  borderColor: document.getElementById('line_color').value,                                             // line color
                  data: yValues.slice(from_value, to_value)                                                             // imported from values.js // also the .slice is basically the python yValues[3:6] here you take all the items from index 3 to 6 and makes a new list of it
                }]
              },
              options: {
                legend: {display: false},
                //scales: { // this is good when you want to set a fixed number height on a graph but in my case ill let the graph adjust by itself
                //  yAxes: [{ticks: {min: 0, max:11}}],
                //}
              }
            });
        }