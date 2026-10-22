const b=document.querySelector('.burger'),l=document.querySelector('nav .links');
if(b&&l)b.addEventListener('click',()=>b.setAttribute('aria-expanded',l.classList.toggle('open')));
