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
    document.getElementById('formOne').submitForms;
    document.getElementById('formTwo').submitForms;
    document.getElementById('formThree').submitForms;
    document.getElementById('formFour').submitForms;
    document.getElementById('formFive').submitForms;
    document.getElementById('formSix').submitForms;
    console.log('All forms submitted');
}