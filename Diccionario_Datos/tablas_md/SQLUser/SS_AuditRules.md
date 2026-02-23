# SQLUser.SS_AuditRules

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUDR_RowId | bigint | PK |  | NO | - |
| AUDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AUDR_Delete | varchar |  |  | SI | Track Delete |
| AUDR_Insert | varchar |  |  | SI | Track Insert |
| AUDR_Owner | varchar |  |  | SI | Owner |
| AUDR_SSTable_DR | bigint |  | FK | SI | Des Ref SSTable |
| AUDR_TableName | varchar |  |  | SI | Table Name |
| AUDR_Update | varchar |  |  | SI | Track Update |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*