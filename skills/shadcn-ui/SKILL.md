---
name: shadcn-ui
description: >
  Sistema de componentes UI open-source de shadcn. Copy-paste de componentes
  accesibles construidos con Radix UI y TailwindCSS. NO es una librería npm —
  los componentes se copian directamente al proyecto.
  Úsalo para cualquier proyecto React/Next.js que necesite componentes de UI
  profesionales: Button, Card, Dialog, Form, Table, Tabs, Select, etc.
  Repo: https://github.com/shadcn-ui/ui | Docs: https://ui.shadcn.com
---

# shadcn/ui — Componentes UI Accesibles y Temables

**Repo:** https://github.com/shadcn-ui/ui  
**Docs:** https://ui.shadcn.com  
**Stack:** React + TailwindCSS + Radix UI  
**Modelo:** Copy-paste al proyecto (NO dependencia npm)

---

## Cuándo usar esta Skill

- Proyecto React/Next.js necesita componentes de UI profesionales
- Quieres componentes 100% personalizables sin pelear con estilos de una librería
- Necesitas accesibilidad (ARIA, keyboard nav) out-of-the-box
- Diseño limpio light/dark mode con tokens CSS

---

## 🚀 Instalación

```bash
# 1. Init en proyecto Next.js existente
npx shadcn@latest init

# Opciones del CLI:
# - Style: Default (recomendado)
# - Base color: Slate / Gray / Zinc
# - CSS variables: Yes
```

## 📦 Agregar componentes

```bash
# Agregar componentes individuales (solo los que necesitas)
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
npx shadcn@latest add form
npx shadcn@latest add table
npx shadcn@latest add tabs
npx shadcn@latest add select
npx shadcn@latest add input
npx shadcn@latest add badge
npx shadcn@latest add avatar
npx shadcn@latest add dropdown-menu

# O todos a la vez
npx shadcn@latest add --all
```

## 🎨 Sistema de Design Tokens (variables CSS)

```css
/* En globals.css — light mode */
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --card: 0 0% 100%;
  --card-foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --accent: 210 40% 96.1%;
  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;
  --radius: 0.5rem;
}
```

## 💻 Uso de Componentes Clave

### Button
```tsx
import { Button } from "@/components/ui/button"

<Button>Click me</Button>
<Button variant="outline">Outline</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="destructive">Delete</Button>
```

### Card (patrón de módulo/dashboard)
```tsx
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"

<Card>
  <CardHeader>
    <CardTitle>Título del Módulo</CardTitle>
    <CardDescription>Descripción corta</CardDescription>
  </CardHeader>
  <CardContent>
    {/* Contenido */}
  </CardContent>
</Card>
```

### Tabs (para apps multi-módulo)
```tsx
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

<Tabs defaultValue="copilot">
  <TabsList>
    <TabsTrigger value="copilot">Copiloto</TabsTrigger>
    <TabsTrigger value="outbound">Outbound</TabsTrigger>
    <TabsTrigger value="interview">Entrevista</TabsTrigger>
  </TabsList>
  <TabsContent value="copilot">...</TabsContent>
</Tabs>
```

### Badge de status
```tsx
import { Badge } from "@/components/ui/badge"

<Badge variant="default">Activo</Badge>
<Badge variant="secondary">Pendiente</Badge>
<Badge variant="destructive">Error</Badge>
<Badge variant="outline">Draft</Badge>
```

## 🏗️ Estructura de archivos generados

```
src/
├── components/
│   └── ui/          # ← Componentes shadcn copiados aquí
│       ├── button.tsx
│       ├── card.tsx
│       └── ...
├── lib/
│   └── utils.ts     # cn() utility para clases
└── app/
    └── globals.css  # Variables CSS del design system
```

## 🌐 ShadcnSpace — Bloques y Layouts adicionales

**Repo:** https://github.com/shadcnspace/shadcnspace  
Bloques completos (hero, navbar, pricing, dashboard) construidos sobre shadcn/ui.

```bash
# Ver catálogo
https://shadcnspace.com
```

## ⚡ Reglas de uso

- Los archivos en `components/ui/` son tuyos — edítalos libremente
- Actualizar shadcn = volver a correr `npx shadcn add [componente]` (sobreescribe)
- Para dark mode: shadcn usa `class="dark"` en `<html>` — toggle con JS
- Si quieres SOLO light mode, no incluyas dark tokens en CSS
