/* ============================================================
   MedWiki-Rheum 全站分享组件 share.js（自包含：一行<script>接入）
   - 右下(左下)浮动分享球 + 弹层：微信扫码(本地QR) / 微博 / QQ好友 / QQ空间 / X / 复制链接
   - 主题自适应：优先消费页面token(--nav-a等)，缺失时回退GLM默认值
   - 规范URL：页面 <html data-share-url="..."> 可覆盖，缺省用 location.href
   - 依赖：/assets/qrcode.min.js（微信二维码；缺失时回退在线生成）
   ============================================================ */
(function(){
  if (window.__mwShare) return; window.__mwShare = true;
  var d = document;
  function init(){
    try {
    var shareUrl = d.documentElement.getAttribute('data-share-url')
                || d.body.getAttribute('data-share-url')
                || location.href;
    var shareTitle = d.title || 'MedWiki-Rheum';
    var u = encodeURIComponent(shareUrl), t = encodeURIComponent(shareTitle);

    var css = [
      '.mw-share-fab{position:fixed;left:16px;bottom:96px;z-index:1300;width:46px;height:46px;border-radius:50%;border:none;cursor:pointer;touch-action:none;user-select:none;-webkit-user-select:none;',
      'background:linear-gradient(135deg,var(--nav-a,#12365F),var(--nav-b,#1B4F8A));border-bottom:3px solid var(--nav-edge,#E8A33D);',
      'box-shadow:0 4px 14px rgba(0,0,0,.28);display:flex;align-items:center;justify-content:center;transition:transform .18s ease;}',
      '.mw-share-fab:hover{transform:translateY(-2px);}',
      '.mw-share-fab svg{width:20px;height:20px;fill:#fff;pointer-events:none;}',
      '.mw-share-pop{position:fixed;z-index:1301;width:242px;',
      'background:var(--surface,#fff);border:1px solid var(--border,#DDE5EC);border-radius:12px;overflow:hidden;',
      'box-shadow:0 10px 30px rgba(0,0,0,.20);}',
      '.mw-share-pop::before{content:"";display:block;height:5px;',
      'background:repeating-linear-gradient(135deg,var(--stripe-1,#1B4F8A) 0 7px,transparent 7px 11px,var(--stripe-2,#7FA8CC) 11px 18px,transparent 18px 23px,var(--stripe-3,#E8A33D) 23px 30px,transparent 30px 35px);}',
      '.mw-share-pop .hd{padding:10px 14px 4px;font-size:11px;font-weight:800;letter-spacing:.12em;color:var(--ink-faint,#93A2B1);}',
      '.mw-share-pop .it{display:flex;align-items:center;gap:10px;padding:8px 14px;cursor:pointer;font-size:13.5px;color:var(--ink,#22303F);text-decoration:none;transition:background .15s;font-family:inherit;}',
      '.mw-share-pop .it:hover{background:var(--accent-soft,#EAF1F8);}',
      '.mw-share-pop .it i{width:10px;height:10px;border-radius:50%;flex:none;}',
      '.mw-share-pop .it .u{margin-left:auto;font-size:11px;color:var(--ink-faint,#93A2B1);}',
      '.mw-share-pop .qr{display:none;padding:4px 14px 14px;text-align:center;}',
      '.mw-share-pop .qr.open{display:block;}',
      '.mw-share-pop .qr .box{display:inline-block;background:#fff;border:1px solid var(--border,#DDE5EC);border-radius:10px;padding:8px;}',
      '.mw-share-pop .qr .box img,.mw-share-pop .qr .box canvas{display:block;}',
      '.mw-share-pop .qr p{font-size:11px;color:var(--ink-soft,#5A6B7C);margin:7px 0 0;line-height:1.6;}',
      '.mw-wx-guide{position:fixed;top:0;left:0;right:0;z-index:1400;background:var(--accent-bright,#E8A33D);color:var(--accent-deep,#12365F);font-size:12.5px;font-weight:600;padding:8px 38px 8px 14px;line-height:1.6;box-shadow:0 2px 10px rgba(0,0,0,.20);}',
      '.mw-wx-guide b{font-weight:800;}',
      '.mw-wx-guide button{position:absolute;right:10px;top:7px;border:none;background:transparent;font-size:16px;line-height:1;cursor:pointer;color:inherit;font-family:inherit;}',
      '.mw-wx-guide span{display:block;}',
      '@media (max-width:480px){.mw-share-pop{width:min(92vw,242px);}}'
    ].join('');
    var st = d.createElement('style'); st.textContent = css; d.head.appendChild(st);

    // FAB
    var fab = d.createElement('button');
    fab.className = 'mw-share-fab';
    fab.setAttribute('aria-label', '分享这一页');
    fab.setAttribute('title', '分享这一页');
    fab.innerHTML = '<svg viewBox="0 0 24 24"><path d="M18 16.1c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92-1.31-2.99-2.92-2.99z"/></svg>';

    // Popover
    var pop = d.createElement('div');
    pop.className = 'mw-share-pop';
    pop.hidden = true;

    var inWeChat = /MicroMessenger/i.test(navigator.userAgent);
    var targets = [
      {k:'wechat',  label:'转发给微信好友', color:'#2AAE67', tip:'微信扫描二维码打开本页 → 转发给朋友'},
      {k:'moments', label:'分享到朋友圈', color:'#2AAE67', tip:'扫描二维码打开本页 → 点右上角「···」→ 分享到朋友圈'},
      {k:'weibo',  label:'微博', color:'#E6162D', href:'https://service.weibo.com/share/share.php?url='+u+'&title='+t},
      {k:'qq',     label:'QQ好友', color:'#12B7F5', href:'https://connect.qq.com/widget/shareqq/index.html?url='+u+'&title='+t},
      {k:'qzone',  label:'QQ空间', color:'#EBB428', href:'https://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url='+u+'&title='+t},
      {k:'x',      label:'X / Twitter', color:'#0F1419', href:'https://twitter.com/intent/tweet?url='+u+'&text='+t},
      {k:'copy',   label:'复制链接', color:'#5E6B7C'}
    ];
    function row(tg){
      var el = d.createElement(tg.href ? 'a' : 'div');
      el.className = 'it';
      if (tg.href) { el.href = tg.href; el.target = '_blank'; el.rel = 'noopener'; }
      el.innerHTML = '<i style="background:' + tg.color + '"></i>' + tg.label + '<span class="u">' + (tg.k==='wechat' ? '二维码' : (tg.href ? '↗' : '')) + '</span>';
      return el;
    }
    var map = {};
    targets.forEach(function(tg){
      var el = row(tg);
      if (tg.k === 'wechat' || tg.k === 'moments') el.addEventListener('click', function(e){ e.preventDefault(); toggleQR(tg.tip); });
      if (tg.k === 'copy') el.addEventListener('click', function(e){ e.preventDefault(); doCopy(el); });
      map[tg.k] = el;
      pop.appendChild(el);
    });
    // QR area
    var qrWrap = d.createElement('div');
    qrWrap.className = 'qr';
    qrWrap.innerHTML = '<span class="box" id="mw-qrbox"></span><p>微信扫一扫，在手机上打开本页后转发</p>';
    pop.appendChild(qrWrap);

    var qrMade = false;
    var tipEl = null;
    function toggleQR(tip){
      var open = qrWrap.classList.toggle('open');
      if (!tipEl) tipEl = qrWrap.querySelector('p');
      if (tip && tipEl) tipEl.textContent = tip;
      if (open && !qrMade) {
        var box = qrWrap.querySelector('#mw-qrbox');
        box.innerHTML = '';
        if (typeof QRCode !== 'undefined') {
          new QRCode(box, { text: shareUrl, width: 132, height: 132, correctLevel: QRCode.CorrectLevel.M });
        } else {
          var img = d.createElement('img');
          img.src = 'https://api.qrserver.com/v1/create-qr-code/?size=132x132&data=' + u;
          img.alt = '二维码';
          img.width = 132; img.height = 132;
          box.appendChild(img);
        }
        qrMade = true;
      }
    }
    function doCopy(el){
      function ok(){ var u2 = el.querySelector('.u'); u2.textContent = '已复制 ✓'; setTimeout(function(){ u2.textContent = ''; }, 1600); }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(shareUrl).then(ok, function(){ legacy(); });
      } else legacy();
      function legacy(){
        var ta = d.createElement('textarea');
        ta.value = shareUrl; ta.style.cssText = 'position:fixed;opacity:0;';
        d.body.appendChild(ta); ta.select();
        try { d.execCommand('copy'); ok(); } catch(e){}
        d.body.removeChild(ta);
      }
    }
    // 可拖拽 + 位置记忆（localStorage按设备保存；拖动≥7px算拖拽，否则算点击）
    var posKey = 'mw-share-pos';
    function placeFab(x, y){
      fab.style.left = x + 'px'; fab.style.top = y + 'px';
      fab.style.right = 'auto'; fab.style.bottom = 'auto';
    }
    try {
      var savedPos = JSON.parse(localStorage.getItem(posKey) || 'null');
      if (savedPos && typeof savedPos.x === 'number' && typeof savedPos.y === 'number'
          && savedPos.x >= 0 && savedPos.y >= 0
          && savedPos.x < window.innerWidth && savedPos.y < window.innerHeight) {
        // 横向钳制到左右边沟（永不遮正文），纵向按记忆保留
        var half = window.innerWidth / 2;
        var gx = (savedPos.x < half) ? Math.max(8, Math.min(savedPos.x, 64))
                                     : Math.max(window.innerWidth - 64, Math.min(savedPos.x, window.innerWidth - 54));
        placeFab(gx, savedPos.y);
      }
    } catch(e){}
    function placePop(){
      var fr = fab.getBoundingClientRect();
      var pw = pop.offsetWidth || 242, ph = pop.offsetHeight || 300;
      var left = Math.max(8, Math.min(fr.left, window.innerWidth - pw - 8));
      var top = fr.top - ph - 10;
      if (top < 8) top = Math.max(8, Math.min(fr.bottom + 10, window.innerHeight - ph - 8));
      pop.style.left = left + 'px'; pop.style.top = top + 'px';
      pop.style.right = 'auto'; pop.style.bottom = 'auto';
    }
    var drag = null, suppressTap = false;
    fab.addEventListener('pointerdown', function(e){
      if (e.button) return;
      var r = fab.getBoundingClientRect();
      drag = { sx: e.clientX, sy: e.clientY, ox: r.left, oy: r.top, moved: false };
      try { fab.setPointerCapture(e.pointerId); } catch(err){}
    });
    fab.addEventListener('pointermove', function(e){
      if (!drag) return;
      if (!drag.moved && Math.abs(e.clientX - drag.sx) + Math.abs(e.clientY - drag.sy) < 7) return;
      drag.moved = true;
      var fw = fab.offsetWidth || 46, fh = fab.offsetHeight || 46;
      var nx = Math.max(8, Math.min(drag.ox + e.clientX - drag.sx, window.innerWidth - fw - 8));
      var ny = Math.max(64, Math.min(drag.oy + e.clientY - drag.sy, window.innerHeight - fh - 8));
      placeFab(nx, ny);
      e.preventDefault();
    });
    function endDrag(){
      if (drag && drag.moved) {
        suppressTap = true;
        setTimeout(function(){ suppressTap = false; }, 80);
        var r = fab.getBoundingClientRect();
        try { localStorage.setItem(posKey, JSON.stringify({ x: Math.round(r.left), y: Math.round(r.top) })); } catch(e){}
        if (!pop.hidden) placePop();
      }
      drag = null;
    }
    fab.addEventListener('pointerup', endDrag);
    fab.addEventListener('pointercancel', function(){ drag = null; });
    window.addEventListener('resize', function(){
      try {
        var sv = JSON.parse(localStorage.getItem(posKey) || 'null');
        if (sv) placeFab(Math.max(8, Math.min(sv.x, window.innerWidth - 54)), Math.max(64, Math.min(sv.y, window.innerHeight - 54)));
      } catch(e){}
      if (!pop.hidden) placePop();
    });

    function toggle(force){
      var show = (typeof force === 'boolean') ? force : pop.hidden;
      pop.hidden = !show;
      if (show) placePop(); else qrWrap.classList.remove('open');
    }
    fab.addEventListener('click', function(){
      if (suppressTap) { suppressTap = false; return; }
      toggle();
    });
    d.addEventListener('click', function(e){
      if (!pop.hidden && !pop.contains(e.target) && !fab.contains(e.target)) toggle(false);
    });
    d.addEventListener('keydown', function(e){ if (e.key === 'Escape') toggle(false); });

    if (inWeChat) {
      var guide = d.createElement('div');
      guide.className = 'mw-wx-guide';
      guide.innerHTML = '<span>微信内浏览：点右上角「···」即可 <b>发送给朋友</b> / <b>分享到朋友圈</b></span><button aria-label="关闭">×</button>';
      guide.querySelector('button').addEventListener('click', function(){ guide.remove(); });
      d.body.appendChild(guide);
    }
    d.body.appendChild(fab);
    d.body.appendChild(pop);
    } catch(err) { window.__mwShareErr = (err && (err.stack || err.message)) || String(err); }
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', init);
  else init();
})();
