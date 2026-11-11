const { exec } = require('child_process');

// Unutar tvoje funkcije nakon što izvučeš podatke:
if (vrijednost > 200) {
    exec('python alarm.py'); // Ovo će pokrenuti prozor i zvuk
}
const puppeteer = require('puppeteer');
const fs = require('fs');

async function checkAir() {
    console.log("Provjeravam zrak...");
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    
    try {
        await page.goto('https://zrak.infomedica.hr/mobilna-stanica-koromacno', { waitUntil: 'networkidle0', timeout: 60000 });
        
        // Čeka da se podaci učitaju
        await page.waitForFunction(() => document.body.innerText.includes('Izmjerene vrijednosti'), { timeout: 30000 });
        
        const text = await page.evaluate(() => document.body.innerText);
        const lines = text.split('\n');
        
        // Izvlači samo dio s vrijednostima
        let start = lines.findIndex(l => l.includes('Izmjerene vrijednosti'));
        let result = lines.slice(start, start + 12).join('\n').trim();
        
        const time = new Date().toLocaleString('hr-HR');
        const zapis = `\n--- ${time} ---\n${result}\n`;
        
        console.log(zapis);
        fs.appendFileSync('zrak-log.txt', zapis);
        
    } catch (err) {
        console.error('Greška:', err.message);
    } finally {
        await browser.close();
    }
}

// Pokreni odmah
checkAir();

// Postavi da se ponavlja svakih 60 minuta (3600000 ms)
setInterval(checkAir, 60 * 60 * 1000);