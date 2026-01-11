async function carregarRifas() {
    const response = await fetch("/rifas");
    const rifas = await response.json();

    const lista = document.getElementById("lista-rifas");

    lista.innerHTML = "";

    rifas.forEach(rifa => {
        const item = document.createElement("li");
        item.innerText = `${rifa.nome} - R$ ${rifa.preco}`;
        lista.appendChild(item);
    });
}

carregarRifas();
