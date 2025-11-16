const titolo = document.getElementById("titolo");
const contenuto = document.getElementById("contenuto");
const bottone = document.getElementById("invia");

bottone.addEventListener('click', function(){

    if(titolo.value.trim() !== "" && contenuto.value.trim() !== "") {
        let nota = {
            titolo: titolo.value.trim(),
            contenuto:contenuto.value.trim()
        }

        console.log(nota);

        window.pywebview.api.aggiungiNota(nota);

        window.pywebview.api.chiudiFinestra();
    }
    window.pywebview.api.aggiornaGrafica();
});