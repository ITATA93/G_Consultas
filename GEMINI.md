# GEMINI.md — AG_Consultas Project Profile

## Identidad del Proyecto
**Nombre**: AG_Consultas  
**Tipo**: Sistema de Mapeo y Consultas SQL para TrakCare/ALMA  
**Base de Datos**: InterSystems IRIS (LIVE-CLOV)  
**Propósito**: Mapear estructura de BD hospitalaria y construir consultas SQL seguras

## Contexto
Este proyecto contiene un **sistema integral de mapeo y construcción de consultas SQL** para la base de datos **TrakCare/ALMA**, un sistema de información hospitalaria implementado sobre **InterSystems IRIS**.

### Componentes Principales
1. **Diccionario de Datos** (SQLite): 11,653 tablas, 450K columnas
2. **Consultas SQL** en producción (`Consultas_live/`)
3. **Exportaciones** de datos
4. **Credenciales** de acceso (protegidas)
5. **Herramientas** de análisis

## Estructura del Proyecto
```
AG_Consultas/
├── .env                        # 🔒 Variables de entorno (gitignored)
├── .env.example                # Template de credenciales
├── Diccionario_Datos/          # 📊 Diccionario completo (SQLite + MD)
│   ├── diccionario.db          # 11,653 tablas, 450K columnas
│   ├── tablas_md/              # 11,654 archivos MD
│   └── sincronizar_todo.py     # Sync con IRIS
├── Consultas_live/             # Consultas SQL + ETL pipelines
│   ├── sync_alma_sidra.py      # ETL principal: 27 tablas
│   └── diccionarios_csv/       # 53 CSVs exportados
├── Exportaciones/              # Datos exportados
├── credentials/                # 🔒 Credenciales (gitignored)
├── herramientas/               # Utilidades Python
│   ├── python/db_config.py     # 🔑 Config centralizada de conexiones
│   ├── caprini_vte/            # Scripts Caprini/VTE
│   └── diagnostico/            # Test de conexión
├── docs/                       # Documentación
├── _archivo/                   # 📦 Proyectos anteriores (gitignored)
└── README.md                   # Documentación principal
```

## Reglas de Seguridad Críticas

### ⛔ PROHIBICIONES ABSOLUTAS
**NUNCA** se permite:
1. ❌ Ejecutar UPDATE, DELETE, INSERT, TRUNCATE, DROP
2. ❌ Modificar datos en la base de datos
3. ❌ Crear o eliminar objetos de BD (tablas, vistas, procedimientos)
4. ❌ Ejecutar consultas sin límite TOP N
5. ❌ Hacer consultas en tablas grandes sin WHERE
6. ❌ Usar `COUNT(*)` en tablas clínicas — satura el servidor IRIS
7. ❌ Ejecutar múltiples queries pesadas en serie sin pausa
8. ❌ Hacer full table scans (queries sin WHERE ni TOP)

### 🛡️ ESTRATEGIA LIVIANA OBLIGATORIA
**SIEMPRE** usar la consulta más ligera posible:
- Para verificar si tiene datos: `SELECT TOP 1 1 FROM schema.tabla` (instantáneo)
- Para muestreo: `SELECT TOP 10 * FROM schema.tabla` (máx 10-20 rows)
- Para contar: **NUNCA** `COUNT(*)`. Usar `SELECT TOP 1 COUNT(*) FROM tabla WHERE RowId < 1000` si es imprescindible
- Para metadatos: preferir `INFORMATION_SCHEMA` sobre queries directas
- Entre queries: agregar `time.sleep(0.5)` para no saturar conexiones

### ✅ OPERACIONES PERMITIDAS
**SOLO** se permite:
1. ✅ Consultas SELECT con TOP N (máx 1000)
2. ✅ Consultas a INFORMATION_SCHEMA
3. ✅ Lectura de diccionarios y metadatos
4. ✅ Análisis de relaciones entre tablas

## Tecnología Base de Datos

### ALMA (Fuente clínica)
- **Motor**: InterSystems IRIS
- **Servidor**: 10.63.180.25:51773
- **Base de Datos**: LIVE-CLOV
- **Esquema principal**: SQLUser

### SIDRA (Destino analítico)
- **Motor**: SQL Server 2019
- **Servidor**: 10.67.119.135:1433
- **Base de Datos**: DB_SIDRA_TEST
- **Herramienta**: DbVisualizer Pro 10.0.20

### Gestión de Credenciales
- Todas las credenciales se cargan desde `.env` (ver `.env.example`)
- Módulo centralizado: `herramientas/python/db_config.py`
- **NUNCA** hardcodear contraseñas en scripts Python

## Dominios Clínicos Mapeados

| Prefijo | Dominio | Tablas clave |
|---------|---------|--------------|
| **PA_** | Administración Pacientes | PA_Adm, PA_Person, PA_PatMas |
| **CT_** | Configuración/Códigos | CT_Loc, CT_CareProv, CT_Nation, CT_Marital |
| **MR_** | Registro Médico | MR_Adm, MR_Diagnos, MR_Medication |
| **OE_** | Órdenes Médicas | OE_Order, OE_OrdItem, OE_OrdExec |
| **LB_** | Laboratorio | LB_Episode, LB_TestSet, LB_TestSetItem |
| **ARC_/AR_** | Facturación | ARC_ItmMast, ARC_ItemCat, AR_PatBillDate |
| **PHC_** | Farmacia | PHC_DrgForm, PHC_AdministrationRoute |
| **ORC_/OR_** | Cirugía/Pabellón | ORC_Operation, OR_Anaesthesia |
| **RB_** | Agenda/Booking | RB_Appointment, RB_Resource |
| **INC_** | Inventario/Insumos | INC_Itm, INC_ItmLoc, INC_ItmBat |
| **SS_** | Sistema/Seguridad | SS_User, SS_UserDefWindow |
| **questionnaire.*** | Formularios Enfermería | QCLXXEVARC, QTCERIESGO, QCLXXMDI |

## Questionnaires de Enfermería (Acceso SQL Directo)

> **IMPORTANTE**: Los questionnaires de TrakCare son **tablas SQL normales** del esquema `questionnaire.*`. Se consultan exactamente igual que cualquier otra tabla, usando el mismo patrón JOIN que Caprini.

### Patrón de acceso universal
```sql
SELECT TOP 100 Q.*, Pat.PAPMI_Name, Adm.PAADM_RowID
FROM questionnaire.<NOMBRE_TABLA> Q
JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId
JOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
```

### Tablas mapeadas y validadas (Feb 2026)

| Tabla | Descripción | Estado |
|-------|-------------|--------|
| `QCLXXEVARC` | Escala Riesgo de Caídas | ⚠️ Vacía (no en uso) |
| `QTCERIESGO` | Categorización Riesgo-Dependencia | ✅ Datos reales |
| `QCLXXMDI` + subtablas | Dispositivos Invasivos (VVP, CVC, etc.) | ✅ Datos reales |
| `QGXXXISS` | Protocolo Insulina | ⚠️ Vacía (no en uso) |
| `QTCEEVRIEST` | ETE/Caprini (producción) | ✅ 386+ registros |
| `QCLXXTPETEH` | Entrega Turno Hospitalización | ❌ Privilege violation |

### Campos clave de cada questionnaire
- **Datos clínicos**: `Q01`, `Q02`, ... `Qnn` (mapeo propio por tabla)
- **Enlace episodio**: `QUESPAAdmDR` → `PA_Adm.PAADM_RowId`
- **Enlace paciente**: `QUESPAPatMasDR` → `PA_PatMas.PAPMI_RowId`
- **Fecha/Hora**: `QUESDate` (Mumps), `QUESTime`
- **Score**: `QUESScore` (campo sistema, algunos formularios)
- **Evaluador**: `QUESUserDR` → `SS_User.SSUSR_RowId`
- **Subtablas**: campo `childsub` enlaza tabla padre→hija (ej: `QCLXXMDIQQ01`)

## Agentes Especializados (Claude Code)

### 1. 🗺️ Agente de Mapeo TrakCare
- **Archivo**: `.claude/agents/mapeo_trakcare.agent`
- **Especialidad**: Analizar y mapear estructura de BD TrakCare/ALMA

### 2. 🔨 Constructor de Consultas SQL
- **Archivo**: `.claude/agents/constructor_consultas.agent`
- **Especialidad**: Construir consultas SQL seguras con límites automáticos

### 3. 🏥 Analista de Datos Clínicos
- **Archivo**: `.claude/agents/analisis_clinico.agent`
- **Especialidad**: Interpretar necesidades clínicas y mapear formularios

## Skills del Diccionario

| Skill | Descripción |
|-------|-------------|
| `/diccionario-stats` | Ver estadísticas actuales (local) |
| `/diccionario-sync` | Sincronizar con servidor IRIS |
| `/diccionario-buscar <término>` | Buscar tablas/columnas |
| `/diccionario-generar-md` | Regenerar documentación MD |
| `/diccionario-utilidad` | Agregar descripción de uso a tablas |

## Normativa de Datos de Salud

**ADVERTENCIA**: Este sistema accede a datos de salud protegidos. El uso indebido está sujeto a sanciones legales según normativa vigente (Ley 19.628 en Chile).

### Principios de Manejo de Datos
1. **Solo lectura**: Nunca modificar datos en producción
2. **Anonimización**: Al exportar datos, anonimizar información sensible
3. **Auditoría**: Registrar todas las consultas ejecutadas
4. **Confidencialidad**: No compartir credenciales ni resultados fuera del ámbito autorizado

## Integración con Plantilla AG

Este proyecto sigue los estándares definidos en `AG_Plantilla`:
- Estructura de carpetas normalizada
- Configuración de agentes según protocolo
- Documentación viva en `docs/`
- Archivado histórico en `_archivo/`

## Comandos Comunes

```powershell
# Sincronizar diccionario desde IRIS
python Diccionario_Datos/sincronizar_todo.py

# Generar documentación MD de tablas
python Diccionario_Datos/generar_md_tablas.py

# Desencriptar credenciales DbVisualizer
python herramientas/python/decrypt_dbvis.py
```

## Mantenimiento

**Última actualización**: 2026-02-17  
**Versión**: 2.2.0 (Questionnaires SQL + Enfermería)  
**Mantenedor**: Equipo de Informática Hospitalaria

## Absolute Rules
1. **NEVER** execute DELETE, DROP, UPDATE, TRUNCATE on databases without confirmation
2. **Read docs/** before starting any task
3. **Update** `CHANGELOG.md` with significant changes
4. **Append** session summaries to `docs/DEVLOG.md`
5. **Update** `docs/TASKS.md` for pending tasks

## Complexity Classifier

| Scope | Level | Action |
|-------|-------|--------|
| 0-1 files, simple question | NIVEL 1 | Respond directly |
| 2-3 files, defined task | NIVEL 2 | Delegate to 1 sub-agent |
| 4+ files or ambiguous | NIVEL 3 | Pipeline: analyst > specialist > reviewer |

## Sub-Agent Dispatch
Available via `.subagents/dispatch.ps1` or `.subagents/dispatch.sh`

## Commit Format
`type(scope): brief description`
Types: feat, fix, docs, refactor, test, chore, style, perf
