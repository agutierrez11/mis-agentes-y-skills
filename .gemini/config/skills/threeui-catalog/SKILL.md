---
name: threeui-catalog
description: Guía de integración de componentes UI 3D interactivos, shaders GLSL, héroes animados en Three.js/React Three Fiber (R3F) y catálogo ThreeUI (@designcodeio/threeui) para experiencias web premium de alto impacto visual.
---

# 🎨 ThreeUI 3D Component Catalog & WebGL Shader Engine

Skill para empaquetar, construir y adaptar componentes tridimensionales interactivos, shaders de fondo reactivos y animaciones de héroes 3D usando ThreeUI (`@designcodeio/threeui`), Three.js y React Three Fiber (R3F).

---

## 🚀 Cuándo Utilizar esta Skill

Invoca esta skill cuando el proyecto requiera:
- **Héroes Web3D & FinTech Impactantes:** Portadas de producto con tarjetas bancarias/POS holográficas en 3D que rotan al movimiento del cursor.
- **Fondos Reactivos con Shaders GLSL:** Fondos interactivos con mallas de partículas, degradados dinámicos de velocidad, auroras cibernéticas o campos de luces tipo *AtTheHorizon*.
- **Páginas de Producto Premium:** Vistas 360° de hardware (lectores de tarjetas, terminales inteligentes, pasarelas de cobro) con controles de cámara limpios (`OrbitControls`, `damp`).
- **Interfaces Inmersivas sin Placeholders:** Experiencias con iluminación de estudio PBR, efectos de dispersión de vidrio (*glassmorphism 3D*) y reflexiones en tiempo real.

---

## 🛠️ Instalación y Dependencias

Para integrar el catálogo oficial de ThreeUI en proyectos React / Next.js / Vite:

```bash
npm install @designcodeio/threeui three @react-three/fiber @react-three/drei lucide-react
```

### Importación Básica:
```tsx
import { AtTheHorizon } from "@designcodeio/threeui";
import "@designcodeio/threeui/style.css";

export function HeroSection() {
  return (
    <div className="relative w-full h-[600px] overflow-hidden rounded-2xl bg-slate-950">
      <AtTheHorizon />
      <div className="absolute inset-0 z-10 flex flex-col items-center justify-center text-center p-6 bg-gradient-to-t from-slate-950/80 to-transparent">
        <h1 className="text-5xl font-bold tracking-tight text-white font-outfit">
          La Nueva Era de Pagos B2B en LATAM
        </h1>
      </div>
    </div>
  );
}
```

---

## 📐 Patrones Arquitectónicos 3D

### 1. Tarjetas Holográficas 3D de Pasarelas de Pago
Muestra tarjetas de crédito/débito o terminales POS flotantes con física de inclinación al hover (`tilt`) y shaders reflectivos.

```tsx
import { Canvas, useFrame } from "@react-three/fiber";
import { Float, MeshTransmissionMaterial, RoundedBox } from "@react-three/drei";
import { useRef } from "react";
import * as THREE from "three";

function HolographicPaymentCard() {
  const meshRef = useRef<THREE.Mesh>(null!);
  
  useFrame((state) => {
    const t = state.clock.getElapsedTime();
    meshRef.current.rotation.y = Math.sin(t / 2) * 0.3;
    meshRef.current.rotation.x = Math.cos(t / 2) * 0.15;
  });

  return (
    <Float speed={2} rotationIntensity={0.5} floatIntensity={1}>
      <RoundedBox ref={meshRef} args={[3.4, 2.1, 0.1]} radius={0.15} smoothness={4}>
        <MeshTransmissionMaterial
          backside
          samples={16}
          thickness={0.2}
          chromaticAberration={0.06}
          anisotropy={0.1}
          distortion={0.2}
          distortionScale={0.3}
          temporalDistortion={0.1}
          color="#06b6d4"
        />
      </RoundedBox>
    </Float>
  );
}

export function PaymentCardCanvas() {
  return (
    <div className="w-full h-80">
      <Canvas camera={{ position: [0, 0, 5], fov: 45 }}>
        <ambientLight intensity={0.7} />
        <directionalLight position={[10, 10, 5]} intensity={1.5} />
        <HolographicPaymentCard />
      </Canvas>
    </div>
  );
}
```

---

## ⚡ Reglas de Rendimiento WebGL

1. **FPS Lock & Adaptive DPI:** Configura `dpr={[1, 2]}` en `<Canvas>` para prevenir caídas de cuadros en pantallas 4K/Retina.
2. **Lazy Loading de Escenas 3D:** Envuelve componentes tridimensionales pesados en `React.lazy()` y `Suspense` con esqueletos 2D de fallback.
3. **Pausa Fuera de Vista (`IntersectionObserver`):** Detén el bucle de animación (`useFrame`) cuando el componente pase fuera del viewport.

---

## 🎨 Paleta Estética Recomendada
- **Fondo:** `#030712` (Slate 950) / `#090d16` (Deep Space Dark)
- **Acentos 3D:** HSL Tonal Azure `#00e5ff`, Electric Purple `#8b5cf6`, Cyan Hologram `#06b6d4`
- **Glassmorphism:** `backdrop-blur-xl border border-white/10 bg-white/5`
