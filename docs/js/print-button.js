document.addEventListener("DOMContentLoaded", function () {
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
});
