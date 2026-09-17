/* ============================================================
   MedWiki-Rheum 站点动效 site-anim.js（GSAP + ScrollTrigger 本地化）
   - 尊重 prefers-reduced-motion；GSAP 缺失时回退到内置 IO 显现
   - 接入页面加载顺序：gsap.min.js → ScrollTrigger.min.js → site-anim.js
   ============================================================ */
(function(){
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // 后台标签打开时跳过动画（rAF冻结会导致from()停在透明态），直接显示终态
  if (reduced || document.hidden || typeof gsap === 'undefined') return;
  if (typeof ScrollTrigger !== 'undefined') gsap.registerPlugin(ScrollTrigger);
  // 兜底：4秒后强制完成所有未完成补间，任何环境（后台标签/节流）内容保证可见
  setTimeout(function(){
    gsap.globalTimeline.getChildren(true, true, true).forEach(function(t){
      try { if (t.progress() < 1) t.progress(1); } catch(e){}
    });
  }, 4000);
  // GSAP接管后，中和 .rv 的CSS过渡避免双重动画
  var st = document.createElement('style');
  st.textContent = '.rv{opacity:1!important;transform:none!important;transition:none!important}';
  document.head.appendChild(st);

  // Hero 入场时间线
  var tl = gsap.timeline({defaults:{ease:'power3.out', duration:.7}});
  tl.from('.mhero .kicker', {y:14, opacity:0})
    .from('.mhero h1', {y:18, opacity:0}, '-=.45')
    .from('.mhero .lede', {y:12, opacity:0}, '-=.5')
    .from('.searchbox', {y:12, opacity:0}, '-=.5')
    .from('.chips .chip', {y:8, opacity:0, stagger:.05, duration:.4}, '-=.45')
    .from('.hpanel', {x:36, opacity:0, duration:.8}, '-=.55');

  if (typeof ScrollTrigger === 'undefined') return;

  // 章节标题
  gsap.utils.toArray('.msec-title').forEach(function(el){
    gsap.from(el, {y:16, opacity:0, duration:.6, scrollTrigger:{trigger:el, start:'top 88%'}});
  });
  // 精选卡：卡片浮起 + 内部元素分组交错（徽章→标题→简介→胶囊→按钮）
  gsap.utils.toArray('.feature').forEach(function(card){
    var tl = gsap.timeline({scrollTrigger:{trigger:card, start:'top 90%'}});
    tl.from(card, {y:22, opacity:0, scale:.985, duration:.6, ease:'power3.out'})
      .from(card.querySelectorAll('.ftag'), {y:-8, opacity:0, duration:.4}, '-=.3')
      .from(card.querySelectorAll('.ftitle'), {y:10, opacity:0, duration:.45}, '-=.32')
      .from(card.querySelectorAll('.fdesc'), {y:8, opacity:0, duration:.4}, '-=.3')
      .from(card.querySelectorAll('.fmeta span'), {y:6, opacity:0, stagger:.06, duration:.35}, '-=.28')
      .from(card.querySelectorAll('.go'), {x:18, opacity:0, duration:.45, ease:'power2.out'}, '-=.35');
  });
  // 覆盖卡 + 分段刻度条交错充填
  gsap.utils.toArray('.cov').forEach(function(el, i){
    gsap.from(el, {y:16, opacity:0, delay:(i%5)*.05, duration:.55, scrollTrigger:{trigger:el, start:'top 92%'}});
  });
  gsap.utils.toArray('.cov .bar').forEach(function(bar){
    var segs = bar.querySelectorAll('i.f');
    if (!segs.length) return;
    gsap.from(segs, {scaleX:0, transformOrigin:'left center', stagger:.04, duration:.5, ease:'power2.out', scrollTrigger:{trigger:bar, start:'top 92%'}});
  });
  // 入口卡批量交错
  ScrollTrigger.batch('.qa', {
    start:'top 94%',
    onEnter: function(b){ gsap.from(b, {y:14, opacity:0, stagger:.045, duration:.5, ease:'power2.out', overwrite:true}); }
  });
  // 时间线自左滑入
  gsap.utils.toArray('.tl-item').forEach(function(el){
    gsap.from(el, {x:-18, opacity:0, duration:.5, scrollTrigger:{trigger:el, start:'top 94%'}});
  });
  // 统计卡
  gsap.utils.toArray('.stat').forEach(function(el, i){
    gsap.from(el, {y:12, opacity:0, delay:(i%8)*.05, duration:.5, scrollTrigger:{trigger:el, start:'top 92%'}});
  });
})();
