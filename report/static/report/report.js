document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#generate-pdf-button').addEventListener('click', () => window.print())
})

// const generatePdf = () => {    
//   var pdf = new jsPDF('p', 'pt', 'letter');
//   source = $('#report-table')[0];
//   specialElementHandlers = {
//       '#bypassme': function (element, renderer) {
//           return true
//       }
//   };
//   margins = {
//       top: 80,
//       bottom: 60,
//       left: 40,
//       width: 522
//   };
//   pdf.fromHTML(
//       source, // HTML string or DOM elem ref.
//       margins.left, // x coord
//       margins.top, { // y coord
//           'width': margins.width, // max width of content on PDF
//           'elementHandlers': specialElementHandlers
//       },
//    function (dispose) {
//        // dispose: object with X, Y of the last line add to the PDF 
//        //          this allow the insertion of new lines after html
//        pdf.save('YourTable.pdf');
//    }, margins
//   );
// }