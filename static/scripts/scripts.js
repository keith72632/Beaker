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