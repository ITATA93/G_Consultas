# Índice de Documentación — AG_Consultas

> Actualizado: 2026-02-16

## 📁 Documentos Principales

| Archivo | Descripción |
|---------|-------------|
| `README.md` | Documentación principal del proyecto |
| `GEMINI.md` | Perfil del proyecto para Gemini |
| `CLAUDE.md` | Instrucciones para Claude Code |
| `CONTEXT_GEMINI_3.0.md` | Contexto expandido para Gemini |
| `.clauderc` | Configuración de agentes Claude |
| `CHANGELOG.md` | Historial de cambios |
| `requirements.txt` | Dependencias Python |
| `.env.example` | Template de variables de entorno |

## 📁 Documentación Técnica

| Archivo | Descripción |
|---------|-------------|
| `docs/guias/GUIA_USO_SISTEMA_MAPEO.md` | Guía de uso del sistema de mapeo TrakCare |
| `docs/ORGANIZACION_COMPLETADA.md` | (Histórico) Organización inicial del repo |

## 📁 Agentes Especializados

| Archivo | Función |
|---------|---------|
| `.claude/agents/mapeo_trakcare.agent` | Mapeo de estructura BD TrakCare/ALMA |
| `.claude/agents/constructor_consultas.agent` | Constructor de consultas SQL seguras |
| `.claude/agents/analisis_clinico.agent` | Análisis de datos clínicos |

## 📁 Consultas en Producción (`Consultas_live/`)

| Archivo | Descripción |
|---------|-------------|
| `01_*.sql` a `23_*.sql` | 23 queries SQL numeradas para TrakCare |
| `sync_alma_sidra.py` | ETL principal: 27 tablas ALMA→SIDRA |
| `21_sync_riesgo_ete_caprini.py` | Sync formularios Caprini (riesgo ETE) |
| `diccionarios_csv/` | 53 CSVs exportados de diccionarios clínicos |

## 📁 Herramientas (`herramientas/`)

| Carpeta | Contenido |
|---------|-----------|
| `python/` | 3 herramientas core: validador SQL, decrypt DbVis, metadata |
| `caprini_vte/` | 17 scripts de análisis y verificación Caprini/VTE |
| `diagnostico/` | 4 scripts de test conexión y schemas |
| `outputs/` | Resultados y dumps de ejecuciones pasadas |
| `_antigua/` | Scripts archivados |

## 📁 Diccionario de Datos (`Diccionario_Datos/`)

| Archivo | Descripción |
|---------|-------------|
| `diccionario.db` | SQLite: 11,653 tablas, ~450K columnas |
| `tablas_md/` | ~11,654 archivos Markdown (uno por tabla) |
| `sincronizar_todo.py` | Sincronización con servidor IRIS |
| `generar_md_tablas.py` | Generador de documentación MD |
| `buscar_diccionario.py` | Búsqueda en diccionario local |

## 📁 Credenciales (`credentials/`) — 🔒 PRIVADO

| Archivo | Acceso |
|---------|--------|
| `alma_iris.txt` | InterSystems IRIS (TrakCare) |
| `sidra.txt` | SQL Server (SIDRA) |
| `accesos_por_ip.txt` | URLs de acceso web |

## 📁 Archivo Histórico (`_archivo/`)

| Carpeta | Contenido |
|---------|-----------|
| `DATOS_ALMA/` | App web histórica + config + scripts (57 items) |
| `_Mapeo_Anterior_2026-01-30/` | Backup diccionario anterior (~11,900 archivos) |
| `consultas/` | Queries organizadas por tipo (admin, clínica, reportes) |
| `etl_datos/` | ETL Pentaho Kettle (11 items) |
