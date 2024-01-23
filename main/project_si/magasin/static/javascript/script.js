function SearchBar() {
    
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementsByClassName("trecherche")[0];
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td1 = tr[i].getElementsByTagName("td")[0];
        td2 = tr[i].getElementsByTagName("td")[1];
        if (td1) {
            txtValue1 = td1.textContent || td1.innerText;
            txtValue2 = td2.textContent || td2.innerText;
            if (txtValue1.toUpperCase().includes(filter) || txtValue2.toUpperCase().includes(filter)) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}


function printPage() {
    window.print();
}


function checkboxChanged(checkbox) {
    var row = checkbox.closest('tr');
    var inputs = row.querySelectorAll("input");

    if (checkbox.checked) {
        row.style.backgroundColor = "#d04462";
        for (var i = 1; i < inputs.length; i++) {
            inputs[i].disabled = false;
        }
    } else {
        row.style.backgroundColor = "#2a292e";
        for (var i = 1; i < inputs.length; i++) {
            inputs[i].disabled = true;
        }
    }
    updateTotal();
}

function updateTotal() {
    var total = 0;
    var checkboxes = document.querySelectorAll('input[name="produits"]:checked');
    
    checkboxes.forEach(function (checkbox) {
      var row = checkbox.closest('tr');
      var quantityInput = row.querySelector('input[name^="quantite"]');
      var priceInput = row.querySelector('#priceCalc');

      total += parseFloat(priceInput.value) * parseInt(quantityInput.value);
    });

    document.getElementById('montant').value = total;
}