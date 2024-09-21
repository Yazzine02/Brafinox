<template>
    <div>
        <header>
            <nav class="navbar">
                <span @click="toggleMenu" class="hamburger-btn material-symbols-rounded">menu</span>
                <a href="#" class="logo">
                    <img src="https://tse1.mm.bing.net/th?id=OIG3.bLiislsdayUNw.FdQQOc&pid=ImgGn" alt="logo">
                    <h2>CodingAPI</h2>
                </a>
                <ul class="links" :class="{ 'show-menu': showMenu }">
                    <span @click="hideMenu" class="close-btn material-symbols-rounded">close</span>
                    <li><a href="#"><b>Home</b></a></li>
                    <li><a href="#"><b>Help</b></a></li>
                </ul>
                <button @click="togglePopup" class="login-btn">se connecter</button>
            </nav>
        </header>

        <div class="blur-bg-overlay" v-if="showPopup"></div>
        <div class="form-popup" v-if="showPopup">
            <span @click="togglePopup" class="close-btn material-symbols-rounded">fermer</span>
            <div class="form-box" :class="{ 'signup': isSignup, 'login': !isSignup }">
                <div class="form-details">
                    <h2>{{ isSignup ? 'cree un compte' : 'Bienvenue' }}</h2>
                    <p>{{ isSignup ? 'Pour rejoindre notre entreprise, veuillez vous inscrire en utilisant vos informations personnelles.' : 'Veuillez vous connecter à l\'aide de vos informations personnelles.' }}</p>
                </div>
                <div class="form-content">
                    <h2>{{ isSignup ? 'S\'inscrire' : 'connexion' }}</h2>
                    <form action="#">
                        <div class="input-field">
                            <input type="text" required>
                            <label>{{ isSignup ? 'Saisissez votre adresse email' : 'Email' }}</label>
                        </div>
                        <div class="input-field">
                            <input type="password" required>
                            <label>{{ isSignup ? 'creé un mots de passe' : 'Mots de passe' }}</label>
                        </div>
                        <a href="#" class="forgot-pass-link" v-if="!isSignup">Mots de passe oublier?</a>
                        <button type="submit">{{ isSignup ? 'S\'inscrire' : 'se connecter' }}</button>
                    </form>
                    <div class="bottom-link">
                        Vous {{ isSignup ? 'avez déjà un compte ?' : 'n\'avez pas de compte ?' }}
                        <a href="#" @click.prevent="toggleSignup">{{ isSignup ? 'Connexion' : 'S\'inscrire' }}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showMenu: false,
            showPopup: false,
            isSignup: false,
        };
    },
    methods: {
        toggleMenu() {
            this.showMenu = !this.showMenu;
        },
        hideMenu() {
            this.showMenu = false;
        },
        togglePopup() {
            this.showPopup = !this.showPopup;
        },
        toggleSignup() {
            this.isSignup = !this.isSignup;
        },
    },
};
</script>

<style scoped>
/* Ajoute ici ton CSS existant, ou importe le fichier CSS si nécessaire */
</style>
