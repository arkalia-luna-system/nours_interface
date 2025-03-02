document.getElementById('send-message').addEventListener('click', async function () {
    const userMessage = document.getElementById('user-message').value;
    if (userMessage.trim() === '') return;
  
    const chatBox = document.getElementById('chat-box');
    
    // Afficher le message de l'utilisateur dans le chat
    chatBox.innerHTML += `<div><strong>Vous:</strong> ${userMessage}</div>`;
    document.getElementById('user-message').value = '';
  
    // Appel à l'API pour envoyer le message
    const response = await fetch('/api/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: userMessage }),
    });
  
    const data = await response.json();
  
    // Afficher la réponse de l'IA dans le chat
    chatBox.innerHTML += `<div><strong>IA:</strong> ${data.generated_text}</div>`;
  
    // Scroller vers le bas pour voir le dernier message
    chatBox.scrollTop = chatBox.scrollHeight;
  });