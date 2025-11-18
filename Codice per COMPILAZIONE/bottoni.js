const nuova_nota = document.getElementById("add");

nuova_nota.addEventListener('click', function(){
    window.pywebview.api.apriForm();
});