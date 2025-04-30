document.getElementById('win-btn').addEventListener('click', () => {
    sendResult('win');
});

document.getElementById('lose-btn').addEventListener('click', () => {
    sendResult('lose');
});

function sendResult(result) {
    fetch('https://your-backend.herokuapp.com/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            user_id: window.Telegram.WebApp.initDataUnsafe.user?.id,
            result: result,
            bet: 100
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('next-bet').textContent = data.new_bet;
        document.getElementById('balance').textContent = data.balance;
        document.getElementById('level').textContent = data.level;
        document.getElementById('result').style.display = 'block';
        
        // Анимация
        const rocket = document.getElementById('rocket');
        rocket.style.backgroundImage = result === 'win' 
            ? "url('assets/rocket.gif')" 
            : "url('assets/explosion.gif')";
    });
}
