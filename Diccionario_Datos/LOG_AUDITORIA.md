# LOG DE AUDITORIA - Diccionario de Datos ALMA
**Ultima actualizacion:** 2026-01-30 19:30

---

## RESUMEN EJECUTIVO

| Metrica | Valor |
|---------|-------|
| Tablas | **11,653** |
| Schemas | **304** |
| Columnas | **450,937** |
| Columnas con descripcion | **425,960** (94%) |
| Relaciones FK | 19,553 |
| **Tablas con Utilidad** | **11,653 (100%)** |
| **Archivos MD generados** | **11,654** |

---

## TAREAS COMPLETADAS

| # | Tarea | Estado | Fecha |
|---|-------|--------|-------|
| 1 | Organizar carpetas a _archivo/ | COMPLETADO | 29-ene |
| 2 | Crear scripts de gestion | COMPLETADO | 29-ene |
| 3 | Migrar SQLUser, questionnaire, websys | COMPLETADO | 29-ene |
| 4 | Importar columnas/relaciones desde CSVs | COMPLETADO | 29-ene |
| 5 | **FASE 1: Importar TODOS los schemas** | **COMPLETADO** | 30-ene |
| 6 | **FASE 2: Importar columnas CON descripciones** | **COMPLETADO** | 30-ene |
| 7 | Crear script unificado sincronizar_todo.py | COMPLETADO | 30-ene |
| 8 | Crear Skills para Claude Code | COMPLETADO | 30-ene |
| 9 | Actualizar README.md | COMPLETADO | 30-ene |
| 10 | **Generar MD por tabla (11,653 archivos)** | **COMPLETADO** | 30-ene |

---

## SKILLS DISPONIBLES

| Skill | Funcion | Servidor |
|-------|---------|----------|
| `/diccionario-stats` | Ver estadisticas y version | NO |
| `/diccionario-sync` | Sincronizar con servidor | SI |
| `/diccionario-export` | Exportar CSV/MD | NO |
| `/diccionario-buscar <termino>` | Buscar tablas/columnas | NO |
| `/diccionario-generar-md` | Generar MD por tabla | NO |
| `/diccionario-historial` | Ver historial de sincronizaciones | NO |
| `/diccionario-utilidad` | Agregar descripcion de uso a tablas | NO |
| `/diccionario-ejemplos` | Obtener valores de ejemplo (anonimizado) | SI* |
| `/diccionario-actividad` | Verificar si tablas tienen datos | SI* |
| `/diccionario-mapeo-completo` | Orquestar mapeo por niveles | SI |

Ubicacion: `c:\_Consultas\.claude\skills\`

---

## SCRIPTS PRINCIPALES

Solo 2 scripts activos (los demas archivados en `_Mapeo_Anterior_2026-01-30/`):

| Script | Comando | Funcion |
|--------|---------|---------|
| **sincronizar_todo.py** | (sin args) | Sincronizar TODO (servidor + local) |
| | `--solo-local` | Solo exportar CSV/MD |
| | `--stats` | Solo ver estadisticas |
| | `--schema NOMBRE` | Sincronizar solo un schema |
| | `--listar-schemas` | Listar schemas del servidor |
| **generar_md_tablas.py** | (sin args) | Generar MD para todas las tablas |
| | `--schema NOMBRE` | Solo un schema |
| | `--tabla PATRON` | Solo tablas que coincidan |
| | `--limpiar` | Limpiar archivos huerfanos |
| | `--archivar` | Archivar MD antes de regenerar |

---

## ARCHIVOS GENERADOS

### Base de Datos
- `diccionario.db` - SQLite principal

### CSVs (para Excel)
- `diccionario_tablas.csv` - 11,653 tablas
- `diccionario_columnas.csv` - 450,937 columnas
- `diccionario_relaciones.csv` - 19,553 relaciones
- `diccionario_resumen.csv` - 304 schemas

### Documentacion MD
- `_INDICE.md` - Indice principal
- `_LISTADO_TABLAS.md` - Lista completa de tablas
- `LOG_AUDITORIA.md` - Este archivo

---

## HISTORIAL DE CAMBIOS

### 2026-01-30 (noche)
- [x] **Documentacion masiva de Utilidad:**
  - 11,653 tablas (100%) con campo `uso_clinico` documentado
  - Categorias: Admisiones, Registro Medico, Ordenes, Catalogos, Lab, Facturacion
  - Subcategorias: Cuestionarios, BI, Regional Chile, Farmacia, Cirugia
  - Patrones: PA_*, MR_*, OE_*, CT_*, ARC_*, LB_*, AR_*, etc.
- [x] **Regeneracion completa de MDs:**
  - 11,654 archivos MD con seccion Utilidad poblada
  - Indice actualizado
- [x] **Actualizacion de README.md:**
  - Documentacion completa del sistema
  - Estructura de archivos y base de datos
  - Guia de scripts y skills

### 2026-01-30 (tarde)
- [x] **Limpieza y reorganizacion:**
  - Archivado completo en `_Mapeo_Anterior_2026-01-30/`
  - Solo 2 scripts activos: `sincronizar_todo.py` y `generar_md_tablas.py`
  - Scripts anteriores movidos a `_Mapeo_Anterior_2026-01-30/scripts_anteriores/`
- [x] **Seccion Utilidad en MDs:**
  - Cada MD ahora incluye seccion `## Utilidad`
  - Campo `uso_clinico` en tablas (vacio por defecto)
  - Preparado para `/diccionario-utilidad` skill
- [x] **Seccion Ejemplos en MDs:**
  - Campo `valores_ejemplo` en columnas (vacio por defecto)
  - Columna "Ejemplo" aparece si hay datos

### 2026-01-30 (manana)
- [x] FASE 1: Importar TODOS los schemas (304 schemas, 11,653 tablas)
- [x] FASE 2: Importar columnas CON descripciones (425,960 con desc de 450,937)
- [x] Crear sincronizar_todo.py (script unificado)
- [x] Crear Skills: diccionario-stats, diccionario-sync, diccionario-export, diccionario-buscar
- [x] Actualizar README.md con seccion Diccionario de Datos
- [x] **Sistema de trazabilidad:**
  - Tabla `metadata` (version, ultima_sync)
  - Tabla `sync_log` (historial de sincronizaciones)
  - Campos `fecha_mapeo`, `fecha_actualizacion`, `fuente` en tablas
  - MD generados incluyen version y fecha de sync
- [x] Skill `/diccionario-historial` para ver historial
- [x] Opcion `--limpiar` en generar_md para eliminar huerfanos

### 2026-01-29
- [x] Organizar carpetas antiguas a _archivo/
- [x] Migrar questionnaire (2,551 tablas)
- [x] Migrar websys (159 tablas)
- [x] Crear LOG_AUDITORIA.md
- [x] Crear scripts de gestion
- [x] Importar 172K columnas y 19K relaciones desde CSVs originales

---

## SISTEMA DE TRAZABILIDAD

### Tablas de auditoria (SQLite)
| Tabla | Contenido |
|-------|-----------|
| `metadata` | Version, ultima_sync_servidor, ultima_exportacion |
| `sync_log` | Historial de cada sincronizacion con fecha, tipo, estadisticas, duracion |

### Campos de auditoria en tablas
| Campo | Descripcion |
|-------|-------------|
| `fecha_mapeo` | Cuando se descubrio la tabla por primera vez |
| `fecha_actualizacion` | Ultima vez que se actualizo desde servidor |
| `fuente` | Origen de los datos (servidor, manual, csv) |

### MD generados incluyen
- Version del diccionario
- Fecha de ultima sincronizacion con servidor
- Fecha de mapeo y actualizacion de cada tabla

---

## NOTAS IMPORTANTES

1. **No saturar servidor** - sincronizar_todo.py hace UNA consulta eficiente
2. **Mantener 3 formatos** - SQLite, CSV, MD sincronizados automaticamente
3. **No guardar datos personales** - Solo estructura y metadatos
4. **94% con descripcion** - 425,960 de 450,937 columnas tienen descripcion
5. **Trazabilidad completa** - Historial de sincronizaciones y fechas en cada tabla

---

## CONEXION AL SERVIDOR

```
Servidor: 10.63.180.25
Puerto: 51773
Namespace: LIVE-CLOV
Driver: intersystems_irispython
```

Credenciales en: `credentials/alma_iris.txt`
