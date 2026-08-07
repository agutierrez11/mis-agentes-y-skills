---
name: emilkowalski-motion
description: Design engineering rules for animation, micro-interactions, physics-based motion transitions, easing functions, and map re-fit invalidation.
---

# Emil Kowalski - Design Engineering & Motion Polish

Elevates the "feel" and polish of software interfaces through precise micro-interactions and motion physics.

## Motion Guidelines:
1. **Physics Easing:** Use `cubic-bezier(0.4, 0, 0.2, 1)` for smooth 150ms-250ms transitions.
2. **Hover Lift Effects:** Cards and rows elevate -1px to -2px on hover with subtle glow shadows (`box-shadow: 0 0 15px rgba(79,70,229,0.3)`).
3. **Container Invalidation:** Always call `invalidateSize()` when switching tabs containing Leaflet/MapLibre canvas containers.
