document.addEventListener("DOMContentLoaded", async function () {
    // Webseite vor dem Login unsichtbar machen
    document.body.style.display = "none";

    const CORRECT_HASH = "74acc7302baedbbf179966c973fed4a9c4a4110c8f2b685092565faa452e85b0"; 

    async function hashPassword(password) {
        const encoder = new TextEncoder();
        const data = encoder.encode(password);
        const hashBuffer = await crypto.subtle.digest("SHA-256", data);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');
    }

    async function checkPassword() {
        let userPassword = prompt("🔒 Bitte Passwort eingeben:");
        if (!userPassword) {
            document.body.innerHTML = "<h2>Zugriff verweigert!</h2>";
            return;
        }

        let hashedInput = await hashPassword(userPassword);

        if (hashedInput === CORRECT_HASH) {
            localStorage.setItem("authenticated", "true");
            document.body.style.display = "block"; // Seite anzeigen
        } else {
            document.body.innerHTML = "<h2>❌ Falsches Passwort!</h2>";
        }
    }

    function logout() {
        localStorage.removeItem("authenticated");
        location.reload();
    }

    // Falls der Nutzer nicht eingeloggt ist → Passwort abfragen
    if (localStorage.getItem("authenticated") === "true") {
        document.body.style.display = "block"; // Seite anzeigen
    } else {
        await checkPassword();
    }

    // Drucken-Button hinzufügen (nach erfolgreichem Login)
    let btn = document.createElement("button");
    btn.innerHTML = "📄 PDF speichern";
    btn.style.position = "fixed";
    btn.style.top = "20px";
    btn.style.right = "20px";
    btn.style.padding = "10px 15px";
    btn.style.background = "#007bff";
    btn.style.color = "white";
    btn.style.border = "none";
    btn.style.borderRadius = "5px";
    btn.style.cursor = "pointer";
    btn.onclick = function () {
        window.print();
    };
    document.body.appendChild(btn);

    // Logout-Button hinzufügen
    let logoutBtn = document.createElement("button");
    logoutBtn.innerHTML = "🔓 Logout";
    logoutBtn.style.position = "fixed";
    logoutBtn.style.top = "20px";
    logoutBtn.style.left = "20px";
    logoutBtn.style.padding = "10px 15px";
    logoutBtn.style.background = "red";
    logoutBtn.style.color = "white";
    logoutBtn.style.border = "none";
    logoutBtn.style.borderRadius = "5px";
    logoutBtn.style.cursor = "pointer";
    logoutBtn.onclick = logout;
    document.body.appendChild(logoutBtn);
});
