# SQLUser.PA_GlobalDispOrdItems

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | PA_GlobalDisp Parent Reference |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_EpisodeType | varchar |  |  | SI | EpisodeType   |
| ITM_ExecNodes | varchar |  |  | SI | Exec Nodes |
| ITM_Include | bit |  |  | SI | Include  |
| ITM_OrdItem_DR | varchar |  | FK | SI | Des Ref PAOrdItem |
| ITM_Qty | double |  |  | SI | Qty  |
| ITM_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*