document.addEventListener('DOMContentLoaded', () => {
    // 1. Sticky Header and Scroll Progress
    const header = document.querySelector('header');
    const handleScroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };
    window.addEventListener('scroll', handleScroll);
    handleScroll();

    // 2. Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.navigation');
    
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenuBtn.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });

        // Close menu when clicking navigation links
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuBtn.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('menu-open');
            });
        });
    }

    // 3. Product Grid Tab Switcher
    const tabButtons = document.querySelectorAll('.tab-btn');
    const productGrids = document.querySelectorAll('.product-grid-tab');

    if (tabButtons.length > 0 && productGrids.length > 0) {
        tabButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetTab = btn.getAttribute('data-tab');

                // Update active tab button
                tabButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // Update active product grid
                productGrids.forEach(grid => {
                    if (grid.id === targetTab) {
                        grid.classList.add('active');
                        grid.style.display = 'grid';
                    } else {
                        grid.classList.remove('active');
                        grid.style.display = 'none';
                    }
                });
            });
        });
    }

    // 4. FAQ Accordion Expand/Collapse
    const faqItems = document.querySelectorAll('.faq-item');
    
    if (faqItems.length > 0) {
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                
                // Close other open FAQ items (optional but nice)
                faqItems.forEach(i => i.classList.remove('active'));
                
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        });
    }

    // 5. Statistics Counter Animation
    const statNumbers = document.querySelectorAll('.stat-number');
    
    if (statNumbers.length > 0) {
        const animateCounter = (el) => {
            const target = parseInt(el.getAttribute('data-target'), 10);
            const duration = 2000; // ms
            const stepTime = 30; // ms
            const stepValue = target / (duration / stepTime);
            let current = 0;
            
            const timer = setInterval(() => {
                current += stepValue;
                if (current >= target) {
                    el.textContent = target.toLocaleString() + (el.getAttribute('data-suffix') || '');
                    clearInterval(timer);
                } else {
                    el.textContent = Math.floor(current).toLocaleString() + (el.getAttribute('data-suffix') || '');
                }
            }, stepTime);
        };

        const observerOptions = {
            root: null,
            threshold: 0.1,
            rootMargin: '0px'
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        statNumbers.forEach(num => observer.observe(num));
    }

    // 6. Countdown Timer for Promotional Banner
    const countdownEl = document.getElementById('promo-countdown');
    if (countdownEl) {
        // Set countdown to 24 hours from now for demonstration purposes
        const countdownDate = new Date().getTime() + (24 * 60 * 60 * 1000);
        
        const updateCountdown = () => {
            const now = new Date().getTime();
            const distance = countdownDate - now;
            
            if (distance < 0) {
                countdownEl.innerHTML = "EXPIRED";
                return;
            }
            
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            const pad = (num) => String(num).padStart(2, '0');
            
            const hoursHtml = `<div class="time-block"><span>${pad(hours)}</span><label>Hours</label></div>`;
            const minsHtml = `<div class="time-block"><span>${pad(minutes)}</span><label>Mins</label></div>`;
            const secsHtml = `<div class="time-block"><span>${pad(seconds)}</span><label>Secs</label></div>`;
            
            countdownEl.innerHTML = hoursHtml + minsHtml + secsHtml;
        };
        
        updateCountdown();
        setInterval(updateCountdown, 1000);
    }
});
