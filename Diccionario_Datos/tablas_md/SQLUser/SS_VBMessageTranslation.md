# SQLUser.SS_VBMessageTranslation

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANS_RowId | bigint | PK |  | NO | - |
| TRANS_Code | varchar |  |  | NO | Code |
| TRANS_Desc | varchar |  |  | NO | Description |
| TRANS_Language_DR | bigint |  | FK | SI | Des Ref Language |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*