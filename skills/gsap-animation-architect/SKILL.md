---
name: gsap-animation-architect
description: Use when building modern, high-performance web animations, micro-interactions, scroll triggers, timelines, and smooth UI transitions using GSAP (GreenSock Animation Platform) in HTML, CSS, and Vanilla JS or frameworks.
---

# GSAP Animation Architect — High Performance Web Animations

This skill provides best practices, templates, and patterns for integrating **GSAP (GreenSock Animation Platform)** into web applications, portfolios, landing pages, and interactive dashboards.

---

## 🛠️ 1. CDN Inclusion (Vanilla JS / Pure HTML)

Include GSAP and key plugins via CDN in `<head>` or before `</body>`:

```html
<!-- GSAP Core -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

<!-- GSAP ScrollTrigger (for scroll-driven animations) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>

<!-- GSAP TextPlugin (for smooth typing and text morphing) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/TextPlugin.min.js"></script>
```

---

## 🚀 2. Essential GSAP Patterns

### 2.1 Staggered Reveal (Cards / Hero Elements)
```javascript
gsap.from(".anim-stagger", {
  duration: 0.8,
  y: 30,
  opacity: 0,
  stagger: 0.15,
  ease: "power3.out",
  clearProps: "all"
});
```

### 2.2 ScrollTrigger Section Unveil
```javascript
gsap.registerPlugin(ScrollTrigger);

gsap.utils.toArray(".scroll-section").forEach((section) => {
  gsap.from(section, {
    scrollTrigger: {
      trigger: section,
      start: "top 85%",
      toggleActions: "play none none reverse"
    },
    opacity: 0,
    y: 40,
    duration: 1,
    ease: "power2.out"
  });
});
```

### 2.3 Real-Time Counter Animation (Metrics / KPIs)
```javascript
function animateCounter(elementId, targetValue, duration = 2) {
  const obj = { value: 0 };
  gsap.to(obj, {
    value: targetValue,
    duration: duration,
    ease: "power1.out",
    onUpdate: () => {
      document.getElementById(elementId).textContent = Math.floor(obj.value).toLocaleString();
    }
  });
}
```

### 2.4 Dynamic Friction Meter / Glowing Status Pulse
```javascript
// Color shift animation for alert states
function setFrictionAlert(level) {
  const colorMap = {
    low: "#10b981",    // Emerald
    medium: "#f59e0b", // Amber
    high: "#ef4444"    // Crimson
  };
  
  gsap.to(".friction-badge", {
    backgroundColor: colorMap[level],
    boxShadow: `0 0 20px ${colorMap[level]}88`,
    duration: 0.6,
    ease: "power2.inOut"
  });
}
```

---

## ⚡ 3. Performance Best Practices

1. **Animate GPU-accelerated properties only:** Prefer `transform` (`x`, `y`, `scale`, `rotation`) and `opacity` over `top`, `left`, `width`, or `height`.
2. **Clear Props After Entry:** Use `clearProps: "all"` on `.from()` animations to avoid inline style conflicts with CSS hover states.
3. **Responsive Guards:** Wrap desktop-only heavy ScrollTriggers inside `gsap.matchMedia()`.
