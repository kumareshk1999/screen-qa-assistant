chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: request.text })
    })
    .then(res => res.json())
    .then(data => {
        chrome.storage.local.set({ answer: data.answer });
    });
});