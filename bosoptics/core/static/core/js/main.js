document.addEventListener('DOMContentLoaded', () => {
    // Page loader
    const loader = document.getElementById('page-loader');
    if (loader) {
        window.addEventListener('load', () => {
            setTimeout(() => loader.classList.add('hidden'), 400);
        });
        setTimeout(() => loader.classList.add('hidden'), 2500);
    }

    // Sticky header
    const header = document.getElementById('site-header');
    const onScroll = () => {
        if (!header) return;
        header.classList.toggle('scrolled', window.scrollY > 60);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Back to top
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => {
            backToTop.classList.toggle('visible', window.scrollY > 500);
        }, { passive: true });
        backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }

    // Mobile menu
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const nav = document.querySelector('.navigation');
    if (mobileBtn && nav) {
        mobileBtn.addEventListener('click', () => {
            mobileBtn.classList.toggle('active');
            nav.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileBtn.classList.remove('active');
                nav.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });
    }

    // Scroll reveal
    const revealEls = document.querySelectorAll('.reveal');
    if (revealEls.length) {
        const revealObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        revealEls.forEach(el => revealObs.observe(el));
    }

    // Product tabs
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabGrids = document.querySelectorAll('.product-grid-tab');
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const target = btn.dataset.tab;
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            tabGrids.forEach(grid => {
                const show = grid.id === target;
                grid.style.display = show ? 'grid' : 'none';
                grid.classList.toggle('active', show);
            });
        });
    });

    // FAQ accordion
    document.querySelectorAll('.faq-item').forEach(item => {
        const q = item.querySelector('.faq-question');
        if (!q) return;
        q.addEventListener('click', () => {
            const wasActive = item.classList.contains('active');
            document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
            if (!wasActive) item.classList.add('active');
        });
    });

    // Stats counter
    const statNums = document.querySelectorAll('.stat-number');
    if (statNums.length) {
        const animate = (el) => {
            const target = parseInt(el.dataset.target, 10);
            const suffix = el.dataset.suffix || '';
            const duration = 2000;
            const start = performance.now();
            const step = (now) => {
                const progress = Math.min((now - start) / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 3);
                el.textContent = Math.floor(target * eased).toLocaleString() + suffix;
                if (progress < 1) requestAnimationFrame(step);
            };
            requestAnimationFrame(step);
        };
        const statObs = new IntersectionObserver((entries, obs) => {
            entries.forEach(e => {
                if (e.isIntersecting) { animate(e.target); obs.unobserve(e.target); }
            });
        }, { threshold: 0.3 });
        statNums.forEach(n => statObs.observe(n));
    }

    // Promo countdown
    const countdown = document.getElementById('promo-countdown');
    if (countdown) {
        const end = Date.now() + 24 * 60 * 60 * 1000;
        const tick = () => {
            const dist = end - Date.now();
            if (dist < 0) { countdown.innerHTML = '<span class="expired">Offer Expired</span>'; return; }
            const h = Math.floor(dist / 3600000) % 24;
            const m = Math.floor(dist / 60000) % 60;
            const s = Math.floor(dist / 1000) % 60;
            const pad = n => String(n).padStart(2, '0');
            countdown.innerHTML = `
                <div class="time-block"><span>${pad(h)}</span><label>Hours</label></div>
                <div class="time-block"><span>${pad(m)}</span><label>Mins</label></div>
                <div class="time-block"><span>${pad(s)}</span><label>Secs</label></div>`;
        };
        tick();
        setInterval(tick, 1000);
    }

    // Auto-dismiss alerts
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(120%)';
            setTimeout(() => alert.remove(), 400);
        }, 4500);
    });

    // Add to cart feedback
    document.querySelectorAll('.btn-add-cart').forEach(btn => {
        btn.addEventListener('click', () => {
            const orig = btn.textContent;
            btn.textContent = 'Added ✓';
            btn.classList.add('added');
            const count = document.querySelector('.cart-count');
            if (count) count.textContent = parseInt(count.textContent || '0', 10) + 1;
            setTimeout(() => { btn.textContent = orig; btn.classList.remove('added'); }, 2000);
        });
    });
});
