

document.getElementById('add-row').addEventListener('click', function() {

    // 1. Access the table
    var table = document.getElementById('myTable').getElementsByTagName('tbody')[0];

    // 2. Create a new row at the end of the table
    var newRow = table.insertRow(table.rows.length);

    // 3. Create new cells in the row
    var nameCell = newRow.insertCell(0);
    var ageCell = newRow.insertCell(1);

    // 4. Set the content of the cells
    nameCell.textContent = 'John Doe';  // Example content
    ageCell.textContent = '30';         // Example content


});




