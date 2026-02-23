# web_Msg.PA_GlobalDispOrdItems

**Schema:** web_Msg
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ITM_Childsub | double |  |  | SI | Childsub |
| ITM_DisableCheckbox | bit |  |  | SI | Disable Checkbox  |
| ITM_EpisodeType | varchar |  |  | SI | EpisodeType   |
| ITM_ExecNodes | varchar |  |  | SI | Exec Nodes |
| ITM_Include | bit |  |  | SI | Include  |
| ITM_OrdItem_DR | varchar |  | FK | SI | Des Ref PAOrdItem |
| ITM_ParRef | bigint |  |  | SI | PA_GlobalDisp Parent Reference
Required by User.P... |
| ITM_Qty | double |  |  | SI | Qty  |
| ITM_RowId | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*