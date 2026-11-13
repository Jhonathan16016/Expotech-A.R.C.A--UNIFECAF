
document.querySelectorAll('.temp').forEach(el =>{
        setInterval(async ()=>{
            try{
                const r = await fetch(el.dataset.url);
                if (!r.ok) return;
                const d = await r.json();
                el.textContent = d.temperatura;
            } catch (e) {}
    },1000);
});
