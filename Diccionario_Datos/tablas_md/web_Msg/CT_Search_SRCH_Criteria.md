# web_Msg.CT_Search_SRCH_Criteria

**Schema:** web_Msg
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CT_Search | varchar | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| SRCH_Criteria_SRCHCCollection | varchar |  |  | SI | - |
| SRCH_Criteria_SRCHCType | varchar |  |  | SI | - |
| SRCH_Criteria_SRCHCValue | varchar |  |  | SI | - |
| element_key | varchar |  |  | NO | SRCHCriteria array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*