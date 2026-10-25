// Links navigate authored chapters. They do not alter assumptions or calculate effects.
(() => {
  const chapters = [...document.querySelectorAll('.chapter')];
  const links = [...document.querySelectorAll('[data-stop]')];
  function show(id, focus = false) {
    if (!chapters.some(chapter => chapter.id === id)) return;
    document.documentElement.classList.add('enhanced');
    chapters.forEach(chapter => { chapter.hidden = chapter.id !== id; });
    links.forEach(link => {
      if (link.dataset.stop === id) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
    if (focus) {
      const heading = document.querySelector(`#${id} h2`);
      heading.focus({preventScroll: true});
      if (matchMedia('(max-width:900px)').matches) heading.scrollIntoView({block: 'start'});
    }
  }
  links.forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    history.pushState(null, '', link.getAttribute('href'));
    show(link.dataset.stop, true);
  }));
  function restore() {
    const id = location.hash.slice(1);
    if (chapters.some(chapter => chapter.id === id)) show(id);
    else if (!id) show('home');
  }
  addEventListener('popstate', restore);
  addEventListener('hashchange', restore);
  show('home');
  restore();
})();
