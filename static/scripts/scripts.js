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