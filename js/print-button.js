document.addEventListener("DOMContentLoaded", async function () {
    // Webseite vor dem Login unsichtbar machen
    document.body.style.display = "none"; // Zu Beginn ist die gesamte Seite unsichtbar

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
            document.body.style.display = "block"; // Erst nach erfolgreichem Login den Inhalt anzeigen
        } else {
            document.body.innerHTML = "<h2>❌ Falsches Passwort!</h2>";
        }
    }

    function logout() {
        localStorage.removeItem("authenticated");
        location.reload(); // Seite neu laden, um den Logout durchzuführen
    }

    // Falls der Nutzer nicht eingeloggt ist → Passwort abfragen
    if (localStorage.getItem("authenticated") === "true") {
        document.body.style.display = "block"; // Seite anzeigen
    } else {
        await checkPassword(); // Passwort eingeben lassen, wenn nicht eingeloggt
    }

    // Drucken-Button hinzufügen (nach erfolgreichem Login)
    let printBtn = document.createElement("button");
    printBtn.innerHTML = "📄 PDF speichern";
    printBtn.style.position = "fixed";
    printBtn.style.top = "20px";
    printBtn.style.right = "20px";
    printBtn.style.padding = "10px 15px";
    printBtn.style.background = "#007bff";
    printBtn.style.color = "white";
    printBtn.style.border = "none";
    printBtn.style.borderRadius = "5px";
    printBtn.style.cursor = "pointer";
    printBtn.onclick = function () {
        window.print();
    };
    document.body.appendChild(printBtn);

    // Logout-Button hinzufügen (diesmal ohne Inline-Styles in JS, sondern nur mit der CSS-Klasse)
    let logoutBtn = document.createElement("button");
    logoutBtn.id = "logout-button"; // ID setzen, damit es durch das CSS gestylt wird
    logoutBtn.innerHTML = "🔓 Logout";
    logoutBtn.onclick = logout;
    document.body.appendChild(logoutBtn);
});
