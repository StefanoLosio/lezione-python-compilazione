async function caricaAgenda() {
    const bacheca = document.getElementById("bacheca");

    bacheca.innerHTML = "";

    const agenda = await window.pywebview.api.getAgenda();
    console.log(agenda)

    Object.values(agenda).forEach(element => {
        const nota = document.createElement("div");
        nota.classList.add("nota");
        nota.id = element.id;

        nota.innerHTML = `
            <div style="display: flex; flex-direction: row; width: 100%; height: 20%; justify-content: space-between;">
                    <div class="nome_nota">${element.titolo}</div>
                    <div class="edit">
                        <button class="mod">✏️</button>
                        <button class="del">🗑️</button>
                    </div>
                </div> 
            <div class="contenuto">${element.contenuto}</div>
        `;

        bacheca.appendChild(nota);
    });
}