# G_Consultas

> Satellite project in the Antigravity ecosystem — Gemini CLI variant.

**Domain:** `01_HOSPITAL_PRIVADO`
**Status:** Active
**Orchestrator:** GEN_OS
**Prefix:** G_
**AG Counterpart:** `AG_Consultas`

## Proposito

Sistema de mapeo y construccion de consultas SQL seguras para la base de datos
hospitalaria TrakCare/ALMA (InterSystems IRIS). Solo lectura, con limites automaticos.

- Mapear la estructura de la base de datos TrakCare/ALMA
- Construir consultas SQL seguras (SELECT con TOP N, max 1000)
- Documentar tablas, relaciones y diccionarios de datos
- Facilitar acceso a informacion clinica sin riesgo para la BD

## Arquitectura

```
G_Consultas/
├── .gemini/                 # Configuracion Gemini CLI
├── .claude/                 # Agentes Claude (mapeo, constructor, analisis)
├── .subagents/              # Dispatch multi-vendor
├── Diccionario_Datos/       # Diccionario completo de BD
│   ├── diccionario.db       # SQLite (11,653 tablas, 450K columnas)
│   ├── tablas_md/           # 11,654 archivos MD documentados
│   └── sincronizar_todo.py  # Sync con servidor IRIS
├── Consultas_live/          # Queries SQL de produccion activa
│   ├── 01-23_*.sql          # 23 queries numeradas
│   └── diccionarios_csv/    # 53 CSVs de diccionarios clinicos
├── herramientas/            # Utilidades Python
│   ├── python/              # Validador SQL, decrypt, metadata
│   ├── caprini_vte/         # 17 scripts Caprini/VTE
│   └── diagnostico/         # Test conexion y schemas
├── credentials/             # Credenciales (gitignored)
├── docs/                    # Documentacion tecnica
└── exports/                 # Exportaciones de sesion
```

## Uso con Gemini CLI

```bash
# Mapear estructura de tablas
gemini "Que tablas contienen datos de pacientes en TrakCare?"

# Construir consulta segura
gemini "Necesito listar pacientes hospitalizados hoy con SELECT TOP 100"

# Explorar diccionario
gemini "Busca en el diccionario tablas relacionadas con laboratorio"

# Analizar relaciones
gemini "Como se relaciona PA_Adm con PA_Person via columnas _DR?"
```

## Scripts

| Script | Ubicacion | Funcion |
|--------|-----------|---------|
| `sincronizar_todo.py` | `Diccionario_Datos/` | Sync diccionario con IRIS |
| `generar_md_tablas.py` | `Diccionario_Datos/` | Genera documentacion MD |
| `sync_alma_sidra.py` | `Consultas_live/` | ETL: 27 tablas ALMA a SIDRA |

## Configuracion

- `GEMINI.md` -- Perfil del proyecto para Gemini CLI
- `CLAUDE.md` -- Instrucciones y reglas de seguridad SQL
- `credentials/` -- Credenciales de conexion (gitignored)
- `.env.example` -- Template de variables de entorno

## Reglas de Seguridad

- Solo consultas SELECT con TOP N (max 1000 registros)
- Prohibido UPDATE, DELETE, INSERT, DROP, TRUNCATE
- WHERE obligatorio en tablas con mas de 10,000 registros
- Timeout de consulta: 30 segundos

## Conexiones de BD

| Base | Motor | Proposito |
|------|-------|-----------|
| ALMA PROD | InterSystems IRIS | Datos clinicos (solo lectura) |
| ALMA UAT | InterSystems IRIS | Ambiente de pruebas |
| SIDRA | SQL Server 2019 | Reportes y analitica |
