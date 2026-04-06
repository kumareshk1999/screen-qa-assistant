chrome.storage.local.get("answer", (data) => {
    document.getElementById("answer").innerText =
        data.answer || "No answer yet";
});