# Indice - Diccionario de Datos ALMA

**Actualizado:** 2026-01-31

## Estadisticas

| Metrica | Cantidad |
|---------|----------|
| Schemas | 304 |
| Tablas | 11,653 |
| Columnas | 450,937 |
| Columnas con descripcion | 425,960 |
| Relaciones FK | 19,553 |

## Documentacion

| Documento | Descripcion |
|-----------|-------------|
| [_LISTADO_TABLAS.md](_LISTADO_TABLAS.md) | Lista completa de tablas |
| [TABLAS_NIVEL_PROFUNDO.md](TABLAS_NIVEL_PROFUNDO.md) | Jerarquias de tablas nivel 3+ (LB_, OR_, MR_, PHC_) |
| [LOG_AUDITORIA.md](LOG_AUDITORIA.md) | Log de cambios |
| `tablas_md/` | Documentacion detallada por tabla |

## Datos

| Archivo | Descripcion |
|---------|-------------|
| `diccionario.db` | Base de datos SQLite (48MB) |
| `diccionario_tablas.csv` | Listado de tablas |
| `diccionario_columnas.csv` | Columnas de todas las tablas |
| `diccionario_relaciones.csv` | Relaciones FK entre tablas |
| `diccionario_resumen.csv` | Resumen por schema |

## Dominios Principales (SQLUser)

| Prefijo | Tablas | Dominio |
|---------|--------|---------|
| PA_ | 347 | Pacientes, Admisiones |
| MR_ | 74 | Registro Medico |
| OE_ | 92 | Ordenes |
| LB_ | 100 | Laboratorio |
| OR_ | 63 | Pabellon/Cirugia |
| PHC_ | 109 | Farmacia |
| CT_ | 204 | Configuracion |
| ARC_ | 291 | Facturacion |
