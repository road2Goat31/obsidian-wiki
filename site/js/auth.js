
const CORRECT_HASH = "95b13345df14c4fd17e105b15961cf6e1386e8ba0ce9e8444aa6b9afebb5b802"; 

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
        location.reload();
    } else {
        document.body.innerHTML = "<h2>❌ Falsches Passwort!</h2>";
    }
}

function logout() {
    localStorage.removeItem("authenticated");
    location.reload();
}

// Falls der Nutzer nicht eingeloggt ist → Passwort abfragen
if (localStorage.getItem("authenticated") !== "true") {
    checkPassword();
}
