const toggleButton = () => {
    var element = document.getElementById('submitBtn');
    element.classList.toggle('btnclick');
    var coagulants = document.getElementById('coagulants');
    if(!coagulants.value){
         element.innerHTML = "Pick Coagulant";
         element.style.cssText = "background-color: #FC0404;"
    }
    element.innerHTML = "Finished";
}

const submitForms = () => {
    document.getElementById('formOne').submit();
    document.getElementById('formTwo').submit();
    document.getElementById('formThree').submit();
    document.getElementById('formFour').submit();
    document.getElementById('formFive').submit();
    document.getElementById('formSix').submit();
    console.log('All forms submitted');
}

const getBig = (e) => {
    e.style.cssText = 'font-size: 22px;';
}

const getSmall = (e) => {
    e.style.cssText = 'font-size: 20px;';
}

const Upload = () => {
    var fileUpload = document.getElementById("fileUpload");
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
    if (regex.test(fileUpload.value.toLowerCase())) {
        if (typeof (FileReader) != "undefined") {
            var reader = new FileReader();
            reader.onload = function (e) {
                var table = document.createElement("table");
                var rows = e.target.result.split("\n");
                for (var i = 0; i < rows.length; i++) {
                    var cells = rows[i].split(",");
                    if (cells.length > 1) {
                        var row = table.insertRow(-1);
                        for (var j = 0; j < cells.length; j++) {
                            var cell = row.insertCell(-1);
                            cell.innerHTML = cells[j];
                        }
                    }
                }
                var dvCSV = document.getElementById("dvCSV");
                dvCSV.innerHTML = "";
                dvCSV.appendChild(table);
            }
            reader.readAsText(fileUpload.files[0]);
        } else {
            alert("This browser does not support HTML5.");
        }
    } else {
        alert("Please upload a valid CSV file.");
    }
}