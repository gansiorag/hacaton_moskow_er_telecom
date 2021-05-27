google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var name = [["{{name}}"]]
        var massiv = {{gist}}
        var data_first = name.concat(massiv);
        var data = google.visualization.arrayToDataTable(data_first)
        var options = {
                      title: 'Распределение юридических лиц \n по количеству счетчиков',
                      legend: { position: 'none' },
                      colors: ['#e7711c'],
                      vAxis: { scaleType: 'mirrorLog' }
                      };

        var chart = new google.visualization.Histogram(document.getElementById('grafity'));
        chart.draw(data, options);
        }