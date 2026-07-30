# ==============================================================================
# BOT DE TELEGRAM: COPILOTO COMERCIAL DE BOLSILLO (CPS & SOCRÁTICO)
# ==============================================================================
# Requiere: pip install python-telegram-bot
# Para iniciar: Pon tu token de Telegram BotFather en la variable TELEGRAM_BOT_TOKEN
# ==============================================================================

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from cps_outbound_v2 import generate_cps_outbound_v2, calculate_cdi

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "TU_TOKEN_DE_TELEGRAM_AQUI")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "⚡ *Copiloto Comercial Intelligential (Telegram Bot)* ⚡\n\n"
        "¡Bienvenido, Antonio! Estoy listo para apoyarte en llamadas y prospección en tiempo real.\n\n"
        "*Comandos Disponibles:*\n"
        "• `/outbound [rol] [empresa]` — Genera copy socrático (Ej: `/outbound CEO MexCredit`)\n"
        "• `/cdi [cartera_mxn]` — Calcula el Costo Diario de Ineficiencia (Ej: `/cdi 150000000`)\n"
        "• `/objecion [tema]` — Respuesta táctica a objeciones (Ej: `/objecion precio`)\n"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

async def outbound_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("⚠️ Uso correcto: `/outbound [CEO|CFO|COMPLIANCE|IT] [Nombre Empresa]`\nEjemplo: `/outbound CFO FinancieraMex`", parse_mode="Markdown")
            return
        
        role = args[0].upper()
        empresa = " ".join(args[1:])
        
        res = generate_cps_outbound_v2(role, "linkedin", empresa, "Director", 100000000)
        
        reply = (
            f"🎯 *Mensaje Outbound Socrático para {role} en {empresa}*\n"
            f"💰 *CDI Proyectado:* ${res['cdi_projected']:,.2f} MXN/día\n\n"
            f"💬 *Hook Sugerido:*\n\"{res['message']}\""
        )
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error al generar mensaje: {str(e)}")

async def cdi_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if not context.args:
            await update.message.reply_text("⚠️ Uso: `/cdi [monto_cartera_mxn]` (Ejemplo: `/cdi 100000000`)", parse_mode="Markdown")
            return
        
        cartera = float(context.args[0])
        cdi_daily = calculate_cdi(portfolio_size_mxn=cartera)
        cdi_monthly = cdi_daily * 30.0
        
        reply = (
            f"📊 *Calculadora CDI (Costo Diario de Ineficiencia)*\n"
            f"💼 *Cartera:* ${cartera:,.2f} MXN\n\n"
            f"🔥 *Pérdida Diaria:* ${cdi_daily:,.2f} MXN/día\n"
            f"📅 *Pérdida Mensual:* ${cdi_monthly:,.2f} MXN/mes\n\n"
            f"💡 *Ángulo:* \"¿Cuánto les cuesta mantener 4 licencias sueltas en lugar de una plataforma unificada?\""
        )
        await update.message.reply_text(reply, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error al calcular CDI: {str(e)}")

async def objecion_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args).lower() if context.args else "general"
    
    objeciones = {
        "precio": "💰 *Objeción de Precio:* Muestra la Calculadora TCO. 'No comparamos licencias sueltas de $5k vs Core. El plan unificado ahorra 45% ($570k MXN) en el Año 1 comparado con pagar 4 proveedores sueltos.'",
        "migracion": "⚙️ *Objeción de Migración:* Muestra la 'Garantía Go-Live 30 Días'. 'El 60% de los tratos estancados temen 8 meses de migración con DynamiCore. Salimos a producción en 30 días con penalización a favor tuyo si fallamos.'",
        "contrato": "📄 *Objeción de Contrato Vigente:* Muestra el 'Bono de Liberación Buy-Out'. 'Te bonificamos los meses restantes de tu software anterior para que no pagues doble renta mientras vence tu contrato.'"
    }
    
    ans = objeciones.get(query, objeciones["precio"])
    await update.message.reply_text(ans, parse_mode="Markdown")

if __name__ == "__main__":
    if TELEGRAM_BOT_TOKEN == "TU_TOKEN_DE_TELEGRAM_AQUI":
        print("⚠️ Por favor configura tu token de Telegram con BotFather.")
    else:
        app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("outbound", outbound_handler))
        app.add_handler(CommandHandler("cdi", cdi_handler))
        app.add_handler(CommandHandler("objecion", objecion_handler))
        print("🤖 Bot de Telegram escuchando...")
        app.run_polling()
