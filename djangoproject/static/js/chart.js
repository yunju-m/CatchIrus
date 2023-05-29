
const ctx = document.getElementById("myChart");
const data = {
  datasets: [{
    label: 'Safety',
    data: [80, 20],
    backgroundColor: [
      '#9DCEFF',
      '#F2F3F6'
    ],
    scaleBeginAtZero: true,
    borderWidth:0,
    hoverOffset: 2,
  }]
}
const options = {
  cutout: '50%',
}
const myChart = new Chart(ctx, {
    type: 'doughnut',
    data,
    options,
});

// var myDoughnutChart = new Chart(ctx, {
//   type: 'doughnut',
//   data: data,
//   options: {
//     plugins: {
//       doughnutlabel: {
//         labels: [
//           {
//             text: 'The title',
//             font: {
//               size: '60'
//             }
//           },
//           {
//             text: getTotal,
//             font: {
//               size: '50'
//             },
//             color: 'grey'
//           },
//           {
//             text: '$100.000',
//             font: {
//               size: '30'
//             },
//             color: 'red'
//           },
//           {
//             text: '95%',
//             font: {
//               size: '45'
//             },
//           color: 'green'
//           }
//         ]
//       }
//     }		
//   }
// });

// var getTotal = function(myDoughnutChart) {
//     var sum = myDoughnutChart.config.data.datasets[0].data.reduce((a, b) => a + b, 0);
//     return `Total: ${sum}`;
// }

