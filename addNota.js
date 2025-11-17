const titolo = document.getElementById("titolo");
const contenuto = document.getElementById("contenuto");
const bottone = document.getElementById("invia");

bottone.addEventListener('click', async function(){

    if(titolo.value.trim() !== "" && contenuto.value.trim() !== "") {
        let nota = {
            titolo: titolo.value.trim(),
            contenuto:contenuto.value.trim()
        }

        console.log(nota);

        await window.pywebview.api.aggiungiNota(nota);
    }
    await window.pywebview.api.aggiornaGrafica();

    await window.pywebview.api.chiudiFinestra();
});