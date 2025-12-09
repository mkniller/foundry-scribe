Hooks.on("chatMessage", async (log, text) => {
  if (!text.startsWith("/scribe")) return;

  const q = text.replace("/scribe","").trim();
  const res = await fetch("http://localhost:8000/ask", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body: JSON.stringify({question:q})
  });
  const data = await res.json();
  ChatMessage.create({content:`<b>Scribe:</b> ${data.answer}`});
  return false;
});