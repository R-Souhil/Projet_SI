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


const printbtn = document.getElementById('print-button');
printbtn.addEventListener('click', function () {
    window.print();
}
)


function checkboxChanged(checkbox) {
    var row = checkbox.parentNode.parentNode;
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
    var quantityInput = document.getElementsByName("quantite_" + checkbox.value)[0];
    quantityInput.disabled = !checkbox.checked;

    updateTotal();
}


function updateTotal() {
    var checkboxes = document.getElementsByName("produits");
    var totalAmount = 0;
    var montantPaye = document.getElementById("paymentfrn");

    for (var i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            var quantityInput = document.getElementsByName("quantite_" + checkboxes[i].value)[0];
            var price = parseFloat(checkboxes[i].parentNode.previousElementSibling.textContent);
            var partialAmount = price * parseFloat(quantityInput.value);
            totalAmount += partialAmount;
        }
    }

    var totalQuantityInput = document.getElementById("montant");
    if (totalQuantityInput) {
        totalQuantityInput.value = totalAmount.toFixed(2);
    }
    montantPaye.max=totalAmount;
}

  function checkboxChanged(checkbox) {
    var quantityInput = document.getElementsByName("quantite_" + checkbox.value)[0];
    quantityInput.disabled = !checkbox.checked;

    updateTotal();
}


function Changed(input) {
    let row = input.parentNode.parentNode;
    let prix_ht = row.children[2].children[0].value;
    let qte = row.children[4].children[0].value;
    console.log(row.children[5].children[0])
    row.children[5].innerText = prix_ht * qte + " DA"
}

function Changed2(input) {
    let row = input.parentNode.parentNode;
    let prix = row.children[2].children[0].value;
    let qte = row.children[3].children[0].value;
    console.log(row.children[4].children[0])
    row.children[4].innerText = prix * qte + " DA"
}
