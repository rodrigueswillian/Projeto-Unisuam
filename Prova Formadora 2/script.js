const form = document.getElementById("formCadastro");
const modal = document.getElementById("modal");
const fechar = document.getElementById("fecharModal");

form.addEventListener("submit", function(e) {
    e.preventDefault();

    let senha = document.getElementById("senha").value;
    let confirmar = document.getElementById("confirmar").value;

    if (senha !== confirmar) {
        alert("As senhas não coincidem!");
        return;
    }

    modal.style.display = "flex";


    form.reset();
});


fechar.addEventListener("click", function() {
    modal.style.display = "none";
});


window.addEventListener("click", function(e) {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});