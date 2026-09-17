(function(){
  var box = document.getElementById('mw-search');
  if (!box) return;
  var input = box.querySelector('input');
  var res = box.querySelector('.s-results');
  var idx = null, items = [], sel = -1, timer = null;

  function esc(s){ return s.replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function load(){
    if (idx) return Promise.resolve(idx);
    return fetch('assets/search-index.json').then(function(r){ return r.json(); }).then(function(j){ idx = j; return idx; });
  }
  function rank(q, e){
    var t = e.t.toLowerCase(), ql = q.toLowerCase();
    if (t.indexOf(ql) === 0) return 0;
    if (t.indexOf(ql) > -1) return 1;
    return 2;
  }
  function render(q){
    res.innerHTML = '';
    items = []; sel = -1;
    if (!q) { res.hidden = true; return; }
    var ql = q.toLowerCase();
    var hits = idx.filter(function(e){ return (e.t + ' ' + e.c).toLowerCase().indexOf(ql) > -1; });
    hits.sort(function(a, b){ return rank(q, a) - rank(q, b); });
    hits = hits.slice(0, 8);
    if (!hits.length) {
      res.hidden = false;
      res.innerHTML = '<div class="none">没有匹配的内容，换个关键词试试</div>';
      return;
    }
    res.hidden = false;
    hits.forEach(function(e){
      var a = document.createElement('a');
      a.className = 'sr'; a.href = e.u;
      a.innerHTML = '<span class="t">' + esc(e.t) + '</span><span class="cat">' + esc(e.c) + '</span>';
      res.appendChild(a); items.push(a);
    });
    sel = 0; items[0].classList.add('sel');
  }
  function move(dir){
    if (!items.length) return;
    if (sel > -1) items[sel].classList.remove('sel');
    sel = (sel + dir + items.length) % items.length;
    items[sel].classList.add('sel');
    items[sel].scrollIntoView({ block: 'nearest' });
  }
  input.addEventListener('input', function(){
    clearTimeout(timer);
    timer = setTimeout(function(){ load().then(function(){ render(input.value.trim()); }); }, 120);
  });
  input.addEventListener('keydown', function(e){
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter') { e.preventDefault(); if (items[sel]) location.href = items[sel].href; }
    else if (e.key === 'Escape') { input.value = ''; render(''); input.blur(); }
  });
  document.addEventListener('click', function(e){
    if (!box.contains(e.target)) { res.hidden = true; res.innerHTML = ''; items = []; sel = -1; }
  });
})();