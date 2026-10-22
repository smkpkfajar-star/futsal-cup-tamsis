const rows=document.getElementById('rows'),add=document.getElementById('add');
const kelas='<select aria-label="Kelas"><option>Pilih kelas</option><option>VII</option><option>VIII</option><option>IX</option></select>';
function addRow(){
  const n=rows.children.length+1;if(n>12)return;
  const tr=document.createElement('tr');
  tr.innerHTML=`<td>${n}</td><td><input placeholder="Nama pemain" aria-label="Nama pemain ${n}"></td><td><input type="number" min="0" max="99" value="0" aria-label="No. punggung ${n}"></td><td>${kelas}</td><td><button class="cam" type="button" aria-label="Foto pemain ${n}"><svg><use href="#cam"/></svg></button></td>`;
  rows.appendChild(tr);add.disabled=n>=12;
}
for(let i=0;i<7;i++)addRow();
add.onclick=addRow;
