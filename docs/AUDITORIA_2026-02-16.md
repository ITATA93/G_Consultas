# 🔍 AUDITORÍA COMPLETA — AG_Consultas
> **Fecha**: 2026-02-16 17:25 CLT  
> **Versión**: 2.1.0  
> **Branch**: `main` (9a43d9f5)  
> **Auditor**: Antigravity Agent  

---

## 📊 RESUMEN EJECUTIVO

| Dimensión | Estado | Nota |
|-----------|--------|------|
| **Estructura** | ✅ PASS | Estructura normalizada AG conforme |
| **Seguridad** | 🔴 CRÍTICO | 27 archivos con credenciales hardcodeadas |
| **Git** | ⚠️ ADVERTENCIA | Credenciales en historial de commits |
| **Diccionario** | ✅ PASS | 11,653 tablas, 450,937 columnas, 19,553 relaciones |
| **Documentación** | ⚠️ ADVERTENCIA | GEMINI.md desactualizado (versión 2.0.0) |
| **Sintaxis Python** | ✅ PASS | Los 3 scripts ETL principales parsean OK |
| **Dotenv** | ✅ PASS | .env carga correctamente las 5 variables |
| **Agentes** | ✅ PASS | 3 agentes Claude + 11 skills + 3 AG skills |
| **Duplicados** | ⚠️ ADVERTENCIA | 2 copias de exportar_usuarios.py |

### Calificación Global: **65/100** ⚠️

---

## 🔴 HALLAZGO CRÍTICO: Credenciales Hardcodeadas (SEC-001)

**Severidad**: CRÍTICA  
**Impacto**: Exposición de contraseñas de bases de datos hospitalarias  

### Password SIDRA (`hkEVC9AFVjFeRTkp`) — 15 archivos

| # | Archivo | Trackeado en Git |
|---|---------|:---:|
| 1 | `Consultas_live/06_crear_schemas_adicionales.py` | ✅ SÍ |
| 2 | `Consultas_live/08_crear_schemas_restantes.py` | ✅ SÍ |
| 3 | `Consultas_live/09_completar_mapeo.py` | ✅ SÍ |
| 4 | `Consultas_live/10_mapear_schemas_externos.py` | ✅ SÍ |
| 5 | `Consultas_live/11_mapear_todo_diccionario.py` | ✅ SÍ |
| 6 | `Consultas_live/12_subir_metadata_diccionario.py` | ✅ SÍ |
| 7 | `Consultas_live/14_exportar_diccionarios.py` | ✅ SÍ |
| 8 | `Consultas_live/16_sync_diccionarios_clinicos.py` | ✅ SÍ |
| 9 | `Consultas_live/17_exportar_todos_csv.py` | ✅ SÍ |
| 10 | `Consultas_live/19_sync_reportes_rem.py` | ✅ SÍ |
| 11 | `Consultas_live/20_sync_definiciones_formularios.py` | ✅ SÍ |
| 12 | `herramientas/caprini_vte/verify_sidra_caprini.py` | ✅ SÍ |
| 13 | `herramientas/diagnostico/check_sidra_schema.py` | ✅ SÍ |
| 14 | `herramientas/diagnostico/test_conexion_sidra.py` | ✅ SÍ |
| 15 | `herramientas/diagnostico/test_sidra_insert.py` | ✅ SÍ |

### Password ALMA (`sd260710sd`) — 19 archivos

Incluye los mismos de arriba más:
- `Consultas_live/15_buscar_ordenes.py`
- `Diccionario_Datos/sincronizar_todo.py`
- `Exportaciones/exportar_usuarios.py`
- `Exportaciones/Usuarios/exportar_usuarios.py`
- Todos los `herramientas/caprini_vte/check_*.py` y `buscar_*.py`

### Scripts ya migrados a .env (3 de 42):
- ✅ `sync_alma_sidra.py`
- ✅ `21_sync_riesgo_ete_caprini.py`
- ✅ `herramientas/caprini_vte/ejecutar_registro_caprini.py`

### Remediación requerida:
1. **Inmediata**: Migrar los 27+ scripts restantes a dotenv
2. **Importante**: Después de migrar, ejecutar `git filter-repo` para limpiar historial
3. **Alternativa**: Si `filter-repo` es demasiado disruptivo, rotar passwords

---

## ⚠️ HALLAZGO: Archivos Duplicados (DUP-001)

| Archivo A | Archivo B | Mismo contenido |
|-----------|-----------|:---:|
| `Exportaciones/exportar_usuarios.py` (10.9 KB) | `Exportaciones/Usuarios/exportar_usuarios.py` (11.3 KB) | ❌ Diferentes |

- Ambos tienen credenciales hardcodeadas y rutas `c:\_Consultas\` (path antiguo)
- La versión en `Usuarios/` tiene 12 queries vs 9 en la raíz
- **Acción**: Consolidar en uno solo y migrar a dotenv

---

## ⚠️ HALLAZGO: Rutas Legacy (PATH-001)

Ambos `exportar_usuarios.py` referencian:
```python
OUTPUT_DIR = r'c:\_Consultas\Exportaciones\Usuarios'
```
Debería ser: `c:\_Repositorio\AG_Proyectos\AG_Consultas\Exportaciones\Usuarios`

---

## ⚠️ HALLAZGO: GEMINI.md Desactualizado (DOC-001)

| Campo | GEMINI.md dice | Realidad |
|-------|---------------|----------|
| Versión | 2.0.0 | 2.1.0 |
| Última actualización | 2026-02-04 | 2026-02-16 |
| Estructura | Falta `.env`, `requirements.txt` | Existen ambos |
| SIDRA | No mencionado | Es componente clave |

---

## ✅ Validaciones Positivas

### Estructura de Proyecto
```
AG_Consultas/                     ← Raíz normalizada AG
├── .agent/                       ← 2 workflows, 3 skills
├── .claude/                      ← 3 agentes, 11 skills
├── .env                          ← Credenciales reales (gitignored ✅)
├── .env.example                  ← Template con placeholders
├── .gitignore                    ← 154 líneas, cubre credenciales
├── GEMINI.md                     ← Perfil proyecto (desactualizado)
├── CLAUDE.md                     ← Instrucciones Claude (actualizado ✅)
├── CHANGELOG.md                  ← Historial (actualizado ✅)
├── requirements.txt              ← 3 dependencias Python
├── Consultas_live/               ← 24 archivos + diccionarios_csv/ (53 CSVs)
├── Diccionario_Datos/            ← SQLite + 11,654 archivos MD
│   ├── diccionario.db            ← 11,653 tablas, 450,937 columnas
│   ├── tablas_md/                ← 11,654 archivos Markdown
│   ├── sincronizar_todo.py       ← Sync con IRIS
│   └── generar_md_tablas.py      ← Generador MD
├── Exportaciones/                ← 3 CSVs + 2 scripts (1 duplicado)
├── herramientas/                 ← Organizado en 5 subcarpetas
│   ├── caprini_vte/              ← 17 scripts Caprini/VTE
│   ├── diagnostico/              ← 4 scripts de diagnóstico
│   ├── python/                   ← 3 herramientas core
│   ├── outputs/                  ← Resultados históricos
│   └── _antigua/                 ← Scripts archivados
├── credentials/                  ← 5 archivos (gitignored ✅)
├── docs/                         ← 3 archivos documentación
└── _archivo/                     ← 12,045 archivos / 173.5 MB (gitignored ✅)
```

### Diccionario de Datos
| Métrica | Valor |
|---------|-------|
| Tablas mapeadas | 11,653 |
| Columnas documentadas | 450,937 |
| Relaciones FK | 19,553 |
| Archivos Markdown | 11,654 |
| CSVs exportados | 53 |

### Git
| Métrica | Valor |
|---------|-------|
| Branch | `main` (up to date with origin) |
| Commits | 3 |
| Archivos trackeados | 23,792 |
| Scripts Python trackeados | 67 |
| `.env` trackeado | ❌ NO (correcto) |
| `credentials/` trackeado | ❌ NO (correcto) |
| `_archivo/` trackeado | ❌ NO (correcto) |
| Working tree | Clean |

### Dotenv Validation
| Variable | Cargada | Valor |
|----------|:-------:|-------|
| `ALMA_HOST` | ✅ | 10.63.180.25 |
| `ALMA_USER` | ✅ | 18233087-6 |
| `SIDRA_HOST` | ✅ | 10.67.119.135 |
| `SIDRA_USER` | ✅ | sidra |
| `SIDRA_PASS` | ✅ | *** (presente) |

### Agentes y Skills
| Componente | Cantidad | Estado |
|------------|:--------:|--------|
| Agentes Claude | 3 | ✅ OK |
| Skills Claude | 11 | ✅ OK |
| Skills AG (.agent) | 3 | ✅ OK |
| Workflows AG | 2 | ✅ OK |

---

## 📋 PLAN DE REMEDIACIÓN (Priorizado)

### P0 — Crítico (Hacer ahora)
1. **SEC-001**: Migrar los 27 scripts restantes a dotenv
   - Crear módulo compartido `herramientas/python/db_config.py` 
   - Importar en todos los scripts en lugar de repetir el bloque dotenv

### P1 — Importante (Esta semana)
2. **DUP-001**: Eliminar `Exportaciones/exportar_usuarios.py` (versión inferior)
3. **PATH-001**: Corregir rutas `c:\_Consultas\` → path dinámico con `Path(__file__)`
4. **DOC-001**: Actualizar GEMINI.md a v2.1.0

### P2 — Mejora (Próxima iteración)
5. Considerar `git filter-repo` para limpiar credenciales del historial
6. Agregar `iris` SDK como dependencia comentada en `requirements.txt`
7. Mover archivos `sidra_test_result.txt` a `herramientas/outputs/`

---

## 📈 Métricas de Cobertura

```
Migración dotenv:    3/42 scripts  =  7.1%  🔴
Documentación:       6/7 docs OK   = 85.7%  ✅
Git protection:      3/3 dirs OK   = 100%   ✅
Syntax validation:   3/3 ETL OK    = 100%   ✅
```

---

*Generado automáticamente por Antigravity Agent — 2026-02-16T17:25-03:00*
