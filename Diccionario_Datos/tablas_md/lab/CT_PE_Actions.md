# lab.CT_PE_Actions

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPB_RowID | double | PK |  | NO | - |
| CTPB_ActionType | varchar |  |  | SI | Action Type |
| CTPB_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTPB_Group | varchar |  |  | SI | Group |
| CTPB_Message | varchar |  |  | SI | Message |
| CTPB_Order | double |  |  | NO | Order number |
| CTPB_PINRequired | varchar |  |  | SI | PIN Required |
| CTPB_UsersList | varchar |  |  | SI | Users List |
| CTPB_ValidatedFlag | varchar |  |  | SI | Validated Flag |
| CTPB_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*