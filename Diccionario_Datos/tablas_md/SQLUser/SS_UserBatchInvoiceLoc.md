# SQLUser.SS_UserBatchInvoiceLoc

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BINVLOC_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| BINVLOC_Childsub | double |  |  | NO | Childsub |
| BINVLOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BINVLOC_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| BINVLOC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*