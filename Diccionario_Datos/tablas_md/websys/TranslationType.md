# websys.TranslationType

**Schema:** websys
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| ComponentContext | varchar |  |  | NO | ComponentContext may contain ComponentId, Workflow... |
| ContextRefClass | varchar |  |  | SI | Class name of context object |
| ContextRefId | varchar |  |  | SI | ID of context object |
| ContextRefOID | varchar |  |  | SI | OID of context object if exists |
| LanguageDR | bigint |  | FK | NO | - |
| Type | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*