// Sélectionne les boutons
const stockButton = document.getElementById('stockBtn');
const clientButton = document.getElementById('clientBtn');

// Redirection lorsque l'utilisateur clique sur le bouton "Stock"
stockButton.addEventListener('click', function() {
    window.location.href = 'stock.html'; // Remplacer par l'URL de la page "stock"
});

// Redirection lorsque l'utilisateur clique sur le bouton "Client"
clientButton.addEventListener('click', function() {
    window.location.href = 'client.html'; // Remplacer par l'URL de la page "client"
});